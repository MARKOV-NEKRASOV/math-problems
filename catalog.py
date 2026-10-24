#!/usr/bin/env python3
"""Maintain the two local research databases and the landing page catalog."""

import argparse
import json
import re
import sqlite3
import subprocess
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PROBLEMS_DB = DATA / "problems.sqlite3"
PAPERS_DB = DATA / "papers.sqlite3"
CATALOG = DATA / "catalog.json"
GENERAL_SOURCE = "https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics"

# Starter reading, not an upper limit. Add as many papers as research requires.
SEED_PAPERS = [
    ("On the equations z^m = F(x,y) and Ax^p + By^q = Cz^r", "Henri Darmon; Andrew Granville", 1995, "https://doi.org/10.1112/blms/27.6.513", "fermat-catalan-conjecture", "Finiteness results for generalized Fermat equations."),
    ("Twists of X(7) and primitive solutions to x² + y³ = z⁷", "Bjorn Poonen; Edward F. Schaefer; Michael Stoll", 2007, "https://arxiv.org/abs/math/0508174", "fermat-catalan-conjecture", "A specific signature of the generalized Fermat equation."),
    ("Modular elliptic curves and Fermat's Last Theorem", "Andrew Wiles", 1995, "https://doi.org/10.2307/2118559", "fermat-catalan-conjecture", "Foundational modularity method relevant to generalized Fermat equations."),
    ("Ring-theoretic properties of certain Hecke algebras", "Richard Taylor; Andrew Wiles", 1995, "https://doi.org/10.2307/2118560", "fermat-catalan-conjecture", "Companion paper for the modularity method."),
    ("Bounded gaps between primes", "Yitang Zhang", 2014, "https://doi.org/10.4007/annals.2014.179.3.7", "twin-prime-conjecture", "Establishes a finite bound for infinitely many prime gaps."),
    ("Small gaps between primes", "James Maynard", 2015, "https://arxiv.org/abs/1311.4600", "twin-prime-conjecture", "Develops a sieve method for bounded prime gaps."),
    ("Almost all orbits of the Collatz map attain almost bounded values", "Terence Tao", 2022, "https://arxiv.org/abs/1909.03562", "collatz-conjecture", "Partial progress on typical Collatz trajectories."),
    ("The ternary Goldbach conjecture is true", "Harald Andrés Helfgott", 2013, "https://arxiv.org/abs/1312.7748", "goldbach-conjecture", "A resolved related problem; useful context for the binary conjecture."),
]


def slugify(value):
    value = value.translate(str.maketrans({"–": "-", "—": "-", "−": "-"}))
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def connect(path):
    connection = sqlite3.connect(path, timeout=15)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 15000")
    return connection


def initialize():
    DATA.mkdir(exist_ok=True)
    renamed_slugs = []
    with connect(PROBLEMS_DB) as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY,
                slug TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                field TEXT NOT NULL,
                statement TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open_unverified',
                source_url TEXT NOT NULL,
                status_checked_at TEXT
            );
            CREATE TABLE IF NOT EXISTS work_items (
                id INTEGER PRIMARY KEY,
                problem_id INTEGER NOT NULL REFERENCES problems(id),
                agent TEXT NOT NULL,
                title TEXT NOT NULL,
                state TEXT NOT NULL DEFAULT 'open' CHECK (state IN ('open','in_progress','done')),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                problem_id INTEGER NOT NULL REFERENCES problems(id),
                agent TEXT NOT NULL,
                body TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS complexity_ratings (
                problem_id INTEGER NOT NULL REFERENCES problems(id),
                agent TEXT NOT NULL,
                score REAL NOT NULL CHECK (score >= 0 AND score <= 1),
                rationale TEXT NOT NULL,
                rated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (problem_id, agent)
            );
            CREATE TABLE IF NOT EXISTS ideas (
                id INTEGER PRIMARY KEY,
                problem_id INTEGER NOT NULL REFERENCES problems(id),
                agent TEXT NOT NULL,
                title TEXT NOT NULL,
                approach TEXT NOT NULL,
                evidence TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS idea_reviews (
                id INTEGER PRIMARY KEY,
                idea_id INTEGER NOT NULL REFERENCES ideas(id),
                reviewer TEXT NOT NULL,
                assessment TEXT NOT NULL CHECK (assessment IN ('supports','questions','counterexample','needs_work')),
                comment TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_problems_field ON problems(field);
            CREATE INDEX IF NOT EXISTS idx_work_problem ON work_items(problem_id);
            CREATE INDEX IF NOT EXISTS idx_notes_problem ON notes(problem_id);
            CREATE INDEX IF NOT EXISTS idx_ideas_problem ON ideas(problem_id);
            CREATE INDEX IF NOT EXISTS idx_reviews_idea ON idea_reviews(idea_id);
        """)
        for row in db.execute("SELECT slug,title FROM problems").fetchall():
            canonical = slugify(row["title"])
            if canonical != row["slug"]:
                db.execute("UPDATE problems SET slug=? WHERE slug=?", (canonical, row["slug"]))
                renamed_slugs.append((row["slug"], canonical))
        lines = (DATA / "seed_problems.tsv").read_text(encoding="utf-8").splitlines()
        if len(lines) != 100:
            raise ValueError(f"Expected 100 seed problems, found {len(lines)}")
        for line in lines:
            title, field, statement = line.split("\t")
            slug = slugify(title)
            source = "https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture" if title == "Fermat–Catalan conjecture" else GENERAL_SOURCE
            db.execute("INSERT OR IGNORE INTO problems (slug,title,field,statement,source_url) VALUES (?,?,?,?,?)", (slug, title, field, statement, source))
    with connect(PAPERS_DB) as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS papers (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                authors TEXT NOT NULL,
                year INTEGER,
                url TEXT NOT NULL UNIQUE,
                doi TEXT,
                added_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS problem_papers (
                problem_slug TEXT NOT NULL,
                paper_id INTEGER NOT NULL REFERENCES papers(id),
                relevance TEXT NOT NULL DEFAULT '',
                PRIMARY KEY (problem_slug,paper_id)
            );
            CREATE INDEX IF NOT EXISTS idx_problem_papers_slug ON problem_papers(problem_slug);
        """)
        for old, new in renamed_slugs:
            db.execute("UPDATE problem_papers SET problem_slug=? WHERE problem_slug=?", (new, old))
        for title, authors, year, url, slug, relevance in SEED_PAPERS:
            db.execute("INSERT OR IGNORE INTO papers (title,authors,year,url) VALUES (?,?,?,?)", (title, authors, year, url))
            paper_id = db.execute("SELECT id FROM papers WHERE url=?", (url,)).fetchone()[0]
            db.execute("INSERT OR IGNORE INTO problem_papers (problem_slug,paper_id,relevance) VALUES (?,?,?)", (slug, paper_id, relevance))


def require_problem(db, slug):
    row = db.execute("SELECT id,title FROM problems WHERE slug=?", (slug,)).fetchone()
    if row is None:
        raise SystemExit(f"Unknown problem slug: {slug}")
    return row


def export_catalog():
    with connect(PROBLEMS_DB) as db:
        problems = [dict(row) for row in db.execute("SELECT slug,title,field,statement,status,source_url FROM problems ORDER BY title")]
        ratings = {row["slug"]: dict(row) for row in db.execute("""
            SELECT p.slug, ROUND(AVG(r.score), 2) AS score, COUNT(*) AS rating_count
            FROM complexity_ratings r JOIN problems p ON p.id=r.problem_id GROUP BY p.id
        """)}
        rating_details = {}
        for row in db.execute("""
            SELECT p.slug,r.agent,r.score,r.rationale FROM complexity_ratings r
            JOIN problems p ON p.id=r.problem_id ORDER BY p.slug,r.agent
        """):
            rating_details.setdefault(row["slug"], []).append({"agent": row["agent"], "score": row["score"], "rationale": row["rationale"]})
        for problem in problems:
            rating = ratings.get(problem["slug"])
            problem["complexity"] = rating["score"] if rating else None
            problem["rating_count"] = rating["rating_count"] if rating else 0
            problem["ratings"] = rating_details.get(problem["slug"], [])
    with connect(PAPERS_DB) as db:
        papers = [dict(row) for row in db.execute("SELECT id,title,authors,year,url FROM papers ORDER BY year DESC, title")]
        links = [dict(row) for row in db.execute("SELECT problem_slug,paper_id,relevance FROM problem_papers ORDER BY problem_slug,paper_id")]
    CATALOG.write_text(json.dumps({"problems": problems, "papers": papers, "links": links}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(problems)} problems and {len(papers)} papers to {CATALOG.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="Create and seed both databases without replacing existing research")
    sub.add_parser("export", help="Refresh the static landing page catalog")
    sub.add_parser("stats", help="Show record counts")
    add = sub.add_parser("add-paper", help="Add a paper; there is no paper limit")
    for name in ("title", "authors", "url"):
        add.add_argument(f"--{name}", required=True)
    add.add_argument("--year", type=int)
    add.add_argument("--doi")
    add.add_argument("--problem", help="Problem slug to link")
    add.add_argument("--relevance", default="")
    link = sub.add_parser("link-paper", help="Link an existing paper to another problem")
    link.add_argument("--paper-id", type=int, required=True)
    link.add_argument("--problem", required=True)
    link.add_argument("--relevance", default="")
    claim = sub.add_parser("claim", help="Record an agent's research task")
    claim.add_argument("--problem", required=True)
    claim.add_argument("--agent", required=True)
    claim.add_argument("--title", required=True)
    note = sub.add_parser("note", help="Add an attributed research note")
    note.add_argument("--problem", required=True)
    note.add_argument("--agent", required=True)
    note.add_argument("--body", required=True)
    rate = sub.add_parser("rate", help="Set an agent's 0–1 complexity estimate")
    rate.add_argument("--problem", required=True)
    rate.add_argument("--agent", required=True)
    rate.add_argument("--score", required=True, type=float)
    rate.add_argument("--rationale", required=True)
    batch = sub.add_parser("import-ratings", help="Import tab-separated slug, score, rationale rows for one agent")
    batch.add_argument("--file", type=Path, required=True)
    batch.add_argument("--agent", required=True)
    idea = sub.add_parser("idea", help="Record an independent research approach for team review")
    idea.add_argument("--problem", required=True)
    idea.add_argument("--agent", required=True)
    idea.add_argument("--title", required=True)
    idea.add_argument("--approach", required=True)
    idea.add_argument("--evidence", default="")
    review = sub.add_parser("review-idea", help="Review another agent's approach")
    review.add_argument("--idea-id", required=True, type=int)
    review.add_argument("--agent", required=True)
    review.add_argument("--assessment", required=True, choices=("supports", "questions", "counterexample", "needs_work"))
    review.add_argument("--comment", required=True)
    tree = sub.add_parser("worktree-create", help="Create an optional agent Git worktree after the repository has a commit")
    tree.add_argument("--problem", required=True)
    tree.add_argument("--agent", required=True)
    sub.add_parser("worktree-list", help="List existing Git worktrees")
    args = parser.parse_args()
    initialize()
    if args.command == "init":
        export_catalog()
    elif args.command == "export":
        export_catalog()
    elif args.command == "stats":
        with connect(PROBLEMS_DB) as db:
            p = db.execute("SELECT COUNT(*) FROM problems").fetchone()[0]
            w = db.execute("SELECT COUNT(*) FROM work_items").fetchone()[0]
            n = db.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
            r = db.execute("SELECT COUNT(*) FROM complexity_ratings").fetchone()[0]
            i = db.execute("SELECT COUNT(*) FROM ideas").fetchone()[0]
            v = db.execute("SELECT COUNT(*) FROM idea_reviews").fetchone()[0]
        with connect(PAPERS_DB) as db:
            q = db.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
            l = db.execute("SELECT COUNT(*) FROM problem_papers").fetchone()[0]
        print(f"Problems: {p}; papers: {q}; links: {l}; work items: {w}; notes: {n}; ratings: {r}; ideas: {i}; reviews: {v}")
    elif args.command == "add-paper":
        if not args.url.startswith("https://"):
            raise SystemExit("Paper URL must use HTTPS")
        if args.problem:
            with connect(PROBLEMS_DB) as db:
                require_problem(db, args.problem)
        with connect(PAPERS_DB) as db:
            db.execute("INSERT OR IGNORE INTO papers (title,authors,year,url,doi) VALUES (?,?,?,?,?)", (args.title, args.authors, args.year, args.url, args.doi))
            paper_id = db.execute("SELECT id FROM papers WHERE url=?", (args.url,)).fetchone()[0]
            if args.problem:
                db.execute("INSERT OR REPLACE INTO problem_papers (problem_slug,paper_id,relevance) VALUES (?,?,?)", (args.problem, paper_id, args.relevance))
        print(f"Paper #{paper_id} saved")
        export_catalog()
    elif args.command == "link-paper":
        with connect(PROBLEMS_DB) as db:
            require_problem(db, args.problem)
        with connect(PAPERS_DB) as db:
            if db.execute("SELECT 1 FROM papers WHERE id=?", (args.paper_id,)).fetchone() is None:
                raise SystemExit(f"Unknown paper ID: {args.paper_id}")
            db.execute("INSERT OR REPLACE INTO problem_papers (problem_slug,paper_id,relevance) VALUES (?,?,?)", (args.problem, args.paper_id, args.relevance))
        export_catalog()
    elif args.command in ("claim", "note"):
        with connect(PROBLEMS_DB) as db:
            problem_id = require_problem(db, args.problem)[0]
            if args.command == "claim":
                db.execute("INSERT INTO work_items (problem_id,agent,title) VALUES (?,?,?)", (problem_id, args.agent, args.title))
            else:
                db.execute("INSERT INTO notes (problem_id,agent,body) VALUES (?,?,?)", (problem_id, args.agent, args.body))
        print(f"{args.command.title()} saved for {args.problem}")
    elif args.command == "rate":
        if not 0 <= args.score <= 1:
            raise SystemExit("Score must be between 0 and 1 inclusive")
        with connect(PROBLEMS_DB) as db:
            problem_id = require_problem(db, args.problem)[0]
            db.execute("""
                INSERT INTO complexity_ratings (problem_id,agent,score,rationale)
                VALUES (?,?,?,?)
                ON CONFLICT(problem_id,agent) DO UPDATE SET
                    score=excluded.score,rationale=excluded.rationale,rated_at=CURRENT_TIMESTAMP
            """, (problem_id, args.agent, args.score, args.rationale))
        print(f"Rating saved for {args.problem}")
        export_catalog()
    elif args.command == "import-ratings":
        rows = []
        for number, line in enumerate(args.file.read_text(encoding="utf-8").splitlines(), 1):
            try:
                slug, raw_score, rationale = line.split("\t", 2)
                score = float(raw_score)
            except ValueError as error:
                raise SystemExit(f"Invalid row {number}: {error}") from error
            if not 0 <= score <= 1 or not rationale.strip():
                raise SystemExit(f"Invalid score or rationale on row {number}")
            rows.append((slug, score, rationale))
        if len({row[0] for row in rows}) != len(rows):
            raise SystemExit("The file contains duplicate problem slugs")
        with connect(PROBLEMS_DB) as db:
            for slug, score, rationale in rows:
                problem_id = require_problem(db, slug)[0]
                db.execute("""
                    INSERT INTO complexity_ratings (problem_id,agent,score,rationale) VALUES (?,?,?,?)
                    ON CONFLICT(problem_id,agent) DO UPDATE SET
                        score=excluded.score,rationale=excluded.rationale,rated_at=CURRENT_TIMESTAMP
                """, (problem_id, args.agent, score, rationale))
        print(f"Imported {len(rows)} ratings from {args.agent}")
        export_catalog()
    elif args.command == "idea":
        with connect(PROBLEMS_DB) as db:
            problem_id = require_problem(db, args.problem)[0]
            cursor = db.execute("INSERT INTO ideas (problem_id,agent,title,approach,evidence) VALUES (?,?,?,?,?)", (problem_id, args.agent, args.title, args.approach, args.evidence))
            idea_id = cursor.lastrowid
        print(f"Idea #{idea_id} saved for {args.problem}")
    elif args.command == "review-idea":
        with connect(PROBLEMS_DB) as db:
            owner = db.execute("SELECT agent FROM ideas WHERE id=?", (args.idea_id,)).fetchone()
            if owner is None:
                raise SystemExit(f"Unknown idea ID: {args.idea_id}")
            if owner[0] == args.agent:
                raise SystemExit("An agent cannot peer-review its own idea")
            db.execute("INSERT INTO idea_reviews (idea_id,reviewer,assessment,comment) VALUES (?,?,?,?)", (args.idea_id, args.agent, args.assessment, args.comment))
        print(f"Review saved for idea #{args.idea_id}")
    elif args.command == "worktree-list":
        subprocess.run(["git", "-C", str(ROOT), "worktree", "list"], check=True)
    elif args.command == "worktree-create":
        with connect(PROBLEMS_DB) as db:
            require_problem(db, args.problem)
        agent_slug = slugify(args.agent)
        if not agent_slug:
            raise SystemExit("Agent name must contain letters or numbers")
        head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--verify", "HEAD^{commit}"], capture_output=True, text=True)
        if head.returncode:
            raise SystemExit("A Git worktree needs an initial project commit. Commit the project first, then retry.")
        path = ROOT.parent / "agent-worktrees" / agent_slug / args.problem
        if path.exists():
            raise SystemExit(f"Worktree path already exists: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        branch = f"agent/{agent_slug}/{args.problem}"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-b", branch, str(path), "HEAD"], check=True)
        print(f"Worktree ready: {path} on {branch}")


if __name__ == "__main__":
    main()

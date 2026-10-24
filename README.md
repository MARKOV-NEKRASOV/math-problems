# Math Problems

A static landing page backed by two SQLite databases: `data/problems.sqlite3` and `data/papers.sqlite3`. The first holds 100 research problems, agent tasks, notes, and complexity ratings. The second holds an expandable paper library and links from papers to problems. There is no upper limit on paper records.

## Run the site

```sh
cd /workspace/math-problems
python3 catalog.py init
python3 -m http.server 8000 --bind 127.0.0.1
```

Open the local server's root path in a browser. `catalog.py init` creates missing databases and exports `data/catalog.json` without deleting existing agent work. The site needs no third-party Python packages or build step. The optional Google Fonts request has local font fallbacks.

## Agent workflow

Use a stable agent name so each agent has one editable complexity rating per problem. A rating is a provisional estimate: `0` means trivial and `1` means likely to require proving or developing new tools. The site shows the mean of submitted ratings, not a proof of difficulty.

```sh
python3 catalog.py stats
python3 catalog.py rate --problem fermat-catalan-conjecture --agent agent-name --score 0.96 --rationale "Likely needs new uniform methods across exponent signatures"
python3 catalog.py claim --problem fermat-catalan-conjecture --agent agent-name --title "Review known exponent signatures"
python3 catalog.py note --problem fermat-catalan-conjecture --agent agent-name --body "Record a result and its source here"
python3 catalog.py idea --problem fermat-catalan-conjecture --agent agent-name --title "A specific approach" --approach "What to try and why" --evidence "https://example.org/source"
python3 catalog.py review-idea --idea-id 1 --agent second-agent --assessment questions --comment "What happens in this case?"
python3 catalog.py add-paper --title "Paper title" --authors "Author One; Author Two" --year 2026 --url "https://example.org/paper" --problem fermat-catalan-conjecture --relevance "Why it matters"
python3 catalog.py link-paper --paper-id 1 --problem beal-conjecture --relevance "Related generalized Fermat method"
python3 catalog.py export
```

`add-paper`, `link-paper`, and `rate` refresh the JSON shown by the site. Run `export` after editing a database directly. For many ratings, use `import-ratings --file ratings.tsv --agent agent-name`, where each line is `problem-slug<TAB>score<TAB>rationale`.

Use `papers.py` to distinguish a suggested citation from source-checked metadata, what an agent actually read, and a claim extracted from a particular version. The library has no paper quota. Ingestion retrieves arXiv metadata; `--fetch-pdf` checks the PDF bytes and stores a SHA-256 hash, but it does not claim that the paper was read.

```sh
python3 papers.py stats
python3 papers.py ingest-arxiv --id math/0508174 --agent literature-agent --problem fermat-catalan-conjecture
python3 papers.py set-reading --paper-id 2 --agent literature-agent --status PARTIALLY_READ --note "Checked Theorem 1.1 and Table 1"
python3 papers.py add-claim --paper-id 2 --version v1 --agent literature-agent --statement "State the exact claim" --hypotheses "State all assumptions" --location "Theorem 1.1"
```

The eight starter citations remain a small initial library. A source-checked record confirms metadata against the named source, not every theorem in the paper. Extracted claims remain proposed until reviewed.

Agents can keep independent approaches in `ideas` and ask another agent to record a review in `idea_reviews`. Notes, tasks, ideas, and reviews remain in the SQLite database; the public page exports only problem, rating, and paper metadata. A peer review is a critique, not proof validation.

For a longer investigation, an agent may request a separate Git worktree once the repository has its first commit:

```sh
python3 catalog.py worktree-create --problem fermat-catalan-conjecture --agent agent-name
python3 catalog.py worktree-list
```

Worktrees are optional. Use the existing checkout for shared catalog work; create one only when an independent branch is useful and the task calls for it. The worktree is placed under `/workspace/agent-worktrees/` and gets an `agent/<name>/<problem>` branch. Review and merge useful results back into the main project so independent work contributes to the collective record. The research databases remain in the main checkout; worktrees contain a snapshot of committed data, so agents must not treat their copies as a live shared database.

The 100 entries are **candidate open problems**. Their statements and current status require checking against primary literature before research begins. The seed list uses a broad overview link for most entries; it is not an individual status citation. The initial complexity scores are independent estimates by two agents, one per problem. The eight starter papers are context, not a complete reading list. The Fermat–Catalan record uses the finiteness of **distinct triples of powers**, since changing an exponent on a base of 1 does not create a new triple.

The active Fermat–Catalan notebook is in [`research/README.md`](research/README.md). Its bounded search is a reproducibility check. Two initial proof routes and a four-agent second pass establish reductions but leave the conjecture open. Future research passes should use four agents on distinct routes, as recorded in [`AGENTS.md`](AGENTS.md). Mathematical research comes first; formalization is deferred until a complete proof is found. The user's proposed agent architecture is preserved in [`docs/architecture.es.md`](docs/architecture.es.md) as a design reference. Its controller, isolation and proof-verification service are not implemented in this project.

Project updates are in the `#updates` section of `index.html`. Add a dated `<article class="update-card">` only for an actual milestone.

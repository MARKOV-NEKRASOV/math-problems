#!/usr/bin/env python3
"""Source-aware paper ingestion and evidence records for the research library."""

import argparse
import hashlib
import json
import re
import sqlite3
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "data" / "papers.sqlite3"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
ARXIV_ID = re.compile(r"(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?\Z")
READING = ("METADATA_ONLY", "ABSTRACT_READ", "PARTIALLY_READ", "FULL_TEXT_READ")


def ensure_schema(db):
    db.executescript("""
        CREATE TABLE IF NOT EXISTS paper_evidence (
            paper_id INTEGER PRIMARY KEY REFERENCES papers(id),
            identity_status TEXT NOT NULL DEFAULT 'candidate'
                CHECK (identity_status IN ('candidate','source_checked','conflict')),
            reading_status TEXT NOT NULL DEFAULT 'METADATA_ONLY'
                CHECK (reading_status IN ('METADATA_ONLY','ABSTRACT_READ','PARTIALLY_READ','FULL_TEXT_READ')),
            extraction_status TEXT NOT NULL DEFAULT 'none'
                CHECK (extraction_status IN ('none','proposed','source_reviewed','questioned')),
            formal_status TEXT NOT NULL DEFAULT 'none'
                CHECK (formal_status IN ('none','draft','statement_reviewed','proof_accepted')),
            metadata_source_url TEXT,
            reading_note TEXT NOT NULL DEFAULT '',
            checked_at TEXT
        );
        CREATE TABLE IF NOT EXISTS paper_identifiers (
            id INTEGER PRIMARY KEY,
            paper_id INTEGER NOT NULL REFERENCES papers(id),
            scheme TEXT NOT NULL CHECK (scheme IN ('arxiv','doi','other')),
            value TEXT NOT NULL,
            source_url TEXT NOT NULL,
            UNIQUE (scheme,value)
        );
        CREATE TABLE IF NOT EXISTS paper_versions (
            id INTEGER PRIMARY KEY,
            paper_id INTEGER NOT NULL REFERENCES papers(id),
            version_label TEXT NOT NULL,
            url TEXT NOT NULL,
            pdf_url TEXT,
            published_at TEXT,
            updated_at TEXT,
            abstract_text TEXT,
            pdf_sha256 TEXT,
            document_access TEXT NOT NULL DEFAULT 'not_retrieved',
            UNIQUE (paper_id,version_label)
        );
        CREATE TABLE IF NOT EXISTS paper_claims (
            id INTEGER PRIMARY KEY,
            version_id INTEGER NOT NULL REFERENCES paper_versions(id),
            claim_text TEXT NOT NULL,
            hypotheses TEXT NOT NULL,
            location TEXT NOT NULL,
            extraction_status TEXT NOT NULL DEFAULT 'proposed'
                CHECK (extraction_status IN ('proposed','source_reviewed','questioned')),
            agent TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS paper_audit_events (
            id INTEGER PRIMARY KEY,
            paper_id INTEGER NOT NULL REFERENCES papers(id),
            agent TEXT NOT NULL,
            action TEXT NOT NULL,
            detail TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_paper_versions_paper ON paper_versions(paper_id);
        CREATE INDEX IF NOT EXISTS idx_paper_claims_version ON paper_claims(version_id);
    """)
    db.execute("INSERT OR IGNORE INTO paper_evidence (paper_id) SELECT id FROM papers")


def request_bytes(url):
    request = urllib.request.Request(url, headers={"User-Agent": "MathProblemsResearch/1.0 (paper metadata review)"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def parse_arxiv(arxiv_id):
    if not ARXIV_ID.fullmatch(arxiv_id):
        raise SystemExit("Invalid arXiv identifier")
    base_id = re.sub(r"v\d+$", "", arxiv_id)
    query_url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id, safe="/")
    root = ET.fromstring(request_bytes(query_url))
    entry = root.find("a:entry", ATOM)
    if entry is None or entry.findtext("a:title", default="", namespaces=ATOM) == "Error":
        raise SystemExit(f"No arXiv entry found for {arxiv_id}")
    entry_id = entry.findtext("a:id", default="", namespaces=ATOM)
    returned_id = urllib.parse.urlparse(entry_id).path.removeprefix("/abs/")
    if re.sub(r"v\d+$", "", returned_id) != base_id:
        raise SystemExit("arXiv returned an unexpected identifier")
    version_match = re.search(r"(v\d+)$", entry_id)
    version = version_match.group(1) if version_match else "unversioned"
    title = " ".join(entry.findtext("a:title", default="", namespaces=ATOM).split())
    authors = "; ".join(" ".join(author.findtext("a:name", default="", namespaces=ATOM).split()) for author in entry.findall("a:author", ATOM))
    published = entry.findtext("a:published", default="", namespaces=ATOM)
    updated = entry.findtext("a:updated", default="", namespaces=ATOM)
    abstract = " ".join(entry.findtext("a:summary", default="", namespaces=ATOM).split())
    links = entry.findall("a:link", ATOM)
    pdf_url = next((link.attrib["href"] for link in links if link.attrib.get("title") == "pdf"), None)
    doi_url = next((link.attrib["href"] for link in links if link.attrib.get("title") == "doi"), None)
    if not title or not authors or not published:
        raise SystemExit("arXiv metadata is incomplete")
    return {"id": base_id, "version": version, "title": title, "authors": authors, "year": int(published[:4]), "published": published, "updated": updated, "abstract": abstract, "pdf_url": pdf_url, "doi_url": doi_url, "query_url": query_url}


def ingest_arxiv(arxiv_id, agent, fetch_pdf=False, problem=None):
    from catalog import connect, initialize, require_problem
    initialize()
    if problem:
        with connect(ROOT / "data" / "problems.sqlite3") as db:
            require_problem(db, problem)
    entry = parse_arxiv(arxiv_id)
    base_url = "https://arxiv.org/abs/" + entry["id"]
    version_url = base_url + (entry["version"] if entry["version"] != "unversioned" else "")
    pdf_hash = None
    if fetch_pdf and entry["pdf_url"]:
        pdf = request_bytes(entry["pdf_url"])
        if not pdf.startswith(b"%PDF-"):
            raise SystemExit("Retrieved arXiv document is not a PDF")
        pdf_hash = hashlib.sha256(pdf).hexdigest()
    with connect(DB) as db:
        row = db.execute("SELECT paper_id FROM paper_identifiers WHERE scheme='arxiv' AND value=?", (entry["id"],)).fetchone()
        if row:
            paper_id = row[0]
        else:
            row = db.execute("SELECT id FROM papers WHERE url=?", (base_url,)).fetchone()
            if row:
                paper_id = row[0]
            else:
                cursor = db.execute("INSERT INTO papers (title,authors,year,url) VALUES (?,?,?,?)", (entry["title"], entry["authors"], entry["year"], base_url))
                paper_id = cursor.lastrowid
        db.execute("UPDATE papers SET title=?,authors=? WHERE id=?", (entry["title"], entry["authors"], paper_id))
        db.execute("INSERT OR IGNORE INTO paper_identifiers (paper_id,scheme,value,source_url) VALUES (?,?,?,?)", (paper_id, "arxiv", entry["id"], entry["query_url"]))
        if entry["doi_url"]:
            doi = entry["doi_url"].split("doi.org/", 1)[-1]
            existing = db.execute("SELECT paper_id FROM paper_identifiers WHERE scheme='doi' AND value=?", (doi,)).fetchone()
            if existing and existing[0] != paper_id:
                raise SystemExit(f"DOI {doi} is already assigned to paper #{existing[0]}; review before merging")
            db.execute("INSERT OR IGNORE INTO paper_identifiers (paper_id,scheme,value,source_url) VALUES (?,?,?,?)", (paper_id, "doi", doi, entry["query_url"]))
        db.execute("""
            INSERT INTO paper_versions (paper_id,version_label,url,pdf_url,published_at,updated_at,abstract_text,pdf_sha256,document_access)
            VALUES (?,?,?,?,?,?,?,?,?)
            ON CONFLICT(paper_id,version_label) DO UPDATE SET
                url=excluded.url,pdf_url=excluded.pdf_url,published_at=excluded.published_at,
                updated_at=excluded.updated_at,abstract_text=excluded.abstract_text,
                pdf_sha256=COALESCE(excluded.pdf_sha256,paper_versions.pdf_sha256),
                document_access=CASE WHEN excluded.pdf_sha256 IS NOT NULL THEN excluded.document_access ELSE paper_versions.document_access END
        """, (paper_id, entry["version"], version_url, entry["pdf_url"], entry["published"], entry["updated"], entry["abstract"], pdf_hash, "hash_only" if pdf_hash else "not_retrieved"))
        db.execute("INSERT OR IGNORE INTO paper_evidence (paper_id) VALUES (?)", (paper_id,))
        db.execute("""
            UPDATE paper_evidence SET identity_status='source_checked',
                reading_status=CASE WHEN reading_status='METADATA_ONLY' THEN 'ABSTRACT_READ' ELSE reading_status END,
                metadata_source_url=?,checked_at=CURRENT_TIMESTAMP WHERE paper_id=?
        """, (entry["query_url"], paper_id))
        if problem:
            db.execute("INSERT OR IGNORE INTO problem_papers (problem_slug,paper_id,relevance) VALUES (?,?,?)", (problem, paper_id, "Source retrieved from arXiv"))
        db.execute("INSERT INTO paper_audit_events (paper_id,agent,action,detail) VALUES (?,?,?,?)", (paper_id, agent, "ingest_arxiv", json.dumps({"id": entry["id"], "version": entry["version"], "pdf_sha256": pdf_hash})))
    from catalog import export_catalog
    export_catalog()
    print(f"Source-checked paper #{paper_id}: {entry['title']} ({entry['version']})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    ingest = sub.add_parser("ingest-arxiv", help="Retrieve and validate an arXiv record")
    ingest.add_argument("--id", required=True)
    ingest.add_argument("--agent", required=True)
    ingest.add_argument("--problem")
    ingest.add_argument("--fetch-pdf", action="store_true", help="Hash a retrieved PDF without claiming it was read")
    reading = sub.add_parser("set-reading", help="Record how much of a specific paper was read")
    reading.add_argument("--paper-id", required=True, type=int)
    reading.add_argument("--agent", required=True)
    reading.add_argument("--status", required=True, choices=READING)
    reading.add_argument("--note", required=True)
    claim = sub.add_parser("add-claim", help="Record a sourced mathematical claim, not a verified proof")
    claim.add_argument("--paper-id", required=True, type=int)
    claim.add_argument("--version", required=True)
    claim.add_argument("--agent", required=True)
    claim.add_argument("--statement", required=True)
    claim.add_argument("--hypotheses", required=True)
    claim.add_argument("--location", required=True)
    sub.add_parser("stats", help="Show paper provenance counts")
    args = parser.parse_args()
    from catalog import connect, initialize
    initialize()
    if args.command == "ingest-arxiv":
        ingest_arxiv(args.id, args.agent, args.fetch_pdf, args.problem)
    elif args.command == "stats":
        with connect(DB) as db:
            print("Papers:", db.execute("SELECT COUNT(*) FROM papers").fetchone()[0])
            print("Source-checked:", db.execute("SELECT COUNT(*) FROM paper_evidence WHERE identity_status='source_checked'").fetchone()[0])
            print("Versions:", db.execute("SELECT COUNT(*) FROM paper_versions").fetchone()[0])
            print("Extracted claims:", db.execute("SELECT COUNT(*) FROM paper_claims").fetchone()[0])
    elif args.command == "set-reading":
        with connect(DB) as db:
            if db.execute("SELECT 1 FROM papers WHERE id=?", (args.paper_id,)).fetchone() is None:
                raise SystemExit("Unknown paper ID")
            db.execute("UPDATE paper_evidence SET reading_status=?,reading_note=? WHERE paper_id=?", (args.status, args.note, args.paper_id))
            db.execute("INSERT INTO paper_audit_events (paper_id,agent,action,detail) VALUES (?,?,?,?)", (args.paper_id, args.agent, "set_reading", json.dumps({"status": args.status, "note": args.note})))
        from catalog import export_catalog
        export_catalog()
        print(f"Reading status saved for paper #{args.paper_id}")
    elif args.command == "add-claim":
        with connect(DB) as db:
            row = db.execute("SELECT id FROM paper_versions WHERE paper_id=? AND version_label=?", (args.paper_id, args.version)).fetchone()
            if row is None:
                raise SystemExit("Unknown paper version; ingest a source first")
            cursor = db.execute("INSERT INTO paper_claims (version_id,claim_text,hypotheses,location,agent) VALUES (?,?,?,?,?)", (row[0], args.statement, args.hypotheses, args.location, args.agent))
            db.execute("UPDATE paper_evidence SET extraction_status='proposed' WHERE paper_id=? AND extraction_status='none'", (args.paper_id,))
            db.execute("INSERT INTO paper_audit_events (paper_id,agent,action,detail) VALUES (?,?,?,?)", (args.paper_id, args.agent, "add_claim", json.dumps({"claim_id": cursor.lastrowid, "version": args.version, "location": args.location})))
        print(f"Proposed claim #{cursor.lastrowid} saved; it is not a verified proof")


if __name__ == "__main__":
    main()

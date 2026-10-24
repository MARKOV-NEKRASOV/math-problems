# Recent-literature audit: Fermat–Catalan and (3,5,7)

**Checked 23 October 2026 (America/Argentina/Buenos_Aires).** This is a bibliographic and provenance audit, not an independent proof review.

## Peter Chocian, arXiv:2609.26996

- The arXiv API returned **v1**, first posted and last updated **22 September 2026, 19:34 UTC**, title *The Primitive Generalized Fermat Equation x^3+y^5=z^7: A computer-assisted proof*, by Peter Chocian. The Atom record contained no DOI. Its abstract and Theorem 1.1 **claim** that there are no nonzero primitive integer solutions, allowing signs. This would resolve one fixed signature if correct; it would not prove Fermat–Catalan uniformly.
- The v1 PDF, §8.4 (printed p. 19), explicitly states that substantial AI-assisted research and review occurred, and that those reviews **do not constitute independent human peer review or proof-assistant formalization**. This is the manuscript's own status statement. A Crossref bibliographic query did not return a matching journal DOI; that search is not exhaustive, so publication status should be described conservatively as *arXiv preprint with no independently confirmed journal publication here*.
- The manuscript §8.5 identifies a public companion repository `bbpcho/primitive-357`, release tag `replay-companion-2026-09-23.1`, a **298,483,791-byte** archive `PRIMITIVE_357_REPLAY_COMPANION_2026-09-23_V4.zip`, and SHA-256 `ecc39d2944092fc2efbfdd17ffe9861e6c1ca68247b06af80bd7bd4bda166c37`. `git ls-remote --tags` confirmed that tag exists. The repository's `release/SHA256SUMS.txt` repeats the digest, and `release/RELEASE_NOTES.md` describes a claimed fresh replay. I did **not** download or replay the large companion or audit its mathematical acceptance checks. Presence of a tag, hashes, logs, and claims of replay is provenance, not independent proof validation.
- The repository README presently says “The paper has not been submitted to arXiv,” although the arXiv API already shows v1. Treat that sentence as stale repository documentation, not as evidence that the arXiv entry is absent. The more recent arXiv metadata controls the version status.
- Existing `research/literature-survey.md` and the paper DB correctly label the (3,5,7) result as a **preprint claim**, not an established classification. Keep that status until a substantive independent proof and certificate audit has occurred. If the author revises the arXiv paper or companion, record both exact versions and hashes; currently the arXiv API shows v1.

## Additional recent source absent from the database

- **Zeraoulia Rafik**, *Monodromy and Frobenius Splitting Sieves for the Generalized Fermat Equation x^5+y^3=z^7: An Optimized Small-Prime Local Reduction*, Preprints.org DOI [10.20944/preprints202609.1761.v1](https://doi.org/10.20944/preprints202609.1761.v1). Crossref identifies it as posted content created 22 September 2026 UTC and supplies its abstract. Chocian's manuscript references a 21 September posting, consistent with a local-date difference or platform timing; the exact platform timestamp was not separately checked. The work studies monodromy and local splitting sieves, conditionally using Putz's enumeration. Chocian §1 says the sieve still retains an exceptional specialization and proves no final exclusion. It is a **recent related preprint**, not a proof of Fermat–Catalan or of the (3,5,7) signature.
- Chocian's bibliography also cites **Pacetti–Villagra Torcomian**, *On the generalized Fermat equation of signature (5,p,3)*, arXiv:2512.17845v1 (2025), as an imported modularity/conductor source. This identifier is a bibliographic lead for the paper database; I did not independently review its theorem statement in this audit.

## Recommended follow-up

1. Add Rafik's DOI and the Pacetti–Villagra Torcomian arXiv record as **candidate/abstract-level** paper records, keeping distinct preprints and source versions.
2. Check future arXiv versions and journal metadata for 2609.26996; do not automatically promote an updated claim.
3. For genuine proof review, freeze one exact Chocian manuscript and companion release, verify archive bytes, reconstruct the cited inputs, rerun the declared checks, then independently inspect the noncomputational argument and imported theorem hypotheses. This remains undone here.

Sources: [arXiv:2609.26996v1](https://arxiv.org/abs/2609.26996v1); [GitHub companion repository](https://github.com/bbpcho/primitive-357); [Crossref DOI record for Rafik](https://api.crossref.org/works/10.20944/preprints202609.1761.v1); [arXiv:2512.17845v1](https://arxiv.org/abs/2512.17845v1).

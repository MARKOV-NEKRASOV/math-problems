# Adversarial review: attempting to close F2-QR at (2,3,p)

**Superseded finding (30 October 2026):** this review's assertion that Proposition 5.1 of arXiv:2605.02632v1 requires `p∤ab` was incorrect. The printed condition is `p∤2rAB(Aa²+Bb^r)`, which for coefficient-one `p∤c` does not involve input-base divisibility. See the [cycle-14 primary-source correction](branch-14-proof-attempt.md). The text below is retained as an audit history, not the current proof scope.

## Cross-review of the other roles

The factorization B13.1 in [the bounds report](branch-13-factorization.md) is algebraically correct, including the converse parity and gcd claims. Its target equation `(u²)^p+(v²)^p=2w^p` belongs to the classical Darmon–Merel Fermat-variant family; the original theorem's exact scope was unavailable here, so the report does not claim a new unsolved family or a closure. The both-odd valuation B13.2 follows from `v₂(z²+y²)=1` and `min(v₂(z−y),v₂(z+y))=1`; it supplies a lower bound only.

The first draft of geometric G-13 omitted semistability at residual primes with `p|ab`. The cited Proposition 5.1 does not give good reduction there. The [corrected G-13](branch-13-geometric-irreducibility.md) adds `p∤ab`. Under this restriction, Propositions 5.1 and 5.2 cover good or multiplicative reduction above `p`; Proposition 5.6 permits the potentially-good place above 2 when `b` is even. The endomorphism-descent step follows the new paper's own Corollary 6.1 proof; I did not independently reprove that step. Only irreducibility, not absolute irreducibility, is claimed from its printed Theorem 6.1.

**Status 2026-10-25: incomplete; no proof of this F2 branch.** I read `AGENTS.md` and the three mandatory protocol documents. At opening I rechecked the repository's primary-source records for Freitas–Naskręcki–Stoll (FNS) arXiv:1703.05058v3, Bennett–Bruni–Freitas arXiv:1702.07827v1, and the queried Mihăilescu preprint arXiv:2509.18275v1. A closing arXiv ID query returned these same versions. The targeted title query `ti:"Fermat_Catalan"` returned zero entries, so it provides no exhaustive literature claim. Reading here is of the repository's theorem quotations and derivations, not a fresh complete proof audit of the papers.

## Candidate contradiction and failure point

Take positive primitive `a²+b³=c^p`, prime `p→∞`, all bases >1. FNS Lemma 2.3 and Proposition 2.4 (as quoted and checked in `research/all-seven-roughness.md`) put the twisted Frey `p`-torsion on one of seven fixed elliptic curves. At every output prime `q≥5`, `q≠p`, one gets `p | q+1 ± a_q(E_i)`, hence `q≥(√p−1)²`. At every input prime `q≥5` with `p>4√q`, the reduction traces must match exactly up to sign; this gives the verified small-prime exclusions of `research/nonzero-trace-sieve.md`. Thus a hypothetical family needs output primes of increasing size and input residues that evade the listed exclusions.

**The attempted final step** was to infer that the finite comparison-curve list bounds either `c` or the available input prime support. It does not. The congruence at an output prime is a *restriction on primes dividing `c`*, not a statement that only finitely many such primes exist. The input trace conditions are activated only at input primes. For any finite set `S` of primes, put `P=∏_{q∈S}q`, choose `b=1+P>1`, and choose infinitely many `a>1` satisfying `a≡1 (mod Pb)`. Then `gcd(a,b)=1`, no prime of S divides `ab`, and every selector based on `q|a` or `q|b` with `q∈S` is vacuous. These `(a,b)` are not claimed to solve the equation; they prove that selector coverage alone is not an arithmetic forcing theorem. The exact missing lemma would force a solution into an excluded input residue class or give a uniform bound on the surviving comparison branch. Neither appears in the checked sources.

Even `q≥p−2√p+1` at all output primes is compatible with `c` and `p` both growing. The fixed-support Siegel lemma from `research/all-prime-escape-profiles.md` rules out keeping support in a *specified finite set*; moving primes evade it. A bound on the number of support primes would not turn those moving primes into a fixed set. The quantitative sufficient F2 target is `log C≤κ log rad(abc)+o(p)` for some κ<6/5 in this fixed `(2,3)` slice. Nothing in the trace equalities yields this global height upper bound.

## Cross-check of other tempting branch closures

* The known `(2,4,ℓ)` complete family in `research/reduction-to-prime-signatures.md` is valuable but is a composite-exponent reduction, not closure of one of the seven all-prime escape profiles. It cannot be transferred to `(2,3,p)` by replacing exponent 4 with 3.
* BBF Theorem 1.1, arXiv:1702.07827v1, eliminates `(3,3,n)` only in its stated range `3≤n≤10^9`; it is not a uniform `(3,3,p)` closure. The bound is on *n*, not on the bases of a hypothetical solution with `n>10^9`.
* The triangle-cover perfectness/genus theorem needs exact pairwise-coprime finite local-monodromy orders and concerns covers. The HGM route has local types `{q,∞,r}` and does not satisfy its hypothesis. Group perfectness cannot be promoted to nonexistence of Diophantine solutions.
* The Mihăilescu v1 Theorem 1 as printed has the explicit unit counterexample `x=y=z=1,e=0`, so its unspecialized no-solution sentence is unsafe. Even a repaired nonunit statement would need theorem and proof scope rechecked before closing a branch.

## Verdict and falsifiable next step

F2-QR with fixed `(2,3)` remains **OPEN**. No other F2/F1/F0 profile was closed by this audit. A decisive next claim must state and prove either: (i) every sufficiently large-p solution lands in a forbidden FNS branch/residue pattern, covering all seven comparison curves and all input supports; or (ii) an actual height inequality with slope `<6/5` and additive term `o(p)` uniform in a,b,c. Independent review would then recheck the exact FNS twisting, irreducibility, and constants. Nothing here warrants Lean formalization.

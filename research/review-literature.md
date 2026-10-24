# Independent review: varying-exponent survey

**Scope.** I checked `research/literature-survey.md` against the text of Chen–Koutsianas, *Darmon's Program: A survey*, arXiv:2507.15149v1, Section 11, and against two of its underlying cited preprints. These are results about families of fixed-shape signatures, not a proof of Fermat–Catalan. No Lean work was done.

## Confirmed statements and exact hypotheses

- Survey Theorem 11.1 says: for a **fixed regular prime** `r` and prime `p` sufficiently large relative to `r`, `x^p+y^p=z^r` has no **nontrivial primitive integer** solution `(a,b,c)` if `r|ab` and `2∤ab`. This matches the notebook. The original Billerey–Chen–Dieulefait–Freitas 2017 article [18] was not independently read in this review.
- Survey Theorem 11.2 says: for **every integer** `n≥3`, `x^n+y^n=z^5` has no nontrivial primitive integer solution when `(2∤ab, 5|ab)` or `(2|ab, 5∤ab)`. This matches Chen–Koutsianas, *A modular approach to Fermat Equations of signature (p,p,5) using Frey hyperelliptic curves*, arXiv:2210.02316, Theorem 1.1. The notebook correctly retains the divisibility hypotheses. **Precision correction:** there are *two* classes outside that theorem: `10|ab` and `gcd(ab,10)=1`. The original paper, after Theorem 1.2, identifies different obstructions: irreducibility for `10|ab`, and elimination of a CM form for `gcd(ab,10)=1`. The notebook currently mentions only the first class.
- Survey Theorem 11.5 says: for `r∈{5,7,11,13}` and **all integers** `n≥2`, `x^r+y^r=z^n` has no nontrivial primitive integer solution if `2|(a+b)` **or** `r|(a+b)`. This matches the notebook. For `r=11`, Billerey–Chen–Dieulefait–Freitas, *On Darmon's program for the generalized Fermat equation*, arXiv:2205.15861v2, Theorem 1.5, states the same result with `abc≠0` and `gcd(a,b,c)=1`. The cases `r=5,7,13` are reported in the survey but their separate original proofs were not audited here.
- Survey Corollaries 11.4 and 11.8 explicitly assume conjectures from Darmon's program. The notebook correctly marks them conditional.

The notebook's abc calculation is arithmetically correct: `(41/42)(101/100)=4141/4200<1`. Its conclusion depends on the unproved abc hypothesis and remains conditional. Its count of ten known examples is dated to 2024 and was not rechecked against current literature here.

## Recent preprint and exact limit

Peter Chocian, arXiv:2609.26996v1, dated 22 September 2026, states in its abstract and Theorem 1.1 that `x^3+y^5=z^7` has **no nonzero primitive integer solution**, allowing signs. The notebook accurately reports this as a **preprint claim**. I inspected its claim and provenance description, not its certificate archive or the complete 40-plus-page proof. It must not be promoted to an established classification on this review. Even if correct, it settles one exponent signature, not uniform finiteness across signatures.

## Concrete next obligation

The family `a^n+b^n=c^5`, `n≥3`, still has two congruence classes outside the cited unconditional Theorem 11.2: `10|ab` and `gcd(ab,10)=1`. A precise subproblem is to eliminate the CM residual representation in the second class uniformly in `n`, while preserving the full first-class irreducibility issue as a separate obligation. This would close one varying-exponent family but still not the full Fermat–Catalan conjecture. For Theorem 11.5, the cited results leave the case `2∤(a+b)` and `r∤(a+b)`; this is a gap in those theorems, not a claim that no other result treats it.

Sources inspected: https://arxiv.org/pdf/2507.15149v1 (Section 11, Theorems 11.1, 11.2, 11.5); https://arxiv.org/pdf/2210.02316 (Theorems 1.1–1.2 and following discussion); https://arxiv.org/pdf/2205.15861v2 (Theorem 1.5); https://arxiv.org/pdf/2609.26996v1 (abstract and Theorem 1.1).

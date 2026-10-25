# Attempt to prove an infinite escape branch: cycle 13

**25 October 2026. Outcome: incomplete.** Four independent roles tested F2 with fixed `(2,3)` and `(2,r)`, and a signed factorization with fixed `(4,4)`. No full seven-profile branch was proved finite. No Lean formalization was started. The detailed records are the [geometric lemma](branch-13-geometric-irreducibility.md), [bounds and factorization](branch-13-factorization.md), [literature audit](branch-13-literature.md), and [adversarial review](branch-13-adversarial-review.md).

## Strongest proved restricted implication

For fixed odd prime `r≥7`, consider positive primitive `a²+b^r=c^p` with `b` even, `p` prime, and **`p∤ab`**. If `c` has a prime factor `ℓ∤2r`, then for all sufficiently large `p` the residual representation of the Jacobian `J_{2,r}` over `Q(ζ_r)^+` is irreducible. This follows by combining the potentially good reduction at 2 in arXiv:2605.02632v1 Proposition 5.6 with its Theorem 6.1, after checking semistability at every place over `p`. If `supp(c)⊆{2,r}`, the earlier fixed-output-support Siegel lemma gives only finitely many distinct powered-value triples for fixed `r`. The threshold depends on `r`; newform elimination remains undone.

The adversarial review found a material error in the initial stronger claim: when `p|a` or `p|b`, the cited good/multiplicative reduction propositions do not establish semistability above `p`. Those solutions remain outside the lemma. Theorem 6.1 prints *irreducible*, while the paper's Corollary 6.1 prints *absolutely irreducible*; this cycle claims only the former.

## Other proof attempts and quantitative gate

For `(2,3,p)`, the Freitas–Naskręcki–Stoll seven-curve residual comparison forces output primes `q≥5` to satisfy `q≥(√p−1)²` (with the usual `q=p` treatment), and input-prime trace filters exclude certain residue patterns. A hypothetical solution may have larger, moving output primes and evade every finite input-prime selector. Thus neither a fixed support nor a uniform upper bound on `p` follows. To close this pair by the current radical strategy requires an actual bound `log C≤κ log rad(abc)+o(p)` with `κ<6/5`, uniform in the bases; none was found.

For `(p,4,4)`, the opposite-parity factorization reduces `x^p+y^4=z^4` exactly to `(u²)^p+(v²)^p=2w^p`. Its source relationship to the Darmon–Merel variant needs a primary theorem-scope check before treating it as an open or newly closed subcase. For `y,z` both odd, the proved valuation condition `t=max(v₂(z−y),v₂(z+y))≡−2 (mod p)` yields `z>2^(p−3)` for odd `p≥5`. This is a **lower** height bound and permits unbounded `z`. The `(p,4,4)` pair is a slice of F2-QR, not the whole profile.

| Escape profile | This cycle's consequence | Status |
| --- | --- | --- |
| F2-PQ, fixed input exponents | `(2,3,p)` moving-support obstruction persists; restricted `(2,r,p)` irreducibility. | OPEN |
| F2-PR, fixed first and output exponents | No uniform exponent/height bound obtained. | OPEN |
| F2-QR, fixed second and output exponents | `(p,4,4)` factor and 2-adic necessary condition only. | OPEN |
| F1-P, one fixed first exponent | Fixed-`r` constants and field degree do not transfer. | OPEN |
| F1-Q, one fixed second exponent | Same dependence obstruction. | OPEN |
| F1-R, one fixed output exponent | No uniform inequality. | OPEN |
| F0, all exponents grow | No uniform inequality. | OPEN |

## Source and next proof obligation

The literature role upgraded [arXiv:2605.02632v1](https://arxiv.org/abs/2605.02632v1) from abstract-only to checked Theorem 1.3, Corollary 6.1, and surrounding hypotheses. Its coefficient `−5` application and its fixed-`r` irreducibility threshold do not prove the coefficient-one F2 family. Start/end version checks found no changed versions among targeted papers; see the full [source ledger](branch-13-literature.md). The original Darmon–Merel article remains unavailable for exact theorem-scope checking.

**Next falsifiable step:** settle semistability at residual primes `p|ab` in the even-`b` construction, then compute the level-lowered newform list for each fixed `r` and eliminate every comparison form with constants tracked as `r` grows. A remaining ghost form or an unbounded field-dependent constant prevents a branch proof. For `(2,3,p)`, any proposed global conclusion must control moving output-prime support, not just finitely many local traces.

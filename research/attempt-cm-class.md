# Fermat–Catalan subproblem: the untreated coprime-to-10 class of `a^n+b^n=c^5`

**Status:** precise partial analysis; no proof of the family or of Fermat–Catalan.

## What Chen–Koutsianas prove and where this case stops

Let `(a,b,c)` be a nontrivial primitive integer solution of `a^n+b^n=c^5`. Chen–Koutsianas, arXiv:2210.02316v2, Theorem 1.1, exclude the classes `(2∤ab,5|ab)` and `(2|ab,5∤ab)` for every `n≥3`. The two remaining classes are `10|ab` and `gcd(ab,10)=1`. Their introduction (following Theorem 1.2) identifies different obstacles: residual-representation irreducibility in the first, and elimination of a complex-multiplication (CM) form in the second.

For a prime input exponent `p≥11` in the class `gcd(ab,10)=1`, `a,b` are odd, hence `c` is even. After the paper's allowed symmetry, Theorem 8.7 proves that the residual representation on `J5^-(a,b,c)[p]` is irreducible for `p>5` when `a≡−1 (mod 4)`. Section 10, proof of Theorem 1.2, then level lowers its quadratic twists to Hilbert newforms over `K=Q(ζ5)^+=Q(√5)` at levels above 2 and 5. For prime `p≥11`, apart from the paper’s stated exceptional prime `p=19`, the trace comparisons eliminate all but four forms: one at the stated level `q2^2 q5^2` and three at `q2^2 q5^3`. The paper identifies them with Jacobians attached to the **trivial** configurations `(−8,8,0)`, `(−1,1,0)`, `(−4,4,0)`, `(−16,16,0)` (with a quadratic twist for the first). These are not solutions with nonzero `c`, but their residual representations remain compatible with the level-lowering data. Remark 5.7 says the corresponding `J5^±(1,−1,0)` has CM by `Q(ζ5)`; the introduction states the surviving forms are quadratic twists of the CM representation of `J5^-(α,−α,0)`.

Thus the *precise obstruction* is not that irreducibility or modularity fails in this class. It is that the residual representation of a hypothetical nontrivial solution could be isomorphic, up to quadratic twist, to one coming from the CM `c=0` family. Theorem 1.2 and Section 10 are the direct sources for the four surviving forms. Section 9 Remark 9.1 discusses a related trace-comparison obstacle for additional higher-level CM forms. Chen–Koutsianas obtain a full asymptotic exclusion only conditionally on Darmon's Conjecture 4.1 (their Corollary 1.3); the `gcd(ab,10)=1` class needs an unconditional way to separate the representations, or a proof of the relevant conjectural image statement.

## Elementary necessary condition for positive solutions

There is a simple uniform local sublemma, although it does **not** remove the CM obstruction. Suppose `a,b,c>0`, `a,b` odd, and `a^n+b^n=c^5` with `n≥3`.

- If `n` is even, both powers on the left are 1 mod 4, giving `a^n+b^n≡2 (mod 4)`, while the even `c` makes `c^5≡0 (mod 4)`. Hence **`n` must be odd**.
- For odd `n`, the lifting-the-exponent identity for odd `a,b` gives `v₂(a^n+b^n)=v₂(a+b)`. Therefore `v₂(a+b)=5v₂(c)`, a positive multiple of 5; in particular **`32|a+b`**. Since `a+b≡0 (mod 4)`, exactly one of the odd inputs is `−1 mod 4`, so after swapping `a,b`, Theorem 8.7 applies without changing signs.

This is a rigorous necessary condition across all odd `n`. It does not distinguish a putative positive solution from the CM `c=0` comparison family, where `a+b=0` and every such divisibility test holds. Any proposed proof must add an obstruction that separates nonzero `c` from this CM representation, rather than treating `32|a+b` as a contradiction.

## Later work checked

As a literature lead not independently reviewed here, Martin Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2, develops a uniform framework and a Magma elimination package. Its headline Theorem 1.1 handles certain equations with coefficients `7,3` and restrictions, such as `7x^p+y^p=3z^5` when `10|ab` for `p>71`; Theorem 1.2 handles `x^5+7y^5=z^p` variants. These do **not** assert an unconditional solution of the coefficient-one class `a^p+b^p=c^5`. An arXiv query through October 2026 found this work and the 2025 survey but no directly stated later theorem closing the unit-coefficient CM case; this search is not exhaustive.

**Next mathematical obligation:** For prime `p` beyond the finite exceptional range in Chen–Koutsianas Section 10, prove that the residual representation of a nontrivial primitive solution with `gcd(ab,10)=1` cannot be a quadratic twist of `J5^-(α,−α,0)[p]`. One would need a new unconditional image or rational-point argument, or an explicit distinguishing invariant that remains nonzero on every nontrivial solution and vanishes on the CM comparison family. The elementary valuation constraint is a useful filter, not such an invariant.

Primary sources: https://arxiv.org/pdf/2210.02316v2 (Theorems 1.1, 1.2, 8.7, Section 10, Remark 5.7 and Section 9 Remark 9.1); https://arxiv.org/pdf/2504.01967v2 (Theorems 1.1–1.2).

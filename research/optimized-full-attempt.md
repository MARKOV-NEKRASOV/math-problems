# Optimized attempt at the full Fermat–Catalan conjecture

**Subsequent progress:** A [primary-source-backed reduction](reduction-to-prime-signatures.md) now proves that the variable `(2,4,ℓ)` family contributes finitely many powered triples. Only the all-prime hyperbolic bucket remains as an infinite exponent class in this reduction.

**Status: incomplete.** Four agents pursued a contradiction from an infinite solution family, a sharper exponent reduction, height and prime-support estimates, and a uniform elliptic-curve construction. The deductions have independent reviews. None proves finiteness of all distinct powered-value triples.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, where the positive bases are coprime, `p,q,r≥2`, and `1/p+1/q+1/r<1`. The conjecture asks for finitely many **distinct `(A,B,C)`**, as the exponents vary.

| Route | Rigorous progress | Unclosed step |
| --- | --- | --- |
| [Irreducible signatures](optimized-signatures.md), [review](review-optimized-signatures.md) | Every eligible powered triple has a representation with either an all-prime hyperbolic signature, `(2,4,ℓ)` for prime `ℓ≥7`, or one of 19 fixed composite-containing signatures. Fixed-signature finiteness handles the 19 cases. | The union over all-prime signatures and `(2,4,ℓ)` still ranges over infinitely many exponents. |
| [Infinite-family contradiction](optimized-contradiction.md), [review](review-optimized-contradiction.md) | An infinite solution family would have unbounded height, largest supporting prime, and reduced prime exponent. It would also violate the abc inequality at `ε=1/42`, with `C/R^(43/42)>R^(1/1722)→∞`. | The relevant abc inequality remains unproved; no unconditional theorem excludes such a family. |
| [Height and support optimization](optimized-heights.md), [review](review-optimized-heights.md) | Under the reported Stewart–Yu bound, `R>c(log C)^3/(loglog C)^9`. If support size `s→∞` and `m=min(p,q,r)`, then `m s log s≤(3+o(1))log C`. | These constraints permit moving prime support and increasing exponents. The exact Stewart–Yu formula was checked only against a secondary source here. |
| [Universal elliptic curve](optimized-descent.md), [review](review-optimized-descent.md) | The curve `Y²=X(X−A)(X+B)` has `j>1728` and odd bad-prime support equal to the odd part of `rad(ABC)`. Its reduced rational `j` denominator grows at least as `(ABC)²/256`. | Real `j` bounds do not bound rational height, and fixed-bad-prime finiteness does not control changing prime sets. |

The exponent reduction is the strongest unconditional simplification from this pass. Its 19 fixed signatures include three excluded outright by Fermat's Last Theorem; keeping them in the finite bucket makes the reduction clean. The irreducible signature classification does not claim a solution for any listed signature. It only narrows the uniform part of the conjecture to two infinite classes.

The contradiction route gives a particularly sharp conditional implication: if an infinite family existed, a single fixed-`ε` abc bound would fail by an unbounded factor. This is not itself a contradiction because the abc bound is conjectural. The unconditional height estimate falls far short of the power-scale radical bound needed to close it.

**Remaining proof obligation:** establish uniform finiteness across all-prime hyperbolic signatures and `(2,4,ℓ)` as `ℓ` varies, or find another unconditional argument bounding all powered-value triples. No complete mathematical proof emerged, so no Lean formalization was started.

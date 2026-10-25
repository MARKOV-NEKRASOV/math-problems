# Integrated attempt at a full Fermat–Catalan proof

**Outcome: a stronger unconditional reduction, no full proof.** This pass combined the project's exponent classification, prime and Gaussian descents, fixed-family theorems, and the universal elliptic-curve height calculation. It proves that the full conjecture is **equivalent to finiteness over all-prime hyperbolic exponent signatures**. It does not establish that remaining finiteness.

The conjecture counts distinct powered triples `(A,B,C)=(x^p,y^q,z^r)` with `A+B=C`, positive primitive bases, exponents at least 2, and `1/p+1/q+1/r<1`. Every eligible triple has an irreducible representation in one of three classes: an all-prime signature, an unordered `(2,4,ℓ)` for prime `ℓ≥7`, or one of [19 fixed composite-containing signatures](optimized-signatures.md). Darmon–Granville handles the 19 fixed signatures.

## Closing the `(2,4,ℓ)` branch

An orientation check matters because the exponents include even entries. For positive `X²+Y^ℓ=Z⁴` and `X⁴+Y^ℓ=Z²`, factor the difference of squares `H²−K²=Y^ℓ`. When `H,K` have opposite parity, its two coprime factors are signed `ℓ`th powers and give `u^ℓ+v^ℓ=2w²`. Bennett–Skinner Theorem 1.1 excludes this for prime `ℓ≥7`. When both are odd, their gcd is 2 and the equation reduces to `u^ℓ+2^(ℓ−2)v^ℓ=w²`. Bennett–Skinner Theorem 1.2 excludes the nonunit cases; the possible unit cases fail by a square congruence or `(w−1)(w+1)=2^(ℓ−2)`. These theorems cover signed integers, so `X⁴+Y^ℓ=Z²` is covered as well by rewriting it as `Z²+(-Y)^ℓ=X⁴`.

The last orientation, `X²+Y⁴=Z^ℓ`, is excluded by Ellenberg Theorem 4.1 for `ℓ≥211`. Finitely many prime exponents `7≤ℓ<211` remain, and each has finitely many primitive solutions by Darmon–Granville. Thus the **whole variable `(2,4,ℓ)` family contributes finitely many powered triples**. The [full proof of this reduction](reduction-to-prime-signatures.md) and [independent review](review-reduction-to-prime-signatures.md) audit all parity, sign, unit, and orientation cases. The paper library records the exact publisher and arXiv versions and theorem hypotheses.

## Attempting to close the all-prime branch

Hyperbolicity forbids two exponent-2 entries, and Fermat's Last Theorem forbids three equal odd primes. Bennett–Skinner Theorem 1.1 with coefficient 1 excludes repeated odd prime powers when the third exponent is 2. Poonen–Schaefer–Stoll historically lists the repeated-prime family with third exponent 3 as determined, but its underlying exception list was not needed for the reduction here. The unresolved moving-prime cases include `(3,3,t)`, `(p,p,t)` with distinct odd primes `p,t≥5`, and pairwise-distinct-prime signatures such as `(2,3,t)` for prime `t≥7`.

For repeated odd prime `p`, the [cyclotomic descent](full-prime-descent.md) gives `a^p+b^p=(a+b)V` and `gcd(a+b,V)|p`. Outside `p|(a+b)`, both factors must be perfect powers of the third exponent. For `p∈{5,7,11,13}`, the source-checked survey Theorem 11.5 excludes `2|(a+b)` and `p|(a+b)`; any survivor has odd `a+b` coprime to `p`, with both factors perfect powers. This is a sharper subcase, but it does not show those cofactor equations have no solutions. Pairwise-distinct primes offer no comparable factorization. The earlier [prime-route review](review-full-prime-descent.md) confirms the valuation algebra.

Suppose infinitely many all-prime powered triples nevertheless exist. Their heights `C` and largest supporting prime escape every fixed bound, while `R=rad(ABC)<C^(41/42)`. The universal Frey curve `E:Y²=X(X−A)(X+B)` has [exact rational height](full-height-conductor.md) `h(j)=6log C+O(1)` and conductor `N(E)≤K₂R`, yielding `h(j)>(252/41)log N(E)−O(1)`. The [independent review](review-full-height-conductor.md) checks the algebra. An unconditional upper height–conductor bound of slope below `252/41` for this family would contradict an infinite sequence. No such bound has been established here. The available unconditional radical bound remains only polylogarithmic in `C`; the [contradiction attempt](full-radical-contradiction.md) and [review](review-full-radical-contradiction.md) show why it is compatible with infinitely many hypothetical solutions.

## What the combined work proves and what it does not

The finite composite-containing signatures and the variable `(2,4,ℓ)` family are controlled by established fixed-signature and family theorems. **The full Fermat–Catalan conjecture now reduces to all-prime hyperbolic signatures**, including infinitely many pairwise-distinct-prime signatures. Fixed-signature finiteness, the cyclotomic cofactor conditions, and the height–conductor lower bound do not bound their union. Treating an unproved abc-strength inequality or an unproved uniform family exclusion as a lemma would make the argument circular.

No complete mathematical proof emerged. Under the user's preference, no Lean formalization was started.

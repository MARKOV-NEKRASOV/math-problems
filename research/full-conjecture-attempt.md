# Attempt to prove the full Fermat–Catalan conjecture

**Outcome: incomplete.** Four agents tried routes intended to handle *every* hyperbolic exponent signature. Each deduction below was checked by a different agent. None proves that only finitely many distinct powered-value triples exist.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, with positive primitive bases, exponents greater than 1, and `σ=1/p+1/q+1/r<1`. The target counts distinct `(A,B,C)`, so changing an exponent on a base of 1 does not create a new solution.

## What the attempt establishes

1. **All signatures have a canonical representation.** Every exponent at least 7 has a divisor that is prime at least 7 or one of `{8,9,10,12,15,25}`. Reducing all three exponents at once preserves the powered values, primitivity, and `σ<1`. Thus it suffices to consider exponents in `{2,3,4,5,6,8,9,10,12,15,25}` together with primes at least 7. The [derivation](whole-exponents.md) and [review](review-whole-exponents.md) are explicit. This set is infinite; `(2,3,ℓ)` remains for every prime `ℓ≥7`.
2. **Height estimates restrict hypothetical large solutions but do not exclude them.** With `R=rad(ABC)`, every solution satisfies `R<C^σ≤C^(41/42)`. The reported Stewart–Yu estimate implies `R>c(log C)^3/(loglog C)^9` for large `C`, hence `min(p,q,r)≤(1+o(1))log C/loglog C`. The [derivation](whole-height.md) and [review](review-whole-height.md) state the exact source limitation: the displayed Stewart–Yu formula was corroborated through a secondary source because the original article was inaccessible. The upper and lower radical bounds remain compatible as `C` grows.
3. **A uniform polynomial analogue is true.** Mason–Stothers implies there are no nonconstant primitive polynomial solutions to `x^p+y^q=z^r` over a characteristic-zero field when `σ<1`. The [proof](whole-geometry.md) and [review](review-whole-geometry.md) cover all signatures simultaneously. The polynomial degree argument does not give the needed integer height bound; infinitely many integer solutions would not automatically interpolate to one polynomial family.
4. **One universal modular strategy stalls.** For `E: Y²=X(X−A)(X+B)`, direct calculation gives `Δ=16A²B²C²`. At primes at least 5 dividing a base, residual inertia is controlled by the corresponding exponent and base valuation. A single modulus does not yield an *exponent-only guarantee* that removes all variable base primes for gcd-one signatures. The [calculation](whole-modular.md) and [review](review-whole-modular.md) do not rule out different Frey objects or simultaneous modular methods.

## The unclosed step

All four routes stop at the same global obligation: prove a bound on the powered values or a uniform finiteness theorem across the infinite set of canonical signatures. Darmon–Granville supplies finiteness for each fixed hyperbolic signature, which does not bound their union. The unproved abc conjecture would give such a bound, but it cannot be used as an established step.

No complete mathematical proof emerged. In accordance with the user's preference, no Lean formalization was started.

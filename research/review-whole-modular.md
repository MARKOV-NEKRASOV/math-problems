# Peer review of the universal modular attempt

**Verdict:** The Frey-curve invariants and local valuation argument are correct, and the note honestly identifies a failure of one simple bounded-level strategy. It does not prove Fermat–Catalan or rule out more sophisticated modular methods. Two sentences need to be narrowed so that a necessary exponent-only criterion is not presented as a necessary condition for every individual solution.

## Checked calculations

For `E:Y²=X(X−A)(X+B)=X³+(B−A)X²−ABX`, direct invariant formulas give `c₄=16(A²+AB+B²)` and `Δ=16A²B²(A+B)²`. Positivity makes the roots distinct. From primitive `A+B=C`, the three powered values are pairwise coprime. At a prime `t≥5` dividing exactly one of `A,B,C`, the reduction of `c₄/16` is respectively `B²`, `A²`, or `A²`, so `c₄` is a `t`-unit. The displayed integral model is minimal with multiplicative reduction, and the three valuations `2p v_t(x)`, `2q v_t(y)`, `2r v_t(z)` are correct. Unit bases simply contribute no primes; the formulas still hold for every prime that does occur.

For `t≥5`, `t≠ℓ`, and prime `ℓ≥3`, the standard Tate-curve exact sequence `0→μ_ℓ→E[ℓ]→Z/ℓ→0` gives trivial residual inertia exactly when `ℓ` divides the minimal discriminant valuation; the nonsplit quadratic twist is unramified at a multiplicative prime and does not change this criterion. Hence the local calculation is a valid **necessary condition for deleting each such prime from the residual conductor**. It is not, by itself, a complete level-lowering theorem: irreducibility and the global modular/level-lowering hypotheses must also be checked. The prime `t=ℓ` and primes `2,3` are outside this criterion and need separate handling.

## Qualification of the failed-step claim

The sentence “the same `ℓ` would need to divide `p,q,r`” is valid only for an **exponent-only guarantee** that deletes primes from every possible non-unit base independently of its valuations. It is not necessary for an individual candidate: when `ℓ∤p`, all primes `t≥5` of `x` might nevertheless have `ℓ|v_t(x)`, or `x=1` might have no supporting prime at all. The later phrase “whenever their valuations are not accidentally multiples of `ℓ`” acknowledges this, but the earlier absolute wording should match it. A replacement is: “For this local criterion to remove all possible base primes uniformly from exponent data alone, one would require `ℓ|p,q,r`. Actual solutions may have extra divisibility in their base valuations or unit bases.”

If an odd `ℓ` did divide all three exponents, Fermat's Last Theorem would indeed exclude positive solutions. Therefore the *simple exponent-only, single-ℓ* path cannot settle the conjecture. This does not prove that no fixed-level representation is possible for a particular candidate via special valuation patterns or a different Frey object. `E[2]` really is the constant trivial Galois module because all three nonzero 2-torsion points have rational coordinates; it cannot distinguish solutions by itself, although a 2-adic or other object might.

The note's `gcd(p,q,r)=1` paragraph should say variable primes **may** remain in the conductor, unless base valuations satisfy additional divisibility. It cannot assert they must remain for every solution. The example `13²+7³=2⁹` correctly refutes elimination of all gcd-one signatures. The tailored `(2,3,ℓ)` Frey program is an appropriate example of how the universal curve's obstacle can be bypassed in one family without proving the full conjecture.

**Unresolved global obligation:** establish a bound or uniform contradiction across all hyperbolic signatures, possibly using different Frey objects or simultaneous representations. The local calculation supplies neither that theorem nor a full proof.

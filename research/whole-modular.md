# Attempt at the full Fermat–Catalan conjecture: a universal modular route

**Outcome:** No proof. The universal Frey curve gives a clean obstruction to the simplest bounded-level strategy across all exponent signatures. This is a failure diagnosis of one proof route, not a theorem ruling out every modular or multi-Frey method.

## Exact target

For positive pairwise-coprime bases `x,y,z`, exponents `p,q,r>1`, and `1/p+1/q+1/r<1`, let `A=x^p`, `B=y^q`, `C=z^r=A+B`. The conjecture counts distinct `(A,B,C)`. Primitivity `gcd(x,y,z)=1` plus the equation makes the bases, and hence `A,B,C`, pairwise coprime.

## A universal Frey curve and its local data

Attach the elliptic curve

`E_(A,B): Y²=X(X−A)(X+B)`.

The three roots `0,A,−B` are distinct because `A,B,C>0`, so `E` is nonsingular and has full rational 2-torsion. Direct Weierstrass invariant calculation gives

`Δ(E)=16 A²B²C²`, `c₄(E)=16(A²+AB+B²)`.

Let `t≥5` be a prime dividing `ABC`. Pairwise coprimality means it divides exactly one of `A,B,C`. In each case `c₄` is a `t`-adic unit: modulo `t` the quadratic expression reduces to `B²`, `A²`, or `A²`, respectively. Thus the displayed integral model is minimal at `t` and has multiplicative reduction, with

- `v_t(Δ)=2p·v_t(x)` if `t|x`;
- `v_t(Δ)=2q·v_t(y)` if `t|y`;
- `v_t(Δ)=2r·v_t(z)` if `t|z`.

For another prime `ℓ≥3`, `ℓ≠t`, the standard Tate-curve description of `E[ℓ]` says its inertia at this multiplicative prime is unipotent and is trivial exactly when `ℓ|v_t(Δ)`. This criterion is the same local mechanism used in Frey-curve level lowering; compare Poonen–Schaefer–Stoll §4 (multiplicative reduction from unit `c₄`) and Freitas–Naskręcki–Stoll Proposition 5.4 (Tate-curve torsion action). At `t≥5`, `ℓ≥3`, the factor 2 is irrelevant, so primes dividing a base can be removed uniformly by the ordinary mod-`ℓ` level-lowering step only when `ℓ` divides the corresponding exponent.

## End-to-end route attempted and where it fails

A tempting proof would select one prime `ℓ`, lower `E[ℓ]` to a bounded list of modular levels independent of `x,y,z`, then rule out the resulting representations or rational points uniformly. For the Tate valuation criterion to remove all possible variable base primes using exponent data alone, the same `ℓ≥3` would need to divide `p,q,r`. An individual solution may have extra divisibility in its base valuations or a unit base, so this is a sufficient condition for that exponent-only strategy, not a necessary condition for every candidate. If such an odd common divisor exists, writing `X=x^(p/ℓ)`, `Y=y^(q/ℓ)`, `Z=z^(r/ℓ)` gives `X^ℓ+Y^ℓ=Z^ℓ`, already impossible by Fermat's Last Theorem. Hence in every actual candidate solution no odd prime divides all three exponents.

If `gcd(p,q,r)=1`, each choice of `ℓ≥3` may leave at least one base's prime divisors in the residual conductor when their valuations are not accidentally multiples of `ℓ`. Their values and number are not bounded by the signature alone; the bounded-level conclusion does not follow. If `gcd(p,q,r)=2`, one can take `ℓ=2`, but this particular curve has **full rational 2-torsion**, so `E[2]` is the same trivial Galois module for every candidate and cannot distinguish a solution. A different Frey object or a genuinely simultaneous argument would be required.

Using three residual representations modulo primes dividing `p`, `q`, and `r` does not immediately fix the issue. Each representation still retains the variable primes from at least one of the other bases; no theorem cited here combines those three unbounded levels into a uniform contradiction. This is the precise failed step, not a proof that such a theorem is impossible.

The failure is consistent with the known positive identity `13²+7³=2⁹`, whose exponents have gcd 1. A blanket claim that gcd-one signatures can be eliminated would contradict an actual solution. It is also consistent with the successful but restricted `(2,3,ℓ)` modular program: Freitas–Naskręcki–Stoll use a specially tailored Frey curve and reduce to seven fixed elliptic curves, yet still do not classify all prime `ℓ` uniformly.

## What a complete modular proof would need

A complete route would need a family of Frey objects or a new uniform theorem that either bounds the exponent signatures/height, or controls the surviving rational points and residual representations **for every hyperbolic signature**, including gcd-one signatures. The local calculations above do not supply that global theorem. No Lean formalization was attempted because no complete mathematical proof was found.

**Sources:** Poonen–Schaefer–Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, [arXiv:math/0508174](https://arxiv.org/abs/math/0508174), §§1.2, 4; Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, [arXiv:1703.05058](https://arxiv.org/abs/1703.05058), Lemma 2.3, Proposition 5.4; Chen–Koutsianas, *Darmon's Program: A survey*, [arXiv:2507.15149](https://arxiv.org/abs/2507.15149), §11 on restricted multi-Frey families. Invariants of the displayed universal curve are computed directly above; the local Tate criterion is invoked as an established theorem, not newly proved here.

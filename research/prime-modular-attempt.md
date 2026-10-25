# Full Fermat–Catalan attempt via modular uniformity after prime-signature reduction

**Outcome: incomplete.** The established reduction leaves only all-prime hyperbolic signatures as a variable-signature obligation. I tested whether modularity plus known finiteness theorems yields a uniform proof. It does not. The route does produce a precise conditional closing lemma for the `(2,3,ℓ)` subfamily and locates the missing theorem.

## Precise target and a natural subfamily

Let `A=x^p`, `B=y^q`, `C=z^r=A+B` with positive primitive bases, primes `p,q,r≥2`, and `1/p+1/q+1/r<1`. Count distinct powered triples `(A,B,C)`. The fixed composite-containing signatures and variable `(2,4,ℓ)` class were handled in the prior source-checked reduction, so full finiteness requires a bound across all-prime signatures. In particular, one needs uniform finiteness for `a²+b³=c^ℓ` as prime `ℓ≥7` varies.

The Frey curve from Freitas–Naskręcki–Stoll for this subfamily is

`E_(a,b): v²=u³+3bu−2a`, with `Δ=−2⁶3³c^ℓ`, `c₄=−2⁴3²b`, and `j=1728 b³/c^ℓ`.

For nontrivial primitive signed solutions and prime `ℓ≥11`, their Proposition 2.4 gives irreducibility of `E[ℓ]`. Their Lemma 2.3 then attaches, after one of the finite quadratic twists `d∈{±1,±2,±3,±6}`, an `ℓ`-torsion representation isomorphic to one of seven fixed rational elliptic curves `27a1,54a1,96a1,288a1,864a1,864b1,864c1`. Poonen–Schaefer–Stoll handles the fixed prime `ℓ=7`. This is a real uniform *first* modular step: the comparison curves do not vary with `ℓ`.

## Attempted closing step: a fixed-curve Frey–Mazur principle

Suppose one could prove the following additional uniform assertion for the seven comparison curves and their finite twists: there is an absolute `L` such that if `ℓ>L` and a rational elliptic curve `E` has `E[ℓ]` isomorphic to the `ℓ`-torsion of one of them, then `E` is `Q`-isogenous to that fixed curve. Apply this to the finite twists of the Frey curve; quadratic twisting does not change `j`. This is a **Frey–Mazur-type statement, not an established input in this notebook**.

Under that assertion, there are only finitely many possible `Q`-isomorphism classes, hence finitely many rational `j(E)` values, because a rational isogeny class has finitely many members up to `Q`-isomorphism. A positive solution has `c≥2` and `gcd(b,c)=1`; therefore the denominator of reduced `j(E)=1728 b³/c^ℓ` is

`c^ℓ / gcd(c^ℓ,1728) ≥ 2^ℓ/1728`.

A fixed finite set of rational `j` values has bounded denominators, so `ℓ` would be bounded. Fixed-signature Darmon–Granville finiteness would then finish the `(2,3,ℓ)` subfamily. Every step after the hypothetical fixed-curve Frey–Mazur assertion is elementary or a standard fixed-signature theorem. The assertion itself is unproved here, and using it as though it were known would be a circular or conditional proof. Moreover, even this conditional argument covers only the `(2,3,ℓ)` family, not pairwise-distinct-prime signatures in general.

## Why available rational-point theorems do not substitute

The level-lowering reduction leads to twists of the full-level modular curve `X(ℓ)` for each prime `ℓ`; their genera grow and their rational points vary. Faltings gives a finite rational-point set for each fixed curve, but a union over infinitely many `ℓ` can still be infinite. Even a uniform *number* of points per curve would not rule out one exceptional positive solution on every curve. As a simple logical model, curves `Y²=X^(2n+1)+1` have growing genus yet each has the rational point `(0,1)`; genus growth alone cannot provide the required cross-curve finiteness. The model is not asserted to correspond to primitive nonunit Fermat–Catalan triples.

There is an additional obstruction for a single universal Frey curve across arbitrary all-prime signatures. For `E:Y²=X(X−A)(X+B)`, at odd `t|ABC` distinct from the selected residual modulus, multiplicative reduction gives `v_t(Δ_min)=2e_t v_t(base)` with `e_t` equal to the prime exponent of that supporting coordinate. A mod-`p` residual representation removes its base primes uniformly only when the selected modulus `p` divides that coordinate's exponent. With three distinct prime exponents, one modulus leaves moving primes from other coordinates in the level. Simultaneous use of three moduli has no established theorem combining those moving levels into a contradiction. This diagnoses the limitation of this particular modular strategy, not of every possible Frey object.

## Exact gap

To finish the full conjecture through this route one needs a new unconditional theorem controlling rational points or residual representations **uniformly over all-prime signatures**, including pairwise-distinct primes. The known seven-curve reduction for `(2,3,ℓ)` and fixed-curve Faltings finiteness do not do so. A Frey–Mazur-type assertion would close one infinite subfamily, but is unproved here and does not by itself cover the rest. No full proof emerged, so no Lean formalization was attempted.

**Sources:** Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4; Poonen–Schaefer–Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, arXiv:math/0508174, Theorem 1.1; the project's independently reviewed `attempt-modular-uniform.md` and `whole-modular.md` for source and local-data checks. The fixed-curve Frey–Mazur premise is explicitly hypothetical.

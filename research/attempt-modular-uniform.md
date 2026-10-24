# Fermat–Catalan research attempt 2: the varying `(2,3,ℓ)` signatures

**Status (24 October 2026): no unconditional proof.** I examined the modular/descent route for the infinite family

`a² + b³ = c^ℓ`, where `ℓ≥7` is prime and `gcd(a,b,c)=1`.

The original Fermat–Catalan problem permits positive bases; the cited modular papers study the stronger signed-integer equation. A theorem for all signed primitive solutions would cover positive solutions, but a signed Catalan solution itself is not a positive solution.

## A valid uniform first reduction

Attach to a solution the Frey curve

`E_(a,b): v² = u³ + 3bu − 2a`.

For a short Weierstrass curve, `Δ = −16(4(3b)³ + 27(−2a)²)`, so here

`Δ(E_(a,b)) = −2⁶3³(a²+b³) = −2⁶3³c^ℓ`, `c₄=−2⁴3²b`, and `j(E_(a,b))=1728b³/c^ℓ`.

These identities are unconditional and valid for every prime `ℓ≥7`. At each prime `q≥5` dividing `c`, the discriminant valuation is a multiple of `ℓ`; this is the key input for level lowering after the necessary local and irreducibility checks. Freitas–Naskręcki–Stoll, Lemma 2.3, proves the precise result: if the `ℓ`-torsion representation is irreducible, some quadratic twist of this Frey curve has `ℓ`-torsion isomorphic to that of one of **seven fixed elliptic curves**, labeled `27a1, 54a1, 96a1, 288a1, 864a1, 864b1, 864c1`. The allowed quadratic twists use `d∈{±1,±2,±3,±6}`. They prove irreducibility for nontrivial primitive integer solutions with prime `ℓ≥11` (Proposition 2.4), and cite Poonen–Schaefer–Stoll for `ℓ=7`. This is genuinely uniform in the prime exponent, but it supplies candidate representations, not a contradiction.

For a **positive** solution, `0<b³<c^ℓ`, hence the associated rational `j`-invariant obeys `0<j<1728`. This extra necessary real condition could help filter rational points, but congruence of `ℓ`-torsion does not identify the two curves' `j`-invariants or preserve that interval.

## Where the descent stops

The fixed curves lead to symplectic and antisymplectic twists `X_E⁺(ℓ)` and `X_E⁻(ℓ)` of the full-level modular curve `X(ℓ)`. A putative solution produces a rational point on a relevant twist, subject to local conditions at 2 and 3. For prime `ℓ≥11`, Freitas–Naskręcki–Stoll narrow the list to **four to ten twists depending on `ℓ mod 24`** (their Table 4). The remaining task is to determine the relevant rational points for all primes `ℓ`; the twists and their genera vary with `ℓ`. Finiteness of rational points separately for each `ℓ` does not give a uniform bound or a finite union.

The obstruction is concrete. The signed solution `3²+(−2)³=1^ℓ` exists for *every* prime `ℓ`, and its Frey curve is nonsingular. Thus at least some candidate residual representations come from actual solutions at every exponent; one cannot dismiss all candidate newforms by a generic level-lowering contradiction. It also shows why counting exponent tuples instead of distinct powered-value triples would misstate Fermat–Catalan. Positivity excludes this particular signed solution, but excluding its residual representation would also exclude a representation known to exist; a separate argument would have to distinguish a hypothetical positive Frey curve within that residual class.

The progression in the sources demonstrates the remaining difficulty. Poonen–Schaefer–Stoll determine the signed primitive solutions for `ℓ=7`. Freitas–Naskręcki–Stoll determine them for `ℓ=11` **assuming GRH** and give partial results for `ℓ=13`. Their `ℓ=11` computation requires Selmer-group Chabauty on points over degree-12 fields; GRH is used for class-group computations in degree-36 fields. Their paper does not claim a uniform classification over all `ℓ`.

A December 2025 preprint by Freitas–Mocanu–Sánchez-Rodríguez makes a narrower but instructive advance: it rules out certain *antisymplectic* twists for listed `(E,ℓ)` pairs, including some primes `ℓ≡19 (mod 24)`. Its Theorem 3.1 says that for each remaining Table 1 pair `(E,ℓ)`, at every prime `q>3`, `q≠ℓ`, a nonempty local antisymplectic twist has a point arising from a `q`-adic primitive solution. This shows the limitation of using independent local exclusions at good primes for those twists. It **does not** assert that such local solutions glue to a global positive integer solution, nor that all global methods fail.

## Exact next obligation

Prove, uniformly over prime `ℓ≥7`, that every relevant rational point on the surviving modular twists either comes from a known signed solution or violates the positivity and integrality constraints; alternatively derive a uniform bound on `ℓ` or on `c`. The Frey-curve identities, level lowering to seven fixed curves, and local refinements stop short of this global statement. No step above yields such a bound, so this attempt remains partial.

## Primary sources checked

1. Poonen, Schaefer, and Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, Duke Math. J. 137 (2007), [arXiv:math/0508174](https://arxiv.org/abs/math/0508174), Theorem 1.1 and §§1.2–1.3.
2. Freitas, Naskręcki, and Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), [arXiv:1703.05058](https://arxiv.org/abs/1703.05058), abstract, §§1–2 (especially Lemma 2.3 and Proposition 2.4), Table 4, Theorem 1.4. The stated `ℓ=11` solution is conditional on GRH.
3. Freitas, Mocanu, and Sánchez-Rodríguez, *Revisiting the equation x²+y³=zᵖ*, preprint dated 11 December 2025, [arXiv:2512.10781](https://arxiv.org/abs/2512.10781), Theorems 1.2 and 3.1.

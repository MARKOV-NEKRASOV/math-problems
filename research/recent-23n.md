# Recent literature for the (2,3,n) Fermat–Catalan family

**Search scope (23 October 2026, Argentina time).** I queried the arXiv Atom API for recent generalized Fermat titles and the exact expression `x^2+y^3=z^p`, inspected versioned abstracts, and read the relevant introductions and theorem statements in the papers below. This is a targeted literature scan, not an exhaustive proof that no other paper exists. None of these sources proves Fermat–Catalan for all exponent signatures, or even uniform finiteness for all prime output exponents in `(2,3,p)`.

## Direct recent papers

1. **Freitas, Mocanu, Sánchez-Rodríguez, [*Revisiting the equation x²+y³=zᵖ*](https://arxiv.org/abs/2512.10781), arXiv:2512.10781v1, submitted 11 December 2025.** The abstract and Theorems 1.2 and 3.1 give local exclusions of certain *antisymplectic* modular twists for listed `(E,p)` pairs and show a limit of local-only tests at good primes for remaining pairs. Theorem 1.2's exclusions concern selected `p≡19 (mod 24)` and `E` among `864a1,864b1,864c1`; they do not classify primitive solutions across all `p`. Already catalogued and partly reviewed in `research/attempt-modular-uniform.md` and its review.
2. **Freitas, Stoll, [*The Generalized Fermat Equation x²+y³=z²⁵*](https://arxiv.org/abs/2506.10667), arXiv:2506.10667v1, submitted 12 June 2025.** The abstract reduces primitive solutions to five degree-10 equations over sextic fields. Theorem 1.1 is **conditional** on those five equations having only expected solutions; the paper explicitly leaves them unresolved, even assuming GRH. Therefore it does not establish an unconditional no-positive-solution result for exponent 25. This status was separately checked in `research/six-exceptions.md` and `research/review-six-exceptions.md`.
3. **Ratcliffe, Grechuk, [*Generalised Fermat equation: a survey of solved cases*](https://arxiv.org/abs/2412.11933), arXiv:2412.11933v2, updated 14 April 2025; journal reference Expositiones Mathematicae (2025), [DOI 10.1016/j.exmath.2025.125688](https://doi.org/10.1016/j.exmath.2025.125688).** Table 1.1 lists solved `(2,3,n)` signatures for `7≤n≤12` and `n=15`, up to permutations. Its introduction singles out `(2,3,25)` as a remaining non-all-prime signature. This survey predates the conditional June 2025 preprint; the latter does not turn `n=25` into an unconditionally solved case. The survey is useful as an index to original papers, not a substitute for their exact sign and solution conventions.

## Recent adjacent method that does not directly cover (2,3,p)

**Cazorla García, Koutsianas, Villagra Torcomian, [*The generalized Fermat equation Ax²+Byʳ=Czᵖ and applications*](https://arxiv.org/abs/2605.02632), arXiv:2605.02632v1, submitted 4 May 2026.** The abstract announces a modular/Frey-hyperelliptic framework. The introduction §1.3 fixes a prime `r`, and §1.6 **explicitly assumes `r≥5`**. Thus the paper cannot be cited as settling or directly applying its theorems to the coefficient-one `(2,3,p)` family. Its Diophantine application, Theorem 1.3, concerns `−5x²+y⁵=z^(2p)` with additional parity/divisibility hypotheses. It may suggest methods to adapt, but no such adaptation to `r=3` is established there.

## Practical next checks

- Keep the `n=25` record marked conditional and preserve its five remaining equations as distinct obligations.
- Read original sources behind the 2025 solved-cases survey before promoting its solution lists; it is a map, not primary proof evidence.
- Continue the surviving modular branches for prime `p≥7`; a local twist exclusion for selected `p` is not a uniform classification.
- If the 2026 `(2,r,p)` machinery is proposed for `r=3`, first prove that its constructions and irreducibility hypotheses extend below its stated `r≥5` range.

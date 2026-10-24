# Six composite exponents in the `(2,3,n)` reduction

**Scope.** Primitive positive `x²+y³=zⁿ` with `n≥7`. The six composite values that have no proper hyperbolic divisor `d≥7` are `8,9,10,12,15,25`. This is a classification audit, not a proof of the whole Fermat–Catalan conjecture. All source theorems below study primitive **integer** solutions, often allowing negative bases; a theorem covering all signed solutions also covers the positive subset.

| n | Checked source and scope | Consequence for positive solutions |
| --- | --- | --- |
| 8 | Poonen–Schaefer–Stoll (PSS) Table 1 lists `{2,3,8}` as determined by Bruin (1999, 2003), with two non-Catalan powered identities. | The identity `96222³+43⁸=30042907²` rearranges to `30042907²+(-96222)³=43⁸`, with negative `y`. The other identity has exponent 8 on the input side and cannot be rearranged to a positive eighth-power RHS. No positive non-Catalan `(2,3,8)` triple is displayed; the original Bruin classification was not separately audited here. |
| 9 | PSS Table 1 lists `{2,3,9}` as determined by Bruin (2004/2005). | The listed positive solution is `13²+7³=2⁹`; arithmetic and coprimality check directly. |
| 10 | David Brown, *Primitive Integral Solutions to x²+y³=z¹⁰*, arXiv:0911.2932v3, Theorem 1.1, directly classifies all primitive integer solutions as 12 signed/trivial triples, with the only nontrivial ones `(±3,−2,±1)`. | No positive-base solution, because every nontrivial solution has `y=-2`. |
| 12 | Any `x²+y³=z¹²` gives `x²+y³=(z²)⁶`. Freitas–Naskręcki–Stoll (FNS), arXiv:1703.05058v3, introduction, says `n=6` reduces to two rank-zero elliptic curves; Freitas–Stoll, arXiv:2506.10667v1, introduction, calls `n=6` fully resolved. | The `n=6` reduction preserves positivity and primitivity, but `n=6` is parabolic (`1/2+1/3+1/6=1`). The exact `n=6` solution list was not extracted from a primary classification here, so do not assert an exact positive count for `n=12` on this evidence alone. Fixed-signature finiteness for `n=12` still follows from Darmon–Granville. |
| 15 | Siksek–Stoll, *The Generalised Fermat Equation x²+y³=z¹⁵*, arXiv:1309.4421v2, Theorem 1.1, directly gives trivial solutions and `(±3,−2,1)` as the only nontrivial primitive integer solutions. | No positive-base solution. |
| 25 | Freitas–Stoll, *The Generalized Fermat Equation x²+y³=z²⁵*, arXiv:2506.10667v1, Theorem 1.1, gives a **conditional** classification: if five explicitly described degree-10 equations over sextic number fields have only expected solutions, then only trivial and signed Catalan solutions remain. The paper explicitly leaves those five equations unresolved, even assuming GRH. | No complete explicit classification established by that preprint. The positive case remains unexcluded by this source. Darmon–Granville guarantees only finiteness for this fixed hyperbolic signature. |

## Reduction and sign cautions

The FNS introduction states that every integer `n≥6` is divisible by one of `6,8,9,10,15,25` or a prime `p≥7`. That reduction permits the **parabolic** divisor 6. Our six-value list instead retains only divisors `d≥7` so the reduced exponent triple `(2,3,d)` stays hyperbolic; this is why 12 appears as a fixed exception. For explicit classification, its reduction to 6 is still useful because the `n=6` case is separately solved.

PSS Table 1 uses braces for all exponent permutations, counts primitive **integer** solutions up to sign changes and permutations, and omits repeated unit-base forms. Positive Fermat–Catalan solutions are a subset; moving terms across the equality can introduce negative bases. The n=8 examples illustrate why orientation matters: `96222³+43⁸=30042907²` gives `30042907²+(-96222)³=43⁸`, with negative `y`. The other PSS identity, `1549034²+33⁸=15613³`, has exponent 8 on the input side. Moving the cube across gives RHS `−33⁸`, which is negative (unlike `(-33)⁸`), so it is not a solution to `x²+y³=z⁸`.

## Exact references

- Poonen, Schaefer, Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, Table 1 and caption, [arXiv:math/0508174v1](https://arxiv.org/pdf/math/0508174v1).
- Freitas, Naskręcki, Stoll, *The generalized Fermat equation with exponents 2, 3, n*, introduction, [arXiv:1703.05058v3](https://arxiv.org/pdf/1703.05058v3).
- Brown, *Primitive Integral Solutions to x²+y³=z¹⁰*, Theorem 1.1, [arXiv:0911.2932v3](https://arxiv.org/pdf/0911.2932v3).
- Siksek, Stoll, *The Generalised Fermat Equation x²+y³=z¹⁵*, Theorem 1.1, [arXiv:1309.4421v2](https://arxiv.org/pdf/1309.4421v2).
- Freitas, Stoll, *The Generalized Fermat Equation x²+y³=z²⁵*, Theorem 1.1 and introduction, [arXiv:2506.10667v1](https://arxiv.org/pdf/2506.10667v1).

**Next literature obligation:** inspect the original `n=6` classification to settle the positive `n=12` subset exactly, and independently audit Bruin's `n=8,9` lists. The infinite prime-exponent family remains the central uniform-finiteness gap regardless of these six fixed cases.

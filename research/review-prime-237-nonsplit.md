# Independent review of the latest `(2,3,p)` note

**Verdict:** The asserted Frey invariants, nonintegral `j`, local `27a1` filter, and source boundaries are sound under the hypotheses stated in [prime-237-nonsplit.md](prime-237-nonsplit.md). They are necessary restrictions, not a proof. The local lower bound can be improved and extended to every one of the seven comparison curves.

For `E:y²=x³+3bx−2a`, the short Weierstrass formulas give `c₄=−144b`, `Δ=−1728(a²+b³)`, and `j=1728b³/(a²+b³)`. Primitivity of `a²+b³=c^p` implies pairwise coprimality of `a,b,c`. Thus the reduced denominator of `j` is `c^p/gcd(c^p,1728)`, which exceeds 1 for `c≥2`, `p≥7`. The non-CM consequence follows because rational CM `j` values are algebraic integers. Positivity gives `0<j<1728`.

The residual comparison must use Freitas–Naskręcki–Stoll (FNS), arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4, only for a nontrivial primitive solution and prime `p≥11`. The small twist has parameter in `{±1,±2,±3,±6}` and has mod-`p` torsion isomorphic to one of seven fixed curves. All seven have conductor supported on `{2,3}`, so have good reduction for `q≥5`. At `q≥5`, `q≠p`, dividing `c`, the Frey curve and its small twist have multiplicative reduction; the minimal discriminant valuation is divisible by `p`. The unramified residual Tate representation has Frobenius trace `±(q+1)` modulo `p`. Consequently `a_q(E_i)≡±(q+1) (mod p)` for the selected comparison curve `E_i`.

The note correctly specializes this to `27a1`, including `a_q(27a1)=0` when `q≡2 (mod 3)` by the bijectivity of cubing over `F_q`; hence `6p|q+1` for odd prime `p≥17`. The source correctly treats non-split-Cartan uniformity as open. Hashimoto et al., arXiv:2608.10919v1, Theorem 1.1 concerns level 13 and does not establish a theorem for all sufficiently large levels. The cited Lemos theorem saying that an image contained in a non-split Cartan normalizer is the *full* normalizer for large `p` does not exclude such a proper image.

**Improvement:** The note derives `q≥√p−1` from the product divisibility. Since `p` is prime, it divides *one* factor `q+1−a_q(E_i)` or `q+1+a_q(E_i)`. Hasse gives `0<q+1±a_q(E_i)≤(√q+1)²`, so `p≤(√q+1)²` and `q≥(√p−1)²`. This holds for all seven comparison curves, not just `27a1`, because all have good reduction at `q≥5`. For `q=p`, the lower bound is automatic. It says every output prime factor `q≥5` is asymptotically at least `p−2√p+1`. This still allows `c` and its prime support to escape, so it does not close `(2,3,p)` or the full conjecture.

No Lean formalization is warranted.

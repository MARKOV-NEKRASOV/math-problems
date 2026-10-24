# Peer review: 27a1 prime-divisor filter

**Verdict:** The filter in `research/attempt-27a1.md` is mathematically sound under the stated `27a1[p]` branch and `q≠p` hypotheses. It is a necessary congruence, not a proof of Fermat–Catalan.

## Primary-source and local checks

1. Freitas–Naskręcki–Stoll, [arXiv:1703.05058, §2, Lemma 2.3](https://arxiv.org/pdf/1703.05058), identifies a twist `E^(d)[p]` with one of seven curves, including `27a1`, for a primitive solution with nonzero `c` and irreducible residual representation. The twist parameter is indeed among `±1,±2,±3,±6`. Their Proposition 2.4 proves irreducibility for nontrivial primitive solutions and prime `p≥11`, so the note's `p≥17` setting meets this requirement. Their displayed model for `27a1` is `y²+y=x³−7`.
2. At a prime `q≥5` dividing `c`, primitivity forces `q∤ab`. The Frey `c₄=−144b` is a `q`-adic unit and `v_q(Δ)=p v_q(c)>0`. Therefore the integral model is minimal at `q` and has multiplicative reduction. Poonen–Schaefer–Stoll, [arXiv:math/0508174, §4, Case 1](https://arxiv.org/pdf/math/0508174), explicitly invokes Silverman AEC VII.5.1(b) for this same `c₄`/discriminant argument in exponent 7. The extension to general prime `p` uses the identical valuations.
3. Since `q≥5`, every permitted `d` is a `q`-adic unit; its quadratic character is either trivial or unramified. For split Tate reduction, the standard exact sequence `0→μ_p→E[p]→Z/p→0` gives diagonal Frobenius eigenvalues `q` and `1` modulo `p`, hence trace `q+1`; a nonsplit or unramified quadratic twist changes both signs. Freitas–Naskręcki–Stoll's Proposition 5.4 proof writes the Tate-curve `p`-torsion basis and its Galois action explicitly, supporting this calculation. Since `p|v_q(Δ)`, the mod-`p` representation is unramified at `q`; it is also globally isomorphic to `27a1[p]`, whose curve has good reduction at `q≥5`. Thus `a_q(27a1)≡±(q+1) (mod p)` and `p|(q+1)²−a_q²`. The excluded case `q=p` matters: at residue characteristic `p`, the stated unramified Tate-curve argument does not apply.
4. When `q≡2 (mod 3)`, cubing permutes `F_q`. For each `y∈F_q`, there is exactly one `x` with `x³=y²+y+7`, so the affine count is `q`; adding infinity gives `a_q=0`. This is a direct proof and does not need a separate CM theorem.

## Sharpening and limits

The final congruence can be sharpened: `q≡2 (mod 3)` makes `3|(q+1)`, while `p≥17` is coprime to 3 and `p|(q+1)`. Since `q≥5` is odd, also `2|(q+1)` and `p` is odd. Hence `6p|(q+1)`, so every such prime divisor satisfies `q≡−1 (mod 6p)` and `q≥6p−1`. This strengthens the note's weaker exclusion of `q<p−1`, but still permits infinitely many candidate primes and yields no bound on `p` or `c`.

**Missing-hypothesis caution:** The representation must actually be in the `27a1` branch of Lemma 2.3. The lemma only guarantees one of seven branches; the new congruence must not be applied to every primitive solution. The proof also requires a nontrivial solution, `c≠0`, `q≥5`, and `q≠p`, all satisfied or expressly assumed in the note. The local trace is a congruence modulo `p`; it must not be confused with the integral trace `±(q+1)` of a singular reduction curve.

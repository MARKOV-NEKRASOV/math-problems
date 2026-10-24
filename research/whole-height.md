# Attempt at the full Fermat–Catalan conjecture: a uniform height route

**Result: incomplete.** This is an attempt to prove finiteness of all distinct powered-value triples simultaneously as the exponents vary. It proves a necessary exponent-height condition, then identifies the step that would be needed to finish. It does not prove the conjecture.

## Exact universe

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, where `x,y,z` are positive integers, `gcd(x,y,z)=1`, `p,q,r>1`, and `σ=1/p+1/q+1/r<1`. We count distinct `(A,B,C)`, not exponent representations. The unit-base cases give only `(1,8,9)` up to exchanging the summands by Mihăilescu's theorem; `z=1` is impossible. Hence an infinite counterexample family, if it exists, has `x,y,z≥2` and unbounded `C`.

Primitivity and the equation make `A,B,C` pairwise coprime. Set `R=rad(ABC)=rad(xyz)`. The elementary inequality `xyz<C^σ`, together with the maximum hyperbolic reciprocal sum `σ≤41/42`, gives

`R < C^σ ≤ C^(41/42)`.                                               (1)

## Attempt using an unconditional abc-type estimate

The Stewart–Yu bound, as displayed in the [abc overview's partial-results section](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results), says that some absolute `K>0` satisfies

`log C < K R^(1/3)(log R)^3`                                         (2)

for coprime positive `A+B=C` with `C>2`. Bibliographic source: C. L. Stewart and Kunrui Yu, *On the abc conjecture, II*, Duke Math. J. 108 (2001), [DOI 10.1215/S0012-7094-01-10815-6](https://doi.org/10.1215/S0012-7094-01-10815-6). The displayed formula has been corroborated through the secondary overview; I could not inspect the paywalled article itself. The following deductions are conditional only on the accuracy of this cited, established inequality, not on the unproved abc conjecture.

Write `L=log C`. A uniform inversion of (2) (proved in the prior [prime-support note](attempt-support.md)) gives, for an absolute `c>0` and all sufficiently large `C`,

`R > c L^3/(log L)^9`.                                                (3)

For completeness: if `R>L^6`, (3) is immediate eventually. Otherwise `log R≤6log L`; cubing (2) gives `L^3<K^3 R(6log L)^9`, so choose `c=min(1,(K^3 6^9)^(-1))`.

Combining (1) and (3) gives a new uniform necessary condition on the varying exponents:

`σ > [3loglog C - 9logloglog C + log c]/log C`.                      (4)

In particular, if `m=min(p,q,r)`, then `σ≤3/m`, and (4) implies

`m < log C/[loglog C - 3logloglog C + (log c)/3]`

for sufficiently large `C`. Thus every hypothetical unbounded family has

`min(p,q,r) ≤ (1+o(1)) log C/loglog C`.                              (5)

This is an unconditional necessary restriction assuming the cited Stewart–Yu formula. It is stronger than the elementary `m≤log_2 C`, but it is far from a uniform bound on any exponent or on `C`.

## Why the attempted proof stops

The desired contradiction would require a **power-scale lower bound** on `R` in terms of `C`. For instance, if one could prove with one constant `K_0` and one `0<η<42/41`, uniformly over every primitive Fermat–Catalan triple, that

`C ≤ K_0 R^(42/41-η)`,                                               (6)

then (1) would give `C < K_0 C^(1-(41/42)η)` and bound `C`. But (6) is not a known unconditional theorem for these triples; on this solution universe it is essentially equivalent to finiteness, since a finite solution set admits a suitable constant `K_0`. Stewart–Yu only yields `R` larger than a **polylogarithm** of `C`, while (6) needs `R` larger than a fixed **power** of `C`. Both (1) and (3) remain compatible as `C→∞` for every fixed hyperbolic signature.

Alternatively, the unproved abc conjecture with `ε=1/42` would give `C≤K_ε R^(1+ε)` and finish as in the existing [first height attempt](attempt-inequality.md). Importing that conjecture as a theorem would invalidate the proof. The present argument reaches (4) but cannot rule out an infinite family with one comparatively small exponent and the others varying.

**Next obligation:** find an unconditional, uniform power-scale height estimate for primitive perfect-power triples, or a different mechanism that controls all exponent signatures simultaneously. No fixed-signature theorem or sparse exceptional-set estimate automatically provides this.

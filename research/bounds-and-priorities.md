# Quantitative bounds and the subproblems that can strengthen them

**25 October 2026.** Bounds below are necessary conditions for primitive hyperbolic Fermat–Catalan solutions. They organize the next research tasks by the parameter each task could actually improve. Increasing the number of excluded examples is useful only when the proof covers an infinite family or sharpens a bound that feeds a later argument.

| Bound | Proved scope and current value | A subproblem that would strengthen it | Limit of the current bound |
| --- | --- | --- | --- |
| Output-prime size | For positive `(2,3,p)`, prime `p≥11`, every prime `q≥5` dividing `c` has `q≥(√p−1)²` ([proof](all-seven-roughness.md)). | Derive a stronger `q` lower bound in each surviving FNS comparison branch, or prove that all large factors of `c` lie in trace classes with a stronger bound. | Large `q` remain available, so this gives no upper bound on `p` or `c`. |
| Input-prime compatibility | For `p≥11`, `5|b` and `7|a` are incompatible. Exact selectors through `q≤101` exclude **42 pairs** for `p≥103`, covering 6.7062% of coprime base pairs in the stated divisibility sense ([metrics](modular-selector-bounds.md)). | Add selector primes while tracking the safe exponent threshold; more decisively, prove that every surviving solution meets incompatible selectors. | The density is of ordinary coprime base pairs, not of Fermat–Catalan solutions. A solution may avoid every prime in a finite list. |
| Repeated-prime sum | For signed coprime odd bases in `a^p+b^p=c^t>0`, `2^t|a+b`. In positive `(3,3,t)` with published `t>10⁹`, the [congruence-corrected size gap](congruence-corrected-size-gaps.md) forces `u≥46,520` in the clean sum `a+b=u^t`, or `u≥6,890` in the ramified sum `a+b=3^(t−1)u^t`. | Couple the necessary gap `H−v` with the discriminant-square identity, or prove a uniform upper bound on `u` as `t` grows. | Larger lower bounds on `u` still permit arbitrarily large bases. |
| Fixed-exponent base gap | In a one-diverging-exponent profile with the other exponents `P,Q` fixed, the [effective theorem](effective-fixed-gap-bounds.md) gives `W≤(10n²)^(40n)[1+(1+|D|)^min(P,Q)]^(11n)`, where `W` is the varying exponent, `D` the fixed-exponent bases' gap, and `n` the polynomial degree. | Improve the huge exponent and height bounds or find a theorem uniform as `D` moves; then test whether the resulting lower rate for `|D|` conflicts with another upper bound. | The inequality forces slow gap growth as `W→∞` but allows it; no upper bound on `D` is proved. |
| Prime support | In that one-diverging-exponent profile, the variable-exponent base's prime support also escapes every fixed set ([signed support lemma](all-prime-escape-profiles.md)). | Couple the moving gap with the moving support, perhaps by an effective S-integral height estimate valid as both vary. | Two escape conditions can hold simultaneously. |
| Radical deficit | An infinite all-prime family has `rad(ABC)<C^(5/6+o(1))`; if two exponents diverge the exponent improves to `1/2+o(1)`, and if three diverge to `o(1)` ([escape profiles](all-prime-escape-profiles.md)). | Supply an unconditional upper bound on `C` in terms of its radical strong enough to contradict a profile, or another argument bypassing this bound. | The required power-strength inequality is not established by the checked unconditional results. |

## How to choose the next lemma

1. State a parameter, its current proved bound, and the exact hypotheses under which it holds.
2. Show that the proposed lemma would improve the bound or eliminate a named infinite subfamily; compute the new value or logical implication before starting a broad generalization.
3. Check the other escape parameters. A larger lower bound on a base, gap, or prime factor is not a contradiction unless some independent theorem gives a conflicting upper bound.
4. Record source version and reading status, and have another agent audit the deduction before using it in the full conjecture.

This board is a prioritization device, not a proof. No Lean formalization has been started.

The [independent quantitative review](review-quantitative-bounds.md) checks the congruence-corrected repeated-prime calculations and the effective fixed-gap theorem's specialization.

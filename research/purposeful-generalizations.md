# Generalizations aimed at Fermat–Catalan case elimination

**25 October 2026. Status: partial results, no full proof.** Four agents generalized existing lemmas only where the broader statement gives a direct implication for primitive hyperbolic Fermat–Catalan solutions. The target remains finiteness of distinct powered-value triples `x^p+y^q=z^r` with `gcd(x,y,z)=1` and `1/p+1/q+1/r<1`. No result below controls all moving exponents and bases.

## Arithmetic geometry: a fixed-gap theorem for every orientation

The [general fixed-gap theorem](general-fixed-gap-finiteness.md) proves that, for any fixed input exponents `P,Q≥2` other than `(2,2)` and any fixed nonzero integer `D`, only finitely many positive triples `x^P+y^Q=z^R` have `x−y=D`, even while `R` and every prime dividing `z` vary. The [independent signed extension](signed-fixed-gap-finiteness.md) covers `m^P−n^Q=k^R>0` under the hyperbolic condition, so it applies when the varying exponent is on **any** coordinate of the original equation.

The construction uses `F_D(T)=T^P±(T−D)^Q`. If this polynomial had a multiple root and `P≠Q`, direct elimination would give

`|D|^|P−Q| = min(P,Q)^min(P,Q) |P−Q|^|P−Q| / max(P,Q)^max(P,Q) < 1`,

impossible for a nonzero integer `D`. If `P=Q`, a multiple root forces `D=0`. Thus the relevant polynomial is squarefree. Schinzel–Tijdeman bounds `R` for `z≥2`; for each remaining `R`, Siegel gives finitely many integral points on a genus-at-least-one curve. The only signed degree-two edge case is `P=Q=3`, where hyperbolicity forces `R≥4` and the genus is still positive. The original Schinzel–Tijdeman proof was not audited here; its standard hypotheses are restated in the paper library's arXiv:1410.8441v2 abstract record.

**Direct implication.** In any hypothetical infinite family with exactly one coordinate exponent diverging and the other two fixed, the difference of the fixed-exponent bases must escape every bounded set. The earlier [signed fixed-support lemma](all-prime-escape-profiles.md) independently forces the variable-exponent base's prime support to escape. These two escapes are compatible, so they do not close that profile.

## Elliptic curves and a finite compatibility graph

For positive primitive `a²+b³=c^p`, prime `p≥11`, Freitas–Naskręcki–Stoll gives one globally selected comparison curve among seven fixed curves, after a small twist. The [input-prime selector lemma](input-prime-branch-selectors.md) uses zero Frobenius traces to prove that `5|b` selects only `27a1`, while `7|a` selects only `288a1`. Thus **no solution can satisfy both `5|b` and `7|a` for any prime `p≥11`**. Its source-checked Lemma 6.1 additionally excludes `5|b` for `p≥17`, `p≡1 (mod 3)`, and `7|a` for `p≥17`, `p≡1 (mod 4)`.

The [finite compatibility graph](input-prime-compatibility-graph.md) generalizes the two-prime selector: its vertices are input-prime divisibility conditions, and an edge exists only if their zero-trace sets share a comparison curve. Exact point counts show that primes `{5,29,41,53}` dividing `b` each select `27a1`, while `{7,19,43}` dividing `a` each select `288a1`. For every prime `p≥59`, the graph has no cross edges and excludes all **12 pairwise divisibility families**. The [point-count script](output_prime_sieve_check.py) checks every listed trace. This is a finite, proved sieve; no claim is made that the selected prime sets exhaust the possible bases.

## Cyclotomic valuations across repeated odd exponents

For coprime signed odd-prime powers `a^p+b^p=c^t>0`, the [valuation-profile lemma](repeated-prime-valuation-profile.md) proves `a+b=u^t` if `p∤a+b`, and `a+b=p^(t−1)u^t` otherwise. Therefore, if both signed bases are odd, `2^t|a+b`; **the entire residue family `a≡b (mod 4)` is impossible** in either orientation. For positive odd inputs in `(3,3,t)` with prime `t≥5`, combining this profile with the earlier simultaneous-factor gap gives `a+b≥4^t`. This excludes a growing size region, but arbitrarily large sums remain possible.

## Remaining construction problem

Each method eliminates an infinite collection of cases or forces escape of a concrete parameter. None makes one of its excluded input patterns unavoidable or bounds the simultaneous growth of exponents, base gaps, and prime support. The next useful step would be a coupling lemma that forces a solution into incompatible modular selector sets, or a geometric height estimate uniform in the moving gap `D`. A compatibility graph is helpful only insofar as new proved local selectors add exclusions; graph combinatorics alone cannot supply the missing arithmetic. No Lean formalization was attempted.

The follow-up [bound dashboard](bounds-and-priorities.md) quantifies these constructions and identifies which exact lemmas could strengthen each bound.

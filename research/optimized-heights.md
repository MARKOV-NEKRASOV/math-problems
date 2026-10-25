# Optimized height and prime-support attempt for the full Fermat–Catalan conjecture

**Outcome: no full proof.** This tries to turn the perfect-power radical deficit into a contradiction by combining the strongest general-purpose unconditional estimate used in the project with prime-support counting. The inequalities leave ample room for an infinite hypothetical family.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B` be primitive positive, non-unit Fermat–Catalan data, with `σ=1/p+1/q+1/r<1`. Put `R=rad(ABC)`, `m=min(p,q,r)`, `s=ω(R)` and `P` the largest prime factor of `R`. Distinct powered-value triples with bounded `C` form a finite set, so an infinite family would have `C→∞`. The bases are pairwise coprime, hence `s≥3`. The elementary power estimate gives

`R≤xyz<C^σ≤C^(41/42)` and `σ≤3/m`.                              (1)

## Trying to force a contradiction from an unconditional abc estimate

The Stewart–Yu estimate is reported in the [abc overview](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results) as `log C<K R^(1/3)(log R)^3` with one absolute `K>0` for coprime `A+B=C`. I could not inspect the original paywalled paper [Stewart–Yu 2001](https://doi.org/10.1215/S0012-7094-01-10815-6), so this exact displayed form has a secondary-source caveat. Its inversion, already proved in `whole-height.md`, gives for `L=log C` and large `C`

`R>c L^3/(log L)^9`                                                    (2)

with one absolute `c>0`. The squeeze between (1) and (2) is compatible with arbitrary large `C`: every fixed positive power `C^σ` eventually exceeds the polylogarithm. Even if `σ→0`, it only forces `m≤(1+o(1)) L/log L`, not a constant bound on exponents.

## Optimizing by support size and smoothness

The `s` distinct primes of `R` are at most `P`, so `R≤P^s`. Let `Q_s` be the product of the first `s` primes; since `R` has `s` distinct prime factors, `Q_s≤R`. Therefore every hypothetical large solution obeys the simultaneous inequalities

`c L^3/(log L)^9 < R ≤ P^s` and `Q_s≤R<C^(3/m)`.                      (3)

For bounded `s≤s₀`, (3) yields `P>c' L^(3/s₀)/(log L)^(9/s₀)` for a positive constant `c'` depending at most on `s₀` and `K`. In particular, if one also proposed `P≤L^δ` for a fixed `δ<3/s₀`, this would be impossible for all sufficiently large `C`. This is a **restricted** contradiction requiring a bound on both support count and largest support prime; neither bound follows from the equation.

If `s→∞`, the [prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem) gives `log Q_s=(1+o(1))s log s`, so (3) implies

`m·s log s ≤ (3+o(1)) log C`.                                           (4)

This tradeoff says a large minimum exponent leaves room for fewer distinct prime factors. It does not bound `m` or `s`: for instance, `m≈sqrt(log C)`, `s≈sqrt(log C)/loglog C` is compatible with (4), and `P` can still grow. The prime number theorem also gives `P≥(3-o(1))loglog C` from (2), as in `attempt-smooth.md`, again far below an exclusion threshold.

## Why quantitative S-unit counting does not finish

For any **fixed** finite prime set `S`, `u=A/C`, `v=B/C` satisfy `u+v=1` in rational `S`-units. The S-unit theorem gives finitely many pairs, so bounded `P` already yields finiteness. Quantitative S-unit bounds may control the number of pairs in terms of the rank or size of a fixed `S`, but a hypothetical family may change `S` at every solution. Summing any positive bound over infinitely many possible supports is not a finiteness argument. A Baker-type bound whose constants depend on the primes in `S` likewise cannot be made uniform merely by setting `s≤s₀`; the actual primes can escape.

One tempting contradiction is to assume that perfect-power structure gives `P≤(log C)^δ` and `s≤s₀` with `δ<3/s₀`, then invoke (3). That *would* work, but neither joint restriction is established. Another is to replace (2) with a power lower bound `R≫C^α` for some `α>41/42`; that would immediately contradict (1) but is stronger than the required restricted abc-type estimate and cannot be inserted as a lemma.

**Exact missing step:** an unconditional restriction on moving prime support or a uniform power-scale lower bound for `R` on these special triples. The existing estimates (1)–(4) and fixed-support S-unit finiteness do not provide it. No Lean formalization was attempted because there is no complete mathematical proof.

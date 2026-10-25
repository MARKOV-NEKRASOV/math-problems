# Full Fermat–Catalan attempt from exponent escape and fixed-support geometry

**Outcome: incomplete.** Combining the all-prime reduction, exact Frey height, and a signed version of the fixed-pair Siegel lemma gives a sharper structural description of every hypothetical infinite family. It does not bound the moving prime support or supply an unconditional height–conductor upper bound.

Let `T=(A,B,C)=(x^p,y^q,z^r)` be a primitive positive powered-value triple with `A+B=C`, prime exponents `p,q,r≥2`, and `σ=1/p+1/q+1/r<1`. Count distinct `T`, not exponent tuples. The existing source-checked reduction makes all non-all-prime exponent classes finite, so an infinite Fermat–Catalan counterexample family would contain infinitely many all-prime representations. Choose, for each triple, an all-prime representation minimizing `max(p,q,r)`. Darmon–Granville fixed-signature finiteness makes the minimax exponent tend to infinity along any sequence of distinct triples. Also `C→∞`, while fixed-`S` S-unit finiteness forces `R=rad(ABC)→∞` and the odd conductor `N_odd=R/2→∞`.

## Escape profiles

Pass to a subsequence on which each of the *three coordinate exponents* either is constant or tends to infinity. This is possible by successively choosing a constant subsequence when an exponent is bounded infinitely often and otherwise taking one tending to infinity. At least one coordinate exponent diverges, since the minimax exponent does. Let `k` be the number of diverging exponents in this profile. The standard perfect-power bound is `R≤xyz<C^σ`; the universal Frey curve has `h(j)=6log C+O(1)` and odd conductor `N_odd=R/2`.

- `k=1`: the other two prime exponents are fixed on this subsequence. They cannot both be 2 by hyperbolicity, so `σ≤5/6+o(1)`, `R<C^(5/6+o(1))`, and `h(j)≥(36/5−o(1))log N_odd`.
- `k=2`: the remaining fixed exponent is at least 2. Thus `σ≤1/2+o(1)`, `R<C^(1/2+o(1))`, and `h(j)≥(12−o(1))log N_odd`.
- `k=3`: `σ→0`, hence `R=C^o(1)` and `h(j)/log N_odd→∞`. In particular, an infinite family of this profile would violate **every** fixed-power bound `C≤K R^B` with `B>0`, but no such unconditional bound is available in the project. This does not itself rule out the profile.

The slope conclusions follow by combining `log N_odd≤σ log C` with `h(j)=6log C+O(1)` and `N_odd→∞`; the positive `o(1)` in a radical upper bound is profile-dependent. If no subsequence of a profile exists, its implication is vacuous; these cases cover any hypothetical infinite sequence after subselection.

## Fixed-support lemma for whichever exponent varies

Here is a signed extension of the reviewed fixed-output-support lemma. Fix integers `P,Q≥2`, `(P,Q)≠(2,2)`, a sign `ε∈{−1,+1}`, and a finite set of primes `S`. There are only finitely many primitive positive powered triples that can be arranged as

`m^P+ε n^Q=k^W>0`, `W≥2`, `supp(k)⊆S`,

where `m,n,k` are positive and the equation is interpreted with the displayed sign. In an original `x^p+y^q=z^r`, moving either positive summand across `=` creates the negative sign, so the lemma applies when **any one** coordinate exponent varies while the other two are fixed, provided its base has support in `S`.

**Proof.** Put `L=lcm(P,Q)` and write the S-supported powered value uniquely as `k^W=Dw^L`, with `D=∏_{q∈S}q^{e_q}`, `0≤e_q<L`, and `w` a positive S-supported integer. There are finitely many `D`. Set `u=m/w^{L/P}` and `v=n/w^{L/Q}`. Then `u,v` are rational S-integers on the smooth affine curve `u^P+εv^Q=D`. Its projective genus is `((P−1)(Q−1)−gcd(P,Q)+1)/2≥1`: the sign does not affect the simple branch points of the degree-`P` cover. Siegel's theorem gives finitely many S-integral `(u,v)` for each `D`. For fixed `(u,v,D)` and `q∈S`, if `t=v_q(w)>0`, then `q|k`; primitivity forbids both `m,n` from being divisible by `q`. Yet `v_q(m)=v_q(u)+(L/P)t` and `v_q(n)=v_q(v)+(L/Q)t`, so sufficiently large `t` would make both positive. Thus every `v_q(w)` is bounded, hence only finitely many `w` and powered triples occur. Unit fixed bases cause no exception.

In the `k=1` escape profile, this lemma implies that the **largest prime factor of the base with the diverging exponent must also tend to infinity**. For each prime bound `B`, the corresponding finite set `S={q≤B}` gives only finitely many triples; remove those triples for each `B`. This is stronger than growth of the prime support of `ABC` as a whole. It still permits the support of that base to change on every solution.

## Attempted closure and exact failure

A proposed proof by contradiction would next claim that one of the three profiles has fixed support for the diverging coordinate, or that the Frey curve's `j`-height admits a universal upper bound of slope below the displayed lower slopes. Neither claim follows from the established results. The fixed-`S` Siegel theorem controls **each** finite `S`, while the hypothetical family can move through infinitely many `S`; bounded support *cardinality* is not a fixed set of primes. In `k=2` or `k=3` the radical deficit is stronger, but Stewart–Yu's reported unconditional estimate gives only `R` larger than a polylogarithm of `C`, which is compatible even with `R=C^o(1)` (for instance scales `log R≈sqrt(log C)` satisfy both). Its exact displayed formula was checked in the project only through a secondary source.

Likewise, no unconditional power-scale `C≤K R^B` or logarithmic `j`-height/conductor upper bound with the required slope is available. Treating weak abc, Szpiro, or uniform isogeny as an established theorem would insert the desired conclusion as an unsupported lemma. The exponent escape profiles, signed Siegel lemma, and height calculation are necessary restrictions on a counterexample family, not a full proof. The all-prime moving-support case remains open; no Lean formalization was attempted.

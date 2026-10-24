# Review: quantitative prime-support escape

**Verdict:** The arithmetic and quantifiers in `research/attempt-support.md` check out under its stated Stewart–Yu inequality. This is an unconditional necessary condition if that cited estimate is used, but it supplies no Fermat–Catalan proof.

- Pairwise coprimality of `A,B,C` follows from the primitive equation. With `x,y,z≥2`, each powered value has at least one prime divisor and their supports are disjoint, so `s=ω(R)≥3`. Since all `s` distinct primes are at most `P`, `R≤P^s`.
- Put `L=log C`. If `R>L^6`, then `R>cL^3/(log L)^9` for all sufficiently large `L` and any `c≤1`. Otherwise `log R≤6log L`. Cubing `L<KR^(1/3)(log R)^3` gives `L³<K³R(log R)^9≤K³R(6log L)^9`, hence `R>L³/[K³6⁹(log L)^9]`. The stated uniform `c=min(1,1/(K³6⁹))` works. Taking `s`th roots of `R≤P^s` gives the displayed `P` bound.
- For fixed `s0≥3`, `3≤s≤s0`, `c≤1`, and sufficiently large `L`, the variable-`s` estimate implies `P>cL^(3/s0)/(log L)^3`: `c^(1/s)≥c`, `L^(3/s)≥L^(3/s0)`, and `(log L)^(9/s)≤(log L)^3`. The stronger `P>L^(3/s0−δ)` for each fixed `δ>0` follows because powers dominate `(log L)^3/c`.
- The conclusion that fixed prime *count* forces the largest supporting prime to diverge along an unbounded sequence of `C` is correct. It is much weaker than bounding the number of solutions. A fixed prime *set* permits Evertse's `S`-unit finiteness, but that theorem has no uniform implication when the set moves.

**Source limitation:** The exact Stewart–Yu displayed bound was attributed to the abc overview in the previous reviewed note; the paywalled primary article was not independently inspected here. The new algebra is valid given that estimate. Keep that provenance explicit instead of calling the displayed formula directly verified from Stewart–Yu's text.

**Minor clarity edit:** Specify `s0≥3` when discussing an infinite family with at most `s0` supporting primes. If `s0<3`, no solutions satisfy the paper's non-unit assumptions, so the statement is vacuous. Also, “for each `δ>0`” means the threshold for `C` may depend on `δ` and `s0`; the constant `c` in the earlier bound remains absolute.

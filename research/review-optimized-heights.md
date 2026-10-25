# Independent review of optimized height/support attempt

**Verdict:** The support-size and exponent tradeoff is mathematically valid under the displayed Stewart–Yu estimate, with one wording correction. It does not prove Fermat–Catalan.

1. For primitive non-unit data, `R≤xyz<C^σ≤C^(41/42)` and `σ≤3/m` are correct. The inversion of `log C<K R^(1/3)(log R)^3` gives `R>cL³/(log L)^9` for `L=log C` large and one absolute `c>0`, as checked in `whole-height.md`. The original Stewart–Yu article was not accessed; the exact formula is corroborated only by the secondary abc overview. Keep that source caveat.
2. With `s=ω(R)≥3` and `P=max supp(R)`, `Q_s≤R≤P^s`. The combined inequalities in (3) follow. If `s≤s₀` for fixed `s₀≥3`, taking `s`th roots gives `P>c^{1/s}L^(3/s)/(log L)^(9/s)`. Because there are only finitely many `s≤s₀` and `L³/(log L)^9→∞`, the claimed uniform lower bound `P>c' L^(3/s₀)/(log L)^(9/s₀)` holds for sufficiently large `L` with `c'>0` depending on `K,s₀`. This contradicts an extra hypothesis `P≤L^δ` for `δ<3/s₀`; neither extra support restriction is established by the equation.
3. As `s→∞`, the prime number theorem implies `log Q_s=(1+o(1))s log s`. From `Q_s<R<C^(3/m)` one obtains `m s log s≤(3+o(1))log C`. The `o(1)` refers to `s→∞`; the inequality remains valid even if `m` varies. The proposed example has `m s log s` on the order of `(1/2)log C`, so it demonstrates compatibility rather than contradiction.
4. The fixed-`S` S-unit argument is applied correctly. A bounded **largest prime** would fix `S={primes≤P}` and imply finiteness, but a bounded **number** of supporting primes does not fix the actual primes. No quantitative fixed-`S` theorem quoted in the note controls the union over moving `S`.

**Wording correction:** “any positive power `C^σ` eventually exceeds the polylogarithm” is true only for a **fixed** `σ>0`. When `σ=σ(C)` tends to zero, compatibility requires a lower bound on `σ` of order `loglog C/log C`, which the note derives via the bound on `m`. Say “for every fixed positive `σ`” to avoid suggesting that *every* varying positive exponent works.

The partial contradiction is rigorously conditional on *both* `s≤s₀` and `P≤(log C)^δ` with `δ<3/s₀`; it is not a proof for unrestricted Fermat–Catalan solutions. The missing uniform support bound is explicitly acknowledged. No Lean work was done.

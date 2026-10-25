# Primitive-divisor attempt on repeated-prime Fermat–Catalan signatures

**Outcome: incomplete.** A Zsigmondy prime gives a uniform congruence and a size restriction for the cyclotomic cofactor in the positive-left orientation. It does not control the simultaneous power in the linear factor. In particular it does not prove full Fermat–Catalan.

Let `a,b>0` be coprime, `a≠b`, and let `p` be an odd prime. Put `U=a+b` and `V=(a^p+b^p)/(a+b)`. Suppose `a^p+b^p=c^t` for prime `t` with `2/p+1/t<1`. For `p≥5`, Zsigmondy's theorem applied to `max(a,b)^(2p)−min(a,b)^(2p)` supplies a prime `Q` whose multiplicative order of `max(a,b)/min(a,b)` modulo `Q` is exactly `2p`. Its only standard exceptional case at exponent `2p≥6` is `(max(a,b),min(a,b),2p)=(2,1,6)`. Thus `Q≡1 (mod 2p)`, `Q|a^p+b^p`, and `Q∤a+b`, so `Q|V`. For `p=3`, the same holds outside `(a,b)=(2,1)` up to permutation. In that exceptional pair `a³+b³=9`, which is not a `t`th power for any eligible prime `t≥5`. The case `a=b=1` gives 2 and also cannot be a `t`th power. Therefore every eligible positive-left repeated-prime solution has a prime `Q|V` with `Q≡1 (mod 2p)`.

Since `gcd(U,V)|p`, the primitive prime `Q>p` cannot divide `U`. Its valuation in `V` is therefore divisible by `t`; in particular `Q^t|V`. Convexity (as in [prime-cube-size-local.md](prime-cube-size-local.md)) gives `V<U^(p−1)`, and hence

`U>Q^(t/(p−1))≥(2p+1)^(t/(p−1))`.                 (1)

Here the last inequality is deliberately crude: `Q≡1 (mod 2p)` implies `Q≥2p+1`. This provides a lower bound on the sum `a+b` in the positive-left orientation. If `p|U`, LTE additionally forces `v_p(U)≡−1 (mod t)`, so `U≥p^(t−1)`; neither bound contradicts the other. If `p∤U`, then `U=u^t` and `V=v^t`; (1) only says `u>Q^(1/(p−1))`. It gives no upper bound on `u` or `t`. The argument does not apply unchanged to the signed orientation `a^p−b^p=c^t`, where `U=a−b` can be small and `V<U^(p−1)` is false.

The earlier Eisenstein family, with `ω²+ω+1=0` and `(N+ω)^t=a+bω`, shows why a primitive prime of `V` is not enough: `V=a²−ab+b²=(N²−N+1)^t` for arbitrarily large `t`. One might hope that the same construction also has `U=a+b` a `t`th power. For sufficiently large `N` at each fixed `t`, a direct gap rules that out. Namely the coefficient-sum map on powers of `ω` has values `s_k=1,1,−2` periodically in `k mod 3`, so

`U=Σ_(k=0)^t binom(t,k) N^(t−k) s_k`.

The `k=0,1` terms are `N^t+tN^(t−1)` and `|s_k|≤2` for `k≥2`. Therefore

`U≥N^t+tN^(t−1)−2(2^t−t−1)N^(t−2)>N^t`

whenever `N>2(2^t−t−1)/t`. On the other hand

`U=(N+1)^t−3Σ_(k≡2 mod 3) binom(t,k)N^(t−k)<(N+1)^t`

for `t≥2`, `N>0`. Thus `N^t<U<(N+1)^t` for all sufficiently large `N` at fixed `t`, so this *specific* infinite Eisenstein construction cannot satisfy the simultaneous `U=u^t` condition. It remains a valid warning that `V=v^t` alone has many solutions. This gap in an example is not a descent for arbitrary `a,b`.

**Unclosed step:** show uniformly for both positive and signed orientations that the simultaneous conditions on `U,V`, with moving `p,t`, have finitely many primitive powered-value solutions. Primitive-divisor congruences and (1) do not do this; pairwise-distinct prime signatures remain wholly separate. No Lean formalization was attempted.

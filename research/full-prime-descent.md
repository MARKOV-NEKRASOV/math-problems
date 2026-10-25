# Full Fermat–Catalan attempt: all-prime signatures and cyclotomic descent

**Outcome: incomplete.** I tried to remove the remaining infinite all-prime signatures by splitting according to repeated prime exponents and then using cyclotomic factorization. The factorization gives a precise necessary equation, but it does not imply a uniform bound on the primes or the powered values.

Write `A=x^p`, `B=y^q`, `C=z^r=A+B`, with `gcd(x,y,z)=1`, `p,q,r` prime, and `1/p+1/q+1/r<1`. Count distinct `(A,B,C)`. The [prior signature reduction](optimized-signatures.md) shows that these all-prime cases, together with `(2,4,ℓ)` and finitely many fixed cases, contain the whole problem. Fermat's Last Theorem removes `p=q=r≥3`; two exponents 2 are not hyperbolic. This leaves repeated-prime cases with exactly two equal odd primes, and pairwise-distinct-prime cases.

## Cyclotomic descent for two equal exponents

Suppose first that `a^p+b^p=c^t`, with odd prime `p`, prime `t≠p`, and `gcd(a,b)=1`. Put

`U=a+b`, `V=(a^p+b^p)/(a+b)=a^(p−1)−a^(p−2)b+⋯−ab^(p−2)+b^(p−1)`.

Then `UV=c^t`. Modulo `U`, substituting `a≡−b` gives `V≡p b^(p−1) (mod U)`. Since `gcd(U,b)=1`, `gcd(U,V)` divides `p`. More precisely it equals 1 if `p∤U` and equals `p` if `p|U`. In the first case, `U=u^t` and `V=v^t` for positive integers `u,v`. In the second case, the lifting-the-exponent lemma gives `v_p(a^p+b^p)=v_p(a+b)+1`, since `p∤ab`, so `v_p(V)=1`. Every other prime of `V` occurs to exponent divisible by `t`. Therefore

`V=p v^t`, with `p∤v`, and `v_p(U)≡−1 (mod t)`.

The historical classification table in [Poonen–Schaefer–Stoll, Table 1](https://arxiv.org/pdf/math/0508174) lists the hyperbolic families `{2,n,n}` and `{3,n,n}` as determined (with sources and small cases distinguished in the [audit](source-darmon-merel.md)). These cover repeated-`p` branches when `t=2` or `3`; they do not supply a uniform result for `t≥5`. Thus a full proof for the remaining repeated-prime branch would need to handle, uniformly in distinct primes `p` (odd) and `t≥5`, the equations `V=v^t` and `V=pv^t` plus the remaining condition on `U`. This is a very restricted cyclotomic perfect-power problem, but nothing in the factorization excludes it. For example `1³+2³=3²` has `U=3` and `V=3`, fitting the `p|U` case; its exponent signature `(3,3,2)` is outside the hyperbolic range, but it disproves any unconditional claim that the factorization is impossible.

If the repeated exponent occurs across the equality, as `c^p−a^p=b^t`, replace `U` by `c−a` and `V` by `(c^p−a^p)/(c−a)`. The same congruence and valuation argument applies (with `c` and `a` coprime). The orientation cannot be silently ignored: fixed-signature results often count signed integer solutions while the Fermat–Catalan conjecture asks for positive `A+B=C`.

## Pairwise-distinct primes and an attempted height contradiction

For pairwise distinct prime `p,q,r`, the cyclotomic factorization above has no two equal powers to exploit. The uniformly valid inequality remains

`R=rad(ABC)≤xyz<C^σ`, where `σ=1/p+1/q+1/r<1`.

If the minimum prime exponent `m=min(p,q,r)` tends to infinity along a hypothetical sequence, then `σ≤3/m→0`, so `R=C^{o(1)}`. This looks extreme, but it does not contradict the known unconditional Stewart–Yu-type estimate reported in [the height notebook](optimized-heights.md), which only forces a polylogarithmic lower bound on `R`. Indeed that estimate merely gives `m≤(1+o(1))log C/loglog C`. If the minimum exponent stays bounded, pass to a subsequence with one fixed prime; `(2,3,ℓ)` with varying prime `ℓ≥7` already survives and no available fixed-signature theorem bounds the union. Neither branch yields a contradiction.

The real point of failure is not the FLT or cyclotomic algebra: it is an absent theorem excluding or uniformly bounding the moving-prime solutions of these cofactor equations and the pairwise-distinct-prime signatures. One cannot infer such a theorem from finiteness for each fixed `(p,q,r)`.

**No full proof has been obtained. No Lean formalization was attempted.**

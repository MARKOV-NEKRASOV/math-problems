# Attempt to finish Fermat–Catalan through the repeated-prime branch

**Outcome: incomplete.** I combined the source-checked all-prime reduction with the two simultaneous cyclotomic perfect-power conditions. A new archimedean gap and a 3-adic local construction clarify what the conditions force and where they fail to give a descent. Neither bounds the moving prime exponents, and the pairwise-distinct-prime signatures remain separate.

## Exact target

Suppose positive primitive bases satisfy `a^p+b^p=c^t`, where `p` is an odd prime, `t` is another prime, and `2/p+1/t<1`. The same signed equation describes positive solutions in which the repeated p-powers straddle the equality, after replacing one base by its negative. The deductions below that use positivity of *both* `a,b` apply only when the two p-powers are on the left.

Write `U=a+b` and `V=(a^p+b^p)/(a+b)`. Primitivity gives `gcd(U,V)|p`. If `p∤U`, then `U=u^t`, `V=v^t` with positive integers `u,v` in the positive-left orientation. If `p|U`, LTE gives `v_p(V)=1`, so `V=pv^t` and `v_p(U)≡−1 (mod t)`. The prior note `research/prime-repeated-attempt.md` and its independent review check these identities and the signed version.

## Testing the simultaneous powers by their real size

For `a,b>0`, write `s=a/(a+b)∈(0,1)`. The exact homogeneous identity gives

`V/U^(p−1)=s^p+(1−s)^p`.

Convexity yields `2^(1−p)≤s^p+(1−s)^p<1`. In the `p∤U` branch, substituting `U=u^t`, `V=v^t` gives

`2^((1−p)/t) u^(p−1)≤v<u^(p−1)`.                         (1)

Since `v` and `u^(p−1)` are integers, `v≤u^(p−1)−1`. Let `H=u^(p−1)`. Comparing this with (1) implies

`t≤(p−1)log 2 / [−log(1−1/H)] < (p−1)(log 2)H`.        (2)

The last strict inequality follows from `−log(1−x)>x` for `x∈(0,1)`. Thus for fixed `p`, a hypothetical sequence with `t→∞` forces `u→∞` at least on the scale `(t/((p−1)log2))^(1/(p−1))`. This is a real restriction, but it allows unbounded `u` and therefore no uniform upper bound on `t`.

For `p=3`, the exact identity `V=U²−3ab` sharpens the interpretation: `U=u^t`, `V=v^t` require

`u^(2t)−v^t=3ab`, `a+b=u^t`, and `4v^t−u^(2t)=3(a−b)²`. (3)

Equation (3) is a generalized Fermat equation with variable `t`. No checked theorem says its integer points are finite as `t` varies. The Eisenstein construction in the previous note shows `V=v^t` alone has coprime positive examples for arbitrarily large `t`; it does not make `U` a t-th power. I found no descent that uses *both* equations in (3) to decrease a positive height.

## Testing the ramified-prime valuation branch at 3

For every odd prime `t≥5`, set `a=3^(t−1)−1`, `b=1`. These are coprime positive integers and `U=a+b=3^(t−1)`. The odd-prime LTE formula gives `v_3(a³+b³)=v_3(a+b)+1=t`. Write `a³+b³=3^t w`, where `w∈Z_3^×`. Because `gcd(t,6)=1`, exponentiation by `t` is an automorphism of `Z_3^×≅{±1}×(1+3Z_3)`. Hence `w` has a t-th root in `Z_3^×`, and `a³+b³=c^t` has a solution `c∈3Z_3` for every such `t` with these *integer* `a,b`. This is a **3-adic local solution**, not an integer one. It proves that the LTE congruence `v_3(U)≡−1 (mod t)` and the local unit-power condition at 3 cannot by themselves eliminate the `3|U` branch uniformly.

## Primary-source restrictions and the remaining gap

Bennett–Bruni–Freitas, arXiv:1702.07827v1, Theorem 1.1, as checked in `research/prime-repeated-attempt.md`, excludes `(3,3,t)` for all `3≤t≤10^9`, for `t≡2 (mod 3)`, for `t≡2 or 3 (mod 5)`, and for additional residue classes. A surviving prime `t` must exceed `10^9` and satisfy `t≡1 or 4 (mod 15)` along with the other restrictions. Those residue classes still contain infinitely many primes. The 3-adic construction is compatible with the theorem because it claims only local solubility, not an integer solution.

The real bound (2), the equations (3), and the 3-adic test do not contradict each other or the remaining prime residue classes. They do not touch pairwise-distinct all-prime signatures such as `(2,3,t)`. A full Fermat–Catalan proof would need a new uniform theorem for these simultaneous perfect-power equations and the distinct-prime branches. No such theorem was proved here; no Lean formalization was attempted.

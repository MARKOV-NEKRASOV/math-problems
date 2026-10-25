# New arithmetic route: a growing Frobenius trace window for `(2,3,p)`

**Outcome: incomplete.** I tested whether the positive `(2,3,p)` subfamily can be closed by combining the reviewed `27a1` level-lowering branch with Hasse bounds and a growing run of matching Frobenius traces. The window is real but too short relative to the unbounded conductor of the Frey curve for a known unconditional isogeny conclusion. Other comparison curves and all remaining prime signatures also remain.

## Exact setting and new consequence

Assume a primitive positive solution `a²+b³=c^p` with prime `p≥17`, and that the FNS small twist `E_d` of `E:y²=x³+3bx−2a` has `E_d[p]≅F[p]` for `F=27a1` and `d∈{±1,±2,±3,±6}`. Here `c≥2`, `gcd(b,c)=1`, and `j(E)=1728b³/c^p` is a noninteger rational, so `E` is non-CM. The independent project note [prime-237-nonsplit.md](prime-237-nonsplit.md) derives from local Tate representations that every prime `q≥5` dividing `c` satisfies `q≥√p−1`, including the easy `q=p` case. Its premise is conditional on this one `27a1` residual branch.

Now let `q≥5` be a prime with `q<√p−1`. Then `q∤c`, so `E_d` has good reduction at `q` (the twist factor `d` has primes only 2,3); `F` also has good reduction there. The residual isomorphism gives `a_q(E_d)≡a_q(F) (mod p)`. Hasse gives `|a_q(E_d)−a_q(F)|≤4√q`. Since `q<√p−1`, one has `4√q<4p^(1/4)<p` for `p≥17` (the last inequality is equivalent to `p>4^(4/3)`). Therefore

`a_q(E_d)=a_q(27a1)` for every prime `5≤q<√p−1`.                 (1)

Thus a hypothetical unbounded sequence in this branch would give non-CM curves whose first growing interval of good Frobenius traces exactly matches the fixed CM curve `27a1` after an allowed small twist. FNS Lemma 6.1 already eliminates `p≡1 (mod 3)` for p≥17, so (1) primarily targets surviving `p≡2 (mod 3)`.

## Why the trace window does not finish the proof

Faltings's isogeny theorem compares traces at *all but finitely many primes*, not at a finite range depending on `p`; the range in (1) has endpoint roughly `√p`. Effective isogeny or Chebotarev bounds depend on the conductor or height of `E_d`, and `c` is unrestricted above. The same local computation forces its prime factors to be *large*, which is compatible with arbitrarily huge `c`. Thus one cannot pass from (1) to a rational isogeny with `27a1`, equal `j`-invariants, or a contradiction. The eight possible twists and seven fixed comparison curves from FNS do not alter this issue. A uniform trace-rigidity theorem independent of the Frey curve's height would be a new deep input and is not asserted here.

This route also cannot cover pairwise distinct prime signatures directly. For the universal full-2-torsion Frey curve `Y²=X(X−A)(X+B)`, each mod-exponent representation deletes the primes of only its matching powered coordinate; complementary conductors still depend on the other two bases. Comparing three trace windows does not give a fixed comparison curve without additional uniformity.

## Source check for a newer modular lead

The arXiv API on 25 October 2026 returned arXiv:2512.17845 (Pacetti–Villagra Torcomian, *On the generalized Fermat equation of signature (5,p,3)*). The project's `research/recent-families.md` records its primary Theorem C as conditional on the authors' Conjecture 1 and restricted to `3∤z`, large `p`, and other finite exceptional exponents. That theorem cannot close either the `(5,p,3)` family unconditionally or all-prime Fermat–Catalan. The 2026 `X_ns^+(13)` preprint arXiv:2608.10919v1, checked in [prime-237-nonsplit.md](prime-237-nonsplit.md), likewise treats a fixed level and leaves the all-large-level CM-only rational-point assertion open.

**Proof obligation still open:** show that no non-CM Frey curve in every surviving comparison branch has the required residual representation for arbitrarily large `p`, or independently establish a uniform finiteness theorem for every all-prime signature. The trace identity (1) is a sieve constraint, not that theorem. No complete proof or Lean formalization resulted.

# Full-conjecture attempt on repeated all-prime signatures

**Outcome: incomplete.** After the source-checked reduction of all composite-containing signatures, Fermat–Catalan still requires finiteness across all-prime hyperbolic signatures. This note attempts to remove the cases with exactly two equal odd prime exponents, including `(3,3,t)` for varying prime `t`. Primary and secondary family results exclude many subcases, but the remaining prime sets are infinite.

## Setup and orientation

Let `a^p+b^p=c^t`, with odd prime `p`, prime `t≠p`, primitive nonzero signed bases and `1/p+1/p+1/t<1`. Signed bases handle all positive Fermat–Catalan orientations: if the repeated `p` exponents straddle `=`, write `c^p−a^p=b^t` as `c^p+(-a)^p=b^t`. We count distinct powered values, not representations. The case `t=2` is excluded by Bennett–Skinner Theorem 1.1 (`C=1`); Poonen–Schaefer–Stoll Table 1 historically lists the `t=3` family `{3,p,p}` as determined, but I do not assume an unaudited uniform exception list. Fermat's Last Theorem excludes `p=t`.

## Cyclotomic contradiction attempt

Factor `a^p+b^p=UV`, where `U=a+b` and `V=(a^p+b^p)/(a+b)`. Since `V≡p b^(p−1) (mod U)` and `gcd(U,b)=1`, `gcd(U,V)|p`. If `p∤U`, coprimality and `UV=c^t` imply `U=u^t`, `V=v^t`. If `p|U`, LTE gives `v_p(V)=1`, so `V=pv^t` with `p∤v` and `v_p(U)≡−1 (mod t)`. These are exact necessary conditions, including for signed `a,b` after replacing absolute-value factors where needed. They do not rule out solutions while both `p,t` vary. The tempting assertion that a primitive prime divisor of `V` must have an odd or non-`t`-multiple valuation is unsupported.

For `p∈{5,7,11,13}`, the source-checked Chen–Koutsianas survey (arXiv:2507.15149v1, Theorem 11.5) reports an unconditional exclusion for every integer `t≥2` when `2|U` or `p|U`. The original `p=11` source was checked in the existing project review; the other three original papers were not independently reread here. Thus any surviving solution for these four fixed `p` has `U` odd and `p∤U`, forcing the clean double-perfect-power system `U=u^t`, `V=v^t`. This is useful, but no cited theorem eliminates that system uniformly in `t`.

The condition `V=v^t` by itself is genuinely weak even when `p=3`. In the Eisenstein integers `Z[ω]`, `ω²+ω+1=0`, let `α=N+ω` with large `N≡0 or 1 (mod 3)` and write `α^t=a+bω`. Choose `N` large relative to `t`, so the complex argument of `α^t` lies between 0 and `π/3`; then `a,b>0`. The coefficients are coprime: a rational prime dividing both would divide `α^t` as a rational integer, but for split or inert primes this would force it to divide both coefficients of `α=N+ω`; the only ramified prime is 3, and `N²−N+1` is prime to 3 by the choice of `N`. Yet `a²−ab+b²=Norm(α^t)=(N²−N+1)^t`. Thus there are coprime positive `a,b` for arbitrarily large `t` with the cyclotomic cofactor `V` a `t`th power. The *simultaneous* requirement that `U=a+b` be a `t`th power is the hard extra condition; ignoring it cannot prove finiteness.

Even retaining both perfect-power conditions only recasts the problem. Since `4V=U²+3(a−b)²`, the `3∤U` branch becomes `4v^t=u^{2t}+3(a−b)²`. This is another variable-exponent generalized Fermat equation; the identity is exact, but there is no checked theorem here proving it insoluble for all prime `t`. Treating that new equation as easier without an exclusion theorem simply moves the gap.

## A stronger primary-source filter for `(3,3,t)`

I read Bennett–Bruni–Freitas, *Sums of two cubes as twisted perfect powers, revisited*, arXiv:1702.07827v1, Theorem 1.1 and its following discussion in the PDF. The theorem summarizes proven exclusions for nonzero pairwise-coprime **signed integers** `a^3+b^3=c^n`. Its displayed list includes all exponents `3≤n≤10^9`, all `n≡2 (mod 3)`, all `n≡2,3 (mod 5)`, and additional explicit congruence classes modulo 78, 106, and 1296. Consequently a hypothetical primitive `(3,3,t)` solution with prime `t≥7` must have `t>10^9`, `t≡1 or 4 (mod 15)`, and avoid the other listed classes. This is a genuine infinite-family restriction, not merely a bounded search result, because the congruence exclusions apply to every exponent in those classes.

The same paper explicitly identifies an elliptic curve of conductor 72, labelled `72A1`, as the obstruction to the straightforward modular proof of the untwisted `a^3+b^3=c^n` equation. Its later theorems mainly concern a nontrivial prime-power coefficient `q^α` on the right; setting `q=1` is outside those hypotheses. The residual prime classes `t≡1 or 4 (mod 15)` are infinite as possible prime indices (Dirichlet), so Theorem 1.1 alone cannot yield finiteness. I found no uniform theorem in the checked source removing all those classes.

## Exact failure of a proposed full proof

After the reductions, the proposed proof would say: every repeated-prime signature either has `t=2` or `3`, lies in an excluded congruence class, or yields `U=u^t` and `V=v^t`; therefore finitely many solutions exist. The final inference is invalid. For `p=3`, infinitely many allowable prime `t` remain after the known congruence filters. For `p≥5`, `p` itself varies, and no theorem checked here bounds solutions of the cofactor-perfect-power system uniformly in `(p,t)`. Restricting `a+b` to be odd and prime to `p` for four fixed `p` does not bound its size or the exponent `t`.

This attempt gives a sharper target—especially `(3,3,t)` with `t>10^9`, `t≡1 or4 (mod15)`—but **does not prove the full conjecture**. It also leaves pairwise-distinct-prime signatures untouched. No Lean formalization was attempted.

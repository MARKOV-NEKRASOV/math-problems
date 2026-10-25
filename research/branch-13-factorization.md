# Bounds role: a concrete F2-QR attempt, 25 October 2026

I read AGENTS.md and all three mandatory F2→F0 documents. I targeted the nonunit, positive, primitive F2-QR subbranch `(p,4,4)` with odd varying `p≥3`, equation `x^p+y^4=z^4`, and the opposite-parity case `y,z` of opposite parity. This is hyperbolic. I sought an upper bound on `p` or `log z^4` incompatible with the radical bound. **No complete F2-QR proof resulted.**

## B13.1, exact factor reduction (PROVED; elementary)

For each odd integer `p≥3`, coprime positive integers `y<z` of opposite parity, and positive integer `x`, the equation `x^p+y^4=z^4` holds if and only if there are coprime odd positive integers `u<v` and `w>0` such that

`u^(2p)+v^(2p)=2w^p`, `y=(v^p-u^p)/2`, `z=(v^p+u^p)/2`, `x=uvw`.

Proof: `z^4-y^4=(z-y)(z+y)(z²+y²)`. The three factors are odd. Their pairwise gcds are 1: `gcd(z-y,z+y)` divides 2 and both are odd; `gcd(z±y,z²+y²)` divides `2y²`, while `gcd(y,z)=1` and each factor is odd. Each factor of the pth power `x^p` is therefore a pth power, say `u^p,v^p,w^p` in displayed order. Solving for y,z and substituting in `z²+y²=w^p` proves the relation. Conversely, coprime odd u,v give integer positive y,z of opposite parity because odd pth powers differ by 2 mod 4 or sum by 2 mod 4, and `gcd(y,z)=1`. Then the algebra yields `z^4-y^4=(uvw)^p`. No assumption that p is prime is needed. □

This gives an exact bijection between the indicated primitive subbranch and primitive odd solutions of the *coefficient-2 generalized Fermat equation* `u^(2p)+v^(2p)=2w^p`. For the entire `(p,4,4)` F2-QR branch, the same-parity case needs another treatment; because `gcd(y,z)=1`, that case means both are odd. It is not covered by this lemma.

## B13.2, the complementary 2-adic gap (PROVED; elementary)

If `y,z` are both odd, let `t=max(v₂(z−y),v₂(z+y))`. Exactly one of `z−y,z+y` has 2-adic valuation 1, the other has valuation `t≥2`; also `v₂(z²+y²)=1`. Therefore

`p·v₂(x)=v₂(z⁴−y⁴)=t+2`.

Consequently `t≡−2 (mod p)` and `t≥p−2` (for `p=3`, `t≥4`). Whichever of `z−y` and `z+y` has valuation `t` is at least `2^t`; hence `2z=(z−y)+(z+y)>2^t`, so `z>2^(p−3)` and `log(z⁴)>4(p−3)log 2`. This raises the elementary height lower bound for the both-odd slice by a factor approaching four, but still supplies **no upper bound**, so it cannot close the branch. The moving 2-adic gap is allowed to grow exponentially with p.

**Previous bound → new restriction → distance to closure.** Previously the general fixed-gap BEG theorem bounded p only if `D=z-y` was fixed, and the radical estimate alone gave `R≤C^(1/p+1/2)`. Now the opposite-parity slice has `D=u^p` and `z+y=v^p`, and is reduced to one explicit coefficient-2 equation. However u,v,w can grow with p, and the exact Darmon–Merel theorem scope for this coefficient-2 family was not verified in this cycle. No upper `L≤κT+o(p)` with `κ<2` (the F2 threshold for 4,4) follows. Even FLT does not apply to the coefficient-2 equation. The reduction therefore does **not** close F2-QR, F1, or F0. It is a source-check target, not an asserted original theorem.

**Counterexample to a tempting shortcut.** The three factors being pth powers does not imply `u=v=1`: the coprime odd pair `(u,v)=(1,3)` has no elementary contradiction from the factorization alone. The new relation `1+3^(2p)=2w^p` must itself be ruled out; bounding its left side below cannot do so.

## Radical/height gate revisited

Here `C=z^4`, `T=log rad(xyz)`, `L=log C`, and `σ=1/p+1/2`. Thus `T≤σL`. A hypothetical upper `L≤κT+E(p)` with any constant `κ<2` and `E(p)=o(p)` would contradict `L≥p log 2` only if **the variable p occurs on the output powered value**. In the present orientation the output exponent is 4, and `L≥p log 2` follows instead from `x^p<z^4` and x≥2 only as `log z^4>p log2`. This does hold because x=uvw≥2 for nonunit x. Then `(1−κσ)L≤E(p)` contradicts E=o(p). The constants must be uniform in y,z and p, and the coefficient-2 reduction supplies no such upper. (The branch-wide threshold is κ<2.)

## Literature check

At the beginning I re-read the local project source audit `research/source-darmon-merel.md` and Poonen–Schaefer–Stoll arXiv:math/0508174v1 Table 1 context: its solved `{2,n,n}`/`{3,n,n}` rows do not directly include `(p,4,4)`. At the close I queried the arXiv API on 2026-10-25 for exact phrase `generalized Fermat equation (4,4,n)` (zero hits) and `Fermat Catalan conjecture` (two broad hits, arXiv:2410.21552v1 and arXiv:1511.05278v1). These are discovery checks, not a completeness claim or theorem audit. I imported no external theorem. Darmon–Merel 1997, DOI `10.1515/crll.1997.490.81`, may be relevant to the coefficient-2 equation since it reads `(u²)^p+(v²)^p=2w^p`; **the theorem's exact statement remains unverified** because the original text was inaccessible. Do not mark the opposite-parity slice closed until its hypotheses have been checked.

**Next falsifiable step:** Seek a primary theorem for all primitive odd `u<v` satisfying `u^(2p)+v^(2p)=2w^p`, with a p-independent large-exponent cutoff and explicit treatment of u=1. Then separately handle y,z both odd and see if all `(p,4,4)` is solved. If the coefficient-2 equation still requires p-dependent level/newforms, abandon it as a route to the full F2 branch.

# Independent review of v10 quantitative lemmas

**Verdict:** The clean and ramified mod-`p` size gaps in [congruence-corrected-size-gaps.md](congruence-corrected-size-gaps.md) check out under their stated positive-left, coprime, and `gcd(t,p−1)=1` hypotheses. The effective fixed-gap exponent bound (6) in [effective-fixed-gap-bounds.md](effective-fixed-gap-bounds.md) correctly specializes Bérczes–Evertse–Győry (BEG), arXiv:1301.7168v1, Theorem 2.3, equation (2.7). Both are necessary/restricted bounds, not a full proof.

## Repeated-prime calculations

In the clean branch `p∤U=a+b`, Fermat's little theorem gives `V=(a^p+b^p)/U≡1 (mod p)`. Since `V=v^t`, `H=u^(p−1)≡1 (mod p)`, and `gcd(t,p−1)=1`, one gets `v≡H≡1 (mod p)`. Positive-left convexity gives `v<H`, so `H−v` is a positive multiple of `p` and is at least `p`. Substitution into `v≥2^{(1−p)/t}H` yields exactly bound (1), with the logarithmic inequality in the correct direction.

In the ramified branch, LTE gives `U=p^(t−1)u^t`, `V=pv^t`, `p∤v`. Expanding with `b=U−a` gives `V≡p a^(p−1) (mod p²)`; coprimality gives `p∤a`. Hence `v^t≡1 (mod p)` and `v≡1 (mod p)`. For `H=p^(p−1)u^(p−1)`, direct algebra confirms `V/U^(p−1)=p^p(v/H)^t`. As `H≡0` and `v≡1 (mod p)`, the positive gap `H−v` is at least `p−1`, producing bound (2) as written. The argument does not transfer its convexity inequality to signed differences.

For `(p,t)=(3,t)` with prime `t>10^9`, the numerical cutoffs are correct: `(2 log 2/3)·46519²≈999,988,354.97` and `(9 log 108/2)·6889²≈999,927,390.33`, both below `10^9`. Thus the least roots allowed by these **necessary** bounds are `u≥46520` clean and `u≥6890` ramified. The parity refinements `46523` and `6891` in the opposite-parity subcases also check out. They exclude bounded-root parameter ranges, not all `t`.

## BEG specialization

I inspected the local arXiv v1 text at Theorem 2.3 and equation (2.7). It states `m≤(10n²s)^(40ns)|D_K|^(6n) P_S^(n²) exp(11nd ĥ)` for a squarefree degree-`n≥2` polynomial `f`, `m≥3`, and `y` neither zero nor a root of unity. For `K=Q`, `S={∞}`, `b=1`, integer coefficients of size at most `H`, we have `d=s=|D_K|=P_S=1` and `ĥ=log H`. Therefore `m≤(10n²)^(40n)H^(11n)` exactly as the note states. The coefficient estimate `H_D≤1+(1+|D|)^min(P,Q)` is safe after choosing whether to parametrize by the first or second fixed base; the degree remains `n_0=max(P,Q)` except for signed equal exponents, where it is `P−1`. Substitution gives formula (6) with no reversed inequality in the hyperbolic range; signed `(2,2,W)` is excluded because its polynomial has degree one. The signed `(3,3,W)` degree-2 case is covered by Theorem 2.3 for `W≥4` under hyperbolicity.

The note's use of BEG Theorems 2.1–2.2 for height cutoffs is also consistent with the displayed equations (2.4) and (2.6) after `K=Q,S={∞}` specialization. I checked the theorem statements, not BEG's complete proofs. No uniform bound in `P,Q,D` follows; formula (6) grows with those parameters.

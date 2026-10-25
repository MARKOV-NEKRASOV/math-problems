# Effective bounds for the fixed-gap Fermat–Catalan slice

**Scope.** This quantifies the signed fixed-gap theorem of [signed-fixed-gap-finiteness.md](signed-fixed-gap-finiteness.md). It yields an explicit, astronomically large bound for the variable exponent and explicit height bounds for each fixed exponent. It does **not** bound solutions uniformly when the gap or the two fixed exponents move.

## Exact external theorem and specialization

Attila Bérczes, Jan-Hendrik Evertse, and Kálmán Győry, *Effective results for hyper- and superelliptic equations over number fields*, arXiv:1301.7168v1 (30 January 2013), Theorems 2.1–2.3, directly inspected in the v1 PDF and TeX source, treat `f(X)=bY^m` over `S`-integers. They assume `f` has degree `n≥2` and no multiple complex roots; Theorem 2.3 also requires `m≥3` and `Y` neither zero nor a root of unity. Theorems 2.1 and 2.2 give explicit logarithmic-height bounds for fixed `m≥3,n≥2` and for `m=2,n≥3`, respectively.

Specialize to `K=Q`, `S={∞}`, `b=1`, and a squarefree `F∈Z[T]` of degree `n`. Put `H=max(1, absolute values of all coefficients of F)`. Then the paper's `d=s=|D_K|=P_S=Q_S=1` and `\hat h=log H`. For an integer solution `F(t)=z^W` with `z≥2` and `W≥3`, Theorem 2.3, equation (2.7), gives the **explicit** exponent bound

`W ≤ C_n H^(11n)`, where `C_n=(10n²)^(40n)`.                 (1)

Theorem 2.1, equation (2.4), gives for `W≥3`

`log max(1,|t|), log z ≤ (6n)^(14 W³ n³) H^(8 W² n³)`.     (2)

For `W=2` and `n≥3`, Theorem 2.2, equation (2.6), gives

`log max(1,|t|), log z ≤ (4n)^(212 n⁴) H^(50 n⁴)`.       (3)

The paper states these as height bounds; for rational integers the logarithmic height is `log max(1,|t|)`. Equations (1)–(3) therefore make the fixed-polynomial solution set **effectively enumerable in principle**. The expressions are far too large to justify an actual exhaustive search here.

## Parameters for fixed-gap Fermat–Catalan

Fix `P,Q≥2`, `ε∈{+1,−1}`, and `D∈Z\{0}`. Write `m^P+ε n^Q=k^W>0` with `m−n=D`, `k≥2`, and require the Fermat–Catalan hyperbolicity condition `1/P+1/Q+1/W<1`. Use `T=m`, so `F(T)=T^P+ε(T−D)^Q`; the independent squarefreeness argument in the signed fixed-gap note applies. The degree is

- `n_0=max(P,Q)` if `ε=+1` or `P≠Q`;
- `n_0=P−1` if `ε=−1` and `P=Q`.

The signed `P=Q=3` edge has `n_0=2`, which **is covered** by (1) and (2) for `W≥3`. Hyperbolicity forces `W>3`, so the degree-2, `W=2` case outside Theorem 2.2 is irrelevant to that Fermat–Catalan slice. The signed `P=Q=2` case has `n_0=1` and is never hyperbolic; it must be excluded from (1)–(7). Indeed, `(n+1)²−n²=2n+1` can equal `3^W` for every `W` by taking `n=(3^W−1)/2`.

For the displayed `F`, its coefficient height `H_D` can be computed exactly by expanding the polynomial. A safe explicit estimate is

`H_D ≤ 1+(1+|D|)^Q`.                                      (4)

One can instead parametrize with `T=n`, giving `F(T)=(T+D)^P+εT^Q` and the alternative estimate `H_D≤1+(1+|D|)^P`. Choose the smaller translated exponent to obtain

`H_D ≤ M_{P,Q,D}:=1+(1+|D|)^min(P,Q)`.                    (5)

Substitute `n=n_0≥2` and `H=M_{P,Q,D}` in (1)–(3). In particular every hyperbolic `W≥3` satisfies the completely explicit bound

`W ≤ (10n_0²)^(40n_0) [1+(1+|D|)^min(P,Q)]^(11n_0)`.     (6)

For positive `(2,3,W)` with `D=1`, choose `T=y`; then `(T+1)²+T³=T³+T²+2T+1`, so `n_0=3`, `H_D=2`, and (1) gives `W≤90^120·2^33`, a 245-digit number. This illustrates effectivity, not practical solvability.

## Quantitative escape and prioritized subproblem

For fixed `P,Q,ε`, let `n_0` be as above, `a=min(P,Q)`, and `C=(10n_0²)^(40n_0)`. Inverting the safe bound (6) gives, for a solution with variable exponent `W`, the necessary condition

`|D| ≥ max(0, ((W/C)^(1/(11n_0))−1)_+^(1/a)−1)`.        (7)

Here `_+` means `max(0,·)`; because `D` is integral one may take the ceiling of the right side. Thus if the two input exponents remain fixed and `W→∞`, their base gap must grow at least at this very weak power scale. The bound is compatible with unbounded gaps and does not prove Fermat–Catalan.

**Specific next construction:** for a chosen fixed input pair, begin with `(P,Q)=(2,3)`, and a concrete finite gap range `1≤|D|≤B`, compute the exact `H_D` and (1) for every `D`, then replace the theoretical giant bounds with certified integral-point computations on `Y^W=F_D(T)` for the remaining exponent cases. A finite `B` eliminates only that bounded-gap slice, but explicit classifications may reveal a structural obstruction that can be generalized to growing `D`. Such a generalized obstruction would need a theorem whose constants are uniform in `D`; the present estimates grow polynomially with `|D|` in (6), and the height bounds grow vastly faster. No such uniform obstruction has been proved here.

**Boundary on effectivity.** The prior proof invoking only Schinzel–Tijdeman and Siegel established finiteness but did not supply a numerical height cutoff; Siegel alone is ineffective in this role. The checked Bérczes–Evertse–Győry theorems supply explicit cutoffs for this squarefree-polynomial slice. They do not make an actually feasible enumeration, and do not give a bound independent of `(P,Q,D)`. No complete proof or Lean formalization is implied.

# Role B: quantitative slack audit for the F2 → F0 program

**Cycle date:** 25 October 2026. **Outcome:** one proved sufficient slack lemma and one source-checked F0 implication; no unconditional upper radical bound and no Fermat–Catalan proof. Count distinct powered-value triples, not exponent tuples. All statements below concern primitive positive `A=x^p`, `B=y^q`, `C=z^r=A+B` with `x,y,z≥2`, `p,q,r≥2`, and `σ=1/p+1/q+1/r<1`. Put `R=rad(ABC)=rad(xyz)`, `L=log C`, `T=log R`, `m=min(p,q,r)`, `M=max(p,q,r)`.

## B12.1 — proved general slack lemma

The elementary bounds are `T≤σL` and `L≥M log 2`. The latter holds even when the exponent `M` belongs to `A` or `B`, since `C>A,B` and every base is at least 2. Thus any proposed height/radical upper bound

`L ≤ κ(p,q,r) T + E(p,q,r)`

with `s(p,q,r):=1−κ(p,q,r)σ>0` implies `sL≤E` and therefore

`E ≥ s M log 2`.                                                   (1)

Consequently **no infinite nonunit family can satisfy such an upper bound with `E=o(sM)` uniformly along that family**. This is a sufficient-criterion lemma, not an established upper bound. Its usefulness is that it states exactly how much dependence on moving exponents the constants may have.

| Profile | Candidate upper bound that would close it | Prior specification → refined allowable error | Dependence that remains fatal |
| --- | --- | --- | --- |
| F2-PQ, F2-PR, F2-QR | Fix the two exponents `a,b`; obtain `κ_{a,b}<ab/(a+b)`, and `L≤κ_{a,b}T+E_{a,b}(w)` as the third exponent `w→∞`. | Previously a fixed multiplicative `K_{a,b}` (`E=O_{a,b}(1)`); it actually suffices to have `E_{a,b}(w)=o_{a,b}(w)`, equivalently `K_{a,b,w}=exp(o_{a,b}(w))`. | If the constants grow linearly in `w` with large coefficient, the inequality may remain compatible with `L≥w log2`. Dependence on `a,b` is harmless only while they stay fixed. |
| F1-P, F1-Q, F1-R | Fix `a`; obtain `κ_a<a` and `L≤κ_aT+E_a(w)` with `w=min` of the other two diverging exponents. | Previously fixed `K_a`; `E_a(w)=o_a(w)` suffices since `s→1−κ_a/a>0` and `M≥w`. | A bound whose constant depends exponentially on either moving exponent may overwhelm the slack. |
| F0 | Obtain `κ=(1−δ)m/3` with absolute `δ>0`, uniformly in all three moving exponents. | The trivial lower bound alone allows `E=o(M)`; the published Stewart–Yu inequality below also allows `E=o(max{M,m log m})`. | Neither proposed `κ` nor this error control is proved. A bound valid only with fixed `p,q` has uncontrolled constants here. |

For F2, `σ=1/a+1/b+1/w`, so `s→s_0:=1−κ_{a,b}(1/a+1/b)>0`. For F1, `σ=1/a+o(1)` and `s→s_0:=1−κ_a/a>0`. These facts prove the table's implications. More sharply, `E(w)≤λ w+o(w)` is still sufficient when `λ<s_0 log2`, because `M≥w` in (1); `o(w)` is a convenient source-independent condition. The seven profiles are all still open; a result for one row does not close the others. Unit bases are excluded here deliberately: `1^w+2³=3²` represents the same powered-value triple for every `w≥7` and shows why `L≥M log2` fails when an exponent is put on 1.

**Existing F2 laboratory under this test.** The repository's effective signed fixed-gap result uses Bérczes–Evertse–Győry to give `w≤(10n²)^(40n)[1+(1+|D|)^a]^(11n)` with `a=min(P,Q)`, `n=max(P,Q)` except signed equal exponents. Thus `log w≤40n log(10n²)+11n log[1+(1+|D|)^a]`. The polynomial squarefreeness proof persists when `P,Q` grow, but this constant becomes of order `n a log(1+|D|)` and the gap `D` itself can move. Moreover it bounds `w` in terms of `D`, rather than giving the needed upper `L≤κT+E`. Therefore it does not pass the F2-to-F1/F0 bridge as currently stated. This is an explicit dependence audit, not a criticism of the fixed-gap theorem.

## B12.2 — F0 Stewart–Yu implication, with source boundary

The reported unconditional Stewart–Yu estimate for coprime positive `A+B=C` is

`L ≤ K R^(1/3) (log R)^3 = K e^(T/3) T³`                    (2)

with an absolute `K`. The original Stewart–Yu 2001 paper, DOI `10.1215/S0012-7094-01-10815-6`, remains **METADATA_ONLY** in the project's paper database because its full text was inaccessible here. I directly read the **introduction, page 2** of Héctor Pastén, *The largest prime factor of n²+1 and improvements on subexponential ABC*, arXiv:2312.03566v1 (6 December 2023), which explicitly restates (2) and attributes it to Stewart–Yu. Pastén's Theorem 1.4 was also read as a theorem statement; its proof was not audited. Thus (2) is well-corroborated by a later primary research paper, but its original proof has not been checked in this project.

For F0, `T≤3L/m`. Since the right side of (2) is increasing for `T>0`, with `u=L/m` we get

`m u = L ≤ 27K e^u u³`, hence `m ≤ 27K e^u u²`.       (3)

Taking logarithms, `u≥log m−2log u−log(27K)`. If `u≥log m`, this already beats the desired bound; otherwise `log u≤loglog m`, so

`L≥m(log m−2loglog m−O_K(1))`.                         (4)

Combining (4) with `L≥M log2` gives `L≥c max{M,m log m}` for some absolute `c>0` and all large `m` (assuming the absolute `K` in (2)). Now the **unproved** objective U from the updated repository,

`L≤((1−δ)m/3)T+E(p,q,r)`, `δ>0` absolute,

would imply `δL≤E` by `T≤3L/m`. It would therefore close F0 if `E=o(max{M,m log m})` uniformly along all F0 solutions. If `E` is allowed to depend only on `m`, the repository's original `E(m)=o(m log m)` is the natural worst-case sufficient condition. This proves sufficiency only; it supplies no U-type upper estimate.

## B12.3 — a newer abc result does not furnish U

Pastén arXiv:2312.03566v1, Theorem 1.4(2), states a subexponential bound

`L ≤ q_* exp(κ sqrt(T log T))`, where `q_*=min{P(A),P(B),P(C)}` and `P(n)` is the largest prime factor.

This improves a different Stewart–Yu estimate in a regime with controlled `q_*`, but it has no coefficient of order `(1−δ)m/3` times `T` and does not alone close F0. As a **consistency test of inequalities only**, the abstract scale `L=m²`, `T=m`, `q_*≥2` satisfies `T≤3L/m`, (2), and Pastén's displayed inequality for all sufficiently large `m` and every fixed `κ>0`. It is not claimed to come from a Fermat–Catalan solution. The scale shows why substituting the newer bound into the radical inequality does not create a contradiction by itself.

## Seven-branch status and next falsifiable task

F2-PQ, F2-PR, F2-QR: **OPEN**. F1-P, F1-Q, F1-R: **OPEN**. F0: **OPEN**. B12.1 refines a *sufficient* upper-bound target for all profiles; B12.2 audits F0 sufficiency, and B12.3 falsifies the idea that the cited Pastén bound already supplies it. No mathematical proof of the required upper bound was obtained.

**Next task:** for one explicit F2 family, seek a proved upper `L≤κ_{a,b}T+E_{a,b}(w)` with `κ_{a,b}<ab/(a+b)` and compute the **exact** growth of `E_{a,b}(w)` from field degree, discriminant, conductor and modularity constants. The first falsifiable gate is `E_{a,b}(w)=o(w)`; if it grows at least linearly with an uncontrolled coefficient, the proposed method does not meet even the F2 threshold. To bridge to F1/F0, the dependence on `a,b` must then be bounded as they themselves grow. Do not promote a fixed-pair theorem to uniformity.

**Literature at start and end of cycle:** queried arXiv metadata for Stewart–Yu/abc and recent generalized-Fermat papers, rechecked arXiv:2312.03566v1 metadata and PDF introduction/Theorem 1.4, and attempted direct DOI and Project Euclid access to Stewart–Yu (403). No claim of exhaustive literature search; the primary full text of Stewart–Yu remains the next source-audit target. No Lean formalization was attempted.

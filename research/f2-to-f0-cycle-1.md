# F2 → F0 research cycle: uniformity audit

**25 October 2026. Status: incomplete.** This cycle follows the [new agent protocol](AGENT_F2_TO_F0_SPEC.md). The objective is finiteness of **distinct powered-value triples** `(A,B,C)=(x^p,y^q,z^r)` with `A+B=C`, positive primitive bases, and `1/p+1/q+1/r<1`. Unit bases and the exceptions in the [prime-signature reduction](reduction-to-prime-signatures.md) remain separate. No complete proof was found; no Lean formalization was started.

Four roles worked on geometry, inequalities, permanent literature discovery, and independent adversarial review. Their full records are [geometry](f2-f0-geometry.md), [bounds](f2-f0-bounds.md), [source watch](f2-f0-literature-watch.md), [protocol review](review-f2-f0-protocol.md), and [cross-review](review-f2-f0-lemmas.md). The literature role searched at the start and end of the cycle; the source table records exact versions and reading limits.

## What the new lemmas establish

**B12.1, a sufficient slack lemma (PROVED).** Put `L=log C`, `T=log rad(ABC)`, `M=max(p,q,r)`, and `σ=1/p+1/q+1/r`, with all bases at least 2. The elementary inequalities `T≤σL` and `L≥M log 2` imply that any *proposed* upper `L≤κT+E`, with `s=1−κσ>0`, must have `E≥sM log 2`. Thus an actual upper bound with `E=o(sM)` would eliminate an infinite family. For F2 with fixed exponents `a,b`, a slope `κ<ab/(a+b)` can tolerate `E_{a,b}(w)=o(w)` as the third exponent `w→∞`, rather than requiring a constant error. For F1 with one fixed exponent `a`, slope `κ<a` and a uniform sublinear error in the smaller of the two growing exponents would suffice. **No such upper bound was obtained.** The permitted constants may depend on `a,b` only while those exponents stay fixed.

**F0 error budget (sufficiency audited, upper bound unproved).** The proposed objective U from [the geometric-barrier note](F2_TO_F0_GEOMETRIC_BARRIER.md) has slope `(1−δ)m/3`, `m=min(p,q,r)`. It would imply `δL≤E`. Pastén's [arXiv:2312.03566v1](https://arxiv.org/abs/2312.03566v1), introduction, restates Stewart–Yu's `L≤K R^(1/3)(log R)^3` with absolute `K`, from which `L≥m(log m−2loglog m−O(1))` follows when `R≤C^(3/m)`. Alongside `L≥M log 2`, an error `E=o(max{M,m log m})` would contradict an infinite F0 sequence; the protocol's `E(m)=o(m log m)` remains a sufficient worst-case condition when the error depends only on `m`. The original Stewart–Yu 2001 article was not accessible here, so its exact displayed theorem is supported by Pastén's later research-paper restatement, not a primary proof audit. Pastén's newer subexponential bound does **not** yield objective U.

**A12-F, a field-dependence test (PROVED for the cited construction).** The rank-two hypergeometric motive for distinct odd `q,r` in [Cazorla García–Villagra Torcomian](https://arxiv.org/abs/2503.21568v2) and [Golfieri Madriaga–Pacetti](https://arxiv.org/abs/2412.08804v2) is presented over `F=Q(ζ_q)^+Q(ζ_r)^+`. Elementary cyclotomic field theory gives

`[F:Q]=(q−1)(r−1)/4`,  `|disc F|=q^((q−3)(r−1)/4) r^((r−3)(q−1)/4)`.

When all exponents grow and `m=min(p,q,r)`, `log|disc F|≥((m−3)(m−1)/2)log m`. Therefore an **uncancelled positive multiple** of `log|disc F|` in a proposed F0 additive error cannot be `o(m log m)`. This is a falsifiable dependency test, not a theorem that such a term is unavoidable. The field is fixed in an F2 family with `q,r` fixed; its degree grows in F1/F0. Naive induction of a rank-two representation to `Q` has rank `2[F:Q]`; this does not preclude a different descent. The 2026 rank-two paper [arXiv:2603.17978v1](https://arxiv.org/abs/2603.17978v1) has selected field and congruence theorems, while its fuller descent remains Conjecture 4.5. No claimed bound on the **minimal** field of every motive follows.

**Geometric design barrier (PROVED within scope; known ingredient).** The [earlier Galois three-point theorem](F2_TO_F0_GEOMETRIC_BARRIER.md) is algebraically sound for pairwise-coprime *exact whole local-monodromy orders*. Conder–Young [arXiv:2410.06571v1](https://arxiv.org/abs/2410.06571v1) records the perfectness of the corresponding triangle group, so this ingredient is not new. The [non-Galois extension](f2-f0-geometry.md) gives a perfect monodromy group and `e1e2e3 | |G|≤n!` for a connected degree-`n` three-point cover with the same exact orders. For distinct prime orders, the direct `n≥max(e_i)` is already a stronger numerical degree lower bound. These are design filters, not Diophantine contradictions. The cited hypergeometric motive has local types `{q,∞,r}`, so the finite three-index hypothesis does not directly apply to it.

## Seven-branch matrix after this cycle

| Escape profile | Current proved restriction | Sufficient closure target still missing | Status |
| --- | --- | --- | --- |
| F2-PQ: `p,q` fixed, `r→∞` | Signed fixed-gap and fixed-support finiteness for fixed auxiliary parameters; effective BEG exponent cap depends on the gap. | `L≤κ_{p,q}T+o(r)` with `κ_{p,q}<pq/(p+q)`, or another uniform F2 argument. | **OPEN** |
| F2-PR: `p,r` fixed, `q→∞` | Same signed lemmas after moving terms; no uniform control as the gap/support moves. | `L≤κ_{p,r}T+o(q)` with `κ_{p,r}<pr/(p+r)`. | **OPEN** |
| F2-QR: `q,r` fixed, `p→∞` | Same limitation; specialized `(2,3,p)` modular filters eliminate proper base-residue families only. | `L≤κ_{q,r}T+o(p)` with `κ_{q,r}<qr/(q+r)`. | **OPEN** |
| F1-P: `p` fixed, `q,r→∞` | `rad(ABC)<C^(1/p+o(1))`; fixed-field HGM constants may already vary with `q` or `r`. | Uniform `L≤κ_pT+o(w)`, `κ_p<p`, `w=min(q,r)`. | **OPEN** |
| F1-Q: `q` fixed, `p,r→∞` | Same radical form and moving-field dependence. | Uniform `L≤κ_qT+o(w)`, `κ_q<q`, `w=min(p,r)`. | **OPEN** |
| F1-R: `r` fixed, `p,q→∞` | Same radical form and moving-field dependence. | Uniform `L≤κ_rT+o(w)`, `κ_r<r`, `w=min(p,q)`. | **OPEN** |
| F0: `p,q,r→∞` | `rad(ABC)≤C^(3/m)`; the named rank-two construction has growing field degree/discriminant. | Prove objective U with absolute slope margin and controlled error, or another uniform contradiction. | **OPEN** |

The seven profiles classify subsequences of a hypothetical infinite family, after choosing exponent representations and using fixed-signature finiteness. A proof of one row does not close another. The [previous case bounds](bounds-and-priorities.md) and [latest tactical refinements](audit-prior-bounds.md) are useful filters, but none gives the upper inequality in this table.

## Audited tactical bounds from the preceding pass

| ID and status | Previous restriction → checked refinement | Exact distance to the F2 → F0 target |
| --- | --- | --- |
| V11-G, **PROVED** for coprime signed equal odd-prime powers | The general fixed-gap exponent cap was enormous; [gap valuations](valuation-gap-bound.md) now give `W | G_p(D)` for `m^p−n^p=k^W`, `D=m−n>1`, hence `W≤1+log₂D` and no `W≥3` when `D` is squarefree. | `D` can move without bound; no upper `log C` versus `log rad` follows for an F2 branch, and no F1/F0 uniformity is gained. |
| V11-M, **PROVED** for positive `(2,3,p)` | The zero-trace graph excluded 42 specified divisibility pairs for `p≥103`; the [nonzero-trace lemma](nonzero-trace-sieve.md) additionally rules out `7|b, a≡±2 (mod 7)` for every `p≥11`, plus four residue patterns for `p≥37`. | Its 12.9266% metric concerns ordinary coprime base pairs, not conjecture solutions. A solution may avoid every finite local filter. |
| V11-R, **PROVED** necessary bounds in positive `(3,3,t)` | Earlier root minima were `u≥46,520` clean and `u≥6,890` ramified; the [mod-8/mod-9 gap](mod-eight-cube-gaps.md) raises clean branch minima to `93,041` for odd `U`, `80,578` or `123,080` for the two even-root classes, and raises ramified odd-input minima to `16,158` or `23,364`. | These are **lower** bounds on possible bases and still allow `u→∞`; they do not supply a conflicting upper bound. |

The [prior-result audit](audit-prior-bounds.md) found two corrections: the effective BEG fixed-gap bound must exclude the signed `(2,2,W)` degree-one case, which lies outside Fermat–Catalan hyperbolicity; and one review transcribed a general source factor as `P_S^n` instead of `P_S^(n²)`. Both repository statements are corrected. The specialized `S={∞}` bound, modular roughness, and numerical repeated-prime cutoffs survive.

## Source and failure ledger

| Source / reading status | Finding used or rejected | F2 → F0 impact |
| --- | --- | --- |
| Golfieri Madriaga–Pacetti, arXiv:2412.08804v2; Definition 1.1 and selected theorems read | H4 rank two over `Q(ζ_q)^+Q(ζ_r)^+`; modularity conditions remain. | Fixed rank does not make field-dependent constants uniform. |
| Cazorla García–Villagra Torcomian, arXiv:2503.21568v2; §§5–6 partly read | Local conductor formulas; Proposition 6.10's printed `v_r(Δ)=0` cases appear to overlap. | Do not import a clean numerical wild-conductor claim until its hypotheses or an erratum resolve the overlap. |
| Chen–Koutsianas, arXiv:2507.15149v1; Conjecture 2.3 and discussion read | Large-image constant is `C_K` for fixed totally real `K`; newform spaces grow with fixed exponents. | Even that conjecture cannot be substituted for F1/F0 uniformity. |
| Pacetti–Villagra Torcomian, arXiv:2512.17845v1; Theorems A–C and §5 read | `(5,p,3)` has ghost-solution specializations; full theorem C assumes a large-image conjecture and `3∤c`. | Conductor control alone does not remove all comparison forms even in this F2 case. |
| Pastén, arXiv:2312.03566v1; intro and Theorem 1.4 read | Restates Stewart–Yu and proves a newer bound with extra factors. | Gives a credible lower-scale baseline, not objective U. |
| Stewart–Yu 2001; Crossref metadata only, original article inaccessible | Exact bound was read through Pastén's later paper. | Preserve this source limitation in the F0 implication. |

The [full source watch](f2-f0-literature-watch.md) also records newly discovered 2026 motives, classical triangle-group provenance, version checks, discarded applications, and the end-of-cycle literature search. No source checked in this cycle proves full Fermat–Catalan.

## Next falsifiable step

For one coefficient-one `(q,r,p)` hypergeometric/Frey construction, derive an **actual** upper `L≤α(q,r,p)T+β(q,r,p)` with every dependence on field degree, discriminant, conductor, residual image, and newform elimination stated. First test the F2 gate: with `q,r` fixed and `p→∞`, can one prove `α<qr/(q+r)` and `β=o(p)`? Then let `q` or `r` grow and test the F1 gate, and finally both for F0. If an essential theorem is conditional, a constant is unbounded or unknown, or a comparison form remains a ghost, record the precise failed gate. A construction that only gives local conductor exponents or fixed-signature modularity has not yet crossed the bridge.

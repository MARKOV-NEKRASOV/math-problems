# Audit of previously pushed Fermat–Catalan bounds

**Scope:** GitHub `main` at `83225fe` in `/workspace/math-problems`. I checked the primary Freitas–Naskręcki–Stoll PDF (arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4), Bennett–Bruni–Freitas PDF (arXiv:1702.07827v1, Theorem 1.1), and Bérczes–Evertse–Győry v1 TeX/PDF (arXiv:1301.7168v1, Theorems 2.1–2.3). I independently checked several algebraic/numeric deductions. No full Fermat–Catalan proof was found.

**Resolution:** The two wording/source-transcription corrections identified below have been applied to [effective-fixed-gap-bounds.md](effective-fixed-gap-bounds.md) and [review-quantitative-bounds.md](review-quantitative-bounds.md). The quoted earlier wording is retained here to explain the audit finding.

## 1. Correct the scope of the effective fixed-gap exponent cap (substantive)

`research/effective-fixed-gap-bounds.md` first allows any `P,Q≥2`, sign `ε∈{±1}`, nonzero `D`, and later says “every `W≥3` satisfies” its equation (6). That is false for the signed equal-square case `P=Q=2`, `ε=−1`: the polynomial `T²−(T−D)²` has degree **one**, whereas Bérczes–Evertse–Győry Theorem 2.3 requires degree `n≥2`. For `D=1`, every `W≥3` gives the integer solution

`m=(3^W+1)/2`, `n=(3^W−1)/2`, `m²−n²=3^W`.

This family is **outside** the hyperbolic Fermat–Catalan range because `1/2+1/2+1/W>1`; it does not refute the intended conjecture-restricted result. Make the quantifier explicit: equation (6) applies when `n_0≥2` and `W≥3`, in particular for the stated hyperbolic slice. It must not be presented as a theorem for all signed fixed-gap equations.

The sibling `research/signed-fixed-gap-finiteness.md` correctly requires hyperbolicity and explicitly excludes `(2,2)`, so no correction to its theorem is needed.

## 2. Correct one transcription of the general BEG source theorem (source fidelity)

`research/review-quantitative-bounds.md:15` transcribes Bérczes–Evertse–Győry Theorem 2.3 as having `P_S^n`. The original TeX for arXiv:1301.7168v1, equation (2.7), line 447 of the downloaded source `hypersuperell2.tex`, is

`m \leq (10n^2s)^{40ns}|D_K|^{6n}P_S^{n^2}e^{11nd\widehat{h}}`.

Thus the exponent of `P_S` is `n²`. This is the **only** occurrence I found in repository text that incorrectly states the general formula. The project specializes to `K=Q`, `S={∞}`, where `P_S=1`; equation (6) of `research/effective-fixed-gap-bounds.md`, its inversion, and the numerical example remain correct. The source's Theorems 2.1/2.2 height exponents `14m³n³s`, `212n⁴s`, `8m²n³`, and `50n⁴` agree with the repository's `Q,S={∞}` specializations.

## 3. Audited bounds that survive the check

- **FNS output-prime roughness.** arXiv:1703.05058v3 Lemma 2.3 gives one of the seven fixed comparison curves after a small twist when `E[p]` is irreducible; Proposition 2.4 proves irreducibility for nontrivial primitive solutions at prime `p≥11`. At `q≥5`, `q≠p`, dividing the output base `c`, the Tate representation argument yields `a_q(F_i)≡±(q+1) (mod p)`. Hasse and primality of `p` then give `p≤(√q+1)²` and `q≥(√p−1)²`; the `q=p` case satisfies the last inequality directly. The claim `5∤c` for `p≥11` follows. The source hypotheses and direction of the inequalities are correct.
- **Modular selector count.** The seven displayed FNS models agree with the models in `research/selector_metrics.py`. Running the script reproduces the `Q=101,P=103` result of 42 missing compatibility edges and `6.706230839...%` density **among coprime integer base pairs**. The note correctly avoids interpreting this as a density of solutions. The threshold conditions `q<P` and `P²>4q` handle the `q=p` and Hasse issues.
- **Repeated-cube cutoff.** Bennett–Bruni–Freitas arXiv:1702.07827v1 Theorem 1.1 explicitly excludes coprime nonzero integer solutions of `A³+B³=C^n` for `3≤n≤10⁹`. The repository's clean and ramified mod-`p` gap algebra checks: `H−v≥p` and `H−v≥p−1`, respectively, under positivity and `gcd(t,p−1)=1`. Substitution gives `u≥46,520` clean and `u≥6,890` ramified for a hypothetical positive `(3,3,t)` solution with prime `t>10⁹`. These are necessary lower bounds only.
- **Signed fixed-gap proof.** The multiple-root computation for `T^P±(T−D)^Q` with integer `D≠0` is sound. Its genus edge `P=Q=3, ε=−1` has degree 2 but hyperbolicity forces `W≥4`, where genus is at least 1. BEG Theorem 2.3 specializes to `W≤(10n²)^{40n}H^{11n}` for `n≥2`, `z≥2`, and the polynomial coefficient bound `H≤1+(1+|D|)^{min(P,Q)}` is valid by choosing the better of the two translations. For `(2,3),D=1`, the optimized polynomial `T³+T²+2T+1` has `H=2`, and `90^120·2^33` indeed has 245 digits.

## Audit boundary

I verified theorem statements and the named deductions, not every proof line of the external papers or every historical fixed-signature classification in the repository. The corrections above narrow wording/source transcription; no checked numerical bound or Fermat–Catalan subfamily exclusion has to be retracted.

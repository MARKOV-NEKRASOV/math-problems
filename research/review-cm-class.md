# Review: the coprime-to-10 class of `a^n+b^n=c^5`

**Verdict:** The elementary lemma is correct, and the central Chen–Koutsianas claims match [arXiv:2210.02316v2](https://arxiv.org/abs/2210.02316). The note remains a partial analysis, not a proof of this family or Fermat–Catalan.

## Source checks

- Theorem 1.1, p. 2, excludes nontrivial primitive integer solutions for all `n≥3` in exactly two cases: `2∤ab, 5|ab` and `2|ab, 5∤ab`. The introduction, pp. 2–3, explicitly names the two remaining obstructions: irreducibility when `10|ab`, and elimination of a CM form when `2∤ab, 5∤ab`.
- Theorem 8.7, p. 26, assumes `5∤ab` and either `2|a, b≡−1 (mod 4)` or `2|c, a≡−1 (mod 4)`. It proves irreducibility of the residual `J5^−` representation for `p>5`. For the note's positive, odd `a,b` case, `2|c`; swapping `a,b` after proving `4|a+b` supplies the required `a≡−1 (mod 4)`. Thus this application is valid for prime `p≥11`.
- Section 10, p. 29, says that in the `2∤ab, 5∤ab` case, the trace elimination leaves **one** form at level `q₂²q₅²` and **three** at `q₂²q₅³` for prime `p∉{2,3,5,19}`. It names the comparison Jacobians `J^−(−8,8,0)` with a quadratic twist and `J^−(−1,1,0)`, `J^−(−4,4,0)`, `J^−(−16,16,0)`. This does not say those forms yield a nontrivial solution. `p=19` is a gap in that elimination statement, not an exhibited solution.
- Remark 5.7, p. 9, says `J5^±(1,−1,0)` has CM by `Q(ζ₅)`. Theorem 1.2 and the introduction explicitly state the residual representation of a hypothetical solution is reducible or a quadratic twist of the CM `c=0` family's representation for sufficiently large prime `p`; Corollary 1.3 needs Darmon's Conjecture 4.1 to conclude asymptotic exclusion. These are represented correctly in the note.

**Attribution refinement:** Remark 9.1 discusses why ordinary trace comparison does not eliminate *additional CM forms in higher-level spaces encountered without twisting* during Theorem 1.1. It is compatible with the note's warning, but Section 10 and Theorem 1.2 are the direct sources for the four surviving forms in this class. Avoid implying Remark 9.1 itself proves the fate of those four forms.

## Elementary check

If `a,b` are odd and `c` even, an even `n` gives `a^n+b^n≡2 (mod 4)` while `c^5≡0 (mod 4)`, so `n` is odd. For odd `n`, the odd-exponent LTE identity gives `v₂(a^n+b^n)=v₂(a+b)`; equality with `c^5` yields `v₂(a+b)=5v₂(c)≥5`. Thus `32|a+b`, and `a,b` have opposite residues `1` and `−1` modulo 4. Swapping them meets Theorem 8.7's `a≡−1 (mod 4)` hypothesis. This necessary condition holds for all odd `n≥3`, but the paper's residual representation step is stated for prime input exponent `p`.

The note's separate summary of Azon's later work was not checked in this review. It should remain a literature lead unless independently source-reviewed.

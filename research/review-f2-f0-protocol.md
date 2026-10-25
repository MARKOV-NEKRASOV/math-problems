# Independent adversarial review: F2→F0 protocol, cycle 1

**Date:** 25 October 2026. **Status:** Theorem G and the stated F2/F1/F0 *sufficiency implications* check out under their exact hypotheses. None is a proof of Fermat–Catalan. The F0 contradiction additionally depends on a Stewart–Yu estimate whose exact display has so far been available in this project through a secondary overview; the primary article has not been rechecked in this review.

## D1 — three-point Galois-cover barrier (PROVED as an elementary implication)

For a connected nontrivial Galois cover `X→P¹_C` with exactly three branch points and pairwise-coprime inertia orders `e1,e2,e3>1`, the branch-cycle elements `g1,g2,g3` generate `G`, have `g1g2g3=1`, and have exact orders `ei`. In `G_ab`, the image of `g1` has order dividing both `e1` and `lcm(e2,e3)`; coprimality kills it, and similarly for the others. Hence `G_ab=1`. Lagrange and pairwise coprimality give `e1e2e3 | |G|`. Riemann–Hurwitz gives `2g−2=|G|(1−σ)`, so the displayed lower genus bound follows. A nontrivial finite perfect group cannot be solvable. No missing sign or factor of two was found.

**Adversarial example:** The Klein quartic's `PSL₂(F₇)` action has branch signature `(2,3,7)`, `|G|=168`, `σ=41/42`, giving `g=1+168(1−41/42)/2=3`, as expected. This checks normalization but does not establish originality. The theorem excludes **bounded-genus connected Galois three-point covers with exactly those inertia orders** in F0 with three distinct prime exponents. It says nothing about non-Galois quotients, fixed-rank motives/representations, covers with additional branch points, or a construction whose inertia indices differ from the exponents. A proposed Diophantine construction must first show that its geometry falls under these assumptions before citing the barrier.

**Previous bound → reviewed bound → distance:** There was no explicit geometric degree lower bound in the previous ledger; this gives `|G|≥e1e2e3` and `g≥1+e1e2e3(1−σ)/2`. It is a design obstruction, not the missing upper bound on `C` or `h(j)`, so its distance to the F0 finiteness threshold is not numerical.

## D2 — F0 inequality U (CONDITIONAL sufficient criterion)

Write `L=log C`, `T=L/m`, `R=rad(xyz)`. The perfect-power inequality `R≤C^(3/m)` and the **proposed, unproved** inequality `L≤(1−δ)m log R/3+E(m)` give `δ L≤E(m)`. If `E(m)=o(m log m)` this is `L=o(m log m)`.

The project's reported Stewart–Yu estimate is `L≤K R^(1/3)(log R)^3` for primitive `A+B=C`. Substituting `R≤exp(3T)` yields `mT≤27K e^T T³`, hence `m≤27K e^T T²`. For `m→∞`, if `T≥log m` we are done; otherwise `log m≤T+2loglog m+O(1)`. Thus `L≥m(log m−2loglog m−O(1))`. This contradicts `δL≤E(m)`. The algebra and quantifiers of the sufficiency claim are sound **provided the reported Stewart–Yu estimate has the exact uniform absolute-constant form used**. The estimate has been corroborated through a secondary abc overview in prior repository notes, not by the original paywalled paper in this review. Record the lower bound as source-dependent until a primary theorem statement is checked.

A stronger observation is that U itself would imply `L=o(m log m)` and the Stewart–Yu lower bound supplies the contradiction; no step of this reasoning proves U. The constants `δ` and the error function must be absolute across all F0 signatures and bases. If `E` depends on the individual signature or grows like `m log m`, the argument fails.

## D3 — F2 and F1 closure thresholds (PROVED sufficient, not obtained)

For fixed two exponent values `a,b`, let `s0=1/a+1/b`; along the variable exponent `t→∞`, `σ=s0+1/t`. If `C≤K_{a,b}R^κ` with `κ<1/s0=ab/(a+b)` and K independent of bases and `t`, then `C≤K C^(κσ)`; eventually `κσ<1`, so C is bounded. Finitely many powered-value triples follow. A different `K_{a,b}` for each fixed pair is allowed for its F2 branch but cannot be unioned over growing `a,b` to close F1/F0.

For one fixed exponent `a`, with the other two tending to infinity, `σ=1/a+o(1)`. A uniform `C≤K_aR^κ` with `κ<a` similarly bounds C along that F1 branch. Here K must be uniform in the other two exponents and all bases. Neither inequality is currently proved. In F0, the U criterion uses absolute `δ` and error, a qualitatively stronger uniformity demand.

## D4 — seven-branch matrix and dependency graph

Choose one eligible exponent representation for each **distinct powered-value triple**, after the separately reviewed reduction to all-prime signatures and unit-base treatment. Fixed-signature Darmon–Granville finiteness implies that an infinite sequence can be refined so every coordinate exponent is either constant or diverges, with at least one diverging. The seven nonempty subsets of `{p,q,r}` give exactly F2-PQ, F2-PR, F2-QR, F1-P, F1-Q, F1-R, F0. All seven uniform obligations remain open. The matrix is exhaustive as a subsequence classification, not a claim that a unique signature belongs intrinsically to each powered-value triple.

| Branch | Current relevant result | Still missing |
| --- | --- | --- |
| F2-PQ / F2-PR / F2-QR | Signed fixed-gap and fixed-support finiteness for each fixed parameter set; BEG effective bounds depend on both fixed exponents and gap. | Uniform control as gap/support move, or a branch-specific power upper bound with `κ<ab/(a+b)`. |
| F1-P / F1-Q / F1-R | Radical exponent at most `1/a+o(1)` for fixed `a`; F2 constants are not uniform in the other exponent. | Upper `C≤K_a R^κ`, `κ<a`, or an alternative uniform closure. |
| F0 | `R≤C^(3/m)`, Theorem G's scoped geometric design barrier; proposed U is sufficient. | Proof of U or another absolute uniform upper bound; no fixed-signature or finite sieve can supply it alone. |

Dependency edges: primary fixed-signature theorem + prime-signature reduction → seven profiles; perfect-power radical inequality + any proposed upper inequality → a profile-specific C bound; Theorem G → rejection only of a matching Galois-cover design; Stewart–Yu (source statement to be primary-audited) + U → F0 contradiction. No edge from a finite modular selector table or a fixed-gap theorem with constants depending on the gap to F0.

## Literature check and next falsifiable target

At cycle start I queried arXiv for “triangle group” with “abelianization” and for “three point” with “perfect group” (25 October 2026); this did not initially identify a source for the perfectness statement. The literature role subsequently found Conder–Young, arXiv:2410.06571v1, which explicitly records that pairwise-coprime triangle groups are perfect. No originality claim is made for that ingredient. I rechecked the repository's Stewart–Yu citation trail: DOI 10.1215/S0012-7094-01-10815-6 is given for *On the abc conjecture, II* (2001), while the precise `log C≤K R^(1/3)(log R)^3` display was later corroborated in Pastén, arXiv:2312.03566v1, introduction. The original 2001 proof remains unread. The geometric team's next falsifiable target is a concrete F2 construction with listed field degree, conductor and motive rank as the other two exponents grow; if any of these parameters grows in a way that destroys the proposed uniform upper bound, that route does not bridge to F0.

No Lean formalization is warranted.

## Tactical v11 lemma check against the new strategic target

I also independently read the [gap valuation](valuation-gap-bound.md), [nonzero-trace](nonzero-trace-sieve.md), and [cube-congruence](mod-eight-cube-gaps.md) notes, and ran the modular character-sum script. Their scoped calculations withstand these checks: the signed equal-odd-exponent gap valuations force `W|G_p(D)` and exclude squarefree `D>1`; the `q=7` nonzero-trace obstruction forbids `7|b, a≡±2 (mod 7)` for `(2,3,p), p≥11`; and the clean/ramified cube mod-8/mod-9 gap minima follow from their congruence classes. These are tactical F2 or fixed-signature restrictions. None supplies constants uniform as two more exponents vary, so none bridges to F1/F0 under the new protocol. Their detailed independent source review is limited to the theorem statements already checked in the project, not full proofs of the external articles.

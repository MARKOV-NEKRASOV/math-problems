# Attempt to close the pairwise-distinct-prime Fermat–Catalan signatures

**Outcome: incomplete.** I tried a height contradiction, modular level lowering with multiple moduli, and permutation of the universal Frey curve. None supplies an unconditional uniform bound for all distinct prime exponents. The exact obstacle remains a moving set of exponents and supporting primes.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B` be primitive positive powered values with pairwise-distinct prime exponents `p,q,r` and reciprocal sum below 1. Count distinct `(A,B,C)`. The source-checked earlier reduction shows that such signatures are among the only unresolved infinite exponent classes; fixed signatures have finitely many primitive solutions by Darmon–Granville.

## Quantified escape and attempted radical contradiction

In any hypothetical infinite distinct family, the largest exponent `M→∞`, since the finitely many ordered prime signatures with `M≤H` each have finitely many solutions. Order the exponents as `s<t<M`; after a subsequence, the possibilities are: `s,t` both fixed, only `s` fixed, or all three grow. Thus `σ=1/s+1/t+1/M` tends respectively to `1/s+1/t`, `1/s`, or 0. The universal bound is `R=rad(ABC)≤xyz<C^σ`. For the case with two fixed smaller primes, the largest possible pair sums and resulting *hypothetical* power-abc thresholds are:

| Smaller distinct primes | `limsup σ` | A uniform bound `C≤K R^κ` would close this branch if |
| --- | ---: | ---: |
| `(2,3)` | `5/6` | `κ<6/5` |
| `(2,≥5)` | `7/10` | `κ<10/7` |
| `(3,≥5)` | `8/15` | `κ<15/8` |
| `(≥5,≥7)` | `12/35` | `κ<35/12` |

These are upper bounds for `σ`, not exclusions. If only `s` stays fixed, the limiting bound improves to `1/s`; if all three grow, `σ→0`. Nevertheless, the general unconditional Stewart–Yu estimate reported in the project only forces a polylogarithmic lower bound on `R` in `C`. It remains compatible with `R<C^σ`, including when `σ→0` slowly. No unconditional fixed-power upper `C≤K R^κ` in the ranges above was verified. A proposed contradiction at this point would insert an abc-strength theorem.

## Why simply running three Frey curves is not a multi-Frey proof

Attach `E(A,B):Y²=X(X−A)(X+B)` to `A+B=C`. At odd primes dividing `ABC`, its discriminant valuation is `2p v_t(x)`, `2q v_t(y)`, or `2r v_t(z)` according to the coordinate. Modulo one chosen exponent prime, level lowering deletes the moving primes of that powered coordinate when the local hypotheses hold; it does not delete primes of the other two powered coordinates merely because their *different* exponents are prime. Running the same object modulo `p`, `q`, and `r` produces three residual representations with generally unbounded complementary levels. Existing multi-Frey theorems in Chen–Koutsianas, *Darmon's Program: a survey*, arXiv:2507.15149v1 §§10–11, patch explicitly constructed Frey objects for fixed-shape signatures and specified residue classes. They do not state a uniform theorem for all distinct varying `p,q,r`.

A more elementary version of the proposed multi-Frey trick also collapses: permuting the three signed terms gives no new `j`-invariant. Write `S=A²+AB+B²`. The signed representations `(A,B)`, `(A,−C)`, `(B,−C)` all have the same `j=256S³/(A²B²C²)`, because `A²−AC+C²=B²−BC+C²=S` when `C=A+B`. Since for eligible positive triples `j>1728`, curves obtained by these sign/permutation choices are rational quadratic twists of one another (some are already isomorphic after translating `X`). Hence simply relabeling the three terms does not create independent Frey arithmetic or repair the moving-level problem. This does not exclude genuinely different higher-dimensional Frey objects.

## Why an all-odd shortcut is unavailable

If `p,q,r≥3`, a claim that there are *no* primitive nonunit solutions is a case of the open Beal conjecture, which is stronger than the finiteness statement sought here. It cannot be used as a lemma. In the `(2,p,q)` branch, the even exponent may occur on either side of the equation; rewriting a signed equation changes which known family theorem applies. The 2026 paper on `Ax²+By^r=Cz^p` in the project's literature ledger assumes `r≥5` and has coefficient/divisibility conditions in its Diophantine applications, so it cannot be applied wholesale to coefficient-one pairwise-distinct signatures. Fixed-signature classifications and the unreviewed `(3,5,7)` preprint concern individual points in this infinite grid.

**Exact missing step:** an unconditional mechanism that simultaneously controls exponent primes and prime support in every pairwise-distinct signature, or a uniform rational-point theorem across the corresponding covers. The discriminant, radical, and `j` calculations are correct necessary conditions; none bounds the union. No complete proof, and therefore no Lean formalization, emerged.

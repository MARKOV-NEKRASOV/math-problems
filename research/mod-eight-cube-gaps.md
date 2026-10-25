# Mod-8 and mod-9 gaps for the simultaneous cube factors

**Outcome: improved necessary bounds for positive `(3,3,t)`, not a proof.** The previous clean and ramified estimates use only congruences modulo 3. The identity `V=U²−3ab`, where `U=a+b` and `V=(a³+b³)/U`, gives additional restrictions modulo 8. For surviving prime `t`, a modulo-9 refinement also applies. These tighten the smallest possible root `u` of `U`, but still allow `u` to grow.

Assume `a,b>0`, `gcd(a,b)=1`, `a³+b³=c^t`, with prime `t≥5`. Bennett–Bruni–Freitas, arXiv:1702.07827v1, Theorem 1.1 (previously source-checked in [prime-repeated-attempt.md](prime-repeated-attempt.md)) excludes `t≤10⁹` and `t≡2 (mod 3)`. Any hypothetical survivor therefore has `t>10⁹` and `t≡1 (mod 6)`. The inequalities below apply to the indicated branches of such a survivor; no existence is asserted.

## Clean branch `3∤U`

The factorization gives `U=u^t`, `V=v^t` with positive integers `u,v`. Put `H=u²` and `δ=H−v>0`. The previous proof gives `δ≡0 (mod 3)` and

`t ≤ 2 log 2 / [−log(1−δ/H)] < (2 log 2/δ)u²`.             (1)

If `U` is even, coprimality makes `a,b` odd, `u` even, and `8|U` because `t≥5`. Then `b≡−a (mod 8)`, so `ab≡−a²≡7 (mod 8)` and `V=U²−3ab≡3 (mod 8)`. Every odd unit modulo 8 has square 1, hence `v^t≡v (mod 8)` for odd `t`, and `v≡3 (mod 8)`. Therefore:

| `u` class | `H=u² (mod 8)` | `δ=H−v (mod 8)` | with `3|δ`, necessarily |
| --- | ---: | ---: | ---: |
| `u≡2 (mod 4)` | 4 | 1 | `δ≥9` |
| `u≡0 (mod 4)` | 0 | 5 | `δ≥21` |

If `U` is odd, exactly one of `a,b` is even and `u,H,V,v` are odd. Then `δ` is even, so `3|δ` already yields `δ≥6`. The surviving residue `t≡1 (mod 6)` gives more: the unit groups modulo 9 have exponent 6, hence `u^t≡u` and `v^t≡v (mod 9)`. From `V=U²−3ab` we obtain

`δ=u²−v≡3ab (mod 9)`.                                  (2)

If exactly one of `a,b` is divisible by 3, then `δ≡0 (mod 9)` and evenness gives `δ≥18`. If neither is divisible by 3, `3∤U` forces them to have the same nonzero residue modulo 3, so `ab≡1 (mod 3)`, `δ≡3 (mod 9)`, and evenness gives `δ≥12`. Thus **uniformly for odd `U`, `δ≥12`**.

Substituting into (1), any survivor with `t>10⁹` satisfies these necessary root bounds:

| Branch | Minimal `δ` used | Necessary root `u` |
| --- | ---: | ---: |
| `U` odd | 12 | `u≥93,041` (odd, `3∤u`) |
| `u≡2 (mod 4)` | 9 | `u≥80,578` (`3∤u`) |
| `u≡0 (mod 4)` | 21 | `u≥123,080` (`3∤u`) |

For example, the first row follows from `u²>10⁹·12/(2 log 2)` and the first odd integer above that threshold that is prime to 3. The bounds use the strict upper estimate in (1), so they are conservative necessary conditions.

Equation (2) also sharpens individual even-`U` subcases: if `u≡2 (mod 4)` and `3∤ab`, then `δ≡1 (mod 8)` and `δ≡3 (mod 9)`, giving `δ≥57` and `u≥202,774`; if `u≡0 (mod 4)` and `3|ab`, then `δ≡5 (mod 8)` and `δ≡0 (mod 9)`, giving `δ≥45` and `u≥180,172`. These do not improve the unconditional rows because the complementary residue cases remain.

## Ramified branch `3|U`

Here `U=3^(t−1)u^t`, `V=3v^t`, `3∤v`. Put `H=9u²`, `δ=H−v>0`. The previous congruence gives `δ≡−1≡2 (mod 3)` and the positive-left size inequality yields

`t ≤ log 108 / [−log(1−δ/H)] < (9 log 108/δ)u²`.        (3)

If `U` is even, `a,b` are odd, `u` is even, and `8|U`. As above, `V≡3 (mod 8)`. Since `V=3v^t` and `t` is odd, `v≡1 (mod 8)`. Thus:

| `u` class | `H=9u² (mod 8)` | `δ (mod 8)` | with `δ≡2 (mod 3)`, necessarily | Necessary `u` if `t>10⁹` |
| --- | ---: | ---: | ---: | ---: |
| `u≡2 (mod 4)` | 4 | 3 | `δ≥11` | `u≥16,158` |
| `u≡0 (mod 4)` | 0 | 7 | `δ≥23` | `u≥23,364` |

If `U` is odd, then `u,H,V,v` are odd and `δ` is even. This is compatible with the prior `δ≥2`; it yields only `u≥6,891` after imposing oddness on the previous root bound. Therefore the new ramified improvement applies to odd `a,b`.

All numerical thresholds were computed from (1) or (3), then rounded upward to the stated parity and `3∤u` restrictions where applicable. They can be verified with rational upper bounds for `log 2` and `log 108` together with integer arithmetic; decimal approximations are not the proof.

## Limit and next subproblem

These congruences shrink the feasible `u` range for every surviving prime `t`, and the even-input subcases give further residue-dependent improvements. They do not bound `u` above. A next lemma would have to combine `δ` with the exact square condition `4V−U²=3(a−b)²`, or exclude the remaining `3|ab` clean subcase that permits `δ=9`. Such a result must hold uniformly in unbounded `u,t` to close this family. No Lean formalization was attempted.

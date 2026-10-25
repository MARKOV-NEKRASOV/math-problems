# Nonzero-trace obstruction at input primes in `(2,3,p)`

**Outcome: proved exclusions of additional infinite base-residue families, not a proof of Fermat–Catalan.** The previous GitHub selector graph used only primes where the Frey curve's local trace is zero. Using its *nonzero* trace gives a direct contradiction for several small-prime residue classes. The theorem applies to positive primitive `a²+b³=c^p` with prime `p≥11`.

## A general local lemma

Let `E:y²=x³+3bx−2a`, and let `F_i` be the one globally selected member of the seven fixed Freitas–Naskręcki–Stoll (FNS) comparison curves for a nontrivial primitive solution, after one of their small quadratic twists. FNS arXiv:1703.05058v3, Proposition 2.4 and Lemma 2.3, give `E^(d)[p]≅F_i[p]` for prime `p≥11`. If a prime `q≥5`, `q≠p`, divides `a` or `b`, primitivity gives `q∤c`, so both curves have good reduction at `q` and the small twist is unramified. Thus

`a_q(F_i)≡χ_d(q) a_q(E) (mod p)`, where `χ_d(q)∈{±1}`.

If `p>4√q`, Hasse's bound gives `|a_q(F_i)−χ_d(q)a_q(E)|≤4√q<p`. The congruence becomes an exact equality. In particular, `|a_q(E)|` must belong to the finite set `{|a_q(F_i)|:i=1,…,7}`. This is the reusable nonzero-trace exclusion lemma. It is stronger than the prior zero-trace selector for residue classes where `a_q(E)≠0`.

## The first new exclusions

At `q=7`, the seven comparison traces are `−1,−1,−4,0,−3,−3,1`; their absolute values are `{0,1,3,4}`. If `7|b`, reduction gives `E:y²=x³−2a`. A direct character sum shows `|a_7(E)|=5` when `a≡2 or 5 (mod 7)`. Since `p≥11>4√7` and `q≠p`, **no positive primitive solution with `7|b` and `a≡±2 (mod 7)` exists for any prime `p≥11`**.

For an elementary check of that first row, the cubes modulo 7 are `0` once, `1` three times, and `−1` three times. For `a≡2`, the values of `x³−2a` are `3,4,2` with those multiplicities, whose quadratic characters sum to `−1+3+3=5`; hence `a_7(E)=−5`. For `a≡−2`, the character sum is `−5` and the trace is `5`.

At `q=13`, the fixed trace absolute set is `{0,1,2,3,4,5,6}`. If `13|b` and `a≡±2 or ±3 (mod 13)`, the Frey trace has absolute value `7`. Therefore that whole residue family is excluded for every prime `p≥17`, when `q≠p` and `p>4√13`.

The same exact calculation yields more exclusions for all primes `p≥37`:

| Divisibility condition | Forbidden residue of the other base | Count among nonzero residues |
| --- | --- | ---: |
| `7|b` | `a mod 7 ∈ {2,5}` | 2 of 6 |
| `13|b` | `a mod 13 ∈ {2,3,10,11}` | 4 of 12 |
| `19|b` | `a mod 19 ∈ {2,3,4,5,6,9,10,13,14,15,16,17}` | 12 of 18 |
| `29|a` | `b mod 29 ∈ {2,3,8,10,11,12,14,15,17,18,19,21,26,27}` | 14 of 28 |
| `31|b` | `a mod 31 ∈ {3,5,6,7,9,10,11,12,13,14,17,18,19,20,21,22,24,25,26,28}` | 20 of 30 |

Every row follows because its Frey absolute trace is absent from the seven comparison absolute traces. For `p≥37`, every listed `q<p` and `p>4√q`, so all rows hold simultaneously. The accompanying [character-sum script](nonzero_trace_check.py) independently computes traces for the seven FNS models and the Frey reductions; it asserts each residue count. The earlier repository script counts points directly, so the two calculations use different finite-field formulas.

As a *priority metric only*, among ordinary coprime positive base pairs `(a,b)`, the natural density excluded by the union of these five local conditions is exactly `11257969/87091200≈12.9266%`. At each prime `q`, a row with `k` forbidden nonzero residues has conditional coprime-pair density `k/(q²−1)`; independence across distinct primes gives the product formula. This is **not** a density of solutions to `a²+b³=c^p`, and it does not imply that the remaining solutions sample residue classes uniformly.

## Stronger branch selection with nonzero traces

At `q=5`, if `5|a` and `b≡±1 (mod 5)`, then `|a_5(E)|=4`. Among the seven comparison curves, only `288a1` has absolute trace 4 at 5. Thus this residue condition selects the `288a1` branch for every prime `p≥11`. FNS Lemma 6.1(2) excludes nontrivial primitive solutions in that branch when `p≥17` and `p≡1 (mod 4)`. Consequently **no positive primitive solution has `5|a`, `b≡±1 (mod 5)`, and prime `p≥17`, `p≡1 (mod 4)`**. The source's congruence restriction is essential.

## Boundary and next subproblem

These theorems remove infinite residue families and raise a finite base-pair coverage metric. A solution could avoid every listed residue pattern; no upper bound on `p`, `a`, `b`, or `c` follows. A mathematically decisive extension would use the equation to *force* one forbidden residue/branch pattern for all sufficiently large `p`, or develop a sieve whose complement is itself controlled by a uniform arithmetic theorem. Enlarging a finite table alone cannot prove the whole conjecture. No Lean formalization was attempted.

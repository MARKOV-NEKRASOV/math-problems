# A CM branch-selector lemma that excludes input-divisibility families

**Outcome: a rigorous exclusion of infinite families within the positive `(2,3,p)` Fermat–Catalan subproblem, not a proof of the full conjecture.** The generalization has a direct target: use primes dividing the **input** bases to select incompatible members of the seven fixed Frey comparison curves. It yields, for every prime `p≥11`, no primitive positive solution of `a²+b³=c^p` with `7|a` and `5|b`. It also eliminates `5|b` for `p≥17, p≡1 (mod 3)` and `7|a` for `p≥17, p≡1 (mod 4)`.

## Source and exact setup

Let `a,b,c>0`, `gcd(a,b,c)=1`, `a²+b³=c^p`, with prime `p≥11`. FNS, *The generalized Fermat equation with exponents 2, 3, n*, arXiv:1703.05058v3, Proposition 2.4 and Lemma 2.3, establish that the Frey curve `E:y²=x³+3bx−2a` has irreducible `E[p]`, and that a quadratic twist `E^(d)`, `d∈{±1,±2,±3,±6}`, has `E^(d)[p]≅F_i[p]` for a **single globally selected** `F_i` in `{27a1,54a1,96a1,288a1,864a1,864b1,864c1}`. These fixed curves have good reduction at every prime `q≥5`. Their equations are printed immediately after FNS Lemma 2.3. Since `a,b,c>0`, the solution is nontrivial in FNS's sense `abc≠0`.

At a prime `q≥5` dividing either `a` or `b`, primitivity and the equation imply `q∤c`, so `E` and its small twist have good reduction at `q` (the twist parameter is a q-adic unit). For `q≠p`, the residual isomorphism implies `a_q(E^(d))≡a_q(F_i) (mod p)`. An unramified quadratic twist changes the trace only by a sign; if `a_q(E)=0`, then `a_q(F_i)≡0 (mod p)`. Hasse gives `|a_q(F_i)|≤2√q`, so `p>2√q` forces **exact** `a_q(F_i)=0`.

Define the finite branch-selector set `Z(q)={i: a_q(F_i)=0}`. This proves the reusable lemma:

> If `q≥5`, `q≠p`, `p>2√q`, and `q|b` with `q≡2 (mod 3)`, then the globally selected `F_i` lies in `Z(q)`. The same holds if `q|a` with `q≡3 (mod 4)`.

Indeed, when `q|b`, `E mod q` is `y²=x³−2a`; cubing permutes `F_q` for `q≡2 (mod 3)`, so its trace is zero. When `q|a`, `E mod q` is `y²=x³+3bx`; for `q≡3 (mod 4)`, the substitution `x↦−x` cancels the quadratic-character sum, so its trace is zero. The conditions on `q` are sufficient; the proof does not claim every zero trace arises this way.

## Explicit family exclusions

Direct point enumeration from the FNS models gives, in the order listed above,

| `q` | Traces `a_q(F_i)` | Selector set |
| ---: | --- | --- |
| 5 | `(0,3,2,−4,−1,2,−2)` | `{27a1}` |
| 7 | `(−1,−1,−4,0,−3,−3,1)` | `{288a1}` |

The [point-count script](output_prime_sieve_check.py) reproduces the finite-field counts underlying this table; `a_q=q+1−#F_i(F_q)`. Since `p≥11>2√7`, the branch selector applies at both primes. If `5|b`, the single global curve must be `27a1`; if `7|a`, it must be `288a1`. Those are different curves, so **no primitive positive solution with `5|b` and `7|a` exists for any prime `p≥11`**. This removes an infinite set of base-divisibility cases over all prime exponents `p≥11`, not merely a finite search box.

FNS Lemma 6.1(1) rules out nontrivial `27a1`-branch solutions for `p≥17` and `p≡1 (mod 3)`. Thus `5|b` is impossible in this prime-exponent congruence class. FNS Lemma 6.1(2) similarly rules out nontrivial `288a1`-branch solutions for `p≥17` and `p≡1 (mod 4)`, so `7|a` is impossible there. FNS states a separate calculation for `p=13`, but I do not use it; the exclusions above have the safe stated ranges. The simultaneous `5|b,7|a` exclusion uses neither Lemma 6.1 nor a conditional GRH computation.

## Why this generalization is useful and where it stops

The input-prime selector is a small-prime sieve for **whole residual branches**. It combines data at different primes through the one global `F_i`, unlike testing each prime against an independently chosen comparison curve. Further selected primes with disjoint `Z(q)` sets can generate more infinite divisibility-family exclusions, but this requires exact finite-field traces and the good-reduction hypotheses. The conditions `5|b` and `7|a` are not forced by the original equation, so the remaining families can avoid them. The full `(2,3,p)` subproblem and all other prime signatures remain open. No Lean formalization was attempted.

**Source reading:** I read FNS arXiv:1703.05058v3 PDF at §2 (Lemma 2.3, Proposition 2.4, displayed models) and §6 (Lemma 6.1), and ran the repository point-count script. The numerical table is a small exact computation supporting the theorem's finite-field premise; the exclusion itself follows from the published residual comparison plus trace argument.

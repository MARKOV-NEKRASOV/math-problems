# A finite compatibility graph for input-prime divisibility in `(2,3,p)`

**Result: 12 excluded infinite divisibility families, with exact scope.** Let `a,b,c>0`, `gcd(a,b,c)=1`, `a²+b³=c^p`, and let `p≥59` be prime. Define

`B={5,29,41,53}` (candidate primes dividing `b`) and `A={7,19,43}` (candidate primes dividing `a`).

Then **no** solution has both `q_b|b` for any `q_b∈B` and `q_a|a` for any `q_a∈A`. This excludes the `4×3=12` pairwise divisibility patterns over every prime exponent `p≥59`. It does not exclude solutions whose bases avoid one of these sets, nor prove the full Fermat–Catalan conjecture.

## Selector lemma and graph definition

FNS, arXiv:1703.05058v3, Proposition 2.4 and Lemma 2.3, attach to every nontrivial primitive solution with `p≥11` one globally selected comparison curve `F_i` from `27a1,54a1,96a1,288a1,864a1,864b1,864c1` such that an allowed small quadratic twist of `E:y²=x³+3bx−2a` has isomorphic mod-`p` torsion. Each `F_i` has good reduction at every prime `q≥5`. If `q|a` or `q|b`, primitivity implies `q∤c`, so `E` has good reduction at `q` too. For `q≠p`, its trace, up to a quadratic-twist sign, is congruent modulo `p` to `a_q(F_i)`.

For a prime `q≥5`, set `Z(q)={i:a_q(F_i)=0}`. If `q≡2 (mod 3)` and `q|b`, then the reduction `E mod q` is `y²=x³−2a`, whose trace is zero because cubing permutes `F_q`. If `q≡3 (mod 4)` and `q|a`, then `E mod q` is `y²=x³+3bx`; pairing `x` with `−x` cancels the quadratic-character sum, so its trace is zero. Thus `a_q(F_i)≡0 (mod p)`. When `p>2√q`, Hasse's bound upgrades this to the exact `F_i∈Z(q)`.

Construct a bipartite **compatibility graph** with left vertices `B`, right vertices `A`, and an edge `(q_b,q_a)` exactly when `Z(q_b)∩Z(q_a)` is nonempty. If a solution has `q_b|b` and `q_a|a`, with both primes distinct from `p` and `p>2√max(q_b,q_a)`, the one globally selected `F_i` belongs to this intersection. Therefore a missing graph edge is a rigorously excluded divisibility family. The graph encodes the one-curve global coupling; it does not add a new Diophantine theorem beyond the selector lemma.

## Exact finite-field computation

Directly enumerating points on the seven FNS models printed after their Lemma 2.3 gives the following traces, in their listed curve order:

| `q` | `a_q(27a1), a_q(54a1), a_q(96a1), a_q(288a1), a_q(864a1), a_q(864b1), a_q(864c1)` | `Z(q)` |
| ---: | --- | --- |
| 5 | `0,3,2,−4,−1,2,−2` | `{27a1}` |
| 29 | `0,6,2,4,−2,−8,−8` | `{27a1}` |
| 41 | `0,−6,2,8,−10,8,−8` | `{27a1}` |
| 53 | `0,9,10,4,13,4,−4` | `{27a1}` |
| 7 | `−1,−1,−4,0,−3,−3,1` | `{288a1}` |
| 19 | `−7,2,−4,0,−6,3,−5` | `{288a1}` |
| 43 | `8,−10,4,0,−6,12,−4` | `{288a1}` |

The selector sets are disjoint across every left-right pair, so this graph has **zero edges**. Each `q∈B` satisfies `q≡2 (mod 3)`; each `q∈A` satisfies `q≡3 (mod 4)`. For prime `p≥59`, all seven `q` are less than `p`, and `p>2√53`; the selector lemma applies simultaneously. This proves the 12 exclusions.

The counts are reproducible with [output_prime_sieve_check.py](output_prime_sieve_check.py): for each listed `q`, compute `q+1−order(model,q)` for every model. I independently ran this calculation and obtained every trace and singleton selector set shown above. These are finite exact counts, not empirical evidence for an unbounded set of primes. No claim is made that infinitely many additional `q` have singleton `Z(q)`.

**Boundary:** FNS Lemma 6.1 gives additional congruence-class exclusions for the CM branches, but the 12-pair theorem here uses only Lemma 2.3, Proposition 2.4, good-reduction trace comparison, and the finite trace table. It does not use GRH or a purported proof of the full conjecture. Lean formalization remains deferred.

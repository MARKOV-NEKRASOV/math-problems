# Quantitative bounds for the finite CM branch-selector sieve

**Purpose.** Rank concrete `(2,3,p)` subproblems by how many input-divisibility families the seven-curve selector already eliminates. These counts concern finite, exact prime sets and coprime input-base pairs. They do **not** estimate a density of Fermat–Catalan solutions or imply that useful selector primes continue indefinitely.

Assume `a,b,c>0`, `gcd(a,b,c)=1`, `a²+b³=c^p`, with prime `p≥11`. Freitas–Naskręcki–Stoll, arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4, give one globally selected fixed comparison curve `F_i` among seven. As proved in [input-prime-branch-selectors.md](input-prime-branch-selectors.md), for `q≥5`, `q≠p`, `p>2√q`: if `q≡2 (mod 3)` divides `b`, or if `q≡3 (mod 4)` divides `a`, then `F_i` belongs to `Z(q)={i:a_q(F_i)=0}`. Two divisibility conditions with disjoint `Z` sets are incompatible.

## Monotone coverage metrics

For cutoff `Q` and integer exponent threshold `P≥11`, let the eligible primes be `q≤Q` with `q<P` and `P²>4q`. These conditions ensure `q≠p` and `p>2√q` for **every** prime `p≥P`. Let `B(Q,P)` consist of eligible `q≡2 (mod 3)` and `A(Q,P)` of eligible `q≡3 (mod 4)`. Put an edge between `q_b∈B` and `q_a∈A` if `Z(q_b)∩Z(q_a)` is nonempty. Each **missing** edge is a proved exclusion of the family `q_b|b, q_a|a` for all prime `p≥P`. Define `N(Q,P)` as the number of missing edges for distinct primes `q_b,q_a`. This number is monotone nondecreasing in both `Q` and `P`.

For a transparent lower-bound coverage density, choose sublists `B*⊆B`, `A*⊆A` for which **every** cross pair is incompatible. The natural density, *among coprime positive integer base pairs `(a,b)`*, of pairs with at least one `q_b∈B*` dividing `b` and at least one `q_a∈A*` dividing `a` is exactly

`δ(B*,A*)=[1−∏_(q∈B*) q/(q+1)] [1−∏_(q∈A*) q/(q+1)]`,

provided the prime lists are disjoint. At a fixed prime `q`, among residue pairs with `gcd(a,b)` not divisible by `q`, the conditional probability that `q` divides one chosen coordinate is `1/(q+1)`; Chinese remaindering and cancellation of the other coprimality factors give the product. This density is monotone under enlargement of the two lists. It is a prioritization metric only: solutions to `a²+b³=c^p` are exceptionally sparse and need not sample base pairs uniformly.

## Exact selectors up to 101

I enumerated `#F_i(F_q)` from the seven displayed FNS models for every prime `5≤q≤101`; the reproducible script is [selector_metrics.py](selector_metrics.py). The primes with an input-divisor role and their zero-trace selectors are:

| Role | Primes grouped by exact `Z(q)` |
| --- | --- |
| `q|b`, `q≡2 (mod 3)` | `Z={27a1}`: `5,29,41,53,89`; `Z={27a1,54a1}`: `17`; `Z={27a1,864c1}`: `101`; other eligible `11,23,47,59,71,83` also contain `288a1` in `Z` and do not create a cross exclusion with the group below. |
| `q|a`, `q≡3 (mod 4)` | `Z={288a1}`: `7,19,43,67`; `Z={288a1,864b1}`: `31`; `Z={288a1,864a1}`: `79`; other eligible `11,23,47,59,71,83` also contain `27a1` in `Z` and do not create a cross exclusion with the group above. |

Thus the fully incompatible lists at `Q=101,P=103` are

`B*={5,17,29,41,53,89,101}`, `A*={7,19,31,43,67,79}`.

Every one of their `7×6=42` cross pairs has disjoint selector sets. Among these, the 12 pairs from the smaller singleton lists in [input-prime-compatibility-graph.md](input-prime-compatibility-graph.md) remain valid. The new pairs include `17|b,7|a`, `5|b,31|a`, `89|b,67|a`, and `101|b,79|a`.

| Cutoff `Q` | Safe prime-exponent threshold `P` | `B*` count | `A*` count | `N(Q,P)` excluded pairs | `δ(B*,A*)` among coprime base pairs |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 11 | 1 | 1 | 1 | 2.0833% |
| 19 | 23 | 2 | 2 | 4 | 3.5938% |
| 29 | 31 | 3 | 2 | 6 | 4.0365% |
| 53 | 59 | 5 | 4 | 20 | 5.7745% |
| 101 | 103 | 7 | 6 | 42 | 6.7062% |

At `Q=101,P=59`, only primes `q<59` are uniformly eligible; the result stays at **20** excluded pairs and **5.7745%** base-pair density. Raising `P` to `103` admits the additional primes. This demonstrates why the cutoff and exponent threshold must be stated together.

## Exact threshold for an individual pair

For an incompatible pair `(q_b,q_a)` from the table, the smallest prime threshold that makes the selector proof valid for **all** prime exponents at or above it is the next prime strictly greater than `max(q_b,q_a)`. Indeed, that removes the `q=p` case and automatically gives `p>2√q` because `q≥5`. Examples:

| Conditions | First safe prime `p` for all later primes |
| --- | ---: |
| `5|b, 7|a` | 11 |
| `17|b, 7|a` | 19 |
| `5|b, 31|a` | 37 |
| `89|b, 67|a` | 97 |
| `101|b, 79|a` | 103 |

At some smaller primes the selector may already work if `p` differs from both input primes and `p>2√max(q_b,q_a)`. The displayed thresholds are **uniform method thresholds**, not claims that these divisibility patterns have solutions below them.

## Next mathematical subproblem

The finite computation says which two-prime input patterns to remove next, but adding small primes produces diminishing density gains. A more consequential extension would prove that an infinite class of primes `q≡2 (mod 3)` has `Z(q)` disjoint from an infinite class of `q≡3 (mod 4)` selectors, or obtain a comparable branch-selection criterion for primes dividing the **output** base. Neither infinite-class statement follows from these counts; zero-trace behavior of the non-CM comparison curves is not controlled here. No full Fermat–Catalan proof or Lean formalization results.

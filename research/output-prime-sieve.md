# Output-prime subproblem for the `(2,3,p)` branch

**Scope.** Consider positive primitive `a²+b³=c^p` with prime `p≥11`. This note strengthens the all-seven roughness bound into a finite-prime sieve and proves why the sieve alone cannot close the surviving `27a1` branch. It does not prove Fermat–Catalan.

## A common-branch divisor lemma

Let `E_1,…,E_7` be the seven fixed curves of Freitas–Naskręcki–Stoll (FNS), arXiv:1703.05058v3, Lemma 2.3, with conductors `27,54,96,288,864,864,864`. For `q≥5` prime define

`D_i(q)=(q+1)²−a_q(E_i)²=#E_i(F_q)·#E_i^tw(F_q)`.

Here `E_i^tw` means a nonsquare quadratic twist over `F_q`; both factors are strictly positive. The same FNS comparison curve `E_i` is selected **globally** for a hypothetical solution; it is not chosen separately at each output prime.

**Lemma.** For some `i∈{1,…,7}`, every prime `q≥5`, `q≠p`, dividing `c` satisfies `p|D_i(q)`. Consequently, for any nonempty set `T` of such output primes,

`p | gcd_{q∈T} D_i(q)`.

**Proof.** FNS Proposition 2.4 provides irreducibility for a nontrivial primitive solution and `p≥11`, and Lemma 2.3 gives a twist `E^(d)[p]≅E_i[p]`, `d∈{±1,±2,±3,±6}`. At `q≥5|c`, primitivity gives `q∤ab`; the Frey curve has a unit `c₄=−144b`, multiplicative reduction, and `v_q(Δ_min)=p v_q(c)`. The twist is unramified at `q`. For `q≠p`, the residual Tate representation has Frobenius trace `±(q+1)` modulo `p`. Since `E_i` has good reduction at `q`, `a_q(E_i)≡±(q+1) (mod p)`, proving `p|D_i(q)` for the same `i` at every such `q`. Taking their gcd proves the second assertion. The case `q=p` is deliberately omitted from the congruence, though it satisfies the general Hasse roughness bound automatically.

Because `p` divides one of the positive factors in `D_i(q)` and Hasse bounds each by `(√q+1)²`, every `q≥5|c` has `q≥(√p−1)²`. For any **fixed** prime `q₀≥5`, the admissible `p` values are among `q₀` itself and the prime factors ≥11 of the finite product `∏_i D_i(q₀)`. Therefore only finitely many positive primitive powered triples can have `q₀|c`: each permitted `p` is a fixed hyperbolic `(2,3,p)` signature, finite by Darmon–Granville. This allows all *other* prime factors of `c` to vary; it is stronger in that direction than the fixed-whole-support Siegel lemma, though still ineffective as a uniform bound.

## Exact tiny-prime checks

The FNS paper displays Weierstrass models for all seven curves immediately after Lemma 2.3. The reproducible [point-count script](output_prime_sieve_check.py) directly enumerates their `F_q`-points and gives the following possible prime factors ≥11 of `D_i(q)` across the seven curves:

| `q` | Possible `p≥11`, `p≠q`, from `p|D_i(q)` | Consequence |
| ---: | --- | --- |
| 5 | none | `5∤c` for all `p≥11` |
| 7 | 11, via `864a1` or `864b1` | `7∤c` for `p≥13` |
| 11 | none | `11∤c` for `p≥13`; `p=11` is the untested `q=p` case |

The `q=5` row follows already from Hasse, since `(√5+1)²<11`. For `q=7`, the seven `#E_i(F_7)` values in FNS model order are `9,9,12,8,11,11,7`; the corresponding twist orders are `7,7,4,8,5,5,9`. Only `11` among primes ≥11 occurs. For `q=11`, the orders are `12,15,8,12,9,18,14` and their twist orders are `12,9,16,12,15,6,10`, so none contains a prime ≥11. These are finite-field counts, not a global classification. In particular, the known `p=11` classification in FNS Theorem 7.1 is **conditional on GRH** and is not invoked here.

## Why the local route does not close

Fix any prime `p≥17` with `p≡2 (mod 3)`, the surviving non-split `27a1` class. There are infinitely many primes `q` satisfying simultaneously

`q≡−1 (mod 6p)` and `q≡1 (mod 4)`:

the conditions form one reduced residue class modulo `12p`, so Dirichlet's theorem applies. For each such `q`, we have `q≡2 (mod 3)`, hence `a_q(27a1)=0` by the bijectivity of cubing on `F_q`; also `p|q+1`. Therefore the `27a1` output-prime trace condition `p|D_27a1(q)` is satisfied for infinitely many `q`, all well beyond the roughness bound.

The original equation also has a primitive `q`-adic local solution with `b=1,c=q`: because `q≡1 (mod 4)`, `−1` has a simple square root modulo `q`. Hensel lifts it to `a∈Z_q^×` satisfying `a²=q^p−1`, so `a²+1=q^p`. This proves compatibility of the **individual output-prime trace test** and the **Diophantine equation at `q`** for infinitely many candidate output primes. It does **not** construct positive integer `a` or a global mod-`p` identification with `27a1[p]`. Thus a contradiction cannot follow solely from the roughness and trace divisibility conditions; a global modular-curve or height argument is still required.

No complete proof or Lean formalization resulted.

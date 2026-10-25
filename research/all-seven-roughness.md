# A stronger local-output obstruction in the `(2,3,p)` family

**Outcome: a reviewed necessary condition, not a full proof.** For positive primitive `a²+b³=c^p`, prime `p≥11`, the seven-curve reduction of Freitas–Naskręcki–Stoll forces every prime `q≥5` dividing `c` to satisfy

`q ≥ (√p−1)² = p−2√p+1`.                                      (1)

This strengthens the prior `q≥√p−1` bound and applies to *all seven* modular branches. It rules out `5|c` for every `p≥11`. It does not bound `p` or `c` and so does not prove even this subfamily finite.

## Exact hypotheses and derivation

Let `a,b,c>0`, `gcd(a,b,c)=1`, `a²+b³=c^p`, and `p≥11` prime. Freitas–Naskręcki–Stoll (FNS), arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4, say that a quadratic twist by some `d∈{±1,±2,±3,±6}` of `E:y²=x³+3bx−2a` has mod-`p` Galois representation isomorphic to `E_i[p]` for one of `27a1`, `54a1`, `96a1`, `288a1`, `864a1`, `864b1`, `864c1`. Their conductors are supported on `{2,3}`, so each has good reduction at every `q≥5`.

If `q≥5`, `q≠p`, divides `c`, primitivity gives `q∤ab`. Hence `c₄(E)=−144b` is a `q`-adic unit and the model is minimal multiplicative with `v_q(Δ_min)=p v_q(c)`. The small twist parameter is a `q`-adic unit, so the local character is unramified and the discriminant valuation retains divisibility by `p`. For `q≠p`, the Tate exact sequence `0→μ_p→E[p]→Z/p→0` gives unramified residual Frobenius eigenvalues `1,q`, possibly multiplied by a common unramified quadratic sign. The comparison therefore yields

`a_q(E_i) ≡ ±(q+1) (mod p)`.

Equivalently, `p | (q+1−a_q(E_i))(q+1+a_q(E_i))`. **Because `p` is prime, it divides one of these factors.** Hasse's bound makes each factor positive and at most `(√q+1)²`. Thus `p≤(√q+1)²`, proving (1). The case `q=p` is excluded from the Tate argument, but satisfies (1) trivially. If `q=5`, `(√5+1)²<11`, contradicting `p≥11`; hence `5∤c`. More generally, any fixed `q≥5` is excluded as soon as `p>(√q+1)²`.

The earlier `27a1` special case remains stronger at primes `q≡2 (mod 3)`: there `a_q(27a1)=0`, so `p|q+1` and in fact `6p|q+1` for the surviving `p≥17` branch. The universal (1) requires neither CM nor a congruence class on `p`.

## Attempted global closure and obstruction

Combining (1) with the reviewed fixed-output-support Siegel lemma shows that an infinite positive `(2,3,p)` family must have a moving output prime divisor of scale at least linear in `p`. This is a sharper escape condition, but it is compatible with arbitrarily large `c`. Local trace congruences characterize where a prime may divide `c`; they do not imply that `c` has a bounded number of prime factors or that all candidate primes are absent. Turning seven residual congruences into rational isogenies would require a uniform theorem not established here. The non-split Cartan branch remains open. Other prime signatures remain even if this branch were closed.

## Recent-paper check and a false shortcut

The arXiv Atom API queried on 25 October 2026 for `ti:"generalized Fermat"` lists the September 2026 `(3,5,7)` preprint, the August 2026 number-field paper, and the May 2026 `(2,r,p)` framework but no newer direct `(2,3,p)` theorem than Freitas–Mocanu–Sánchez-Rodríguez, arXiv:2512.10781v1. This targeted query is not an exhaustive literature search. Hashimoto–Lido–Lombardo–Mascot–Parent, arXiv:2608.10919v1, treats non-split Cartan level 13 and does not supply a uniform all-level theorem.

Preda Mihăilescu, arXiv:2509.18275v1, Theorem 1 claims no integer solutions of `(x^P+y^P)/(x+y)=P^e z^Q` for distinct odd primes `P>3,Q` and `e∈{0,1}` with nonzero coprime integer `x,y,z`. As **literally stated**, this is contradicted by `x=y=z=1`, `e=0`, for every such pair; the paper's introduction gives no nonunit restriction in its displayed equation. The proof's final parity contradiction also fails on this explicit unit instance. A corrected nontrivial version could still be valuable, but this preprint theorem cannot be inserted into a rigorous Fermat–Catalan argument without auditing and repairing its precise hypotheses and proof.

No complete proof was obtained, and no Lean formalization was started.

# Full-scope Fermat–Catalan attempt through the remaining (2,3,prime) family

**Outcome: no full proof.** After the project's source-checked reduction, every unresolved infinite exponent class has all exponents prime. The subfamily `a²+b³=c^p`, prime `p≥7`, is one indispensable test. This pass combines the existing uniform Frey reduction with a new fixed-output-support lemma and checks the newest relevant preprint. It reaches an exact missing step, not a contradiction.

## Exact family and Frey reduction

Let `a,b,c` be positive integers with `gcd(a,b,c)=1` and `a²+b³=c^p`, where `p≥7` is prime. We count powered triples, not exponent tuples; `c≥2`. The Frey curve

`E_(a,b): Y²=X³+3bX−2a`

has `Δ=−2⁶3³c^p`, `c₄=−2⁴3²b`, and `j=1728b³/c^p`. Thus `0<j<1728`, and for every prime `q≥5` dividing `c`, the curve has multiplicative reduction with discriminant valuation a multiple of `p`. Freitas–Naskręcki–Stoll, arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4, show for primitive nontrivial solutions and prime `p≥11` that a small quadratic twist of `E_(a,b)[p]` matches the `p`-torsion of one of seven fixed curves. The twist parameter is in `{±1,±2,±3,±6}`; the fixed curves are `27a1`, `54a1`, `96a1`, `288a1`, `864a1`, `864b1`, `864c1`. The cited irreducibility and level-lowering conditions are part of this statement, not automatic for arbitrary elliptic curves.

## Attempt to turn the seven curves into a contradiction

A tempting step is: “Since the residual representation comes from a fixed curve, the original Frey curve has the fixed curve's conductor; therefore `c` has no prime `q≥5`.” **That implication is false.** Mod-`p` level lowering can remove a multiplicative prime precisely because `v_q(Δ)` is divisible by `p`; the original curve still has bad reduction at `q`. A residual isomorphism does not establish a rational isogeny or equal conductors.

If one *assumed* a uniform Frey–Mazur-type theorem saying that, for all sufficiently large `p`, any two elliptic curves over `Q` with isomorphic mod-`p` Galois representations are `Q`-isogenous, then each small twist of the Frey curve would be isogenous to one of the seven fixed curves. Isogenous curves have the same conductor. Since the twist parameters have no prime factors `q≥5`, a hypothetical `q≥5` dividing `c` would stay a bad multiplicative prime of the twisted Frey curve, contradicting the fixed conductor. This would force `supp(c)⊆{2,3}` for all sufficiently large `p`. **Frey–Mazur uniformity is conjectural, so this is not an unconditional step.**

## Unconditional fixed-output-support lemma

For any fixed finite set `S` of primes, there are only finitely many primitive positive powered triples `a²+b³=c^p` with prime `p≥7` and `supp(c)⊆S`.

**Proof.** Set `C=c^p`. Factor `C=D w⁶`, where `D=∏_(q∈S) q^{e_q}` with `0≤e_q≤5` and `w` is a positive integer supported on `S`. There are finitely many possible `D`. Put `u=b/w²`, `v=a/w³`. These are `S`-integers and satisfy `v²+u³=D`. For each nonzero `D`, this is a nonsingular genus-one curve, so Siegel's theorem gives finitely many `S`-integral pairs `(u,v)`. Fix one such pair and `D`. For any `q∈S`, write `t=v_q(w)`, `α=v_q(v)`, and `β=v_q(u)`. If `t>0`, then `q|C` and hence `q|c`. But `v_q(a)=α+3t` and `v_q(b)=β+2t`; primitivity forbids both being positive. Since `a,b` are integers, one of these two nonnegative values must equal zero, which bounds `t` in terms of the fixed pair. Thus only finitely many `w` occur. Each gives one `a,b,C`; as `c≥2`, only finitely many `c,p` can represent a fixed `C`. This proves the lemma. The same proof handles `S={2,3}`. The lemma does **not** say the equation itself fixes `S`.

This lemma would finish the `(2,3,p)` family after a proved uniform deduction `supp(c)⊆S` for a fixed `S`; no such deduction follows from the known residual-representation result. Moreover, even finishing this family would leave other all-prime signatures such as `(3,3,p)` and `(2,5,p)`.

## Recent-paper check and local route

The most direct later paper checked in this project is Freitas–Mocanu–Sánchez-Rodríguez, *Revisiting the equation x²+y³=zᵖ*, arXiv:2512.10781v1 (11 December 2025), Theorems 1.2 and 3.1. It excludes selected antisymplectic twists for certain `(E,p)` pairs and shows why separate good-prime local tests do not eliminate every remaining pair. It does not classify positive solutions uniformly in `p`. The necessary real range `0<j<1728` cannot be imposed on a fixed comparison curve's `j`: an isomorphism of `p`-torsion does not preserve the `j`-invariant.

I also checked the newer Nuno Freitas preprint *On Fermat-type equations of signature (r,r,p)*, arXiv:2609.32509v1 (26 September 2026), abstract, introduction, and Theorem 1.1. It proves an asymptotic exclusion for `x^r+y^r=Cz^p` with fixed prime `r≥11` and infinitely many **coefficients `C>2`** satisfying conditions on their prime divisors and an auxiliary finite set `L_r`; the lower bound on `p` depends on `r,C`. The theorem explicitly requires `C>2`, so it cannot be specialized to the coefficient-one repeated-prime cases within Fermat–Catalan. Its use of several Frey curves and trace separation may inspire a coefficient-one argument, but that adaptation is not in the theorem.

**Missing full-proof step:** Unconditionally show, across all prime signatures, that moving supporting primes or surviving modular-twist rational points cannot produce infinitely many positive primitive powered triples. The fixed-output-support lemma is a rigorous restricted finiteness statement, and the Frey–Mazur closure is explicitly conditional. Neither proves Fermat–Catalan. No Lean formalization was attempted.

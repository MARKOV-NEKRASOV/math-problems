# Audited fixed-gap bound and a sharper equal-exponent slice

**Outcome: a direct infinite-family exclusion within signed repeated-prime Fermat–Catalan signatures, not a full proof.** The checked Bérczes–Evertse–Győry exponent bound for a general fixed gap remains valid but enormous. In the signed equal-prime case, the project's earlier cyclotomic valuation profile gives a much smaller, exact divisibility bound on the variable exponent. The latter is a corollary of an existing result, stated here as a bound useful for deciding which fixed-gap subproblems remain.

## Audit of the general geometric bound

For fixed `P,Q≥2`, sign `ε`, nonzero integer base gap `D=m−n`, and `m^P+ε n^Q=k^W>0`, the repository uses the squarefree polynomial `F(T)=T^P+ε(T−D)^Q`. Its degree `d` is `max(P,Q)`, except `ε=−1,P=Q`, when `d=P−1`. Directly from Bérczes–Evertse–Győry, arXiv:1301.7168v1, Theorem 2.3, equation (2.7), with `K=Q`, `S={∞}`, coefficient height `H`, and `k≥2`, one gets

`W ≤ (10d²)^(40d) H^(11d)` for `W≥3`, `d≥2`.             (1)

Choosing which base is the polynomial variable gives `H≤1+(1+|D|)^min(P,Q)`, so the repository's displayed bound follows. The signed `(P,Q)=(3,3)` edge has `d=2`, and hyperbolicity forces `W≥4`; it lies within Theorem 2.3. No source-hypothesis error was found in this exponent specialization. The bound is uniform over integer solutions for **fixed** `P,Q,D`, but its right side grows with all three parameters. The paper's Theorems 2.1–2.2 provide effective height bounds; their enormous constants do not make a practical global search.

## Exact divisibility cap when the fixed exponents are equal and odd prime

**Lemma.** Let `p≥3` be an odd prime and let coprime positive integers `m>n≥1` satisfy

`m^p−n^p=k^W`, with `k≥2`, `W≥2`. Put `D=m−n>0`. Then either

`D=u^W` if `p∤D`, or `D=p^(W−1)u^W` if `p|D`, for a positive integer `u`.   (2)

Equivalently, for every prime `ℓ|D` with `ℓ≠p`, `W|v_ℓ(D)`, and if `p|D`, `W|v_p(D)+1`. Thus when `D>1` the allowable `W` divide the positive integer

`G_p(D)=gcd({v_ℓ(D): ℓ|D, ℓ≠p} ∪ {v_p(D)+1 if p|D})`.     (3)

In particular `W≤G_p(D)≤1+log₂D`. If `p∤D`, the stronger `W≤log₂D` holds. These caps replace the astronomical geometric bound (1) on this slice. If `D=1`, the set in (3) is empty and the lemma gives no bound; no claim about that case follows. Indeed `8³−7³=13²` is a primitive `D=1` instance when `W=2`; that signature is outside Fermat–Catalan's hyperbolic range, but it prevents extending the squarefree-gap exclusion to all exponents without a new argument.

**Proof.** Write `m^p−n^p=(m−n)S`, where `S=∑_(j=0)^(p−1)m^(p−1−j)n^j`. Modulo `D`, `S≡p n^(p−1)`. Because `gcd(D,n)=gcd(m,n)=1`, every prime `ℓ≠p` dividing `D` does not divide `S`; hence its valuation in `k^W` is exactly `v_ℓ(D)` and is divisible by `W`. If `p|D`, then `p∤mn`, and LTE gives `v_p(m^p−n^p)=v_p(D)+1`, again divisible by `W`. Therefore the prime exponents of `D` are multiples of `W` away from `p`, and its p-exponent is congruent to `−1 (mod W)`, yielding (2) and (3). Since `D≥2` and every non-p prime exponent is ≤`log₂D`, while `v_p(D)+1≤1+log₂D`, the displayed numerical caps follow. □

For every `W≥3`, **no primitive signed repeated-prime solution can have squarefree `D>1`**. Indeed, if `D` has a non-p prime then (3) has a `1`; if `D=p`, (3) is `2`. More generally, a fixed gap `D` with `G_p(D)<W` is eliminated outright. This is a genuine infinite exponent-family exclusion for each such `D`, though it repeats the valuation mechanism already present in the repository's signed profile. The case `D=1`, positive-left equal exponents, and pairwise-distinct exponent signatures require other arguments.

## Scope relative to the full conjecture

When two equal prime-power terms straddle `x^p+y^q=z^p`, move one to obtain `z^p−x^p=y^q`; the lemma applies with `W=q` and `D=z−x`, provided the bases are positive and primitive. It removes all squarefree nonunit base gaps for every odd prime `q≥3` in that orientation. It does **not** bound `D` as solutions vary: (2) allows gaps that are large perfect powers or `p^(W−1)` times one. It cannot alone prove finiteness across moving exponents.

**Checks.** I re-read the BEG v1 Theorem 2.3 assumptions and its exact constant; checked the factor congruence and LTE hypotheses algebraically. No Lean formalization is warranted.

# Fermat–Catalan: inequality/height proof attempt (October 2026)

**Status: no unconditional proof.** The argument below proves elementary reductions and shows exactly where an unproved abc-type estimate would be needed. It makes no new claim about the full conjecture.

## Target and sources

For positive integers `x,y,z` with `gcd(x,y,z)=1`, and integers `p,q,r>1` satisfying `1/p+1/q+1/r<1`, consider `A=x^p`, `B=y^q`, `C=z^r` with `A+B=C`. The conjecture asks for finitely many **distinct triples `(A,B,C)`**, not finitely many exponent tuples. The distinction matters when a base is 1. The fixed-signature Darmon–Granville result is stated in [Poonen–Schaefer–Stoll, Introduction §1.2](https://arxiv.org/abs/math/0508174) and the [Fermat–Catalan overview](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture).

## Unconditional lemmas

1. **Uniform hyperbolic gap.** After sorting the exponents as `2≤p≤q≤r`, every triple with `1/p+1/q+1/r<1` satisfies

   `1/p+1/q+1/r ≤ 1/2+1/3+1/7 = 41/42`.

   Proof by cases: if `p≥4`, the sum is at most `3/4`. If `p=3`, its maximum below 1 is `1/3+1/3+1/4=11/12`. If `p=2`, then `q≥3`: for `q=3` hyperbolicity forces `r≥7`; for `q=4` it forces `r≥5`, giving at most `19/20`; and for `q≥5` the sum is at most `1/2+2/5=9/10`. Equality `41/42` occurs at `{2,3,7}`. Poonen–Schaefer–Stoll §1.3.1 also identifies `{2,3,7}` as the negative-Euler-characteristic signature nearest zero.

2. **Primitive bases are pairwise coprime.** If a prime divides any two of `x,y,z`, the equation forces it to divide the third, contradicting `gcd(x,y,z)=1`. Consequently `A,B,C` are pairwise coprime, so the standard abc formulation applies to them. Moreover `rad(ABC)=rad(xyz)≤xyz`.

3. **Every such solution is a high-quality abc triple.** Since `x^p<C`, `y^q<C`, and `z^r=C`, we have `xyz<C^(1/p+1/q+1/r)≤C^(41/42)` (strict if `x,y>0`). Thus `rad(ABC)<C^(41/42)`, equivalently `C>rad(ABC)^(42/41)` when `rad(ABC)>1`. This is an elementary consequence of the equation and the uniform gap; it does **not** say there are finitely many such triples.

4. **Known reductions.** If `d=gcd(p,q,r)≥3`, setting `X=x^(p/d)`, `Y=y^(q/d)`, `Z=z^(r/d)` gives `X^d+Y^d=Z^d`, excluded by Fermat's Last Theorem. If a base on the left is 1, Mihăilescu's theorem on consecutive perfect powers leaves the single powered-value triple `(1,8,9)` (up to swapping the summands); varying the exponent on 1 does not produce new powered-value triples. These use established deep theorems, not new elementary proofs.

## Conditional abc route and exact gap

Assume the unproved **abc conjecture** in the form: for every `ε>0`, there is `K_ε` such that every coprime positive `A+B=C` satisfies `C≤K_ε rad(ABC)^(1+ε)`. Choose `ε=1/42`. Then, using Lemma 3,

`C ≤ K_(1/42) · C^((41/42)(43/42)) = K_(1/42) · C^(1763/1764)`.

Hence `C^(1/1764)≤K_(1/42)` and `C≤K_(1/42)^1764`. Only finitely many `(A,B,C)` remain. The overview explicitly states that abc implies Fermat–Catalan. **This is conditional, not a proof of the open conjecture.**

The failed unconditional step is the missing upper bound `C≤K·rad(ABC)^(1+ε)` (or another bound strong enough for these special perfect-power triples). Lemma 3 gives an *upper* bound on `rad(ABC)` in terms of `C`; reversing that inequality would be invalid. A restricted abc estimate with exponent strictly below `42/41` and one constant uniform over all Fermat–Catalan triples would suffice, but proving it is essentially the original uniform-finiteness challenge, not an established lemma.

Darmon–Granville proves finiteness **for each fixed** hyperbolic exponent signature, via descent and Faltings' theorem; Poonen–Schaefer–Stoll §1.2 explains this. It does not bound the union as `(p,q,r)` varies. Finiteness of each member of an infinite family alone cannot yield finiteness of the union.

## Next proof obligation

Find an unconditional mechanism that bounds `C` or the exponent signatures uniformly for primitive perfect-power triples, or a different reduction to finitely many already classified signatures. A proof for one fixed signature, or a bounded computation, is valuable partial work but does not close this obligation. Formalization is deferred until a complete mathematical proof is found. Any future statement must count powered-value triples rather than exponent tuples.

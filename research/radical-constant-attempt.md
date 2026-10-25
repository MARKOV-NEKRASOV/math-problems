# New radical-optimization attempt for Fermat–Catalan

**Outcome: incomplete.** The exact real optimization below sharpens the constant in the radical bound for each exponent signature. It does not change the power of the height and therefore does not close any infinite moving-prime branch.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B` be a primitive positive triple, with `p,q,r>=2` and reciprocal sum `sigma<1`. Set `R=rad(ABC)` and `s=A/C` in `(0,1)`. Primitivity gives `R=rad(xyz)<=xyz`, and hence the exact inequality

`R <= C^sigma s^(1/p)(1-s)^(1/q)`.

The function in `s` has log derivative `1/(ps)-1/(q(1-s))` and strictly negative second log derivative. Its unique maximum occurs at `s=q/(p+q)`. Thus

`R <= theta(p,q) C^sigma`,

`theta(p,q) = (q/(p+q))^(1/p) (p/(p+q))^(1/q) < 1`.       (1)

The constant is `0.570727...` for input exponents `(2,3)`, `0.657843...` for `(2,5)`, and `0.702694...` for `(3,5)`. The bound is a strict improvement over `R<C^sigma`, but is independent of `r`; it does not force a uniform contradiction. Indeed, along balanced input exponents `p,q->infinity`, `theta(p,q)->1`. When `p,q` are fixed, the constant remains below 1 but cannot offset an unbounded factor `C^delta` from a missing positive power gap.

For example, suppose one had an unconditional estimate `C<=K R^kappa` for this special family. Combining it with (1) gives `C^(1-kappa sigma)<=K theta(p,q)^kappa`. If `kappa sigma<1` uniformly eventually, then `C` is bounded. The constant matters only at the equality threshold `kappa sigma=1`, where a contradiction would require the *specific* constant `K theta^kappa<1`; no known theorem in the checked project supplies such a sharp constant. This cannot replace the abc-strength missing estimate.

I also checked whether requiring all three exponents to grow might combine (1) with Stewart–Yu's unconditional polylogarithmic radical lower bound. It cannot: `R=C^o(1)` still permits `log R` to dominate any fixed multiple of `log log C`. For example the abstract scale `R=exp(sqrt(log C))` satisfies both a polylogarithmic lower bound and `R=C^o(1)`. This is only a consistency check of inequalities, not an example of a powered triple.

The [distinct-prime branch review](review-distinct-prime-escape.md) checks the underlying escape analysis. No complete proof or Lean formalization resulted.

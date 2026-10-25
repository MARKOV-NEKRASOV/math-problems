# Fermat–Catalan full-proof attempt through elliptic height and conductor

**Outcome: incomplete.** The new exact calculation below sharpens the prior `j`-invariant observation to a uniform relation `h(j)=6 log C+O(1)` and produces a quantitative height–conductor gap for every hypothetical solution. No established height–conductor theorem closes that gap for this family.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, with positive pairwise-coprime powered values, exponents at least 2, and `1/p+1/q+1/r<1`. Count distinct powered triples. Attach `E:Y²=X(X−A)(X+B)`, and set `S=A²+AB+B²=C²−AB`. The direct invariant formulas are `Δ=16(ABC)²`, `c₄=16S`, and `j=256S³/(ABC)²`. As in the earlier universal curve note, `gcd(S,ABC)=1` and the identity for `j−1728` gives `j>1728` for a Fermat–Catalan solution.

## Uniform exact logarithmic-height lemma

Write `d=gcd(256,(ABC)²)`. The coprimality above gives the reduced rational expression `j=(256S³/d)/((ABC)²/d)`. Since `AB≤C²/4`, one has `(3/4)C²≤S<C²`. The reduced numerator therefore satisfies

`(27/64) C⁶ ≤ 256S³/d < 256 C⁶`.

Since `j>1728>1`, the reduced numerator exceeds the reduced denominator. Thus the absolute logarithmic Weil height of the rational number `j` is exactly the log of that numerator, and

`6 log C + log(27/64) ≤ h(j) < 6 log C + log 256`.       (1)

The constants do not depend on the exponent signature or the bases. This strengthens the earlier denominator lower bound: real `j` might remain bounded, yet its arithmetic height grows at the precise scale `6 log C`.

At each odd prime dividing `ABC`, `c₄` is a unit, the model has multiplicative reduction, and the conductor exponent is 1. At odd primes outside `ABC`, it has good reduction. The conductor exponent at 2 is bounded by an absolute constant for elliptic curves over `Q` (a standard consequence of the Tate-algorithm classification; I did not independently verify a sharp numerical bound from a primary source). Consequently, with `R=rad(ABC)` and conductor `N(E)`, there is an absolute `K₂` such that `N(E)≤K₂R`. The elementary perfect-power estimate gives `R≤xyz<C^σ≤C^(41/42)`. Therefore

`N(E) < K₂ C^(41/42)`, and from (1),

`h(j) > (252/41) log N(E) − (252/41) log K₂ + log(27/64)`.       (2)

The coefficient `252/41=6+6/41` is strictly above 6. If there were infinitely many powered-value triples, their `C` and `N` would both become unbounded along a subsequence (bounded `N` gives bounded prime support, then fixed-`S` S-unit finiteness), and (2) would hold for that sequence. A **proved** uniform upper bound `h(j)≤(6+ε)log N+K_ε` for this special family with any fixed `ε<6/41` would contradict (2) for large `N`. Such an upper bound is not established here; introducing it would smuggle in an abc-strength assertion. The standard conjectural abc inequality itself gives a bound of this type: `C≤K_δ R^(1+δ)` implies via (1) `h(j)≤6(1+δ)log N+O_δ(1)`, using `R≤2N`.

## Testing a uniform-geometry shortcut

Each fixed hyperbolic signature defines a high-genus covering of the thrice-punctured line, and Faltings/Darmon–Granville makes its primitive rational-point set finite. The family contains infinitely many covers as prime exponents vary. A uniform *number* bound for rational points on each cover would still allow one new rational point on every cover, so it would not prove the conjecture. The orbifold hyperbolicity condition corresponds to `1/p+1/q+1/r<1`, but geometry alone does not turn isolated rational points on infinitely many covers into a positive-dimensional rational family. The Mason–Stothers proof over `Q(t)` applies to an actual nonconstant polynomial family, not to a sequence of unrelated rational points.

The hoped-for elliptic route also fails at an exact location: `j>1728` is a real bound below, while its arithmetic height is *unbounded* by (1), and the bad-prime set grows with `R`. Northcott and Shafarevich apply with a height bound or fixed bad-prime set; neither is available. The lower bound (2) says hypothetical solutions occupy a high height–conductor region, but no unconditional theorem used here excludes that region.

**Exact missing theorem:** a uniform upper height–conductor bound of slope less than `252/41` for this Frey family, or an independent unconditional uniform bound on exponents/heights across all signatures. This note is an attempt at the full conjecture, not a proof. No Lean formalization was attempted.

Sources for the established background: Poonen–Schaefer–Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, arXiv:math/0508174 (fixed-signature context); standard Tate-algorithm conductor facts for elliptic curves; Evertse, *On equations in S-units and the Thue–Mahler equation*, DOI 10.1007/BF01388644. Formulas (1)–(2) are direct calculations in this note.

# Full Fermat–Catalan proof attempt through unconditional radical estimates

**Outcome: no complete proof.** This pass tests an explicit proof by contradiction against the strongest general radical estimate already documented in the project, a fixed-support `S`-unit argument, and a quantitative support split. It produces a conditional criterion for closing the proof, but the criterion is not known unconditionally.

Let `A=x^p`, `B=y^q`, `C=z^r=A+B`, with positive bases `x,y,z`, `gcd(x,y,z)=1`, `p,q,r>=2`, and `sigma=1/p+1/q+1/r<1`. Count distinct powered-value triples `(A,B,C)`. Unit-base triples are finite by Mihailescu; discard them under the hypothesis of an infinite family. Then `A,B,C` are pairwise coprime. Put `R=rad(ABC)=rad(xyz)`, `s=omega(R)`, `P=max supp(R)`, and `L=log C`.

## Attempted contradiction

The hyperbolic reciprocal sum has maximum `41/42`, attained at the signature `(2,3,7)`. Since `x<C^(1/p)`, `y<C^(1/q)`, and `z=C^(1/r)`, every putative solution satisfies

`R <= xyz < C^sigma <= C^(41/42)`.                                      (1)

For any infinite family, `C` is unbounded. The fixed-`S` theorem for `S`-unit equations shows `P` is unbounded: with primes in a fixed finite `S`, the rational pair `(A/C,B/C)` consists of `S`-units solving `u+v=1` and determines the primitive integer triple. Fixed hyperbolic signatures have finitely many primitive solutions by Darmon–Granville, so the reduced exponent signatures also escape every finite set. Both statements allow *simultaneous* escape by excluding a finite union at each stage.

The cited Stewart–Yu general abc estimate is reported as

`L < K R^(1/3) (log R)^3`                                               (2)

for one absolute `K`. The original Duke Math. J. article was not accessible in this project; the displayed form was checked only against the secondary [abc overview](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results). Inverting (2) gives `R>c L^3/(log L)^9` for large `C`, as shown in [the earlier height note](whole-height.md). Thus the attempted squeeze is

`c L^3/(log L)^9 < R < exp((41/42)L)`.                                 (3)

Both sides of (3) can hold for arbitrarily large `L`: the lower bound is only polynomial in `L`, whereas the upper bound is exponential in `L`. Substitution of (1) directly into (2) gives `L<K exp((41/126)L)((41/42)L)^3`, again true for all large `L`. This is the precise point where the unrestricted contradiction attempt fails.

## Optimizing the split by number and size of supporting primes

Use `R<=P^s`, and let `Q_s` denote the product of the first `s` primes, so `Q_s<=R`. Combining the unconditional estimates yields

`c L^3/(log L)^9 < R <= P^s` and `Q_s < exp((3/m)L)`, where `m=min(p,q,r)`. (4)

If `s<=s0` for a fixed integer `s0>=3`, then (4) forces

`P > c0 L^(3/s0)/(log L)^(9/s0)` for large `L`, with `c0>0` fixed.     (5)

Therefore a uniform theorem forcing **both** `s<=s0` and `P<=L^delta` for some `delta<3/s0` would give a contradiction. Neither of those two restrictions follows from the Fermat–Catalan equation. Merely bounding `s` would leave moving large primes, so fixed-`S` finiteness is insufficient.

If instead `s` grows, the prime number theorem gives `log Q_s=(1+o(1))s log s`. Equation (4) then yields

`m s log s <= (3+o(1)) L`.                                               (6)

This excludes certain simultaneous growth rates, but it does not force `m` or `s` bounded. For example, as a *consistency check on the inequalities only*, take a parameter `t->infinity` with `L=t^3`, `m=t`, `s=t`. Then the left side of (6) is `t^2 log t`, smaller than `3t^3`, and there is a wide interval between the polylogarithmic lower bound on `R` and its perfect-power upper bound. This example is not asserted to be a solution of the Diophantine equation.

## Could a special-case abc bound close it?

Yes, but this is exactly the missing theorem. An unconditional estimate `C <= K_epsilon R^(1+epsilon)` for these primitive perfect-power triples, at one fixed `epsilon<1/41`, would combine with (1) to give `C <= K_epsilon C^((41/42)(1+epsilon))`, whose exponent is below 1; hence `C` would be bounded. The usual abc conjecture gives such an estimate for every positive `epsilon`, but is not an established input. Equivalently, a lower radical bound `R >= c C^alpha` with `alpha>41/42` on this solution universe would finish. A generic polylogarithmic bound such as (2) does not approach that threshold.

Even for the special family `(2,3,ell)` with `ell` prime, the exponent sum is `5/6+1/ell`, approaching `5/6` but remaining bounded away from 1. A restricted power-scale radical estimate with one uniform constant and a fixed exponent gap above that sum across all `ell` would settle this family. No source checked in the project supplies one. Fixed-signature finiteness, fixed-support finiteness, and unconditional general abc estimates have distinct constants or hypotheses and cannot be unioned over moving signatures and support.

**Conclusion:** The contradiction proof stops at (3), and the optimized support split stops at unproved simultaneous restrictions on `s` and `P`. The new work is a precise falsifiable closure criterion, not a proof of the full Fermat–Catalan conjecture. No Lean formalization was attempted.

Sources: Stewart and Yu, *On the abc conjecture, II*, Duke Math. J. 108 (2001), DOI 10.1215/S0012-7094-01-10815-6 (displayed estimate checked through a secondary overview); Evertse, *On equations in S-units and the Thue–Mahler equation*, DOI 10.1007/BF01388644; Darmon–Granville's fixed-signature finiteness as stated in Poonen–Schaefer–Stoll, Introduction section 1.2, arXiv:math/0508174.

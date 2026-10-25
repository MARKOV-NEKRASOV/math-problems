# Independent review of the repeated-prime proof attempt

**Verdict:** I checked the source-dependent `(3,3,t)` exclusion and the cyclotomic residue deductions in `prime-repeated-attempt.md`. They are correct as restrictions on a hypothetical solution, not a proof of global finiteness. The note preserves the signed orientation required by the source theorem.

## Primary-source check

I read Bennett–Bruni–Freitas, *Sums of two cubes as twisted perfect powers, revisited*, arXiv:1702.07827v1, Theorem 1.1 and the discussion immediately after it in the PDF text at `source PDF text, inspected locally`. The theorem is a **summary of earlier results** credited there to Bruin, Chen–Siksek, Dahmen, Freitas, and Kraus. It excludes nonzero relatively prime integer solutions of `A³+B³=C^n` for the displayed classes: every integer `3≤n≤10^9`; every `n≡2 (mod 3)`; every `n≡2,3 (mod 5)`; and the listed classes modulo 78, 106, and 1296. The theorem concerns signed integers and does not require positivity, so it applies to the positive left-summand orientation and also to a repeated cube on opposite sides after moving a cube across `=` with a negative base.

For prime `t≥7`, primality removes residues 0 modulo 3 and 5. Exclusion of `t≡2 (mod 3)` leaves `t≡1 (mod 3)`. Exclusion of `t≡2,3 (mod 5)` leaves `t≡1 or 4 (mod 5)`. The Chinese remainder theorem gives `t≡1 or 4 (mod 15)`. The independent bound `3≤t≤10^9` forces `t>10^9`. The note also says a survivor must avoid the other displayed residue classes. This is the exact conclusion justified by the theorem. Both classes `1` and `4` modulo 15 contain infinitely many primes by Dirichlet, so the conclusion does not bound `t`.

The paper's following paragraph states that the ordinary sum-of-two-cubes modular approach has an obstruction at conductor 72, curve `72A1`. The later main theorems of that paper impose a coefficient `q^α` with `q≥5` prime and `α>0`; `q=1` is outside their hypotheses. The note correctly avoids transferring those results to `A³+B³=C^n`.

## Algebra and orientation check

For odd prime `p`, `a^p+b^p=(a+b)V` with `V≡p b^(p−1) (mod a+b)`. Primitivity implies `gcd(a+b,b)=1`, so `gcd(a+b,V)|p`. If `p|(a+b)`, signed LTE still gives `v_p(V)=1` because `p∤ab`. For a signed solution the factors should be treated as **signed** perfect powers when the third exponent `t` is odd; this holds in the residual `t≥5` branch. In the `p∤a+b` branch both signed factors are `t`th powers. In the `p|a+b` branch `V=pv^t` and `v_p(a+b)≡−1 (mod t)`. The note uses these only as necessary conditions.

The source-checked Chen–Koutsianas survey Theorem 11.5 applies to primitive signed `a^p+b^p=c^t` for `p∈{5,7,11,13}` and excludes `2|(a+b)` or `p|(a+b)`. If the repeated powers originally straddle `=`, the substitution `b→−b` preserves the odd pth power and primitivity; the condition then refers to the **signed** sum/difference of their bases, not automatically to the sum of two original positive bases. The note states this orientation correctly. The case `t=2` is covered by Bennett–Skinner's signed `C=1` theorem; the historical `t=3` table row is left as a source-audit caveat rather than silently removed.

**Remaining gap:** The surviving prime classes for `(3,3,t)` and the cofactor equations for other repeated `p` remain infinite. This review validates the restrictions only; it does not establish a full Fermat–Catalan proof.

## Review of the appended Eisenstein-integer construction

The new construction is correct and illustrates why `V=v^t` alone is weak. Let `ω²+ω+1=0` and `α=N+ω` with `N≡0 or 1 (mod 3)`. Its norm is `N²−N+1≡1 (mod 3)`. Also `α−\bar α=ω−ω²` has norm 3, so a common Eisenstein prime of `α` and `\bar α` would lie above 3; the norm condition rules that out. Thus `gcd(α,\bar α)=1` in `Z[ω]`.

Write `α^t=a+bω`. If a rational prime `q` divided both integer coefficients `a,b`, then `q` would divide both `α^t` and its conjugate in `Z[ω]`. Any Eisenstein prime above `q` would consequently divide both `α` and `\bar α`, contradicting their coprimality. This argument handles split, inert, and ramified rational primes uniformly; the restriction on `N mod 3` is essential for the ramified prime 3. Hence `gcd(a,b)=1`.

In the complex embedding `ω=−1/2+i√3/2`, `arg(N+ω)>0` and tends to zero as `N→∞`. For any fixed odd prime `t`, choose an arbitrarily large admissible `N` with `0<t arg(N+ω)<π/3`. Then `Im(α^t)>0` makes `b>0`, while `Re(α^t)>0` and `a=Re(α^t)+b/2` make `a>0`. Multiplicativity of the Eisenstein norm gives `a²−ab+b²=(N²−N+1)^t`. Varying `N` gives infinitely many primitive positive examples for each fixed `t` (and one may choose such an `N` for each arbitrarily large prime `t`). These examples do **not** satisfy `a+b=u^t` as far as the construction shows; they are not Fermat–Catalan solutions. The note correctly presents them only as counterexamples to eliminating the cofactor-power condition in isolation.

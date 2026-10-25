# A precise simultaneous-power lemma for the repeated-cube branch

**Outcome: a restricted theorem, not a full proof.** In the clean cyclotomic branch, the simultaneous requirements on `U=a+b` and `V=(a³+b³)/(a+b)` exclude the smallest possible t-th-power sum. They do not exclude unbounded sums or all prime exponents.

## Lemma (fixed root of the linear factor)

Let `p≥3` be an odd prime, `t≥3` an odd integer, and `a,b>0` coprime. Suppose

`a^p+b^p=c^t`, `p∤a+b`, and `a+b=u^t`

with integer `u≥2`. Then `V=(a^p+b^p)/(a+b)=v^t` for a positive integer `v`, and

`2^((1−p)/t)u^(p−1)≤v≤u^(p−1)−1`.

Consequently, with `H=u^(p−1)`, necessarily

`t≤(p−1)log 2 / [−log(1−1/H)]`.                 (1)

In particular, if `p=3` and `u=2`, then `t≤4` and there is **no** such solution for any eligible prime `t≥5`. More generally, for each fixed pair `(p,u)` only finitely many t are possible in this positive-left clean branch.

**Proof.** The identity `V≡p b^(p−1) (mod U)` and `gcd(U,b)=1` show `gcd(U,V)|p`; because `p∤U`, the factors are coprime. As `UV=c^t`, each positive factor is a t-th power. Put `s=a/U∈(0,1)`. Then `V/U^(p−1)=s^p+(1−s)^p`, which lies in `[2^(1−p),1)`. Substitute `U=u^t`, `V=v^t` and take t-th roots. As `v` is integral and strictly below the integer `H=u^(p−1)`, it is at most `H−1`. Thus `2^((1−p)/t)H≤H−1`. Taking logarithms gives (1). For `p=3,u=2`, (1) yields `t≤2 log2/log(4/3)=4.818...`, so integer `t≤4`. Equivalently, `v≤3` but `v^t≥4^t/4>3^t` for `t≥5`. □

The ramified case is distinct. If `p|U`, LTE yields `v_p(V)=1` and `v_p(U)≡−1 (mod t)`. Hence `U=p^t` is impossible for every `p,t≥3`: it has `v_p(U)=t≡0 (mod t)`. This does **not** rule out general p-supported `U` such as `p^(t−1)` times other factors.

## Why this cannot finish the conjecture

The bound (1) grows with `u`. It says that if `t` grows for fixed `p`, then the t-th root `u` of `a+b` must grow; it gives no upper bound on `u` or `t`. The lemma uses `a,b>0` and does not transfer directly to a signed difference of two p-th powers. The ramified branch and all pairwise-distinct prime signatures remain open.

## Recent source check

I downloaded and read arXiv:2509.18275v1, Preda Mihăilescu, *The strong Fermat-Catalan Equation* (submitted September 2025), introduction, Theorem 1 and §§2–3. Its Theorem 1 asserts that for distinct odd primes `p>3,q` and `e∈{0,1}`, the signed nonzero coprime equation `(x^p+y^p)/(x+y)=p^e z^q` has no solutions; it claims the `(p,p,q)` Fermat–Catalan family with `p>3` as a corollary. **As literally printed, Theorem 1 is false:** `x=y=z=1`, `e=0` gives `(1^p+1^p)/(1+1)=1=1^q` for every allowed pair `p,q`. The proof later imposes `x>|y|≥1` (Assumption 1), which excludes this unit example, so the literal counterexample does not itself settle the intended nonunit theorem. The author explicitly says p=3 is excluded because the cofactor equation has infinitely many Eisenstein-norm examples. This is a stronger intended claim than this elementary lemma, and it addresses the *cofactor alone*. I did not establish an independent validation of the preprint's cyclotomic ideal argument, so it is a research lead, not an audited theorem that closes the branch in this project. In particular, even if a corrected nonunit theorem were ultimately validated, `(3,3,t)` and all pairwise-distinct signatures would still require separate uniform treatment.

No Lean formalization was attempted.

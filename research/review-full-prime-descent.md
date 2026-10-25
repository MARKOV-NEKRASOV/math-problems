# Independent review of all-prime cyclotomic descent

**Verdict:** The factorization, gcd, and valuation deductions in `full-prime-descent.md` are correct under the stated assumptions. They provide necessary cofactor equations, not a full proof of Fermat–Catalan.

For odd prime `p`, `a^p+b^p=(a+b)V`, and modulo `U=a+b`, `a≡−b` makes each of the `p` alternating terms in `V` congruent to `b^(p−1)`. Hence `V≡p b^(p−1) (mod U)`. Primitivity gives `gcd(U,b)=1`, so `gcd(U,V)|p`. If `p∤U`, the gcd is 1. If `p|U`, then `p∤ab` and the odd-prime LTE formula gives `v_p(a^p+b^p)=v_p(U)+1`, hence `v_p(V)=1` and `gcd(U,V)=p`, even when `p²|U`.

Now impose `UV=c^t` with prime `t≠p`. In the coprime case, unique factorization in positive integers yields `U=u^t`, `V=v^t`. In the `p|U` case, every prime other than `p` dividing `V` has valuation divisible by `t`, while `v_p(V)=1`; therefore `V=pv^t` with `p∤v`, and `v_p(U)+1≡0 (mod t)`. These are exact necessary conditions. They do not assert that `U` or `V` is small or forbid solutions for varying `p,t`.

For `c^p−a^p=b^t`, take `U=c−a` and `V=(c^p−a^p)/(c−a)`. Modulo `U`, `V≡p a^(p−1)`. Pairwise coprimality gives `gcd(U,a)=1`, and LTE for a difference of odd `p`th powers gives the same `p`-adic valuation when `p|U`. The orientation argument is sound.

I also checked the branch split. Hyperbolicity excludes two exponents equal to 2. FLT excludes all three equal odd primes. Thus exactly two equal odd primes or three pairwise distinct primes remain among all-prime signatures. The cited Poonen–Schaefer–Stoll table is a historical solved-case summary for repeated families with third exponent 2 or 3; the note properly avoids attributing an exact theorem range solely to Darmon–Merel. It does not supply a uniform result for third exponent at least 5.

**Unclosed gap:** The cofactor equations `V=v^t` and `V=pv^t` range over varying prime `p,t` and varying coprime bases. No cited theorem excludes their positive solutions or bounds their powered values. Fixed-signature finiteness cannot control that union. No full proof follows.

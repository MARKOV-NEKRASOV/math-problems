# Independent review of repeated-prime v6 note

**Verdict:** The new elementary size gap and 3-adic example are correct as necessary/local statements, with their stated positive-left and prime-exponent restrictions. They do not prove the conjecture.

For primitive positive `a,b`, `gcd(a+b,(a^p+b^p)/(a+b))=gcd(a+b,p)` for odd prime `p`, since the cofactor is congruent to `p a^(p-1)` modulo `a+b`. Thus the split into `p∤(a+b)` and `p|(a+b)` is valid. In the first branch coprimality of the factors of the `t`th power gives `U=u^t`, `V=v^t`. Convexity of `s^p+(1-s)^p` on `(0,1)` gives exactly `2^(1-p)≤V/U^(p-1)<1`. Taking `H=u^(p-1)`, integrality gives `v≤H-1`, so `2^(-(p-1)log 2/t)≤1-1/H` and hence `t≤(p-1)log 2/[-log(1-1/H)]<(p-1)(log 2)H`. The inequality direction and strict second inequality are correct. It forces `u` to grow with `t` for fixed `p`, not an upper bound on `t`.

For `p=3`, expanding `(a+b)^3-3ab(a+b)` yields the first identity in (3). Also `4(a²-ab+b²)-(a+b)²=3(a-b)²`, yielding the second. Both are correct. In the ramified branch, `a=3^(t-1)-1`, `b=1` are coprime and `v_3(a³+b³)=v_3(a+b)+v_3(3)=t` by LTE. For prime `t≥5`, raising to the `t`th power is an automorphism of `Z_3^×` since `gcd(t,6)=1`; hence a 3-adic root `c` exists. This checks solubility only over `Q_3`; the constructed integer sum is generally not an integer `t`th power. No global conclusion follows.

The cited Bennett–Bruni–Freitas restrictions were source-reviewed earlier in the repository. The note correctly limits its new real inequality to the orientation with both `p`-powers positive on the left. Its final blocker is accurately stated.

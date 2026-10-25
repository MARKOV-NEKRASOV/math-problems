# Congruence-corrected size gaps for repeated-prime signatures

**Outcome: proved necessary bounds that remove infinite parameter ranges, not a full Fermat–Catalan proof.** The preceding real-size bounds treated `v` merely as an integer below a nearby integer `H`. A mod-`p` condition forces it to skip additional integers. This generalizes the clean and ramified gaps uniformly for positive-left repeated odd-prime signatures and yields explicit minimum roots in the surviving `(3,3,t)` family.

## The clean branch

Let `a,b>0` be coprime, `p` an odd prime, `t>=3` an odd integer with `gcd(t,p−1)=1`, and suppose `a^p+b^p=c^t`, `p∤U=a+b`. The factorization gives `U=u^t`, `V=(a^p+b^p)/U=v^t`. Put `H=u^(p−1)`. Since `p∤U`, Fermat's little theorem and the freshman-dream congruence yield

`V≡(a+b)^(p−1)≡1 (mod p)`.

As exponentiation by `t` is a permutation of `F_p^×`, `v≡1 (mod p)`. Also `H≡1 (mod p)`. The positive-left convexity inequality gives `2^((1−p)/t)H≤v<H`; thus the integer gap `H−v` is a **positive multiple of `p`**, in particular `H−v≥p`. Therefore `H>p` and

`t ≤ (p−1)log 2 / [-log(1−p/H)] < ((p−1)log 2/p) H`.       (1)

The strict second bound uses `−log(1−x)>x` for `0<x<1`. This replaces the earlier gap of one integer by a gap of at least `p`. It applies to all odd prime `t>p−1`, and also to any odd `t` coprime to `p−1`. For fixed `p,u`, it excludes every larger `t`, but `u` may grow.

## The ramified branch

Under the same positive-left hypotheses, suppose `p|U`. The valuation-profile lemma in [repeated-prime-valuation-profile.md](repeated-prime-valuation-profile.md) gives `U=p^(t−1)u^t` and `V=pv^t`, `p∤v`. The binomial expansion of `V` with `b=U−a` shows `V≡p a^(p−1) (mod p²)`: the intermediate binomial coefficients are multiples of `p`, and every term beyond the first has another factor of `U`, while `U^(p−1)` is divisible by `p²`. Hence `v^t=V/p≡a^(p−1)≡1 (mod p)`, and `gcd(t,p−1)=1` gives `v≡1 (mod p)`.

Set `H=p^(p−1)u^(p−1)`. Then `H≡0 (mod p)`, so the positive integer gap `H−v` is congruent to `−1 (mod p)` and is at least `p−1`. Direct normalization gives

`V/U^(p−1)=p^p (v/H)^t`.

Combining it with `2^(1−p)≤V/U^(p−1)<1` yields

`H/(2^(p−1)p^p)^(1/t) ≤ v < H/(p^p)^(1/t) < H`.

Since `v≤H−(p−1)`, we obtain `H>p−1` and

`t ≤ log(2^(p−1)p^p) / [-log(1−(p−1)/H)] < [H/(p−1)] log(2^(p−1)p^p)`.  (2)

This is a new ramified size gap for each fixed `p,u`; it does not bound `u`.

## Explicit surviving `(3,3,t)` bounds

Bennett–Bruni–Freitas, arXiv:1702.07827v1, Theorem 1.1 (source-checked earlier in [prime-repeated-attempt.md](prime-repeated-attempt.md)) excludes nonzero coprime signed `a³+b³=c^t` for every `3≤t≤10^9`. Thus any hypothetical eligible prime `t` in this signature satisfies `t>10^9`. As `gcd(t,2)=1`, (1) and (2) apply without a further congruence condition.

- **Clean (`3∤U`):** (1) gives `t < (2 log 2/3)u²`. Since `(2 log 2/3)·46519² < 10^9`, necessarily `u≥46520`, hence `a+b=u^t≥46520^t`. If `a,b` have opposite parity then `u` is odd and prime to 3, so the first admissible integer is `u≥46523`; if both are odd, `u` is even and `u≥46520` remains possible as far as these necessary conditions show.
- **Ramified (`3|U`):** (2) gives `t < (9 log 108/2)u²`. Since `(9 log 108/2)·6889² < 10^9`, necessarily `u≥6890`, hence `a+b=3^(t−1)u^t≥3^(t−1)6890^t`. If `a,b` have opposite parity, `u` is odd and thus `u≥6891`; if both are odd, `u` is even and `u≥6890` remains possible.

The numerical inequalities have comfortable margins: the respective upper values are approximately `999,988,354.97` and `999,927,390.33`, both strictly below `10^9`. They can be certified, for example, using rational upper bounds `log 2<0.69315` and `log 108<4.6822`, which give strict upper values below `10^9` as well.

The gap arguments above use `a,b>0`. For signed orientation the valuation profile and mod-`p` congruences persist, but `V/U^(p−1)<1` need not hold, so neither (1) nor (2) is asserted there.

## Precise next lemma target

The remaining simultaneous-power problem is now localized to large roots: `u≥46520` clean or `u≥6890` ramified for positive `(3,3,t)` and `t>10^9`. A useful next lemma would couple the integer gap `H−v` to the discriminant identity `4V−U²=3(a−b)²` and prove that **no admissible gap can make the right side a square** for every such `u,t` (or otherwise give a uniform bound on `t`). Proving this only for a fixed `u` or a finite interval of `u` would remove a subfamily, but would not yet close the moving-root branch. The real-size and mod-`p` restrictions alone allow `u→∞` and therefore do not prove the full conjecture.

No Lean formalization was attempted.

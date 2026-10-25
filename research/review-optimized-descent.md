# Independent review of the universal elliptic-curve attempt

**Verdict:** The invariant formulas and the obstruction to the proposed finiteness arguments are correct. They do not prove the full conjecture.

For `E:Y²=X(X−A)(X+B)`, direct expansion gives `c₄=16(A²+AB+B²)`, `Δ=16A²B²(A+B)²`, and `j=c₄³/Δ=256(A²+AB+B²)³/(A²B²C²)`. Expanding both sides confirms the factorization used for `j−1728`. Equality requires `A=B`, and primitivity then gives `A=B=1`, `C=2`, impossible when `C=z^r` with `r>1`. Thus `j>1728` for eligible positive triples.

The arithmetic-height claim also checks out. If a prime divides `A`, `B`, or `C`, the polynomial `S=A²+AB+B²` reduces to the square of a coprime nonzero residue. Consequently `gcd(S,ABC)=1`. The denominator of reduced `j` is exactly `(ABC)²/gcd(256,(ABC)²)`, which grows with `C`. A fixed rational `j` therefore permits bounded `ABC` and only finitely many integer triples. Yet the real inequality `j>1728` and even a bounded real interval supply no *upper* bound on rational height.

At every odd prime dividing `ABC`, `c₄` is a unit and `Δ` is divisible by the prime, giving multiplicative bad reduction. Away from `2ABC`, the model has good reduction. The bad-prime set therefore varies with `ABC`; the fixed-set Shafarevich theorem cannot be applied uniformly. The note correctly identifies this as the blocked step. A numerical bound on real `j`, or a finite number of isomorphism classes for each fixed prime set, cannot turn this into a proof across moving supports.

# Independent review of the elliptic height–conductor attempt

**Verdict:** The uniform `j`-height identity and height–conductor slope follow from the stated local conductor bound. They are necessary consequences of a Fermat–Catalan solution, not a contradiction or a proof of finiteness.

I checked the algebra independently. For `S=A²+AB+B²=C²−AB`, pairwise coprimality gives `gcd(S,ABC)=1`: modulo a prime of `A`, `B`, or `C`, `S` reduces to the square of a unit. Thus the only cancellation in `j=256S³/(ABC)²` is `d=gcd(256,(ABC)²)`, with `1≤d≤256`. Since `AB≤C²/4`, the reduced numerator lies between `(27/64)C⁶` and `256C⁶`. The previous factorization of `j−1728` shows `j>1728`, so the numerator is larger than the denominator. Hence `h(j)=6log C+O(1)` with absolute constants as displayed.

At an odd prime of `ABC`, `c₄=16S` is a unit and the discriminant is divisible by the prime; the reduction is multiplicative and its conductor exponent is 1. Away from `2ABC` the model has good reduction. A universally bounded conductor exponent at 2 for elliptic curves over `Q` gives `N(E)≤K₂ rad(ABC)` for some absolute `K₂`. The note does not cite a checked primary source for a sharp numerical value of `K₂`; its argument needs only its existence. Combining this with `rad(ABC)<C^(41/42)` gives `h(j)>(252/41)log N−O(1)`, as claimed.

The **missing step** is an unconditional upper height–conductor estimate with slope below `252/41` for these curves. Neither Northcott nor fixed-support Shafarevich finiteness supplies it: the rational heights and bad-prime sets can both grow. The note correctly refrains from asserting that such an upper estimate is known. Its geometry discussion also does not convert infinitely many fixed-signature finiteness statements into global finiteness.

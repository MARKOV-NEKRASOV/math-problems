# Full-proof attempt on the remaining prime signatures

**Result: still incomplete.** Four agents pursued the all-prime hyperbolic signatures left by the [source-checked global reduction](reduction-to-prime-signatures.md). They tested modular uniformity for `(2,3,p)`, cyclotomic descent for repeated prime exponents, and an optimized infinite-family contradiction. This pass proves restricted finiteness and stronger necessary bounds, but gives no unconditional bound on every all-prime signature.

## Attempted contradiction for an infinite family

Suppose infinitely many **distinct powered-value triples** `(A,B,C)=(x^p,y^q,z^r)` exist with prime hyperbolic exponents. Darmon–Granville makes the triples with bounded exponent signatures finite. The [reviewed escape lemma](asymptotic-prime-obstruction.md) therefore chooses representations whose maximum exponent `M→∞`. The other two exponents cannot both be 2, so `σ=1/p+1/q+1/r≤5/6+1/M` and

`R=rad(ABC)<C^(5/6+o(1))`.

This improves the old pointwise `41/42` exponent. For the universal elliptic curve, the [exact height calculation](full-height-conductor.md) gives `h(j)=6log C+O(1)` and an odd conductor equal to the odd part of `R`. Consequently a hypothetical infinite family has `h(j)≥(36/5−o(1))log N`. It would violate **every** fixed-`ε` abc bound with `ε<1/5`; the [independent review](review-asymptotic-prime-obstruction.md) checks these quantifiers. No proved upper height–conductor or radical bound of that strength is available in this attempt, so the contradiction stops there. The [height route](prime-height-attempt.md) gives explicit thresholds and branchwise variants.

## What the remaining family reductions actually do

- For `(3,3,t)`, a [source-checked theorem](prime-repeated-attempt.md) of Bennett–Bruni–Freitas excludes all prime `t≤10⁹` and several infinite residue classes. A survivor has `t>10⁹`, `t≡1 or 4 (mod 15)`, plus further restrictions. The [review](review-prime-repeated-attempt.md) confirms the theorem statement and signed orientations. Those remaining residue classes still contain infinitely many primes. Cyclotomic factorization forces two simultaneous perfect-power factors in one branch; an explicit Eisenstein construction shows that **one** factor can be a `t`th power for arbitrarily large `t`, so that shortcut fails.
- For `(2,3,t)`, Freitas–Naskręcki–Stoll reduces a Frey curve's mod-`t` representation, after a small twist, to one of seven fixed curves. This does not equate their conductors or `j`-invariants. A [Frey–Mazur-type closing step](prime-modular-attempt.md) would bound `t`, but it is unproved; its [review](review-prime-modular-attempt.md) preserves that condition. A [new fixed-output-support lemma](prime-237-attempt.md) proves finiteness when primes dividing the output base `c` lie in a fixed finite set. Its [review](review-prime-237-support.md) confirms the Siegel and valuation argument; no unconditional step fixes that prime set. The [full route review](review-prime-237-attempt.md) also records a 2026 preprint whose coefficient hypothesis `C>2` excludes the coefficient-one conjecture.
- More generally, for **fixed** input exponents `P,Q≥2` other than `(2,2)` and a **fixed** finite set of output primes `S`, the [generalized lemma](fixed-output-support.md) gives finitely many powered triples as the output exponent varies. Its [independent review](review-fixed-output-support.md) checks the superelliptic genus, Siegel finiteness, and primitivity bound. In the full conjecture, both the input exponents and output prime support may move.

## Exact unproved step

The remaining all-prime signatures include `(2,3,t)`, `(3,3,t)`, `(2,p,q)`, and signatures with three distinct primes at least 5. The established theorems above do not control their union. A full proof needs an unconditional uniform bound across moving prime exponents and prime support, or a new argument eliminating every surviving branch. Fixed-signature finiteness, separate modular curves, conditional Frey–Mazur, and the sharpened abc-quality obstruction cannot substitute for that bound. No complete mathematical proof was found, so no Lean formalization was started.

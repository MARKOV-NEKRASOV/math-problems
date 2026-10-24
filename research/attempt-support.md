# Fermat–Catalan: quantitative prime-support escape

**Status:** Unconditional necessary conditions, not a proof of Fermat–Catalan. This develops the fixed-support observation in `research/attempt-height.md` into an explicit (weak) growth condition.

Let `A=x^p`, `B=y^q`, `C=z^r` be a primitive positive Fermat–Catalan solution, with `A+B=C`, `p,q,r>1`, reciprocal sum below 1, and `x,y,z>=2`. Set `R=rad(ABC)`, `s=ω(R)` (number of distinct prime factors), and `P=P(R)` (largest prime factor). The three powered values are pairwise coprime, so `s>=3` and `R<=P^s`.

## A quantitative unconditional lemma

The Stewart–Yu bound reported in the [abc overview](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results) for [Stewart–Yu, *On the abc conjecture, II* (2001)](https://doi.org/10.1215/S0012-7094-01-10815-6) has the form

`log C < K R^(1/3) (log R)^3`,

with one absolute constant `K>0` for coprime positive `A+B=C`, `C>2`. It implies that, for some absolute `c>0` and all sufficiently large `C`,

`R > c (log C)^3/(log log C)^9`,

and therefore

`P > c^(1/s) (log C)^(3/s)/(log log C)^(9/s)`.

**Proof.** Write `L=log C`. If `R>L^6`, the first inequality is immediate for large `L`. Otherwise `log R<=6 log L`; cubing Stewart–Yu gives `L^3<K^3 R (log R)^9<=K^3 R (6 log L)^9`. Take `c=min(1,1/(K^3 6^9))`. The bound for `P` follows from `R<=P^s`. This proof does not use any perfect-power structure except to place the triple in the primitive `A+B=C` setting.

For any fixed `s0≥3`, a hypothetical sequence of solutions with at most `s0` distinct prime factors must satisfy

`P > c (log C)^(3/s0)/(log log C)^3`.

Here `c<=1`, `s>=3`, and `s<=s0` give the displayed uniform bound. For each fixed `δ>0`, this also yields `P>(log C)^(3/s0-δ)` once `C` exceeds a threshold that may depend on `δ` and `s0`. In particular, such a sequence cannot have its largest supporting prime fixed. The fixed-`S` finiteness theorem ([Evertse 1984](https://doi.org/10.1007/BF01388644)) is stronger when the actual set `S` is fixed; the displayed estimate adds information when the primes move while their count stays bounded.

## Why this does not close the conjecture

The inequality `R<C^(41/42)` from the hyperbolic exponent gap and the new polylogarithmic lower bound on `R` are compatible for arbitrarily large `C`. Even with a fixed number `s0` of supporting primes, the estimate only requires their largest member to grow like a power of `log C`; it does not bound `C`, `P`, or the exponents. Quantitative `S`-unit bounds for each fixed `S` likewise depend on `S` and cannot be unioned over all moving prime sets without a new uniform restriction.

**Concrete next obligation:** find an unconditional restriction on the *moving* prime support or a bound on `C` uniform in that support and in `(p,q,r)`. Any proposed bound strong enough to imply full finiteness must be proved independently, not imported from a fixed-`S` theorem. Formalization remains deferred under the user's preference.

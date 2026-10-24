# Fermat–Catalan: smooth-support and explicit height check

**Status:** One further unconditional necessary bound on prime support; no proof of Fermat–Catalan. No Lean work.

Let `A=x^p`, `B=y^q`, `C=z^r` be a primitive positive Fermat–Catalan solution with non-unit bases, and write `R=rad(ABC)`, `P=P(R)` for the largest prime factor of `ABC`, and `θ(t)=Σ_{prime ℓ≤t} log ℓ`. Because every prime factor of `R` is at most `P`, `log R≤θ(P)`. The [abc overview's account](https://en.wikipedia.org/wiki/Abc_conjecture#Partial_results) of [Stewart–Yu (2001)](https://doi.org/10.1215/S0012-7094-01-10815-6) gives an absolute constant `K` such that `log C<K R^(1/3)(log R)^3` for coprime positive `A+B=C` and `C>2`. The displayed formula was checked against the overview; the primary article is paywalled in this environment.

## Uniform smooth-support consequence

For every such triple,

`log C < K exp(θ(P)/3) θ(P)^3`.                                      (1)

This is an upper bound on `C` in terms of the *largest* supporting prime, even when the number of supporting primes varies. By the prime number theorem in its equivalent Chebyshev-function form `θ(t)~t` ([reference](https://en.wikipedia.org/wiki/Prime_number_theorem)), any sequence of these triples with `C→∞` must satisfy

`P ≥ (3-o(1)) log log C`.                                                  (2)

**Proof.** The first inequality follows from `R≤exp(θ(P))` and monotonicity of `u^(1/3)(log u)^3` for `u>1`. Put `L=log log C`. Taking logarithms of (1) gives

`L < log K + θ(P)/3 + 3 log θ(P)`.

If `θ(P)≥6L`, then `θ(P)≥(3-o(1))L` is immediate. Otherwise `log θ(P)≤log(6L)`, hence `θ(P)>3L-9log(6L)-3log K`. Therefore `θ(P)≥(3-o(1))L`, and `θ(P)~P` yields (2). The estimate applies to all coprime `A+B=C` triples, not specifically to perfect powers.

Using the more explicit inversion already proved in `research/attempt-support.md`, one can also write `θ(P)>3loglog C-9logloglog C-O(1)`. The prime number theorem turns this into (2). If an effective, explicit upper bound for `θ(P)` is supplied, (1) also gives an effective bound for `C` with a specified cap on `P`, subject to making the Stewart–Yu constant `K` explicit.

## Why counting smooth numbers or fixed-S bounds stop here

For each fixed `P`, the set `S={primes≤P}` is fixed, so the `S`-unit theorem gives only finitely many primitive `A+B=C` with all prime factors in `S` ([Evertse 1984](https://doi.org/10.1007/BF01388644)). Its constants depend on `S`; applying it separately to all `P` gives a countable union of finite sets, which can still be infinite. Formula (1) quantifies this dependence weakly but permits unbounded `P` and `C`.

Smooth-number density estimates count *individual integers* below a size cutoff. Even an extremely small density of smooth `x`, `y`, or `z` cannot imply that no solutions occur beyond the cutoff. For example, the powers `2^m` are arbitrarily large despite having one fixed prime factor; the equation, not a density heuristic, is what the fixed-`S` theorem controls. To turn a density count into finiteness one would need a theorem counting **simultaneous primitive perfect-power solutions** uniformly as both the exponent signature and smoothness bound vary. None of the cited results provides this.

The elementary Fermat–Catalan upper bound `R<C^(41/42)` and (2) are compatible for arbitrarily large `C`; this route leaves the central uniform-finiteness obligation unresolved.

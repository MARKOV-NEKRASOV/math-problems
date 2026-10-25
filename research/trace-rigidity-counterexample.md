# Stress test of trace rigidity in the `(2,3,p)` modular route

**Outcome: incomplete.** A precise finite-trace claim suggested by the growing Frobenius window is false, even among primitive positive Frey-shaped curves with `0<j<1728`. The global condition `a²+b³=c^p` is indispensable; at primes below `p`, its reduction is locally too weak to repair this counterexample. A restricted uniform residual-isogeny theorem would finish `(2,3,p)`, but remains unproved.

## A counterexample to height-free finite-trace rigidity

Fix any `Q≥5` and let `M=∏_{5≤q≤Q,\ q\text{ prime}}q`. The fixed CM curve `F=27a1` has integral model `y²+y=x³−7`, which transforms over `Q` by `X=4x`, `Y=8y+4` to `Y²=X³−432`. For each positive `t≡1 (mod 6)`, set

`a=216`, `b=Mt`, `E_t: Y²=X³+3bX−2a=X³+3MtX−432`.

Then `gcd(a,b)=1`, and `a²+b³=46656+(Mt)³>0`. The invariant is

`j(E_t)=1728 (Mt)³/[46656+(Mt)³]`,

so `0<j(E_t)<1728`. Since `gcd(216,Mt)=1`, the numerator and denominator of `b³/(a²+b³)` are coprime; the reduced denominator of `j(E_t)` is `D/gcd(D,1728)`, where `D=46656+(Mt)³>1728`. Therefore `j(E_t)` is nonintegral. Every `E_t` is non-CM, and hence cannot be `Q`-isogenous to the CM curve `F` (CM is preserved by isogeny). Moreover these `j`-values are strictly increasing as `t` grows.

For every prime `5≤q≤Q`, `q|M`, so the displayed integral equation of `E_t` reduces to `Y²=X³−432` modulo `q`, exactly the same equation as the transformed `F`. Because `q∤46656`, both reductions are good. Consequently

`a_q(E_t)=a_q(F)` for every prime `5≤q≤Q`, for infinitely many primitive positive pairs `(a,b)` whose Frey-shaped curves are non-CM and not isogenous to `F`.

In particular, setting `Q=⌊√p−1⌋` for each prime `p` disproves any proposed theorem saying that matching the `27a1` traces only throughout the interval `q<√p−1` forces isogeny **without using the global pth-power equation or an independent bound on curve height/conductor**. This is a logical counterexample to that lemma, not a Fermat–Catalan solution: `46656+(Mt)³` is not asserted to be an integer `p`th power.

## Why small-prime power congruences do not salvage the shortcut

For any prime `q<p`, the exponentiation map `u↦u^p` on `F_q^×` is bijective: `gcd(p,q−1)=1`. Thus whenever `q∤a²+b³`, the congruence `a²+b³≡c^p (mod q)` admits a nonzero `c` automatically. In the family above, all `q≥5` dividing `M` satisfy `a²+b³≡216²≠0 (mod q)`; if `p>Q`, every one of these congruences has a solution for `c`. Thus adding the individual local pth-power condition at all primes in the trace window does not rule out the counterexample family. The compatibility of residues across all primes in the interval follows by the Chinese remainder theorem, but that only gives a modular `c`, not an integer equality `c^p=a²+b³`.

## A mathematically sufficient, explicitly unproved lemma

Here is the actual uniform statement that would close the positive `(2,3,p)` subfamily: there exists an absolute `P` such that for every prime `p>P`, every primitive positive solution `a²+b³=c^p`, every allowed small twist `E_d` of its Frey curve, and every one of the seven FNS comparison curves `F_i`, an isomorphism `E_d[p]≅F_i[p]` implies that `E_d` is `Q`-isogenous to `F_i`. FNS supplies such a residual isomorphism for `p≥11`; this extra implication is a **restricted Frey–Mazur-type theorem**, not established by the trace window.

Why it suffices: each fixed rational isogeny class has finitely many rational `j`-invariants; taking the seven curves and eight twist choices still yields a finite set. Twisting does not change `j`, while for a primitive positive solution `j(E)=1728b³/c^p` and `gcd(b,c)=1`. The denominator of this rational number is `c^p/gcd(c^p,1728)`. Since `c≥2`, it grows without bound as `p→∞`, incompatible with a fixed finite set of `j`-invariants. Therefore the hypothetical lemma would bound `p`; Darmon–Granville would then give finitely many powered triples in `(2,3,p)` across the remaining fixed primes. It would still leave the other all-prime Fermat–Catalan signatures.

The constructed `E_t` does **not** refute this restricted lemma, because it lacks the required global perfect-power identity and residual `p`-torsion isomorphism. It only shows precisely why finite trace data and small-prime congruences cannot replace those global hypotheses. No complete proof or Lean formalization follows.

Sources for fixed-curve model and residual setup: Freitas–Naskręcki–Stoll, arXiv:1703.05058v3, Lemma 2.3 and Proposition 2.4; reviewed project notes `research/review-27a1.md` and `research/trace-window-attempt.md`. The family construction and its checks above are elementary.

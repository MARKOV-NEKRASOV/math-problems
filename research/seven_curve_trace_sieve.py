#!/usr/bin/env python3
"""Independent exact arithmetic check of the seven-curve necessary trace sieve.

From Freitas–Naskrecki–Stoll, Lemma 2.3 and Proposition 2.4, every
primitive nontrivial a^2+b^3=c^p, p>=11 prime, has one comparison
curve F below. For q>=5, q|c, q!=p, its mod-p trace gives
    p | (q+1)^2 - a_q(F)^2.
The script verifies the *necessary* condition only; it does not prove
the equation has (or lacks) solutions.
"""
from math import isqrt

# Curve: y^2 + a1*x*y + a3*y = x^3 + a2*x^2 + a4*x + a6
CURVES = {
    "27a1": (0, 0, 1, 0, -7),
    "54a1": (1, -1, 0, 12, 8),
    "96a1": (0, 1, 0, -2, 0),
    "288a1": (0, 0, 0, 3, 0),
    "864a1": (0, 0, 0, -3, 6),
    "864b1": (0, 0, 0, -24, 48),
    "864c1": (0, 0, 0, 24, -16),
}


def primes_up_to(n):
    for v in range(2, n + 1):
        if all(v % k for k in range(2, isqrt(v) + 1)):
            yield v


def legendre(a, q):
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def trace(curve, q):
    a1, a2, a3, a4, a6 = curve
    # Count roots in y by discriminant: 1 + chi(discriminant)
    return -sum(
        legendre((a1*x+a3)**2 + 4*(x**3+a2*x*x+a4*x+a6), q)
        for x in range(q)
    )


def direct_trace(curve, q):
    a1, a2, a3, a4, a6 = curve
    total = 1  # point at infinity
    for x in range(q):
        rhs = (x**3+a2*x*x+a4*x+a6) % q
        for y in range(q):
            if (y*y+(a1*x+a3)*y-rhs) % q == 0:
                total += 1
    return q + 1 - total


def allowed_exponents_for_output_prime(q):
    if q < 5 or q not in set(primes_up_to(q)):
        raise ValueError("q must be prime >= 5")
    # p=q is excluded from the local trace argument and must be
    # treated separately (even if p>=11).
    out = set()
    for name, c in CURVES.items():
        a = trace(c, q)
        assert a*a <= 4*q, (name, q, a)
        for p in primes_up_to((isqrt(q)+2)**2):
            if p >= 11 and p != q and ((q + 1 - a) % p == 0 or
                                        (q + 1 + a) % p == 0):
                out.add(p)
    return sorted(out)


def main():
    for q in primes_up_to(59):
        if q < 5:
            continue
        for name, curve in CURVES.items():
            assert trace(curve, q) == direct_trace(curve, q), (name, q)
        allowed = allowed_exponents_for_output_prime(q)
        print(f"q={q:2d}: possible p>=11, p!=q = {allowed}")
    assert allowed_exponents_for_output_prime(5) == []
    assert allowed_exponents_for_output_prime(7) == [11]
    assert allowed_exponents_for_output_prime(11) == []
    assert allowed_exponents_for_output_prime(23) == []
    print("Cross-check passed: exact character sums and point counts agree.")
    print("These outputs are NECESSARY exclusions, not sufficient conditions.")


if __name__ == "__main__":
    main()

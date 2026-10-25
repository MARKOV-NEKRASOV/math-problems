#!/usr/bin/env python3
"""Exact 27a1 trace filter for a *necessary* Fermat-Catalan condition.

Does not attempt to solve a^2+b^3=c^p or certify any positive solution.
Applies only if the residual comparison curve is 27a1 and q >= 5, q != p.
"""
from math import isqrt


def primes_under(n: int):
    for v in range(2, n):
        if v < 2 or any(v % k == 0 for k in range(2, isqrt(v) + 1)):
            continue
        yield v


def legendre(u: int, q: int) -> int:
    residue = u % q
    if residue == 0:
        return 0
    return 1 if pow(residue, (q - 1) // 2, q) == 1 else -1


def trace_27a1(q: int) -> int:
    # y^2 + y = x^3 - 7 has discriminant 4*x^3 - 27 in y
    return -sum(legendre(4*x*x*x - 27, q) for x in range(q))


def trace_27a1_by_counting(q: int) -> int:
    count = 1  # infinity
    for x in range(q):
        rhs = (x*x*x - 7) % q
        for y in range(q):
            if (y*y + y - rhs) % q == 0:
                count += 1
    return q + 1 - count


def main():
    print("q  a_q  (q+1-a_q)*(q+1+a_q)   possible p>=11 dividing")
    for q in primes_under(80):
        if q < 5:
            continue
        aq = trace_27a1(q)
        assert aq == trace_27a1_by_counting(q)
        assert aq*aq <= 4*q  # Hasse
        if q % 3 == 2:
            assert aq == 0
        factor = (q+1-aq)*(q+1+aq)
        admissible = [
            p for p in primes_under(factor+1)
            if p >= 11 and p != q and factor % p == 0
        ]
        print(f"{q:2d} {aq:4d} {factor:11d} {admissible}")
    print("Only a necessary sieve for the 27a1 comparison branch.")


if __name__ == "__main__":
    main()

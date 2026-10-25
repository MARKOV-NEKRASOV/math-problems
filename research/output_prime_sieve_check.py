#!/usr/bin/env python3
"""Count F_q-points on the seven curves in FNS, arXiv:1703.05058v3.

The models are those displayed immediately after Lemma 2.3. Each tuple is
(a1, a2, a3, a4, a6) in the general Weierstrass equation
    y^2 + a1*x*y + a3*y = x^3 + a2*x^2 + a4*x + a6.
This direct enumeration needs no computer-algebra package.
"""

CURVES = {
    "27a1": (0, 0, 1, 0, -7),       # y^2 + y = x^3 - 7
    "54a1": (1, -1, 0, 12, 8),      # y^2 + xy = x^3 - x^2 + 12x + 8
    "96a1": (0, 1, 0, -2, 0),       # y^2 = x^3 + x^2 - 2x
    "288a1": (0, 0, 0, 3, 0),       # y^2 = x^3 + 3x
    "864a1": (0, 0, 0, -3, 6),      # y^2 = x^3 - 3x + 6
    "864b1": (0, 0, 0, -24, 48),    # y^2 = x^3 - 24x + 48
    "864c1": (0, 0, 0, 24, -16),    # y^2 = x^3 + 24x - 16
}


def order(model, prime):
    a1, a2, a3, a4, a6 = model
    # The initial 1 is the point at infinity.
    return 1 + sum(
        (y*y + a1*x*y + a3*y - x*x*x - a2*x*x - a4*x - a6) % prime == 0
        for x in range(prime) for y in range(prime)
    )


def prime_factors(number):
    factors = set()
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors


EXPECTED = {
    5: ([6, 3, 4, 10, 7, 4, 8], [6, 9, 8, 2, 5, 8, 4]),
    7: ([9, 9, 12, 8, 11, 11, 7], [7, 7, 4, 8, 5, 5, 9]),
    11: ([12, 15, 8, 12, 9, 18, 14], [12, 9, 16, 12, 15, 6, 10]),
}


for q, expected in EXPECTED.items():
    orders = [order(model, q) for model in CURVES.values()]
    twists = [2 * (q + 1) - n for n in orders]
    assert (orders, twists) == expected, (q, orders, twists)
    admissible = sorted(
        {p for n, tw in zip(orders, twists)
         for p in prime_factors(n * tw) if p >= 11 and p != q}
    )
    print(f"q={q}: orders={orders}; twist orders={twists}; possible p>=11, p!=q: {admissible}")

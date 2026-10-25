# FC-L09 — Lema local: las valuaciones de un primo primitivo no están acotadas

**Estado: demostración elemental mediante Hensel (sujeta a revisión independiente).** Este lema no demuestra Fermat–Catalan; descarta un atajo tentador para cerrar el descenso.

Sea p≥3 un primo impar y q un primo con q≡1 (mod 2p). Elegimos g de orden 2p en F_q^×. Entonces g^p=-1, y el polinomio f(X)=X^p+1 satisface f(g)=0 y f'(g)=p g^(p-1)≠0 (mod q). Por el lema de Hensel, existe un único entero q-ádico α congruente con g módulo q que satisface α^p+1=0 exactamente.

Para cualquier entero t≥1, elijamos un entero positivo a_t que sea congruente con α+q^t módulo q^(t+1). Entonces, como f'(α) es una unidad q-ádica,

    v_q(a_t^p+1)=t.

En efecto, por Taylor en Z_q, f(α+q^t)=f'(α)q^t+sum_{k≥2} binom(p,k)α^(p-k)q^(tk); el primer sumando tiene valuación t y los siguientes al menos 2t, incluso para t=1. La congruencia módulo q^(t+1) preserva la valuación exactamente t. Además gcd(a_t,1)=1 y ord_q(a_t)=2p, así que q es un divisor primitivo de a_t^(2p)-1 situado en a_t^p+1.

**Proposición.** Para cada p primo impar y q≡1 (mod 2p), existen infinitos enteros positivos a, coprimos con 1, tales que q es un divisor primitivo de a^(2p)-1 y v_q(a^p+1)=t para cualquier t prescrito ≥1.

Analogamente para la resta: elegir una raíz g de orden p y elevar desde f(X)=X^p-1 permite v_q(a^p-1)=t para todo t≥1 si q≡1 (mod p); en particular con q≡1 (mod 2p).

## Implicación para la arquitectura de pruebas

Bang–Zsigmondy asegura un primo primitivo q, pero **no** permite deducir que su valuación v_q(a^p±b^p) sea 1 ni que evite múltiplos de t. La pretensión de cerrar a^p±b^p=c^t solo con 'un primo primitivo aparece una vez' queda refutada por estas familias locales. La dificultad global reside en la simultaneidad de las valuaciones y condiciones de todos los primos, no en una raíz simple individual.

**Advertencia:** los enteros a construidos aquí no se afirman soluciones de a^p±1=c^t. El teorema es estrictamente local y sirve como control adversarial del paso S03 del grafo.
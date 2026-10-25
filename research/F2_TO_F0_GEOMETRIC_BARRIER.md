# RESULTADO ESTRUCTURAL F2→F0: BARRERA DE COMPLEJIDAD GEOMÉTRICA

**Estado (25-10-2026):** demostración elemental [revisada independientemente](review-f2-f0-protocol.md). Conder–Young, [arXiv:2410.06571v1](https://arxiv.org/abs/2410.06571v1), registra que el grupo triangular con índices coprimos es perfecto; no se reclama originalidad de esa parte. La [extensión no galoisiana](f2-f0-geometry.md) también fue revisada, con hipótesis estrictas sobre los órdenes completos de monodromía. **No prueba F0 ni Fermat–Catalan.**

## Teorema G: recubrimientos galoisianos de tres puntos con índices coprimos

Sea X→P¹_C un recubrimiento conexo **de Galois**, no trivial, ramificado en exactamente tres puntos con índices de ramificación e1,e2,e3>1 **coprimos dos a dos**. Supongamos que σ=1/e1+1/e2+1/e3<1 y sea G su grupo de monodromía. Entonces:

\[
G=[G,G],\quad e_1e_2e_3\mid |G|,\quad
g(X)=1+\frac{|G|}{2}(1-\sigma)
\ge1+\frac{e_1e_2e_3}{2}(1-\sigma).
\]

En particular, G no puede ser un grupo resoluble no trivial.

**Demostración.** La monodromía alrededor de los tres puntos da generadores g1,g2,g3 de G, de órdenes respectivos e1,e2,e3, con g1*g2*g3=1. En la abelianización de G, la imagen de g1 es el inverso del producto de las imágenes de g2,g3. Por tanto su orden divide simultáneamente e1 y mcm(e2,e3). Como son coprimos, la imagen de g1 es trivial. El mismo argumento vale para g2 y g3; generan G, así que la abelianización es trivial y G es perfecto. Un grupo finito perfecto no trivial no es resoluble. Por Lagrange cada ei divide |G|; su coprimalidad da e1*e2*e3 | |G|. Riemann–Hurwitz para una cubierta galoisiana de tres puntos afirma
\[
2g(X)-2=-2|G|+\sum_i |G|(1-1/e_i)=|G|(1-\sigma).
\]
Los resultados se siguen. QED.

**Corolario F0 (solo firma con índices coprimos).** Si e1=p,e2=q,e3=r son tres primos distintos y m=min(p,q,r), entonces
\[
g(X)\ge1+\frac{m^3}{2}(1-3/m).
\]
Un intento que insista en codificar **exactamente** los tres índices como ramificación de una cubierta de Galois de tres puntos no puede utilizar curvas de género uniformemente acotado cuando m→∞.

**Límite explícito:** no afecta a representaciones de Galois de rango fijo, motivos hipergeométricos, cubiertas no galoisianas o índices de ramificación que no coincidan con p,q,r; tampoco cubre exponentes con factores comunes. Es una herramienta para descartar diseños, no una contradicción diofántica.

Para cubiertas no galoisianas, la [nota de geometría](f2-f0-geometry.md) prueba una barrera distinta de grado bajo órdenes completos coprimos; la fórmula de género anterior sigue siendo solo para la cubierta galoisiana. El motivo hipergeométrico citado en el programa tiene tipos locales `{q,∞,r}`, por lo que esta barrera de tres órdenes finitos no se le aplica directamente.

## Objetivo U: puente cuantitativo suficiente, NO demostrado

Para cualquier solución primitiva no unitaria definamos C=z^r, R=rad(xyz), m=min(p,q,r). Si existieran δ>0 constante y E(m)=o(m log m) **uniformes** tales que para m suficientemente grande
\[
\log C\le ((1-\delta)m/3)\log R+E(m),
\tag{U}
\]
la rama F0 no contendría ninguna sucesión infinita.

**Prueba de la implicación.** Como R≤C^{3/m}, de (U) se obtiene δ log C≤E(m)=o(m log m). La cota Stewart–Yu para abc, combinada con R≤C^{3/m}, da la cota INCONDICIONAL log C≥m(log m-2 loglog m-O(1)) para m→∞; ambas son incompatibles. QED de la implicación. La desigualdad (U) sigue abierta.

## Trabajo nuevo para agentes

1. Estimar dependencia exacta de los conductores/constantes de los motivos F2 al mover el segundo exponente.
2. Controlar simultáneamente grado del campo, discriminante, imagen de Galois y reducción residual.
3. Investigar si un motivo de rango fijo evita la barrera de complejidad demostrada arriba SIN perder información aritmética sobre los tres exponentes.
4. Buscar una desigualdad superior tipo (U), o una alternativa suficiente, sin introducir conjeturas no demostradas.

**Fuentes de partida:** Cazorla García–Villagra Torcomian (2026), DOI 10.1007/s40993-026-00698-2; Chen–Koutsianas (2025), arXiv:2507.15149; teoría clásica de Riemann–Hurwitz y grupos triangulares. No atribuir originalidad sin búsqueda bibliográfica.

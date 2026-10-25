# FC-L08 — Finitud con dos exponentes variables y soporte de salida fijo

**Estado: DEMOSTRACIÓN MATEMÁTICA COMPLETA DEL SUBPROBLEMA, condicionada únicamente a resultados clásicos publicados; pendiente de arbitraje independiente.** No es una demostración de la conjetura de Fermat–Catalan ni una afirmación de originalidad.

## Enunciado

Sea \(\mathcal S\) un conjunto finito de números primos. Existen solamente finitas cuádruplas de enteros positivos \(a,b,c,t\), y primos impares \(p\ge3\), que satisfacen

\[
a^p+b^p=c^t\quad\text{o}\quad a^p-b^p=c^t\;(a>b),\qquad
t\ge2,\quad\gcd(a,b,c)=1,\quad \operatorname{supp}(c)\subseteq\mathcal S.
\]

La palabra «finitas» se aplica a las quíntuplas \((a,b,c,p,t)\), no solo a los valores potenciados: en efecto \(c\ge2\), así que una misma potencia \(c^t\) admite solamente finitas representaciones con \(t\ge2\).

**Relevancia:** la hipótesis permite variar ambos exponentes \(p,t\); no fija \(a,b,c\), ni el número de factores primos de \(c\). Solo fija cuáles son los primos *permitidos*.

### Paso 1. Aislar un primo grande mediante Bang–Zsigmondy

La primitividad implica \(\gcd(a,b)=1\). Para la suma, \(a=b\) obligaría \(a=b=1\) y \(c^t=2\), imposible; podemos entonces intercambiar \(a,b\) para suponer \(a>b\). Si \(p\ge5\), Bang–Zsigmondy aplicado a \(a^{2p}-b^{2p}\) proporciona un primo \(q\) cuyo orden multiplicativo de \(a/b\bmod q\) es exactamente \(2p\): el exponente \(2p\ge10\) evita las excepciones de Zsigmondy. Este primo divide \(a^p+b^p\), pero no \(a^p-b^p\), por la primitividad. En consecuencia,

\[
q\mid c,\qquad 2p\mid q-1.
\]

Para la resta, Bang–Zsigmondy aplicado a \(a^p-b^p\) proporciona \(q\) de orden exactamente \(p\) para \(a/b\bmod q\). Así \(p\mid q-1\), y como \(p\) es impar y \(q\ne2\), también \(2p\mid q-1\).

En cualquiera de las dos orientaciones, si existe una solución con \(p\ge5\), hay un primo \(q\in\mathcal S\) que cumple

\[
\boxed{p\le (\max\mathcal S-1)/2.}
\]

Si \(\mathcal S=\varnothing\) no hay solución, porque \(c^t>1\). El caso \(p=3\) constituye un único valor adicional. **Por tanto, \(p\) recorre un conjunto finito.**

### Paso 2. Finitud para un primo \(p\) fijo y un exponente \(t\) variable

Escribamos \(a^p+\epsilon b^p=c^t\), con \(\epsilon\in\{+1,-1\}\). Como \(p\) es impar, podemos poner \(b'=b\) si \(\epsilon=+1\), y \(b'=-b\) si \(\epsilon=-1\). Entonces

\[
a^p+(b')^p=C=c^t.
\]

Sea \(\mathcal S=\{q_1,\ldots,q_s\}\). Para cada \(q\in\mathcal S\), escribamos
\(v_q(C)=p k_q+e_q\) con \(k_q\ge0\) y \(0\le e_q<p\). Definamos

\[
w=\prod_{q\in\mathcal S}q^{k_q},
\qquad D=\prod_{q\in\mathcal S}q^{e_q}.
\]

Entonces \(C=Dw^p\), donde \(D\) está en un conjunto finito de a lo sumo \(p^{|\mathcal S|}\) valores, y \(w\) está soportado en \(\mathcal S\). Poniendo

\[
u=a/w,\qquad v=b'/w
\]

obtenemos la ecuación

\[
u^p+v^p=D,\qquad u,v\in\mathbb Z[\mathcal S^{-1}].
\]

Para \(D>0\), la curva afín lisa \(u^p+v^p=D\) tiene compactificación lisa geométricamente integral de género \((p-1)(p-2)/2\ge1\). Por el teorema de Siegel sobre puntos \(\mathcal S\)-enteros, tiene un número finito de pares \((u,v)\).

Queda justificar por qué cada par fijo genera solo finitas escalas \(w\). En realidad, a lo sumo una. Para cada \(q\in\mathcal S\), si \(k=v_q(w)\), se cumple

\[
v_q(a)=v_q(u)+k,\qquad v_q(b)=v_q(v)+k.
\]

Como \(\gcd(a,b)=1\), el mínimo de las dos valuaciones es cero, y por tanto

\[
\boxed{k=-\min\{v_q(u),v_q(v)\}.}
\]

Esta fórmula determina \(k\) de forma única para cada \(q\in\mathcal S\), o bien descarta el par si el valor no es un entero no negativo. En consecuencia determina a lo sumo un \(w\), y entonces a lo sumo unos enteros \(a,b,C\). Como \(C\ge2\), existen finitas parejas \(c,t\) con \(c^t=C\). Así hay finitas soluciones para \(p\) fijo.

### Conclusión

El paso 1 permite solo finitos valores de \(p\), y el paso 2 da finitud para cada uno de ellos. Su unión es finita. \(\square\)

## Corolarios y límites

1. Para cualquier \(B\ge2\), hay finitas soluciones primitivas positivas en las dos orientaciones con \(\max\operatorname{supp}(c)\le B\), aunque ambos exponentes varíen. Basta tomar \(\mathcal S=\{q\text{ primo}:q\le B\}\).
2. Toda solución con \(p\ge5\) obliga a que \(c\) contenga un primo \(q\equiv1\pmod{2p}\) y, por tanto, \(P^+(c)\ge2p+1\).
3. Una familia hipotética infinita de soluciones con dos exponentes \(p\) repetidos debe hacer crecer el mayor divisor primo de \(c\). Esto **no** contradice Fermat–Catalan: el conjunto \(\mathcal S\) podría crecer sin límite.
4. El argumento es de **finitud**, no un algoritmo efectivo para enumerar soluciones: Siegel por sí solo no suministra una enumeración práctica general.
5. El lema de soporte fijo del repositorio se refiere a la suma con dos exponentes de entrada fijos. Aquí se prueba también el caso de la **resta**, importante cuando dos potencias con exponente repetido aparecen a lados opuestos de la igualdad.

## Control de errores

- **No** se afirma que un primo primitivo aparezca con valuación 1. Por ejemplo, \(3^5-1^5=242=2\cdot11^2\), y \(11\equiv1\pmod{10}\).
- La excepción de Bang–Zsigmondy en exponente 6 no aplica porque \(2p\ge10\) para \(p\ge5\). El caso \(p=3\) se cubre separadamente por Siegel.
- «Dos exponentes repetidos» no significa que las tres bases sean coprimas por pares *a priori*; esa conclusión se deriva de \(\gcd(a,b,c)=1\) y de la ecuación.

## Bibliografía inicial

- Bang–Zsigmondy: https://mathworld.wolfram.com/ZsigmondyTheorem.html ; https://proofwiki.org/wiki/Zsigmondy%27s_Theorem
- Siegel, finitud de puntos S-enteros: teorema clásico sobre curvas afines de género al menos 1.
- Revisión de generalizadas de Fermat: https://arxiv.org/abs/2507.15149 ; https://www.sciencedirect.com/science/article/pii/S072308692500043X
- Trabajo previo en este repositorio: [fixed-output-support.md](fixed-output-support.md), cuya argumentación usa las curvas \(u^P+v^Q=D\).

**Auditoría pendiente:** otro agente debe revisar el alcance exacto de Bang–Zsigmondy para el signo menos y la reconstrucción de escalas \(w\), sin aceptar esta nota como artículo arbitrado.

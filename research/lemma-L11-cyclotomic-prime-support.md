# FC-L11 — Cota ciclotómica para la cantidad de divisores primos

**Estado: prueba matemática del subproblema, pendiente de revisión independiente; NO prueba Fermat–Catalan ni reivindica prioridad.** Fecha: octubre de 2026.

## Teorema A

Sean a,b>1 enteros coprimos y n≥3 impar. Escribimos ω(m) para la cantidad de primos distintos que dividen m, y τ(n) para la cantidad de divisores positivos de n.

\[
\boxed{\omega(a^n+b^n)\ge\tau(n).}
\]

Si a>b, también vale

\[
\boxed{\omega(a^n-b^n)\ge\tau(n)-{\mathbf1}_{a-b=1}.}
\]

### Prueba para la suma

Podemos suponer a>b porque gcd(a,b)=1 y a,b>1. Para cada divisor d>1 de n, aplicar Bang–Zsigmondy a a^(2d)-b^(2d). Como d es impar y d≥3, el exponente 2d≥6 evita todas las excepciones: en exponente 6 la única pareja excepcional es (a,b)=(2,1), descartada por b>1. Así existe un primo q_d cuyo orden multiplicativo de a/b módulo q_d es exactamente 2d. En particular q_d∤ab, q_d es impar, (a/b)^d≡−1 (mod q_d), y q_d|a^d+b^d|a^n+b^n (porque n/d es impar).

Los q_d para d>1 son todos distintos: sus órdenes 2d son diferentes. Además a+b>1 tiene un divisor primo q_1, y q_1 es distinto de todos los q_d porque el orden de a/b módulo q_1 es como máximo 2, mientras el de q_d es 2d≥6. Tenemos un primo distinto por cada divisor positivo d de n, esto es τ(n). QED.

### Prueba para la diferencia

Para cada divisor d>1 de n, ahora aplicar Zsigmondy a a^d-b^d. Puesto que d es impar, d≥3, no hay excepciones y se obtiene un primo primitivo r_d de orden exactamente d, divisor de a^d-b^d y de a^n-b^n. Los primos son distintos. Si a-b>1, cualquier primo r_1 que divide a-b posee orden 1 y es distinto de los anteriores: ω≥τ(n). Si a-b=1 falta esa contribución y ω≥τ(n)−1. QED.

## Corolarios exactos

**B1 — Restricción uniforme sobre la factorización del exponente.** Si a^n+b^n=c^t, con a,b>1, gcd(a,b)=1, t≥2 y n impar≥3, entonces τ(n)≤ω(c). Si a^n−b^n=c^t, a>b>1, entonces τ(n)−1_{a-b=1}≤ω(c). Estas desigualdades son independientes de las magnitudes de los primos de c.

Si n=∏ l_i^(e_i), τ(n)=∏(e_i+1). Por consiguiente, si ω(c)=s, en la suma n puede tener a lo sumo floor(log₂ s) factores primos distintos y cada multiplicidad e_i≤s−1. NO acota el tamaño de los primos l_i.

**B2 — Soporte primo total tres.** Consideremos A+B=C de Fermat–Catalan, con bases x,y,z>1, gcd(x,y,z)=1 y ω(ABC)=3. Por la ecuación, las bases son coprimas dos a dos; cada una debe estar soportada en exactamente un primo, y los tres primos son distintos. Uno es 2, pues exactamente uno de A,B,C es par.

Supongamos que dos exponentes tienen el mismo valor impar n≥3.

- Si las potencias de exponente n están sumando en el lado izquierdo, escribimos a^n+b^n=c^t. La base c es una potencia de un único primo: ω(c)=1. Pero τ(n)≥2, contradicción. **Esta rama no tiene soluciones**.
- Si esos dos exponentes aparecen a lados opuestos, reordenamos como a^n−b^n=c^t, a>b>1. La base c sigue siendo potencia de un único primo, así que 1=ω(c)≥τ(n)−1_{a-b=1}. Para n impar≥3, τ(n)≥2, y necesariamente a−b=1 y τ(n)=2. Por tanto, **n es un primo impar** y **a,b son potencias de primos consecutivas**. Uno de a,b es una potencia de 2.

Si los exponentes internos de ambas potencias de primos son ≥2, el teorema de Mihăilescu sobre potencias perfectas consecutivas fuerza {a,b}={8,9}. De lo contrario, al menos una de estas dos bases es un primo.

**Esta reducción NO cierra Fermat–Catalan:** por ejemplo 8³−7³=13² es una solución de la ecuación residual, pero la firma (3,3,2) no es hiperbólica. Una familia hiperbólica superviviente con primo n≥5 y exponente t≥3 requiere un teorema adicional.

## Subproblema FC-S10 para los agentes

Investigar la finitud de las soluciones primitivas positivas

\[
a^p-b^p=c^t,\quad a=b+1,\quad p\ge5\text{ primo},\quad t\ge3,
\]

donde a,b,c son potencias de tres primos distintos, uno de a,b es una potencia de 2, y c es una potencia de un primo distinto. Separar (i) cuando uno de a,b es un primo impar, (ii) cuando {a,b}={8,9}. Verificar por separado la exclusión de t=2 por Bennett–Skinner antes de considerarla eliminada en cualquier argumento global.

## Falsadores y límites

- No inferir que q_d aparezca con valuación 1: Hensel permite valuaciones arbitrarias (ver lemma-L09-hensel-primitive-valuations.md).
- No permitir bases unidad: el caso 1³+2³=3² muestra una excepción.
- No concluir una cota sobre n a partir de τ(n) acotada: n podría ser arbitrariamente primo.
- La cota para diferencias exige a>b y coprimalidad. El teorema de Mihăilescu se usa únicamente para bases que SON potencias perfectas internas con exponentes ≥2.

## Fuentes

Bang–Zsigmondy y excepciones: https://proofwiki.org/wiki/Zsigmondy%27s_Theorem y https://mathworld.wolfram.com/ZsigmondyTheorem.html .
Mihăilescu: teorema de Catalan sobre potencias perfectas consecutivas.
Bennett–Skinner: https://doi.org/10.4153/CJM-2004-002-2 .

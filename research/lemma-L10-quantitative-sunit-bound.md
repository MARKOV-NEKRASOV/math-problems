# FC-L10 — Cota cuantitativa de Evertse para cualquier firma y exponente

**Estado: derivación rigurosa a partir de un teorema publicado; alcance exacto = soporte primo S fijado.** No resuelve Fermat–Catalan.

## Enunciado

Sea \(S\) un conjunto finito de \(s\) primos racionales. Denotemos por \(\mathcal F(S)\) las ternas **distintas de valores potenciados**
\((A,B,C)=(x^p,y^q,z^r)\), con \(x,y,z>0\), \(p,q,r\ge2\),
\(\gcd(x,y,z)=1\), \(A+B=C\), \(1/p+1/q+1/r<1\) y todos los divisores primos de \(ABC\) pertenecientes a \(S\).

Entonces

\[
\boxed{\#\mathcal F(S)\le 3\cdot7^{\,2s+3}.}
\]

La cota **no depende de qué primos** componen S, ni de las bases, de los exponentes, de las firmas ni de la altura C. La cota es deliberadamente muy poco ajustada.

## Demostración

Como \(\gcd(x,y,z)=1\) y \(x^p+y^q=z^r\), todo primo que divide dos de \(x,y,z\) dividiría el tercero; luego los tres son coprimos dos a dos. Igual ocurre para sus potencias \(A,B,C\).

Pongamos

\[
u=A/C,\qquad v=B/C.
\]

Entonces \(u+v=1\) y \(u,v\in\mathbb Z[S^{-1}]^\times\), pues numeradores y denominadores solo contienen primos de S. El teorema cuantitativo de Evertse (1984) establece que esta ecuación de S-unidades racionales posee a lo sumo \(3\cdot7^{3+2|S|}\) soluciones ordenadas \((u,v)\). La presentación de este límite exacto figura en R. von Känel, *Integral points on moduli schemes of elliptic curves*, §7.2, citando [Evertse, Theorem 1].

El mapa \((A,B,C)\mapsto(A/C,B/C)\) es inyectivo entre ternas primitivas: en efecto \(\gcd(A,C)=1\), por lo que el denominador reducido de \(u=A/C\) es exactamente \(C\); recuperamos C del denominador de u, y luego A=uC y B=vC. Por tanto, el número de ternas candidatas (y a fortiori el de Fermat–Catalan) es como máximo el número de soluciones S-unitarias indicado. QED.

## Corolario elemental y nivel de cuantificadores

Si todas las bases \(x,y,z>1\), los tres soportes primos son no vacíos y disjuntos; en particular \(\omega(ABC)\ge3\). Cuando \(\omega(ABC)=3\), cada una de las tres bases es potencia de **un primo distinto**. Eso crea un subproblema bien definido de **tres bases primo-potencia**, con los tres primos permitidos a variar.

**Importante: NO se deduce finitud global para \(\omega(ABC)\le s\)**, porque existen infinitos conjuntos posibles S con \(|S|\le s\). La cota por conjunto se puede aplicar a cada uno, pero la unión sobre infinitos conjuntos podría ser infinita. Tampoco establece una cota para C independiente de S.

## Nuevo subproblema abierto S09

Probar o refutar la siguiente afirmación más débil que Fermat–Catalan:

«Para cada entero fijo s, hay solo finitas ternas de Fermat–Catalan con \(\omega(ABC)\le s\), aunque los propios primos cambien.»

Ni Evertse, ni la cota del presente lema, ni el simple hecho de que cada firma fija tenga finitas soluciones demuestran esta afirmación. Resolver el caso s=3 sería ya un resultado interesante: toda terna no unitaria en ese caso tiene las formas \(A=\ell^{k_1}, B=m^{k_2}, C=n^{k_3}\), con \(\ell,m,n\) primos distintos y los exponentes compuestos sujetos a las firmas hiperbólicas.

**Puente necesario:** una herramienta que haga *escapar* o controle conjuntamente la cantidad de soportes S variables admisibles, no solo sus soluciones por separado.

## Referencias

- J.-H. Evertse, *On equations in S-units and the Thue–Mahler equation*, Invent. Math. 75 (1984), 561–584, DOI: https://doi.org/10.1007/BF01388644.
- R. von Känel, *Integral points on moduli schemes of elliptic curves*, Transactions of the London Mathematical Society 1 (2014), §7.2: https://academic.oup.com/tlms/article/1/1/85/2841113 (reproduce \(3\cdot7^{3+2|S|}\)).
- I. E. Shparlinski and C. L. Stewart, *Counting solvable S-unit equations*: https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/countingsunitsr.pdf (también resume una versión cuantitativa).

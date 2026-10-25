# FC-S09 — Prueba cuantitativa por soporte de radical y un obstáculo de uniformidad

**Estado: parcial, con teoremas demostrados y puente abierto explícito.**

## Resultado demostrado

Sea B≥2, y π(B) el número de primos racionales ≤B. Entre todas las ternas de Fermat–Catalan primitivas positivas, hay a lo sumo

    3 · 7^(3+2π(B))

ternas distintas cuya mayor prima divisora del producto ABC es ≤B, independientemente de los exponentes. Esto es aplicación inmediata de FC-L10 tomando S={primos≤B}, sin necesidad de fijar las firmas. La cota puede ser inmensa, pero es finita y **explícita**.

Más aún, para cada s fijo y cada conjunto S de s primos, hay ≤3·7^(3+2s) ternas; el lado derecho no depende del tamaño de los primos de S. **Esto no implica** que exista una cota solo en función de s para todas las ternas cuyo soporte tenga cardinal s: los conjuntos S son infinitos.

## Subproblema que abrir

**S09(a):** Probar que para cualquier s fijo hay finitas ternas hiperbólicas primitivas con ω(ABC)≤s, permitiendo mover los primos. Incluso s=3 sería un avance restringido significativo. Por la coprimalidad dos a dos, si x,y,z>1 entonces ω(ABC)≥3, y ω=3 exige una potencia de primo distinta en cada una de las tres coordenadas.

**S09(b):** Para s=3, ¿puede una construcción multi-Frey o el teorema de divisores primitivos imponer una relación adicional entre los *tres primos base* que contradiga una familia infinita con exponentes variables? La cota de Evertse por S no sirve para relacionar conjuntos S diferentes.

**S09(c):** Reducir el problema a los casos donde los tres exponentes primos mínimos crecen o a una firma de entrada fija, según la partición del DAG. Formular límites efectivos específicos por escenario, nunca inferirlos automáticamente de Siegel.

## Método de falsación

Para cualquier afirmación sobre un divisor primitivo q y la valuación v_q, probar contra FC-L09: el levantamiento de Hensel permite valuaciones arbitrarias para un primo primitivo dado. Exigir explícitamente un argumento global adicional.

## Fuente

R. von Känel (2014), reproduciendo la cota de Evertse para S-unidades: https://academic.oup.com/tlms/article/1/1/85/2841113

FC-L10: [lemma-L10-quantitative-sunit-bound.md](lemma-L10-quantitative-sunit-bound.md).
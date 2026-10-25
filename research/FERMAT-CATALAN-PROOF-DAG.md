# Fermat–Catalan: mapa de lemas, dependencias y subproblemas

**Estado: conjetura abierta.** Los nodos ROJO siguen sin demostración. Los nuevos lemas AMARILLO requieren revisión independiente antes de incorporarse como resultados firmes. Actualizado: octubre 2026.

## Objetivo
Demostrar que existen finitas ternas distintas (A,B,C)=(x^p,y^q,z^r) primitivas positivas, con A+B=C, p,q,r≥2 y 1/p+1/q+1/r<1. Contar ternas de potencias, no representaciones redundantes.

## Inventario de resultados y dependencias

| Nodo | Estado | Contenido | Depende de |
|---|---|---|---|
| L01 | VERDE | A,B,C son coprimos dos a dos | ecuación y primitividad |
| L02 | VERDE | R=rad(ABC)≤xyz<C^σ; σ≤41/42 | L01 y desigualdad hiperbólica |
| L03 | VERDE | Finitud para cada firma fija | Darmon–Granville |
| L04 | VERDE según fuentes del repo | Reducción a firmas primas + 19 firmas compuestas fijas + (2,4,l) | optimized-signatures.md |
| L05 | VERDE según fuentes del repo | Familia (2,4,l) contribuye finitas ternas | Bennett–Skinner, Ellenberg, L03; revision de orientaciones |
| L06 | VERDE | Una familia infinita restante tiene mayor exponente primo divergente y R<C^(5/6+o(1)) | L03–L05 |
| L07 | VERDE | Finitud con dos exponentes de entrada fijos y soporte de salida S fijo | fixed-output-support.md, Siegel |
| L08 | AMARILLO | Finitud de a^p±b^p=c^t con p,t variables, p≥3 primo impar, supp(c)⊆S fijo | Bang–Zsigmondy + Siegel; lemma-L08-variable-repeated-primes-fixed-support.md |
| L09 | AMARILLO | En a²+b³=c^p, p≥11, cada q≥5 que divide c satisface p≤(sqrt(q)+1)² | FNS + Tate + Hasse; prime-output-trace-sieve.md |
| L10 | AMARILLO | Para q≥5 fijo, hay finitas soluciones a²+b³=c^p con q|c | L03 y L09 |
| L11 | VERDE | Una familia infinita admite subsucesión con dos exponentes fijos, uno fijo, o ninguno fijo | L03 y extracción sucesiva |
| L12 | VERDE | h(j(E))=6 log C+O(1), N(E)≤K rad(ABC) para Frey universal | full-height-conductor.md |
| L13 | ROJO | Finitud uniforme con dos exponentes primos fijos y tercero móvil, sin soporte fijo | nuevas técnicas |
| L14 | ROJO | Finitud con un solo exponente primo fijo, otros dos móviles | nuevas técnicas |
| L15 | ROJO | Finitud cuando los tres exponentes primos crecen | nueva desigualdad global o descenso |
| FC | META | Fermat–Catalan | L04–L05 y cierre completo L13–L15 |

## Diagrama dirigido (Mermaid)

~~~mermaid
flowchart TD
 FC[Conjetura Fermat–Catalan] --> RED[L04 reducción de firmas]
 RED --> FIX[19 firmas compuestas fijas]
 RED --> VAR24[Firma variable 2-4-primo]
 RED --> PRIME[Unión de firmas primas]
 FIX --> DG[L03 Darmon–Granville]
 VAR24 --> EE[L05 Bennett–Skinner y Ellenberg]
 PRIME --> CONTR[Suponer infinitas ternas]
 CONTR --> ESC[L06 exponente máximo diverge]
 ESC --> TRI{L11 partición de subsucesiones}
 TRI --> F2[L13: dos exponentes fijos]
 TRI --> F1[L14: un exponente fijo]
 TRI --> F0[L15: ninguno fijo]
 F2 --> SUP[L07–L10: soporte primo y trazas locales]
 F1 --> MULTI[Multi-Frey: puente abierto]
 F0 --> HEIGHT[L12: altura/conductor; cota superior abierta]
 F2 --> CIERRE[Cierre uniforme de tres ramas]
 F1 --> CIERRE
 F0 --> CIERRE
 CIERRE --> NEG[Contradicción]
 NEG --> FC
 classDef closed fill:#d8f3dc,stroke:#208453,color:#111;
 classDef open fill:#ffe0e0,stroke:#af3333,color:#111;
 class DG,EE,FIX,VAR24,RED,ESC,TRI closed;
 class F2,F1,F0,CIERRE,MULTI,HEIGHT open;
~~~

Las flechas salientes de FC indican descomposición del objetivo, NO una prueba circular. La dirección de la demostración sería demostrar cada rama abierta y regresar desde CIERRE.

## Tres escenarios exhaustivos para intentar reducción al absurdo

Ordenar los exponentes primos u≤v≤w. Por L03, en una secuencia infinita de ternas distintas debe tender w a infinito (con selección apropiada). Tras pasar a subsucesión:

**F2**: u,v fijos, w→∞. Entonces R≤C^(1/u+1/v+o(1)) y el caso más débil es (u,v)=(2,3), pendiente de finitud uniforme.

**F1**: u fijo; v,w→∞. Entonces R≤C^(1/u+o(1))≤C^(1/2+o(1)).

**F0**: u,v,w→∞. Entonces R≤C^o(1) y h(j)/log N(E)→∞. Una cota de pendiente finita para esta familia especial de curvas bastaría para cerrar F0, pero NO está probada.

En todos los casos la cota universal hipotética h(j(E))≤(36/5−δ)log N(E)+O(1), con δ>0, bastaría para una contradicción junto a L06. NO debe introducirse como lema demostrado: puede requerir ideas de fuerza abc/Szpiro.

## Subproblemas inmediatos y criterios de éxito

| ID | Experimento matemático | Éxito verificable |
|---|---|---|
| S01 | Auditar completamente la prueba L08, incluyendo la resta y el caso p=3 | referee sin lagunas |
| S02 | Pasar de q fijo a un divisor q variable acotado por alguna función del exponente p | desigualdad global que domine L09 |
| S03 | En a^p±b^p=c^t, usar Zsigmondy y analizar v_q para q≡1 mod 2p | lema uniforme con valuaciones, probado sin asumir que son 1 |
| S04 | Construir dos objetos de Frey para controlar p y t simultáneamente | contradicción de trazas/inercia de teoremas existentes |
| S05 | Buscar cota altura/conductor *especial* para exponente mínimo divergente | pendiente absoluta K<∞ sobre las curvas relevantes |
| S06 | Extender Siegel de soporte primo fijo a soporte con cardinal acotado pero primos móviles | teorema uniforme, no simple reformulación de Siegel |
| S07 | Revisar literatura 2025–26 sobre firmas primas distintas y repetidas | enunciados y excepciones auditados en original |

## Protocolos de colaboración

Agente A: constructor y búsqueda de lemas. Agente B: adversario que intenta construir contraejemplos. Agente C: fuentes (signos, coeficientes, hipótesis y bibliografía). Agente D: integrador del grafo. Un subproblema no asciende a VERDE sin demostración y revisión independiente. Los resultados que dependan de abc, Frey–Mazur, GRH o de preprints sin auditar deben etiquetarse CONDICIONAL o NO VERIFICADO.

Prioridad operativa: S01, luego S03 sobre el mismo primo primitivo, y S05 para el escenario F0. Formalización Lean de FC pospuesta hasta encontrar una demostración matemática completa, según AGENTS.md.
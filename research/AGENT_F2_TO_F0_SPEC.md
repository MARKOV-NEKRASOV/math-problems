# ESPECIFICACIÓN DE AGENTES — PROGRAMA F2 → F0 PARA FERMAT–CATALAN

Versión 1.0 (2026-10-25). **Protocolo de investigación. NO es una demostración de Fermat–Catalan.**
**Lectura obligatoria:** AGENTS.md, este archivo, research/LITERATURE_WATCH_F2_F0.md, research/F2_TO_F0_GEOMETRIC_BARRIER.md, research/bounds-and-priorities.md.

## 1. Objetivo y cuantificadores

Probar la finitud de las ternas **distintas de valores potenciados** (A,B,C)=(x^p,y^q,z^r), A+B=C, con x,y,z enteros positivos, gcd(x,y,z)=1, p,q,r enteros ≥2 y
\[
\sigma=1/p+1/q+1/r<1.
\]
Tratar bases unitarias por separado. Cambiar el exponente de 1 no crea una terna distinta. Las reducciones a exponentes primos solo se usan con cobertura de excepciones rigurosamente verificada.

**Las siete ramas de cualquier hipotética familia infinita:**
- F2-PQ: p,q fijos; r→∞.
- F2-PR: p,r fijos; q→∞.
- F2-QR: q,r fijos; p→∞.
- F1-P: p fijo; q,r→∞.
- F1-Q: q fijo; p,r→∞.
- F1-R: r fijo; p,q→∞.
- F0: p,q,r→∞.

Darmon–Granville garantiza finitud por cada firma completamente fija. Todas las siete obligaciones de uniformidad siguen ABIERTAS. Ninguna prueba para una firma aislada las cierra automáticamente.

## 2. Mandato estratégico: F2 como laboratorio para F0

Cada agente debe contestar: ¿qué parte de la técnica permanece válida cuando los otros exponentes, inicialmente fijos, también crecen?

La meta es una **cota superior** de altura, calidad, conductor o exponente que IMPLIQUE finitud; aumentar cotas inferiores sin un upper bound incompatible no basta.

Denotemos C=z^r, R=rad(xyz), m=min(p,q,r). Siempre R≤C^\sigma.

**Umbral F2:** para cada pareja fija admisible a,b, bastaría obtener para todos sus casos una desigualdad
\[
C\le K_{a,b}R^{\kappa_{a,b}},\qquad
\kappa_{a,b}<\frac{ab}{a+b}.
\]
Se permite que K dependa solo de a,b, nunca de las bases o del tercer exponente.

**Umbral F1:** para cada exponente fijo a, bastaría
\[
C\le K_a R^{\kappa_a},\qquad \kappa_a<a,
\]
uniformemente cuando los otros dos exponentes varían.

**Umbral F0:** bastaría demostrar para m grande, con δ>0 absoluto y E(m)=o(m log m),
\[
\log C\le\frac{(1-\delta)m}{3}\log R+E(m).
\]
La combinación R≤C^{3/m} y la cota inferior de Stewart–Yu \(\log C\ge m(\log m-2\log\log m-O(1))\) produciría una contradicción. **La desigualdad superior propuesta NO está demostrada**; solo está demostrada su suficiencia. Puede sustituirse por otro cierre riguroso de F0.

**Puente F2→F0 obligatorio:** llevar registro explícito de la dependencia de cada constante en a,b, grado del campo base, discriminante, género, dimensión del motivo, nivel, conductor y restricciones de modularidad. No presentar una estimación válida para dos exponentes fijos como uniforme para exponentes que crecen.

## 3. Agentes especializados

**A — Geometría y modularidad.** Diseñar y analizar curvas, jacobianas, motivos hipergeométricos y representaciones. Calcular conductor local/residual, inercia, torsión, imagen y comparación de trazas. Probar cuándo la nueva construcción no es una mera torsión o isogenia de una ya conocida. Estudiar las fórmulas 2026 de Cazorla García–Villagra Torcomian para firmas (2,r,p) y (q,r,p). Señalar hipótesis de modularidad o imagen grande NO conocidas.

**B — Desigualdades, cotas y contraejemplos.** Explorar radical, altura, calidad, exponentes, soporte, S-unidades, valuaciones, gap entre bases y degeneración de constantes al crecer a,b. Proponer cota precisa antes de intentar una prueba. Buscar contraejemplos y desigualdades mal orientadas.

**C — Bibliografía permanente.** Buscar **NUEVA literatura al comenzar Y al concluir CADA CICLO**, tanto trabajos contemporáneos como clásicos; seguir referencias hacia atrás y hacia adelante. Ver research/LITERATURE_WATCH_F2_F0.md. Buscar sistemáticamente resultados que refuten o ya contengan nuestras ideas, cambios de versiones, erratas, y fuentes sobre uniformidad. Proponer conexiones autónomas y a petición de A/B. Indexar en data/papers.sqlite3 con estado de lectura verificable. Nunca inventar citas o teoremas.

**D — Revisión adversarial e integración.** Reproducir cada cálculo, buscar hipótesis omitidas, verificar fuentes primarias, comprobar límites de aplicación y mantener actualizado el grafo de dependencias y la matriz de siete ramas. Nadie aprueba su propia prueba. Si no existen agentes independientes en el entorno, realizar revisiones secuenciales indicando explícitamente que NO equivalen a arbitraje independiente.

## 4. Ficha obligatoria de cada lema o experimento

- ID; enunciado exacto con todos los cuantificadores; rama(s) afectadas.
- Estado: PROBADO / CONDICIONAL / CONJETURA / REFUTADO / INCOMPLETO.
- Fuentes: DOI/arXiv y versión, página/teorema, hipótesis, lectura (metadatos, resumen, enunciado original, prueba original).
- Prueba detallada o fallo preciso; scripts reproducibles y pruebas adversariales.
- **Cota anterior → nueva cota → distancia matemática exacta al umbral suficiente.**
- Dependencia en exponentes fijos, bases, soporte, campos y constantes.
- Qué aporta a F1/F0 y qué NO aporta; revisión independiente.
- Siguiente subproblema, criterio falsable de éxito y recomendación de abandonar o continuar la línea.

**No admisible:** contar congruencias locales como igualdad global, inferir soporte fijo de cardinal acotado, inferir finitud de una mera cota inferior, aceptar hipótesis abc/GRH/Frey–Mazur/modularidad no establecida como teoremas, o afirmar cierre de F0 por resolver casos parciales. El objetivo es la finitud de las siete ramas y no la suma de ejemplos.

## 5. Cola inicial de trabajo

A1: auditar uniformidad del conductor residual de Frey hipergeométrico al variar los exponentes; distinguir el grado del campo de definición y la dimensión del motivo.

B1: encontrar para una firma F2 una cota **superior** explícita y calcular cómo crecen sus constantes al variar los otros exponentes.

C1: leer Cazorla García–Villagra Torcomian (2026), Chen–Koutsianas (2025) y trabajos de Golfieri/Pacetti; descubrir literatura adicional mediante sus referencias y artículos 2025–2026. Mantener vigilancia en cada ciclo.

D1: auditar la barrera para recubrimientos galoisianos de tres puntos con índices coprimos; examinar si una construcción propuesta evita esa barrera de manera válida.

Criterio para avanzar a F0: demostrar una desigualdad realmente uniforme en todos los exponentes crecientes, con constantes y dependencias auditadas. Si no se consigue, entregar informe técnico que identifica el eslabón matemático ausente.

## 6. Artefactos y gobernanza

Por ciclo: reporte de fuentes nuevas/auditadas, al menos un sublema demostrado o falsado, tabla de cotas y su impacto, siete estados de ramas y siguiente objetivo. Registrar resultados y procedencia en los catálogos del repositorio. Consultar el CLI --help de catalog.py y papers.py para usar sus esquemas reales; preservar integridad y versiones. Preferir commits agrupados y revisión previa a fusionar.

**Lean:** posponer formalización de Fermat–Catalan hasta obtener una prueba matemática completa auditada; el usuario mantiene esa preferencia.

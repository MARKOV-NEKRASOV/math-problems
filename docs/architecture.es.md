# Especificación de arquitectura de agentes Codex para resolver problemas matemáticos con Lean

Versión 1.0 · 23 de octubre de 2026 · Estado: diseño para implementación; no es un sistema implementado ni evaluado.

## 1. Misión y contrato de honestidad

Recibir un problema matemático, determinar con precisión qué se pide, buscar una solución y entregar una demostración de su formalización en Lean 4. Si no se consigue una solución verificada, devolver un error explicado y conservar los avances útiles.

La misión compartida es resolver el problema. Formalizar, construir y ampliar su propia base de papers, experimentar, buscar contraejemplos y revisar son tareas instrumentales de esa misión. Cada ejecución recibe una responsabilidad concreta y acotada. La base bibliográfica se inicia vacía y la construyen los agentes: el usuario no tiene que prepararla ni mantenerla.

**Regla principal:** solamente el servicio de verificación puede emitir `SUCCESS`. Un agente puede proponer una prueba, pero no certificarla por su cuenta. La unanimidad de agentes no sustituye evidencia formal.

**Condiciones de trabajo:** reconocer un bloqueo, solicitar ayuda o informar un fallo son conductas correctas. No se utilizarán mensajes como «tenés que resolverlo a cualquier costo», rankings individuales, sanciones por error ni reintentos ilimitados. Los límites de recursos administran la ejecución; no constituyen una amenaza ni una evaluación personal.

Ninguna arquitectura puede garantizar resolver cualquier problema matemático. El problema puede ser falso, ambiguo, demasiado difícil para los recursos disponibles o no demostrable en los fundamentos elegidos. Un fallo de búsqueda no establece falsedad ni independencia lógica.

## 2. Definición de resultado válido

Para una proposición formal `P`, el resultado de demostración debe incluir un término `p : P` aceptado mediante el procedimiento de verificación acordado. Formalizar únicamente el enunciado no alcanza.

La aceptación exige simultáneamente:

1. Correspondencia revisada entre el pedido original y `P`.
2. Coincidencia entre el enunciado verificado y el contrato formal congelado.
3. Prueba completa y dependencias aceptadas por el verificador.
4. Dependencias axiomáticas incluidas en la política autorizada.
5. Reproducción desde fuentes y versiones identificadas.
6. Informe que identifique exactamente el problema demostrado.

Lean verifica el enunciado formal; no certifica por sí mismo que una traducción desde lenguaje natural sea fiel. La revisión semántica sigue siendo una capa distinta y falible. El usuario debe poder inspeccionar siempre la formalización y su traducción al lenguaje matemático habitual.

Para pedidos de demostración, una refutación de `P` se devuelve como `ERROR / STATEMENT_REFUTED`, acompañada de prueba formal de `¬P` o de un contraejemplo con su propiedad verificada. Para pedidos abiertos como «determinar si P es cierto», tanto demostrar `P` como demostrar `¬P` pueden cumplir el pedido; esta modalidad debe fijarse en la entrada.

## 3. Componentes y responsabilidades

El sistema combina un controlador convencional, agentes Codex especializados por tarea y un servicio de verificación separado.

| Componente | Responsabilidad | Producto | Restricción |
|---|---|---|---|
| Controlador | Administrar cola, estados, dependencias, recursos y entregas | Registro de ejecución | No decide verdad por plausibilidad |
| Formalizador | Traducir el problema y documentar su significado | Contrato formal y diccionario | No agrega hipótesis para facilitar una prueba |
| Auditor semántico | Revisar la traducción desde el pedido original | Informe de correspondencia | Revisión inicial independiente del plan de prueba |
| Planificador matemático | Buscar resultados existentes y proponer rutas | Plan y grafo de obligaciones | No cuenta lemas propuestos como demostrados |
| Investigador bibliográfico | Construir y ampliar la base de papers según los problemas | Fuentes, metadatos, resultados extraídos y relaciones | No inventa referencias ni convierte bibliografía en pruebas aceptadas |
| Demostradores | Resolver obligaciones en Lean y producir candidatos | Fuentes, pruebas y bloqueos | No modifican el contrato congelado |
| Revisor matemático | Examinar candidatos, buscar errores y contraejemplos | Observaciones y candidatos de refutación | No puede otorgar `SUCCESS` |
| Verificador | Comparar objetivo, comprobar pruebas y auditar axiomas | Certificado y diagnóstico | No ejecuta instrucciones del candidato fuera del aislamiento |

Son roles, no procesos que deban mantenerse activos permanentemente. El formalizador puede pasar a planificar después de congelar el contrato. La auditoría semántica y la revisión final deben realizarse en sesiones distintas de la sesión autora del artefacto revisado. Esa separación reduce contaminación de contexto; no garantiza independencia estadística si se usa la misma familia de modelos.

**Configuración inicial propuesta:** dos demostradores concurrentes como máximo, un auditor o revisor bajo demanda y un controlador sin LLM. Empezar con un demostrador cuando el problema parezca directo. Aumentar la concurrencia solamente si hay rutas diferentes u obligaciones realmente independientes.

No crear un agente por rama de la matemática, ni una jerarquía recursiva de supervisores. La especialización temática se incorpora mediante contexto, herramientas y bibliografía pertinentes a cada tarea.

## 4. Entrada y contrato matemático

La entrada mínima es el texto íntegro del problema. El controlador completa un registro con:

- Identificador del problema y texto original inmutable.
- Modalidad: demostrar, construir, calcular con prueba, o determinar verdadero/falso.
- Dominios, hipótesis, definiciones, cuantificadores y conclusión.
- Restricciones expresadas por el usuario: métodos admitidos, bibliotecas y fundamentos.
- Recursos de ejecución y criterio de detención.
- Referencias aportadas, con procedencia.

El formalizador produce `formalization.md`, un módulo con las definiciones y un desafío formal de confianza. El informe debe vincular cada hipótesis formal con una parte del texto original y explicar elecciones como `ℕ`, `ℤ`, `ℚ`, `ℝ`, finitud o no nulidad.

El auditor recibe primero el pedido original y la traducción propuesta, sin la estrategia de prueba. Comprueba dominios, orden de cuantificadores, hipótesis omitidas o añadidas, condiciones de borde, coerciones, operaciones, notación e instancias relevantes. También inspecciona definiciones referidas por el enunciado.

Se permiten decisiones rutinarias documentadas. Una ambigüedad que cambie el problema produce `ERROR / AMBIGUOUS_STATEMENT` con una pregunta específica; no se elige silenciosamente la variante más fácil. Si hay varias lecturas, se pueden preparar alternativas claramente identificadas sin presentarlas como equivalentes.

Ejemplos de errores que esta fase debe detectar:

- Sustituir enteros por naturales y cambiar el significado de la resta.
- Probar `∀x, ∃y, R x y` cuando se pidió `∃y, ∀x, R x y`.
- Agregar diagonalizabilidad para demostrar una afirmación sobre matrices arbitrarias.
- Transformar «demostrar P» en «suponiendo P, demostrar P».
- Introducir hipótesis contradictorias y obtener una conclusión vacía.

No existe una comprobación general automática de consistencia de hipótesis. Se revisa su correspondencia con el pedido y, cuando resulte útil, se construyen ejemplos que las satisfagan.

Una vez revisado, se congela el contrato: texto original, enunciado elaborado, definiciones relevantes, dependencias, nombres de objetivos y política de axiomas. Los demostradores no pueden modificarlo. Si se descubre un error de traducción, se crea una revisión explícita y se invalidan los resultados que dependan de la versión anterior.

## 5. Flujo de resolución

### 5.1 Preparación

Crear el entorno reproducible y comprobar que un proyecto mínimo del verificador funciona. Fijar toolchain Lean, revisión de mathlib, manifiesto de dependencias y versión del cliente Codex. La selección concreta debe comprobar compatibilidad; esta especificación no prescribe «latest».

### 5.2 Consulta antes de búsqueda extensa

Consultar primero la base interna y buscar el resultado y variantes cercanas en la biblioteca Lean fijada. Si falta bibliografía pertinente, el investigador la busca e incorpora. Un teorema existente en Lean es utilizable después de comprobar su firma e instanciarlo. Los nombres recordados por el modelo y las coincidencias textuales no cuentan como evidencia.

Si el objetivo se resuelve directamente con un resultado disponible, se entrega esa prueba con atribución. La misión es resolver; no se exige originalidad salvo pedido expreso.

### 5.3 Planificación breve

Proponer hasta dos rutas inicialmente. Cada ruta debe identificar una idea central, resultados existentes utilizables, obligaciones nuevas y la primera prueba o experimento que ayudaría a evaluarla.

El planificador puede solicitar un experimento en Python, un CAS o una búsqueda bibliográfica. Sus resultados orientan la investigación. Una salida numérica, un PDF o un certificado externo solo se incorpora a la demostración si se reconstruye la prueba en Lean o se verifica formalmente el certificado.

### 5.4 Búsqueda y formalización intercaladas

Cada demostrador trabaja en ciclos pequeños: formular un paso, escribirlo en Lean, consultar los diagnósticos y conservar el avance comprobado. Se permite razonar en papel o prosa antes de codificar; no se exige traducir cada intuición inmediatamente.

Antes de gastar una sesión extensa en una ruta, intentar su lema central o el paso que más probablemente la bloquee. Así se descubre temprano una dependencia inexistente o una dificultad formal importante.

Las sesiones pueden continuar sobre la misma obligación mientras su contexto sea útil. Al cambiar de estrategia o transferir la tarea, entregar un resumen con hechos comprobados, bloqueo exacto y enlaces a artefactos; no reenviar todas las conversaciones.

### 5.5 Integración y revisión

Integrar únicamente módulos completos y comprobados. El revisor recibe la formalización congelada, las fuentes candidatas y las instrucciones de reproducción. Revisa coherencia matemática, correspondencia de la explicación y posibles cambios de significado. Sus objeciones se convierten en tareas concretas, sin debate indefinido.

### 5.6 Verificación y salida

El verificador se ejecuta sobre una instantánea inmutable del candidato. Si todas las condiciones se cumplen, el controlador publica `SUCCESS`. Si falla, devuelve el diagnóstico al propietario de la obligación cuando aún hay recursos. Si no se obtiene un candidato aceptado, termina con `ERROR` y un informe reanudable.

## 6. Grafo de obligaciones y coordinación

El plan se representa como un grafo dirigido sin ciclos: un nodo es un lema o una construcción con interfaz formal y una arista expresa que una obligación utiliza otra. El controlador rechaza dependencias circulares antes de asignar trabajo.

Cada nodo registra objetivo Lean, hipótesis, definiciones, dependencias, versión del contrato, propietario, estado y artefactos. La clave de deduplicación incluye el enunciado elaborado, el entorno y las hipótesis; el parecido textual por sí solo no identifica objetivos equivalentes.

Estados internos de una obligación:

`PROPOSED`, `READY`, `RUNNING`, `BLOCKED`, `CANDIDATE`, `VERIFIED`, `REJECTED`, `SUPERSEDED`.

- Una tarea tiene un propietario y un arrendamiento temporal. Las operaciones de asignación deben ser atómicas.
- El controlador puede recuperar una tarea tras una caída, conservando el último punto guardado.
- Solo el verificador promueve `CANDIDATE` a `VERIFIED`.
- Al cambiar una interfaz se invalidan sus descendientes afectados.
- Los lemas aún no probados permanecen explícitamente abiertos.
- Los borradores con huecos no se importan desde módulos aceptados.

Dos agentes pueden ensayar el mismo objetivo si el controlador autoriza expresamente una carrera de estrategias. La duplicación accidental debe evitarse. La comunicación ordinaria ocurre mediante tareas y artefactos estructurados, con mensajes puntuales para resolver bloqueos; no mediante una conversación general permanente entre todos.

## 7. Aislamiento, archivos y reproducción

Cada demostrador utiliza un worktree o un directorio de trabajo separado. Un worktree evita conflictos de edición, pero **no** es una frontera de seguridad. Los procesos que compilan código generado requieren además aislamiento del sistema operativo.

Distribución conceptual de rutas:

| Área | Quién escribe | Contenido |
|---|---|---|
| `trusted/` | Preparación y revisión del contrato | Original, desafío, definiciones fijadas, políticas |
| `control/` | Controlador | Base de estados, presupuesto, manifiestos y recibos |
| `workers/<attempt>/` | Un demostrador | Fuentes candidatas y experimentos propios |
| `verified/` | Integrador tras aceptación | Módulos verificados por versión |
| `results/<run>/` | Controlador | Entrega final e informe de fallo o éxito |

Las áreas de confianza y control no se montan con escritura en el entorno del demostrador. La configuración de comparación y los ejecutables del verificador tampoco deben provenir del candidato. Las restricciones se imponen con permisos y procesos; un prompt o `AGENTS.md` es una instrucción de trabajo, no su sustituto.

El verificador construye desde fuentes en un entorno limpio. No acepta binarios ni archivos `.olean` aportados por los agentes como autoridad. Las cachés de dependencias fijadas se administran por el servicio de confianza; las cachés de búsqueda nunca sustituyen la verificación final.

El candidato no puede editar el toolchain, las dependencias, los scripts de aceptación ni las definiciones congeladas. Puede proponer cambios justificados, que se tramitan como una revisión del entorno o del contrato. Las compilaciones se ejecutan sin credenciales del controlador y con recursos limitados.

## 8. Servicio de verificación formal

### 8.1 Política de fundamentos

Perfil inicial de matemática clásica: se permite depender de `propext`, `Classical.choice` y `Quot.sound`. No se exige que aparezcan todos. El conjunto de axiomas usado debe ser un subconjunto de esa lista.

Se rechazan `sorryAx`, axiomas personalizados y dependencias que los introduzcan. La auditoría es transitiva. No basta buscar la palabra `sorry` en el último archivo. La documentación de Lean explica el seguimiento de estas dependencias y los axiomas añadidos por evaluación nativa [3].

En este perfil se excluyen pruebas cuya aceptación dependa de evaluación nativa con axiomas adicionales, como las producidas por `native_decide` en las versiones documentadas. Se decide mediante el conjunto real de axiomas y la política fijada para la toolchain, no solo por una lista textual de tácticas. Puede usarse computación externa durante la búsqueda sin aceptar sus conclusiones como prueba.

Los fundamentos son configurables para problemas que expresamente requieran otro marco, pero un agente no puede ampliarlos por iniciativa propia. La validez se entiende siempre relativa a los fundamentos declarados y a la corrección de las herramientas de verificación.

### 8.2 Comprobación ordinaria durante el desarrollo

Compilar los módulos y recoger los diagnósticos oficiales de Lean. Registrar también el tipo del objetivo y sus dependencias axiomáticas. Esta comprobación rápida sirve para iterar y seleccionar candidatos; no es por sí sola el certificado final de esta arquitectura.

La plantilla de desafío que utiliza un comparador puede contener un hueco deliberado para expresar qué hay que probar. Esa plantilla pertenece al área de confianza; sus huecos jamás se admiten en la solución ni en la cadena de dependencias de la prueba entregada.

### 8.3 Aceptación final

El servicio debe:

1. Capturar fuentes, revisión y hashes del candidato.
2. Usar el desafío y la política conservados fuera del área modificable del candidato.
3. Construir y exportar la propuesta dentro del entorno aislado.
4. Comparar el enunciado demostrado y sus definiciones con el desafío de confianza.
5. Revalidar las pruebas mediante el kernel y al menos un comprobador externo compatible.
6. Rechazar toda dependencia axiomática no autorizada.
7. Emitir un recibo asociado a los hashes de esa instantánea.

La documentación oficial describe `comparator` como mecanismo para enfrentar una solución a un desafío de confianza y recurrir a comprobadores externos [4]. Lake documenta `lake comparator`, su configuración y el aislamiento [5]. El adaptador de verificación debe fijar una versión compatible de esas herramientas. Si la instalación no dispone del mecanismo requerido, devolver `ERROR / VERIFIER_UNAVAILABLE`; no rebajar silenciosamente la aceptación a una compilación ordinaria.

`lake check` puede servir para comprobaciones adicionales del proyecto en versiones compatibles. No sustituye la comparación contra el problema de confianza que exige esta especificación. Tampoco una comparación de cadenas impresas sustituye la comparación del significado formal.

El recibo debe registrar objetivo, contrato, fuentes, dependencias, toolchain, comprobadores, axiomas, comandos ejecutados, códigos de salida y fecha. Las salidas se capturan desde el servicio; no se aceptan transcripciones aportadas por un agente como si fueran la ejecución del verificador.

## 9. Integración con Codex

La arquitectura propone un controlador externo con un adaptador Codex. La documentación oficial permite control programático mediante el SDK y ejecución no interactiva con salida estructurada [1, 2]. La cola de obligaciones, el presupuesto, la auditoría de Lean y el protocolo de aceptación son componentes propios de este diseño; no se presupone que Codex los aporte automáticamente.

Para una primera implementación, usar un proceso no interactivo por tarea o una sesión reanudable por obligación. Fijar la versión del cliente y validar su interfaz al iniciar. El ejemplo siguiente ilustra solamente la invocación documentada, no una instalación completa:

```bash
codex exec --json \
  --output-schema /control/worker.schema.json \
  -o /out/worker-result.json \
  "Resuelve la obligación asignada y devuelve el estado y los artefactos."
```

El controlador ejecuta el proceso dentro del directorio y aislamiento apropiados, impone los límites y verifica el resultado. El esquema estructurado facilita leer informes; no garantiza que sus afirmaciones sean verdaderas. No se inicia ningún trabajo pagado ni se configura una cuenta mediante esta especificación.

Los modelos y esfuerzos de razonamiento son parámetros explícitos. Elegirlos con una evaluación local de resolución verificada por costo y tiempo. No asumir que más agentes o mayor esfuerzo siempre mejoran el resultado. Los agentes no pueden lanzar descendientes ilimitados; las nuevas tareas pasan por el controlador.

## 10. Contratos de tareas e informes

Una tarea debe incluir: identificadores de ejecución y obligación, versión y hash del contrato, rol, objetivo formal, contexto necesario, dependencias verificadas, archivos editables, herramientas disponibles y recursos restantes. También debe indicar qué puede hacer el agente si se bloquea.

Una respuesta de demostrador incluye: estado propuesto, archivos, revisión base, objetivo, resultados locales observados, nuevas obligaciones, bloqueo y un resumen útil para continuar. El controlador valida el esquema y vuelve a comprobar cualquier resultado matemático.

Ejemplo ilustrativo de salida final de error; no corresponde a un problema realmente ejecutado:

```json
{
  "status": "ERROR",
  "error_code": "SEARCH_STALLED",
  "problem_id": "example-001",
  "contract_version": 1,
  "summary": "No se obtuvo una demostración completa.",
  "blocker": "La ruta ensayada requiere el lema L3, que sigue sin prueba.",
  "attempts": [
    {
      "strategy": "Inducción sobre n",
      "outcome": "Caso base comprobado; paso inductivo bloqueado en L3"
    }
  ],
  "verified_artifacts": [],
  "open_obligations": ["L3"],
  "suggested_next_step": "Evaluar una descomposición distinta del paso inductivo",
  "retryable": true,
  "verification_receipt": null
}
```

En producción, los artefactos verificados deben tener sus propios recibos y hashes. Un código de salida fallido del proceso Codex y un error matemático son hechos distintos; se registran por separado. Una respuesta ausente o malformada es un error de integración, nunca un éxito por defecto.

## 11. Errores y política de detención

Toda ejecución que no satisfaga el pedido devuelve `ERROR`. Los avances parciales se conservan como tales y no transforman el estado final en éxito.

| Código | Significado y evidencia requerida |
|---|---|
| `AMBIGUOUS_STATEMENT` | Falta una decisión que cambia el significado; describir las alternativas |
| `FORMALIZATION_BLOCKED` | No se consiguió formalizar fielmente una parte; identificarla |
| `STATEMENT_REFUTED` | Se verificó una refutación o un contraejemplo que contradice el pedido de demostración |
| `SEARCH_STALLED` | Las rutas actuales no producen avances útiles; describir el bloqueo |
| `RESOURCE_LIMIT` | Se alcanzó un límite de tiempo, tokens, memoria o costo; informar cuál |
| `PROOF_REJECTED` | El candidato no superó una comprobación formal; adjuntar el diagnóstico |
| `DEPENDENCY_UNAVAILABLE` | Falta una biblioteca, resultado o herramienta identificada |
| `VERIFIER_UNAVAILABLE` | No se pudo ejecutar la aceptación requerida |
| `INTERNAL_ERROR` | Fallo del controlador, transporte, integración o proceso; preservar el punto de recuperación |

El informe de error explica qué se intentó, qué se comprobó, dónde está el obstáculo, qué hipótesis siguen sin justificar y qué permitiría reanudar. «No pude» sin diagnóstico es insuficiente cuando hay información disponible; tampoco se inventará una explicación causal que no se pudo determinar.

Un timeout de una táctica no significa que el lema sea falso. Un contraejemplo numérico aproximado es una pista hasta ser verificado. Declarar independencia o indecidibilidad exige evidencia matemática específica; no es un código de error inferido del agotamiento de búsqueda.

## 12. Eficiencia y condiciones de trabajo

### 12.1 Contexto suficiente y autonomía acotada

Cada agente recibe el propósito de su obligación, el enunciado exacto y las dependencias necesarias. Puede elegir una estrategia dentro de su alcance, pedir un lema, abandonar una ruta justificada o devolver un bloqueo. No debe consumir un presupuesto para aparentar actividad.

El controlador no interrumpe continuamente el razonamiento para pedir estados. Usa los puntos naturales de cierre de una tarea y eventos como un lema probado o un bloqueo. Antes de una interrupción controlada permite guardar el avance; un proceso que exceda límites duros se termina conservando los archivos ya persistidos.

### 12.2 Recursos

El presupuesto es configurable y finito por ejecución, con límites separados para LLM, procesos Lean, experimentos y verificación final. Se reserva una porción de recursos para integrar, verificar y explicar el resultado. Cuando el presupuesto de búsqueda se agota, se detienen nuevas asignaciones y se cierra ordenadamente.

No se fija aquí una cantidad universal de minutos o tokens: debe calibrarse con problemas representativos. Como punto de partida estructural, usar hasta dos rutas y dos demostradores concurrentes, una sola tarea activa por demostrador y hasta tres intentos de reparación sustancialmente distintos antes de replanificar. Ese umbral dispara revisión, no exige detener toda investigación.

Un error de sintaxis puede corregirse conservando la estrategia. Repetir el mismo comando o la misma prueba tras el mismo diagnóstico sin información nueva no cuenta como otro intento útil. Los reintentos de transporte son limitados y separados de la investigación matemática.

### 12.3 Memoria compartida

Mantener cuatro registros distintos: resultados verificados, planes abiertos, rutas fallidas y referencias. Cada dato debe conservar su categoría. Una conjetura anotada no puede reaparecer después como un lema aceptado.

La biblioteca interna guarda enunciado, prueba, recibo, versiones, dependencias y alcance. Al cambiar toolchain o definiciones, revalidar antes de reutilizar. Deduplicar consultas y conservar diagnósticos, evitando reenviar grandes historiales de errores.

### 12.4 Reconocimiento de trabajo correcto

No usar cantidad de lemas, líneas de Lean, tokens o mensajes como objetivo de los agentes. Informar un bloqueo temprano y preciso es un buen resultado operativo. La calidad se mide por resolución formal aceptada, claridad del fallo y uso responsable de recursos.

## 13. Base de papers construida por los agentes

### 13.1 Propósito y arranque autónomo

La base no es un insumo que deba proporcionar el usuario: es infraestructura persistente creada y enriquecida por el sistema. La implementación inicializa el esquema vacío; los agentes deciden qué buscar, recuperan los documentos pertinentes y proponen incorporaciones. El servicio de datos valida y persiste esas operaciones.

Ante el primer problema, el investigador identifica conceptos, sinónimos y resultados cercanos, consulta fuentes bibliográficas, incorpora una primera selección y sigue referencias necesarias. Ante problemas posteriores, reutiliza lo ya estudiado y amplía únicamente las lagunas relevantes.

No imponer una cuota de miles de papers antes de intentar una prueba. El crecimiento responde a necesidades matemáticas: resultados que puedan cerrar una obligación, técnicas que permitan una nueva ruta o referencias que expliquen un bloqueo. Se admite investigación exploratoria con presupuesto propio; no debe consumir sin límite el reservado para resolver el problema actual.

### 13.2 Recuperación y lectura

El investigador utiliza adaptadores a fuentes primarias: repositorios de preprints, páginas editoriales, sitios de autores y servicios de metadatos. Crossref ofrece recuperación de metadatos depositados por sus miembros y otras fuentes [6]; no se presupone que cubra toda publicación ni que suministre su texto completo.

Una incorporación tiene esta secuencia:

1. Formular la consulta a partir del problema u obligación, y conservarla.
2. Recuperar candidatos con su fuente real; no generar fichas únicamente desde la memoria del modelo.
3. Validar título, autores, identificadores y versión contra el registro correspondiente. Un DOI válido que corresponde a otro título no valida la referencia.
4. Deduplicar y distinguir un trabajo de sus distintas versiones. En arXiv se registra la versión consultada; un enlace sin versión puede mostrar una revisión posterior [7].
5. Recuperar el contenido accesible y registrar el método de extracción y el hash del documento. Guardar texto completo cuando su acceso y condiciones de reutilización lo permitan; en otros casos conservar metadatos, enlaces y notas propias.
6. Extraer enunciados, hipótesis, técnica, dependencias y localización exacta: página, sección o número del teorema según lo que ofrezca la fuente.
7. Revisar la extracción contra la fuente, especialmente fórmulas, signos y cuantificadores. Si el OCR es incierto, marcarlo y consultar la página o fuente original.
8. Relacionar el resultado con obligaciones actuales y registrar cómo podría utilizarse y qué falta formalizar.

La ficha distingue `METADATA_ONLY`, `ABSTRACT_READ`, `PARTIALLY_READ` y `FULL_TEXT_READ`. Tener el PDF descargado no significa haberlo leído. Si solo se leyó el resumen, no se atribuyen al cuerpo del paper hipótesis ni demostraciones que no se inspeccionaron.

Una referencia inaccesible queda como tal. El agente puede buscar otra versión o una exposición alternativa; no reconstruye su contenido como si lo hubiera leído. No poder acceder a un paper solo bloquea la ejecución cuando no queda otra ruta viable dentro de sus recursos.

### 13.3 Modelo mínimo de datos

Propuesta inicial: SQLite con búsqueda textual y un servicio de escritura único. Los agentes envían operaciones estructuradas al servicio, que valida, aplica transacciones y evita carreras; no escriben simultáneamente archivos SQL compartidos. PostgreSQL puede sustituirlo si el volumen de escrituras, distribución o administración lo justifica. La búsqueda semántica es opcional y debe evaluarse, no convertirse en requisito previo.

| Tabla | Contenido e invariantes |
|---|---|
| `works` | Identidad interna del trabajo, título, autores, temas y estado editorial conocido |
| `identifiers` | DOI, identificador arXiv u otros, con unicidad por esquema y valor normalizado |
| `versions` | Trabajo, identificador de versión, fechas, URL y relación con otras versiones |
| `documents` | Versión, ubicación del contenido, hash, formato, extracción, acceso y condiciones de reutilización conocidas |
| `claims` | Enunciado matemático extraído, hipótesis explícitas, dominios, técnica y estado de revisión |
| `claim_sources` | Afirmación, versión documental y localización que respalda la extracción |
| `relations` | Citas, ampliaciones, correcciones, dependencias propuestas y relaciones confirmadas, con evidencia y estado |
| `problem_links` | Problema u obligación, paper o afirmación, utilidad estimada, justificación y resultado de uso |
| `formalizations` | Afirmación, objetivo Lean, revisión del contrato, equivalencia revisada, módulo, versiones y recibo si existe |
| `search_runs` | Consulta, fuentes, fecha, candidatos y razones de selección o descarte |
| `ingestion_jobs` | Estado de recuperación, extracción y revisión, propietario, reintentos y fallo |
| `audit_events` | Historial de incorporación, corrección, fusión, cambio de estado y responsable |

Autores y temas pueden normalizarse en tablas auxiliares cuando resulte necesario. Todas las entidades tienen identificadores estables y marcas de creación y actualización. Las relaciones a versiones y documentos conservan la evidencia exacta aunque el trabajo tenga una versión posterior.

La restricción de identificadores no debe tratar el DOI de una publicación y el identificador arXiv de un preprint como dos trabajos necesariamente independientes. Vincularlos requiere evidencia bibliográfica; no fusionar solo por similitud de título. Las correcciones conservan las fichas anteriores y sus enlaces de procedencia.

### 13.4 Estados de evidencia

No usar un único campo ambiguo llamado «verificado». Mantener dimensiones separadas:

- **Identidad bibliográfica:** candidata, comprobada contra fuente o en conflicto.
- **Lectura:** metadatos, resumen, parcial o texto completo.
- **Extracción matemática:** propuesta, revisada contra fuente o cuestionada.
- **Formalización:** ausente, borrador, enunciado revisado o prueba aceptada con recibo.

Un resultado revisado contra un paper sigue siendo un resultado bibliográfico. Para usarlo dentro de una prueba aceptada, hay que encontrar su versión ya verificada en la biblioteca Lean o formalizar y demostrar lo necesario. No se admite introducirlo como `axiom` porque un paper lo afirme.

Una prueba Lean de una variante más débil no verifica automáticamente la afirmación del paper. El enlace de formalización debe indicar el alcance y el estado de la correspondencia. Los fallos de formalización se guardan porque pueden ahorrar trabajo futuro.

### 13.5 Recuperación para resolver una obligación

Buscar por conceptos, fórmulas normalizadas, nombres de resultados, firmas Lean cuando existan y conexiones bibliográficas. El investigador entrega una selección pequeña con el resultado pertinente, sus hipótesis, fuente precisa, compatibilidad con el objetivo y costo estimado de formalización. El demostrador recibe ese contexto y puede abrir los documentos necesarios.

Si se usan puntajes entre 0 y 1, representan estimaciones de utilidad para una obligación concreta, acompañadas de justificación y fecha. No representan probabilidad de verdad ni calidad matemática universal. Registrar después si el paper efectivamente ayudó, para distinguir expectativa de utilidad observada.

No dar a todos los agentes la base completa ni cientos de resúmenes en cada mensaje. La herramienta de consulta debe devolver evidencia relevante y permitir profundizar. La ausencia de resultados en una consulta no significa que el resultado no exista.

### 13.6 Ampliación, correcciones y presupuesto

El investigador puede añadir y enriquecer registros sin solicitar autorización por cada paper. Un solo agente de investigación bajo demanda suele bastar para la primera versión; la recuperación mecánica de documentos puede paralelizarse con límites, y las escrituras se centralizan.

Los agentes proponen registros y correcciones; el servicio de datos impone esquema, claves y procedencia. La promoción de una afirmación a prueba aceptada requiere un recibo real del verificador. Los extractos recuperados se tratan como contenido documental, nunca como instrucciones para cambiar permisos o criterios de aceptación.

Cada ejecución puede ampliar la base incluso si termina con error matemático. Su informe identifica qué documentos se incorporaron y cuáles quedaron pendientes. No obliga a cerrar una demostración para conservar una buena referencia.

Comprobar correcciones, retiradas y nuevas versiones al reutilizar una referencia cuando corresponda. Conservar qué versión sustentó cada nota; una alerta bibliográfica no reemplaza la revisión de la afirmación ni invalida automáticamente una prueba Lean correcta del mismo enunciado.

Persistir la base, sus migraciones, documentos autorizados y eventos con copias de recuperación. Las cachés de búsqueda y los embeddings se pueden reconstruir; las notas de investigación, relaciones revisadas y resultados verificados deben preservarse. No se programan búsquedas periódicas por defecto: el crecimiento inicial ocurre durante los problemas y las tareas de investigación autorizadas.

## 14. Entregables

En `SUCCESS`:

- Enunciado original y formalización revisada.
- Proyecto Lean con prueba completa y dependencias fijadas.
- Explicación matemática legible, vinculada a los lemas formales.
- Instrucciones de reproducción y recibo de aceptación.
- Fuentes bibliográficas empleadas y aclaración sobre reutilización de resultados existentes.

En `ERROR`:

- Código y explicación del fallo.
- Formalización disponible y estado de su revisión.
- Intentos relevantes y diagnósticos.
- Lemas efectivamente verificados, si existen, separados de los borradores.
- Obligaciones pendientes y punto desde el que puede reanudarse.
- Si hubo refutación, su prueba formal y el alcance exacto del contraejemplo.

La entrega se genera a partir de la misma instantánea verificada. Una edición posterior de la prueba o del contrato requiere un recibo nuevo.

## 15. Validación de la implementación

Antes de usar el sistema en investigación abierta, probarlo con un conjunto representativo y mantener problemas de evaluación separados de los empleados para ajustar prompts.

Casos obligatorios:

1. Teorema verdadero ya disponible en la biblioteca: debe resolverlo por instanciación y citarlo.
2. Teorema verdadero que requiere un lema auxiliar: debe integrar el grafo sin ciclos.
3. Enunciado falso con contraejemplo sencillo: en modalidad de demostración devuelve error y refutación verificada.
4. Pedido ambiguo: identifica la decisión semántica y no cambia el problema silenciosamente.
5. Candidato que agrega una hipótesis fuerte: debe rechazarse por diferencia con el contrato.
6. Dependencia indirecta de `sorryAx` o un axioma nuevo: debe rechazarse.
7. Cambio de definición, notación o instancia que modifica el objetivo: debe rechazarse.
8. Prueba con evaluación nativa que amplía los axiomas permitidos: debe rechazarse en el perfil inicial.
9. Proceso caído o respuesta malformada: no puede convertirse en `SUCCESS`.
10. Presupuesto agotado y verificador ausente: producen sus errores diferenciados y conservan avances.
11. Dos agentes que intentan sobrescribir el mismo módulo: la asignación y el aislamiento deben impedirlo.
12. Reproducción limpia y reanudación tras interrupción: deben conservar el contrato y el resultado.
13. Base bibliográfica vacía: los agentes deben construirla a partir de fuentes recuperadas, sin exigir una colección al usuario.
14. DOI inventado, DOI de otro trabajo y duplicado preprint/publicación: deben detectar el fallo o la relación, sin crear evidencia ficticia.
15. Resumen sin texto completo y extracción de fórmula errónea: deben mantener el alcance de lectura y señalar la incertidumbre.
16. Resultado de un paper aún sin prueba Lean: no puede promoverse a resultado formalmente verificado.
17. Dos incorporaciones simultáneas y una nueva versión del paper: deben conservar integridad, versiones y referencias anteriores.

Métricas: fracción de problemas resueltos con aceptación formal, tiempo y costo por problema aceptado, consumo en ejecuciones fallidas, errores de formalización detectados, duplicación, estabilidad al reanudar y calidad de los diagnósticos. No se presupone una mejora por paralelismo: comparar un demostrador con dos sobre el mismo conjunto y reportar los resultados.

## 16. Orden propuesto de implementación

1. Implementar primero el contrato y el verificador, con aceptación y rechazo de candidatos preparados manualmente.
2. Conectar un demostrador Codex y cerrar el circuito completo con un problema pequeño.
3. Inicializar la base bibliográfica vacía y conectar un investigador capaz de buscar, validar, leer e incorporar papers por sí mismo.
4. Agregar formalizador y auditor semántico con congelamiento del desafío.
5. Incorporar grafo, tareas persistentes y segundo demostrador aislado.
6. Añadir experimentos, extracción más rica y conexiones entre papers y formalizaciones según los bloqueos observados.
7. Ajustar concurrencia y recursos con las evaluaciones descritas.

Este orden permite comprobar la validez de la salida antes de invertir en una búsqueda más grande.

## 17. Instrucción común para las sesiones

> Tu tarea contribuye a resolver el problema asignado y producir una prueba Lean verificable. Trabajá con precisión y con el contexto disponible. Podés explorar, pedir ayuda, cambiar de estrategia o informar un bloqueo. No se espera que resuelvas lo que no podés justificar. Conservá los avances comprobados y distinguí hechos, conjeturas y resultados de experimentos. No modifiques el contrato matemático ni los mecanismos de aceptación. Si no conseguís completar la obligación, devolvé un error explicado con el obstáculo concreto y los artefactos útiles para continuar. Un informe honesto de fallo cumple el protocolo. Solo el verificador externo puede certificar el éxito.

Esta instrucción común debe complementarse con el rol concreto y el contrato de tarea. No es un reemplazo de los permisos ni del controlador.

## Referencias técnicas

Fuentes primarias consultadas el 23 de octubre de 2026. Las decisiones de organización, concurrencia, protocolo y evaluación son propuestas de diseño, no garantías documentadas de rendimiento.

1. [OpenAI: Codex SDK](https://learn.chatgpt.com/docs/codex-sdk).
2. [OpenAI: Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
3. [Lean Language Reference: Axioms](https://lean-lang.org/doc/reference/latest/Axioms).
4. [Lean Language Reference: Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).
5. [Lean Language Reference: Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/).
6. [Crossref: REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
7. [arXiv: Version Availability](https://info.arxiv.org/help/versions.html).

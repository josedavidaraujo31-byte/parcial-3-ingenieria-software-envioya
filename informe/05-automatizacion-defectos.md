# Parte 5 — Automatización, ejecución y defectos

## Suite automatizada

La función heredada y la configuración personalizada se encuentran en `envios.py`. La suite `tests/test_envios.py` automatiza los 38 casos CP01–CP38 de la Parte 3 y agrega el camino de caja blanca con `flag=True`. Las expectativas corresponden a R1–R8, no al comportamiento observado del legado.

Instalación y ejecución desde la raíz del repositorio:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -vv --tb=short --cov=envios --cov-branch --cov-report=term-missing
```

## Resultado contra el código heredado

Ejecución realizada con Python 3.13.0, pytest 9.2.0 y pytest-cov 7.1.0.

```text
collected 39 items
22 failed, 17 passed

Name        Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------
envios.py      29      0     26      0   100%
-------------------------------------------------------
TOTAL          29      0     26      0   100%
```

El 100 % medido corresponde a cobertura de sentencias y ramas del módulo `envios.py`; no significa que la implementación cumpla los requisitos. Las pruebas fallidas son evidencia de defectos. El porcentaje de casos que pasan en la línea base es `17 / 39 × 100 = 43,59 %`; fallan `22 / 39 × 100 = 56,41 %`.

La salida completa de esta ejecución está guardada en [`evidencia/pytest-baseline-final.txt`](../evidencia/pytest-baseline-final.txt).

Las capturas auténticas de consola están guardadas en [`evidencia/pytest-baseline-capture.png`](../evidencia/pytest-baseline-capture.png) (línea base: 22 fallos y 17 aprobaciones) y [`evidencia/pytest-regression-capture.png`](../evidencia/pytest-regression-capture.png) (regresión: 64 aprobadas). La segunda ejecución se realizó desde la raíz del repositorio con `python -m pytest -q --tb=no --color=no`.

## Registro de defectos

Se consideran cuatro defectos raíz. Algunos casos pueden revelar más de uno, por ejemplo CP27 tiene tanto el recargo de sábado omitido como un resultado afectado por truncamiento.

| ID | Título y requisito | Pasos para reproducir | Esperado | Obtenido en legado | Severidad / prioridad |
|---|---|---|---|---|---|
| DEF-01 | No valida zona ni día; R2. | Ejecutar CP18 (`z="desconocida"`), CP19 (`d=0`) o CP20 (`d=8`). | Lanzar un error para zona o día fuera del dominio. | No lanza `ValueError` y continúa con el cálculo. | Alta / P1: se acepta una solicitud inválida y se devuelve un costo que puede ser incorrecto. |
| DEF-02 | Omite el recargo del sábado; R5. | Ejecutar CP15: `calc(4, "urbana", "normal", 6)`. | $11.000: tarifa base $9.000 más $2.000. | $9.000; la condición heredada `d > 6` solo considera domingo. | Alta / P1: se cobra menos de lo establecido en cada envío de sábado. |
| DEF-03 | Trunca en vez de redondear a $100; R8. | Ejecutar CP09: `calc(10.0625, "urbana", "normal", 1)`. También CP21, CP22, CP24, CP25, CP33 y CP37. | CP09 debe dar $9.100 (mitad hacia arriba); los otros casos deben redondear al centenar más cercano. | CP09 da $9.000; la conversión `int(t / 100) * 100` siempre descarta la fracción. | Media / P1: puede subestimar la tarifa hasta en $100; difiere del redondeo requerido cuando los últimos dos dígitos son 50 o más. |
| DEF-04 | Mensaje de peso inválido no coincide con R1. | Ejecutar CP01, CP11 o CP12 y leer `ValueError`. | Mensaje exacto `peso inválido`. | El mensaje es `peso invalido`, sin tilde. | Baja / P2: el rechazo sucede, pero incumple el mensaje especificado y puede romper consumidores que comparen el texto. |

## Métricas de línea base

- Casos ejecutados: **39** (38 de caja negra y 1 camino de caja blanca para `flag`).
- Casos aprobados: **17 (43,59 %)**.
- Casos fallidos: **22 (56,41 %)**.
- Defectos raíz registrados: **4** — alta: 2; media: 1; baja: 1.
- Líneas físicas de `envios.py`: **40**.
- Densidad: `4 defectos / 40 líneas × 100 = 10 defectos por cada 100 líneas`.
- Cobertura de sentencias: **100 %**.
- Cobertura de ramas: **100 %**.

Estas son métricas de la versión heredada configurada para los parámetros 410026. En la Parte 6 se corregirán los defectos y se repetirá la misma suite como regresión.

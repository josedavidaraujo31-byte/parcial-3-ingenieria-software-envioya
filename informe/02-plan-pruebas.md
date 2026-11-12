# Parte 2 — Plan de pruebas

## Alcance

Se verificará el cálculo de EnvíaYa para PMAX=50 kg, L1=3 kg, L2=10 kg, recargo rural=20 %, recargo nacional=40 %, descuento VIP=15 %, descuento empresarial=12 % y recargo de fin de semana=$2.000. El alcance incluye R1–R9, la función heredada, la versión corregida y la solicitud empresarial. Los pagos, la persistencia, la interfaz gráfica y los servicios externos quedan fuera del alcance porque el enunciado no los define.

## Niveles de prueba

| Nivel | Aplicación |
|---|---|
| Unidad | Probar aisladamente validaciones, tramos, zona, fin de semana, descuentos, mínimo y redondeo de `calc`. |
| Integración | Verificar configuración y colaboración entre la función de cálculo y las estrategias de zona o descuento introducidas en la refactorización. |
| Sistema | Ejecutar el flujo completo de cálculo con combinaciones representativas de entradas válidas e inválidas. |
| Aceptación | Contrastar resultados con R1–R8 y los casos calculados manualmente; el estudiante revisa la evidencia y el docente evalúa en la sustentación. |

## Estrategia

- Caja negra: particiones de equivalencia, análisis de límites y tabla de decisión.
- Caja blanca: cobertura de sentencias y ramas, además de caminos independientes del código heredado.
- Automatización: pytest; se guardarán los casos esperados antes de ejecutar.
- Línea base: ejecutar la suite contra el código heredado y registrar los fallos como evidencia, no como una ejecución aprobada.
- Regresión: repetir la misma suite después de corregir y refactorizar.

## Ambiente y datos

Python 3, pytest y pytest-cov en entorno local, sin dependencias de red ni servicios externos. La configuración de prueba será L1=3, L2=10, recargo rural=0.20, recargo nacional=0.40, descuentos VIP=0.15 y empresarial=0.12, y recargo fin de semana=$2.000. Se probarán pesos alrededor de 0, 3, 10 y 50 kg; zonas válidas e inválidas; días 1, 6, 7 y fuera del intervalo; clientes normal, frecuente, VIP y empresarial; y cupón ausente, válido o desconocido.

Se probará el cliente empresarial en L2 exacto y por encima de L2, en zonas rural y nacional, con cupón y en fin de semana. El enunciado no establece qué hacer con valores de cliente distintos de normal, frecuente, VIP o empresarial; ese comportamiento queda pendiente de confirmación.

## Roles

- **Estudiante:** analista, diseñador de pruebas, desarrollador y responsable de registrar resultados, defectos y evidencia.
- **Compañero revisor, si está disponible:** revisa trazabilidad y cálculos esperados.
- **Docente:** valida el trabajo y plantea el defecto o cambio de la sustentación.

## Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| Parámetros o resultados esperados incorrectos | Revisar las fórmulas del documento y conservar los cálculos manuales. |
| Confundir defecto heredado con regla del negocio | Asociar cada caso a un requisito y fijar la expectativa antes de ejecutar. |
| No cubrir límites o combinaciones | Usar valores alrededor de 0, L1, L2 y PMAX y una tabla de decisión. |
| La refactorización altera resultados | Ejecutar la misma suite antes y después y comparar. |
| Cobertura alta pero poca utilidad | Priorizar cobertura de requisitos y ramas, no solo el porcentaje de líneas. |
| Cliente inválido sin comportamiento definido | Confirmarlo con el docente antes de establecer expectativa. |
| Interpretar como `>= L2` la exención de zona | Probar exactamente 10 kg y 10,5 kg en zona con recargo (CP40–CP42). |

## Criterios de entrada y salida

**Entrada:** parámetros calculados, R1–R8 identificados, casos con entradas y resultados esperados documentados, y pytest disponible.

**Salida de la línea base:** suite ejecutada, fallos reproducibles vinculados a requisitos, defectos registrados y cobertura medida.

**Salida después de corregir:** pasan todos los casos de R1–R9, no quedan defectos críticos o altos abiertos, la trazabilidad está actualizada y la cobertura real de sentencias y ramas está medida y reportada. La meta es cubrir todas las ramas relevantes de la función o justificar las no cubiertas.

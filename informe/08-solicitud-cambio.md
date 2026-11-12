# Parte 8 — Solicitud de cambio: cliente empresarial

## Solicitud

Para `CAMBIO=1`, incorporar el tipo de cliente `empresarial`, con 12 % de descuento. Para este tipo de cliente, cuando el peso sea **mayor que L2=10 kg**, no se cobra el recargo rural ni el nacional.

## Clasificación del mantenimiento

**Perfectivo (mejora funcional).** La solicitud incorpora una nueva categoría de cliente y amplía las reglas de cálculo para atender una necesidad de negocio. No corrige un defecto de la versión 2.0.0 ni responde a un cambio del entorno técnico.

## Análisis de impacto y trazabilidad

| Elemento | Impacto | Requisito / verificación |
|---|---|---|
| Parámetros | Añadir descuento empresarial de 12 %; conservar L2=10 kg y recargos existentes. | R3, R4, R9 |
| `calc` en `envios.py` | Aplicar el descuento empresarial; omitir la estrategia de zona solo si el cliente es empresarial y el peso supera L2. La firma pública no cambia. | R4, R6, R9 |
| Fin de semana y cupón | El recargo de fin de semana continúa antes de los descuentos; `ENVIO10` se aplica después del descuento empresarial. | R5, R6, R9; CP43–CP44 |
| Pruebas | Añadir seis casos de aceptación: descuento, límite exacto, exención rural/nacional, cupón y fin de semana. | CP39–CP44; `tests/test_business_customer.py` |
| Requisitos y pruebas | Actualizar las historias, matriz de trazabilidad, particiones, criterios y cálculos esperados. | `informe/01-requisitos.md`, `informe/02-plan-pruebas.md`, `informe/03-caja-negra.md` |
| Distribución | Documentar versión menor compatible y política añadida. | `CHANGELOG.md`, `RELEASE_NOTES_v2.1.0.md`, `informe/07-versionado.md` |

## Criterios de aceptación

1. Empresarial recibe 12 % de descuento sobre el subtotal calculado después de la zona y del recargo de fin de semana.
2. A exactamente 10 kg se aplica el recargo rural o nacional existente; por encima de 10 kg se omite.
3. La exención no elimina el recargo de fin de semana ni invalida el cupón.
4. Con cupón válido, se aplica primero el descuento empresarial y después el 10 % del cupón.
5. Se conserva la firma de `calc`; los tipos de cliente anteriores mantienen sus resultados.
6. Los resultados respetan el mínimo y redondeo definidos en R8.

## Supuestos y riesgos

- La solicitud no especifica el orden explícito de los descuentos combinados. Se mantiene la regla R6: descuento por tipo de cliente y luego cupón; empresarial se trata como otro tipo de cliente.
- “Mayor que L2” se interpreta estrictamente: 10 kg conserva el recargo; 10,5 kg no lo recibe.
- Solo se exime el recargo de zona. No se exime el recargo de fin de semana ni se altera la tarifa base.
- No se cambia el comportamiento de valores de cliente distintos de los tipos descritos.
- Riesgo principal: una comparación inclusiva en el límite podría eximir erróneamente el recargo a 10 kg; CP40 frente a CP41 detecta esa regresión.

## Evidencia

Las pruebas nuevas se ejecutaron primero contra 2.0.0 y fallaron en los seis casos; el resultado está en `evidencia/pytest-cambio-business-red.txt`. Después de la implementación, la suite completa pasó: 64 pruebas y 100 % de cobertura de sentencias y ramas de `envios.py`. La ejecución está en `evidencia/pytest-business-suite.txt`.

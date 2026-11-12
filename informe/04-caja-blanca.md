# Parte 4 — Caja blanca

Análisis de la función heredada `calc`. Para el grafo se separa `p <= 0 or p > 50` en dos predicados, dado el cortocircuito de Python. Las acciones se representan en las aristas.

## Grafo de flujo

Predicados: D1 `p <= 0`; D2 `p > 50`; D3 `p <= L1`; D4 `p <= L2`; D5 zona urbana; D6 zona rural; D7 zona nacional; D8 `d > 6`; D9 cliente frecuente; D10 cliente VIP; D11 cupón presente; D12 cupón `ENVIO10`; D13 `t < 5000`; D14 `flag`.

```text
Inicio → D1 ─sí→ error → Fin
          └no→ D2 ─sí→ error → Fin
                  └no→ D3
                       ├sí→ t=6000 ─────┐
                       └no→ D4           │
                            ├sí→ t=9000 ─┤
                            └no→ tarifa proporcional
                                         ↓
D5 urbana? ─sí──────────────────────────→ D8
    └no→ D6 rural? ─sí→ recargo rural ─→ D8
             └no→ D7 nacional?
                       ├sí→ recargo nacional → D8
                       └no→ sigue sin recargo → D8
D8 fin de semana? → D9 frecuente? → D10 VIP?
                  → D11 cupón presente?
                       ├no→ D13
                       └sí→ D12 ENVIO10? → D13
D13 mínimo? → D14 flag? ─sí→ imprimir → Fin
                            └no→ retornar → Fin
```

La zona inválida sigue hacia el cálculo sin recargo; el código heredado no lanza el error requerido por R2.

## Complejidad ciclomática

El grafo comprimido tiene 16 nodos (14 predicados, inicio y fin) y 29 aristas:

1. Aristas y nodos: `V(G) = E - N + 2 = 29 - 16 + 2 = 15`.
2. Nodos predicado: `V(G) = P + 1 = 14 + 1 = 15`.
3. Regiones: 15.

La complejidad ciclomática es **15**. Si `p <= 0 or p > 50` se cuenta como un único predicado, el resultado sería 14; aquí se modela el cortocircuito explícitamente.

## Caminos independientes

`flag` solo existe en el código heredado. `—` representa cupón ausente. Entradas en orden: `p, zona, cliente, día, cupón, flag`.

| Camino | Entradas de prueba | Rama nueva ejercitada | Esperado según R1–R8 |
|---|---|---|---|
| P0 | `4, otra, normal, 5, OTRO, False` | Base; zona inválida pasa por los tres no; cupón desconocido | Error de zona |
| P1 | `0, urbana, normal, 5, —, False` | D1 sí | Error “peso inválido” |
| P2 | `50.001, urbana, normal, 5, —, False` | D1 no, D2 sí | Error “peso inválido” |
| P3 | `3, urbana, normal, 5, —, False` | D3 sí | $6.000 |
| P4 | `11, urbana, normal, 5, —, False` | D3 no, D4 no | $9.800 |
| P5 | `4, urbana, normal, 5, OTRO, False` | D5 sí | $9.000 |
| P6 | `4, rural, normal, 5, OTRO, False` | D5 no, D6 sí | $10.800 |
| P7 | `4, nacional, normal, 5, OTRO, False` | D5 no, D6 no, D7 sí | $12.600 |
| P8 | `4, otra, normal, 6, OTRO, False` | D8 sí | Error de zona |
| P9 | `4, otra, frecuente, 5, OTRO, False` | D9 sí | Error de zona |
| P10 | `4, otra, vip, 5, OTRO, False` | D10 sí | Error de zona |
| P11 | `4, otra, normal, 5, —, False` | D11 no | Error de zona |
| P12 | `4, otra, normal, 5, ENVIO10, False` | D11 sí, D12 sí | Error de zona |
| P13 | `1, urbana, vip, 5, ENVIO10, False` | D13 sí | $5.000 |
| P14 | `4, urbana, normal, 5, —, True` | D14 sí | $9.000 e imprime costo |

P0 y P8–P12 tienen resultado esperado de error por la zona. La función heredada continúa el cálculo; por ejemplo, P0 devuelve $9.000. Esos casos revelan la falta de validación de zona.

## Cobertura diseñada

El conjunto P0–P14 está diseñado para cubrir las sentencias y ambas salidas de cada predicado. En particular, cubre ambas evaluaciones de `or`, las tres comparaciones de zona, cupón ausente/presente, cupón válido/desconocido, costo debajo/no debajo del mínimo y `flag` falso/verdadero.

Esta es cobertura **diseñada**, no medida. El porcentaje real de sentencias y ramas se debe obtener ejecutando la suite con pytest-cov. Para esta configuración PMAX=50 coincide con el tope fijo heredado y D es par, por lo que `p <= L1` incluye 3 kg; esos aspectos no son defectos en este caso.

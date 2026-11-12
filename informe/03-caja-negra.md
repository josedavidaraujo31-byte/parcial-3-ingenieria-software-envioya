# Parte 3 — Diseño de casos de caja negra

## Particiones de equivalencia

| Entrada | Particiones válidas | Inválidas o especiales |
|---|---|---|
| Peso | `0 < p <= 50 kg` | `p <= 0`, `p > 50` |
| Zona | `urbana`, `rural`, `nacional` | Cualquier otra zona: error según R2 |
| Cliente | `normal`, `frecuente`, `vip`, `empresarial` | Otro valor: comportamiento no definido en el enunciado; confirmar con el docente |
| Día | Entero de 1 a 7 | Menor que 1 o mayor que 7: error según R2 |
| Cupón | Ausente o `ENVIO10` | Desconocido: se ignora (F par) |

## Valores límite

Se usa 0,001 kg como incremento para probar valores decimales.

| Límite | Valores | Esperado |
|---|---|---|
| 0 | -0,001; 0; 0,001 | Inválido; inválido; válido |
| L1=3 kg | 2,999; 3; 3,001 | Tramo 1; tramo 1 incluido; tramo 2 |
| L2=10 kg | 9,999; 10; 10,001 | Tramo 2; tramo 2 incluido; tarifa proporcional |
| PMAX=50 kg | 50; 50,001 | Válido; inválido |

## Tabla de decisión

El recargo de fin de semana se agrega antes de los descuentos. Para B impar, se aplican los descuentos combinados primero cliente y luego cupón.

| Cliente | Cupón | Día hábil | Fin de semana |
|---|---|---|---|
| Normal | Ausente | Sin descuento | +$2.000 |
| Normal | `ENVIO10` | 10 % | +$2.000; después 10 % |
| Normal | Desconocido | Se ignora | +$2.000; cupón ignorado |
| Frecuente | Ausente | 5 % | +$2.000; después 5 % |
| Frecuente | `ENVIO10` | 5 %, luego 10 % | +$2.000; luego 5 % y 10 % |
| Frecuente | Desconocido | 5 %; cupón ignorado | +$2.000; después 5 % |
| VIP | Ausente | 15 % | +$2.000; después 15 % |
| VIP | `ENVIO10` | 15 %, luego 10 % | +$2.000; luego 15 % y 10 % |
| VIP | Desconocido | 15 %; cupón ignorado | +$2.000; después 15 % |

La cobertura de las 18 combinaciones se identifica con las referencias CP15, CP17, CP21–CP27 y CP30–CP38 de la matriz.

Para el cliente empresarial se comprueban por separado el descuento de 12 %, la regla estricta `peso > L2` para omitir el recargo de zona, y la interacción con cupón y fin de semana (CP39–CP44).

## Matriz de casos de prueba

Entradas en orden: peso, zona, cliente, día, cupón. `—` indica cupón ausente. Los resultados son expectativas según R1–R9, no resultados observados del código heredado.

| ID | Req. | Entradas | Esperado | Técnica |
|---|---|---|---:|---|
| CP01 | R1 | 0, urbana, normal, 1, — | Error “peso inválido” | Partición inválida |
| CP02 | R1/R3 | 0,001, urbana, normal, 1, — | $6.000 | Límite válido |
| CP03 | R3 | 2,999, urbana, normal, 1, — | $6.000 | Límite L1 |
| CP04 | R3 | 3, urbana, normal, 1, — | $6.000 | L1 incluido |
| CP05 | R3 | 3,001, urbana, normal, 1, — | $9.000 | Límite L1 |
| CP06 | R3 | 9,999, urbana, normal, 1, — | $9.000 | Límite L2 |
| CP07 | R3 | 10, urbana, normal, 1, — | $9.000 | L2 incluido |
| CP08 | R3 | 10,001, urbana, normal, 1, — | $9.000 | Límite L2 |
| CP09 | R3/R8 | 10,0625, urbana, normal, 1, — | $9.100 | Mitad hacia arriba |
| CP10 | R1/R3 | 50, urbana, normal, 1, — | $41.000 | PMAX incluido |
| CP11 | R1 | 50,001, urbana, normal, 1, — | Error “peso inválido” | Límite inválido |
| CP12 | R1 | -0,001, urbana, normal, 1, — | Error “peso inválido” | Partición inválida |
| CP13 | R4 | 4, rural, normal, 1, — | $10.800 | Zona rural |
| CP14 | R4 | 4, nacional, normal, 1, — | $12.600 | Zona nacional |
| CP15 | R5 | 4, urbana, normal, 6, — | $11.000 | Sábado |
| CP16 | R5 | 4, urbana, normal, 7, — | $11.000 | Domingo |
| CP17 | R5 | 4, urbana, normal, 5, — | $9.000 | Día hábil |
| CP18 | R2 | 4, desconocida, normal, 1, — | Error de zona | Partición inválida |
| CP19 | R2 | 4, urbana, normal, 0, — | Error de día | Límite inválido |
| CP20 | R2 | 4, urbana, normal, 8, — | Error de día | Límite inválido |
| CP21 | R6 | 4, urbana, frecuente, 1, — | $8.600 | Descuento frecuente y redondeo |
| CP22 | R6 | 4, urbana, vip, 1, — | $7.700 | Descuento VIP y redondeo |
| CP23 | R6 | 4, urbana, normal, 1, ENVIO10 | $8.100 | Cupón válido |
| CP24 | R6 | 4, urbana, frecuente, 1, ENVIO10 | $7.700 | Descuentos secuenciales |
| CP25 | R6 | 4, urbana, vip, 1, ENVIO10 | $6.900 | Descuentos secuenciales |
| CP26 | R7 | 4, urbana, normal, 1, OTRO | $9.000 | Cupón desconocido |
| CP27 | R5/R6 | 4, urbana, frecuente, 6, ENVIO10 | $9.400 | Tabla de decisión y orden |
| CP28 | R8 | 1, urbana, vip, 1, ENVIO10 | $5.000 | Costo mínimo |
| CP29 | R3 | 10,5, urbana, normal, 1, — | $9.400 | Tarifa proporcional |
| CP30 | R5/R6 | 4, urbana, normal, 6, ENVIO10 | $9.900 | Decisión: normal/cupón/fin de semana |
| CP31 | R5/R7 | 4, urbana, normal, 6, OTRO | $11.000 | Decisión: cupón desconocido/fin de semana |
| CP32 | R5/R6 | 4, urbana, frecuente, 6, — | $10.500 | Decisión: frecuente/sin cupón/fin de semana |
| CP33 | R6/R7 | 4, urbana, frecuente, 5, OTRO | $8.600 | Decisión: frecuente/cupón desconocido |
| CP34 | R5/R6/R7 | 4, urbana, frecuente, 6, OTRO | $10.500 | Decisión: frecuente/desconocido/fin de semana |
| CP35 | R5/R6 | 4, urbana, vip, 6, — | $9.400 | Decisión: VIP/sin cupón/fin de semana |
| CP36 | R5/R6 | 4, urbana, vip, 6, ENVIO10 | $8.400 | Decisión: VIP/cupón/fin de semana |
| CP37 | R6/R7 | 4, urbana, vip, 5, OTRO | $7.700 | Decisión: VIP/cupón desconocido |
| CP38 | R5/R6/R7 | 4, urbana, vip, 6, OTRO | $9.400 | Decisión: VIP/desconocido/fin de semana |
| CP39 | R9 | 4, urbana, empresarial, 1, — | $7.900 | Descuento empresarial |
| CP40 | R4/R9 | 10, rural, empresarial, 1, — | $9.500 | L2 incluido: conserva recargo rural y aplica descuento |
| CP41 | R3/R9 | 10,5, rural, empresarial, 1, — | $8.300 | Sobre L2: exención rural y descuento |
| CP42 | R3/R9 | 10,5, nacional, empresarial, 1, — | $8.300 | Sobre L2: exención nacional y descuento |
| CP43 | R6/R9 | 4, urbana, empresarial, 1, ENVIO10 | $7.100 | Descuentos empresarial y cupón secuenciales |
| CP44 | R5/R9 | 4, urbana, empresarial, 6, — | $9.700 | Fin de semana antes del descuento empresarial |

## Cálculos manuales

1. **CP09:** `$9.000 + (10,0625 - 10) × $800 = $9.050`; es mitad exacta entre $9.000 y $9.100, por tanto queda **$9.100**.
2. **CP13:** tarifa base $9.000; rural: `$9.000 × 1,20 = $10.800`.
3. **CP24:** `$9.000 × 0,95 = $8.550`; luego `$8.550 × 0,90 = $7.695`; redondeo: **$7.700**.
4. **CP27:** `$9.000 + $2.000 = $11.000`; frecuente: `$11.000 × 0,95 = $10.450`; cupón: `$10.450 × 0,90 = $9.405`; redondeo: **$9.400**.
5. **CP28:** `$6.000 × 0,85 × 0,90 = $4.590`; aplicar mínimo: **$5.000**.
6. **CP39:** `$9.000 × 0,88 = $7.920`; redondeo: **$7.900**.
7. **CP40:** `$9.000 × 1,20 × 0,88 = $9.504`; redondeo: **$9.500**. Al ser exactamente L2, no se exime el recargo.
8. **CP41/CP42:** `$9.000 + (10,5 - 10) × $800 = $9.400`; al superar L2 no se aplica recargo de zona; `$9.400 × 0,88 = $8.272`; redondeo: **$8.300**.
9. **CP43:** `$9.000 × 0,88 × 0,90 = $7.128`; redondeo: **$7.100**.
10. **CP44:** `($9.000 + $2.000) × 0,88 = $9.680`; redondeo: **$9.700**.

**Pendiente:** el resultado de un tipo de cliente no reconocido requiere confirmación; no se asigna expectativa hasta aclararlo.

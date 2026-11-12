# Parte 1 — Requisitos y criterios de aceptación

**Estudiante:** [escribir nombre]  
**Código estudiantil:** [escribir código completo; últimos seis dígitos: 410026]

## Parámetros personalizados

| Parámetro | Cálculo | Valor |
|---|---:|---:|
| A, B, C, D, E, F | Últimos seis dígitos | 4, 1, 0, 0, 2, 6 |
| PMAX | 30 + 5 × A | 50 kg |
| L1 | 2 + (B mod 3) | 3 kg |
| L2 | 10 + C | 10 kg |
| RR | 10 + 5 × (E mod 4) | 20 % |
| RN | 40 + 5 × (F mod 3) | 40 % |
| V | 10 + 5 × (A mod 3) | 15 % |
| S | 2000 + 500 × (C mod 4) | $2.000 |
| CAMBIO | (A + F) mod 3 | 1: cliente empresarial |

## Especificación del cálculo

1. **R1 — Peso:** debe cumplirse `0 < peso <= 50 kg`. Si no, se lanza `ValueError` con el mensaje `peso inválido`.
2. **R2 — Zona, día y cliente:** la zona debe ser `urbana`, `rural` o `nacional`, y el día debe estar entre 1 y 7; en caso contrario, se lanza un error. Los clientes descritos ahora incluyen `normal`, `frecuente`, `vip` y `empresarial`. El comportamiento para otros valores de cliente sigue sin estar definido.
3. **R3 — Tarifa base:** hasta 3 kg inclusive cuesta $6.000; más de 3 y hasta 10 kg inclusive cuesta $9.000; sobre 10 kg cuesta $9.000 más $800 por cada kg sobre 10, proporcionalmente.
4. **R4 — Zona:** urbana no tiene recargo; rural agrega 20 % y nacional agrega 40 %.
5. **R5 — Fin de semana:** sábado (día 6) y domingo (día 7) agregan $2.000 antes de los descuentos.
6. **R6 — Descuentos:** frecuente recibe 5 %, VIP 15 % y empresarial recibe 12 % según R9; el cupón `ENVIO10` aplica 10 %. Como B=1 es impar, si se combinan cliente y cupón se aplican ambos, primero el descuento del cliente y luego el del cupón.
7. **R7 — Cupón desconocido:** como F=6 es par, se ignora.
8. **R8 — Mínimo y redondeo:** el costo no puede ser menor de $5.000. Se redondea al múltiplo de $100 más cercano; las mitades redondean hacia arriba.
9. **R9 — Cliente empresarial (solicitud de cambio):** recibe 12 % de descuento. Si su peso es mayor que L2=10 kg, no se aplica recargo de zona rural ni nacional; en exactamente 10 kg sí se aplica. El recargo de fin de semana se mantiene. Si se usa `ENVIO10`, los descuentos se aplican primero como descuento empresarial y después como cupón, según R6.

**Orden del cálculo:** tarifa base, recargo de zona, recargo de fin de semana si aplica, descuento de cliente, cupón si aplica, mínimo de $5.000 y redondeo final.

## Historias de usuario

### HU-01 — Calcular tarifa base y recargo de zona

**Dado** un peso válido de hasta 50 kg, una zona válida y un día entre 1 y 7,  
**Cuando** solicito calcular el costo del envío,  
**Entonces** se selecciona el tramo correcto (L1=3 kg incluido y L2=10 kg incluido) y se aplica el recargo de la zona correspondiente.

### HU-02 — Aplicar recargo de fin de semana y descuentos

**Dado** un envío válido, un cliente admitido y un cupón opcional,  
**Cuando** es sábado o domingo y hay descuentos aplicables,  
**Entonces** se agregan primero $2.000 y después se aplican, en orden, el descuento del cliente y el cupón válido; un cupón desconocido se ignora.

### HU-03 — Validar entradas y obtener el costo final

**Dado** un peso, una zona y un día,  
**Cuando** solicito el cálculo,  
**Entonces** se rechaza el peso fuera del intervalo y la zona o el día inválidos; para entradas válidas, se aplica el mínimo de $5.000 y se redondea a $100 con mitades hacia arriba.

### HU-04 — Aplicar condiciones del cliente empresarial

**Dado** un envío válido de un cliente empresarial.

**Cuando** se calcula su costo con zona, día y cupón opcional.

**Entonces** se aplica 12 % de descuento; si el peso supera 10 kg, se omite únicamente el recargo de zona, y el fin de semana y el cupón conservan el orden especificado.

## Matriz de trazabilidad

| Requisito | Historia | Casos de prueba previstos |
|---|---|---|
| R1 | HU-01, HU-03 | Peso <=0, peso apenas válido, 50 kg y mayor de 50 kg |
| R2 | HU-01, HU-03 | Zonas válidas e inválidas; días 1, 7 y fuera del intervalo |
| R3 | HU-01 | Pesos alrededor de 3 kg y 10 kg; peso superior a 10 kg |
| R4 | HU-01 | Urbana, rural y nacional |
| R5 | HU-02 | Días 5, 6 y 7; orden del recargo |
| R6 | HU-02, HU-04 | Normal, frecuente, VIP y empresarial con cupón ausente o válido |
| R7 | HU-02 | Cupón ausente, `ENVIO10` y desconocido |
| R8 | HU-03 | Costo menor al mínimo y redondeo abajo, arriba y en mitad exacta |
| R9 | HU-04 | CP39–CP44: descuento, L2 exacto y superado, zonas rural/nacional, cupón y fin de semana |

**Pendiente:** confirmar con el docente cómo tratar un valor de cliente no admitido; el documento no fija ese resultado. Los casos definidos se identifican como CP01–CP44 en la Parte 3.

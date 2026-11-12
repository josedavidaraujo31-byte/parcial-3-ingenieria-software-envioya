# EnvíaYa 2.1.0

Release date: 2026-11-11

## Summary

Adds the requested business-customer pricing policy without changing the public `calc` signature.

## Changes

- Business customers receive a 12% discount.
- For business shipments weighing more than 10 kg, rural and national zone surcharges are not applied. At exactly 10 kg, the zone surcharge remains.
- The weekend surcharge still precedes discounts. If `ENVIO10` is provided, it follows the 12% business discount.

## Verification

The six new acceptance cases are CP39–CP44. The complete suite passes 64 tests with 100% statement and branch coverage of `envios.py`. Their expected values and impact traceability are documented in `informe/08-solicitud-cambio.md` and `informe/03-caja-negra.md`; the run is preserved in `evidencia/pytest-business-suite.txt`.

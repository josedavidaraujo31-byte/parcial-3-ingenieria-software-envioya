# EnvíaYa 2.0.0

Release date: 2026-11-11

## Summary

The legacy shipping calculation has been corrected and refactored. Zone pricing now uses the Strategy pattern, and the regression suite verifies all specified requirements.

## Breaking change

The `flag` argument was removed from `calc`, along with its console-print side effect.

Before:

```python
calc(p, z, c, d, cup=None, flag=False)
```

Now:

```python
calc(weight, zone, customer_type, day, coupon=None)
```

Callers must remove `flag` from invocations. The incompatible signature change warrants a major version bump to `2.0.0`.

## Corrections

- Invalid zones and days raise `ValueError`.
- Saturday and Sunday receive the weekend surcharge before discounts.
- Totals use decimal arithmetic and round half up to the nearest $100.
- Invalid weights report exactly `peso inválido`.

## Verification

The complete suite passes with 58 tests and 100% statement and branch coverage of `envios.py`. See `evidencia/pytest-versioned-suite.txt` and `informe/07-versionado.md`.

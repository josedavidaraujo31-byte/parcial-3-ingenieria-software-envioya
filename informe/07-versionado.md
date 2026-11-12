# Parte 7 — Gestión de configuración

## Etiquetas y versiones

| Etiqueta | Commit | Contenido |
|---|---|---|
| `v1.0.0` | `e1c30a6` | Línea base heredada configurada, antes de corregir su lógica. |
| `v2.0.0` | Commit de integración de esta entrega | Implementación corregida, refactorizada y regresión ampliada. |

`v2.0.0` es una versión **major**: se quitó el argumento público `flag` de `calc`, por lo que las llamadas antiguas que lo pasaban dejan de ser compatibles. La versión también corrige defectos visibles de cálculo. La etiqueta `v1.0.0` preserva el legado sin cambios, y `CHANGELOG.md` mantiene el formato Keep a Changelog.

## Ramas e integración

Los cuatro defectos ya se corrigieron en el commit `c937a9a` de la Parte 6. Para no duplicar ni reescribir esas correcciones, las ramas `fix/DEF-*` de este punto agregan pruebas de regresión aisladas para cada arreglo; cada rama fue integrada a `work/punto-7` mediante un merge `--no-ff`.

| Rama | Trabajo aislado | Commit de la rama |
|---|---|---|
| `fix/DEF-01` | Rechazo de zona y día inválidos | `4e73361` |
| `fix/DEF-02` | Recargo sábado/domingo y orden respecto al cupón | `45cb5f9` |
| `fix/DEF-03` | Redondeo abajo, mitad exacta y arriba | `49248e2` |
| `fix/DEF-04` | Mensaje exacto de peso inválido | `830fbdb` |
| `refactor/estrategia` | Comportamiento aislado de las estrategias de zona | `d592ee3` |
| `test/suite` | Contrato público sin el argumento heredado `flag` | `8ebbe45` |

El commit `c937a9a` contiene la implementación de la Parte 6. La rama de integración reúne las ramas indicadas y se publica en `main` después de pasar la regresión completa.

## Verificación y evidencia

La suite final contiene los 38 casos CP01–CP38, cinco comprobaciones adicionales de la Parte 6 y quince pruebas de las ramas de configuración. Las 58 pruebas pasan con 100 % de cobertura de sentencias y ramas de `envios.py`. La salida completa está en [`evidencia/pytest-versioned-suite.txt`](../evidencia/pytest-versioned-suite.txt).

La salida del comando `git log --oneline --graph --all` se adjunta en [`evidencia/git-log-point7.txt`](../evidencia/git-log-point7.txt).

Los commits y sus marcas de tiempo son auténticos; no se modificaron ni retrofecharon para simular intervalos.

# parcial-3-ingenieria-software-envioya
Parcial 3 de Ingeniería de Software: pruebas, mantenimiento y evolución de EnvíaYa.

## Pruebas

Instala las dependencias de desarrollo y ejecuta la suite con cobertura de ramas:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -vv --tb=short --cov=envios --cov-branch --cov-report=term-missing
```

La suite debe pasar sobre la implementación refactorizada. El resultado previo del código heredado y los defectos encontrados están documentados en `informe/05-automatizacion-defectos.md`; la refactorización y su comparación están en `informe/06-refactorizacion.md`.

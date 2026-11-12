# parcial-3-ingenieria-software-envioya
Parcial 3 de Ingeniería de Software: pruebas, mantenimiento y evolución de EnvíaYa.

## Pruebas

Instala las dependencias de desarrollo y ejecuta la suite con cobertura de ramas:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -vv --tb=short --cov=envios --cov-branch --cov-report=term-missing
```

La línea base de la función heredada contiene fallos esperados; consulta el informe de la Parte 5 en `informe/05-automatizacion-defectos.md`.

# parcial-3-ingenieria-software-envioya
Parcial 3 de Ingeniería de Software: pruebas, mantenimiento y evolución de EnvíaYa.

## Pruebas

Instala las dependencias de desarrollo y ejecuta la suite con cobertura de ramas:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -vv --tb=short --cov=envios --cov-branch --cov-report=term-missing
```

La suite debe pasar sobre la implementación refactorizada. El resultado previo del código heredado y los defectos encontrados están documentados en `informe/05-automatizacion-defectos.md`; la refactorización y su comparación están en `informe/06-refactorizacion.md`.

## Versiones

Consulta el [CHANGELOG](CHANGELOG.md), las [notas de v2.0.0](RELEASE_NOTES_v2.0.0.md), las [notas de v2.1.0](RELEASE_NOTES_v2.1.0.md), el [análisis de impacto de la Parte 8](informe/08-solicitud-cambio.md) y el [informe de gestión de configuración](informe/07-versionado.md).

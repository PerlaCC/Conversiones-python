# Conversiones-python

Práctica U4_9 – Agentes en Jenkins (DevOps, Unidad 4 CI/CD).

- `conversiones.py`: funciones de conversión (cm↔pulgadas, pies↔metros, millas↔km, galones↔litros, libras↔kg) y dos agregadas por el equipo: °C↔°F y onzas↔gramos.
- `test_conversiones.py`: pruebas unitarias con pytest.
- `Jenkinsfile`: pipeline que corre en el agente con etiqueta `python`.

Ejecutar localmente:

```
python3 conversiones.py
python3 -m pytest
```

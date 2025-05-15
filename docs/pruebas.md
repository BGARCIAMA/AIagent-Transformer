
# Pruebas con diferentes tipos de Datos

Este documento presenta un conjunto de pruebas realizadas utilizando datos en distintos formatos y estructuras. El objetivo es validar el correcto funcionamiento del agente transformador en escenarios variados.

## Archivos Probados

1. **`prueba.csv`**
   - Columnas: `nombre_cliente`, `fecha_transacción`, `monto_total`, `numero_cuenta`, `estatus_pago`
   - Resultado: Mapeo correcto de 3 de 5 columnas (60%), transformación aprobada.

2. **`sample_json.json`**
   - Datos anidados convertidos a formato tabular.
   - Resultado: Transformación y análisis exitosos.

3. **`sample_xml.xml`**
   - Archivo con múltiples registros y estructura jerárquica.
   - Resultado: Parsed correctamente con `xml.etree`.

## Validaciones Realizadas

- Validación estructural con `validate_structure_consistency()`
- Evaluación de columnas coincidentes.
- Transformaciones semánticas exportadas en los tres formatos.



# Análisis de Precisión de las Transformaciones

Este documento detalla el análisis de precisión realizado sobre los resultados de transformación semántica aplicando embeddings.

## Métricas Evaluadas

- **Porcentaje de columnas correctamente mapeadas**
  - Se compararon columnas originales vs. columnas destino estándar esperadas.
  - Se consideró una coincidencia válida cuando la similitud coseno fue > 0.7.

- **Promedio de similitud coseno por par mapeado**
  - Resultado típico entre 0.78 y 0.92 para nombres con relación semántica directa.

## Ejemplo

| Columna Original     | Columna Sugerida     | Similitud |
|----------------------|----------------------|-----------|
| nombre_cliente       | cliente_nombre       | 0.91      |
| fecha_transacción    | transaction_date     | 0.83      |
| monto_total          | total_amount         | 0.89      |
| estatus_pago         |                      | < 0.6     |

## Conclusión

- Los mapeos generados fueron precisos en al menos un 80% de los casos cuando existía un referente semántico claro.
- El sistema es robusto a variantes sintácticas, pero puede requerir ajuste en umbrales para evitar falsos positivos.

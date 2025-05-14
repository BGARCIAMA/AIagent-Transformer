
# Documentación de los Algoritmos de Transformación

Este documento describe el funcionamiento interno de los componentes clave de la herramienta de transformación semántica de datos.

## 1. Análisis de Estructura (`parser.py`)
- El módulo `parser.py` detecta automáticamente el tipo de archivo (CSV, JSON, XML).
- Extrae la estructura tabular usando `pandas`, `json` y `xml.etree`.
- Devuelve un DataFrame y una lista de columnas detectadas.

## 2. Mapeo Semántico (`transformer.py`)
- Utiliza el modelo `all-MiniLM-L6-v2` de `sentence-transformers` para convertir nombres de columnas a vectores.
- Calcula similitudes entre columnas fuente y un esquema destino estándar mediante `cosine similarity`.
- Retorna un diccionario que mapea columnas fuente con las más similares del esquema destino.
- Aplica este mapeo al DataFrame antes de exportar.

## 3. Validación de Consistencia (`validator.py`)
- Compara columnas originales y transformadas para evaluar si hay pérdida de estructura.
- Calcula el porcentaje de columnas que se mantienen.
- Si se supera un umbral configurable, la transformación se considera válida.

## 4. Visualización (`visualizer.py`)
- Muestra la estructura del DataFrame en formato JSON o tabla interactiva para facilitar la inspección del usuario.

## Aplicación Principal (`streamlit_app.py`)
- Interfaz desarrollada en Streamlit.
- Permite cargar archivos, visualizar estructuras, aplicar transformación semántica y validar el resultado.
- Muestra el mapeo detectado y permite exportar en múltiples formatos.

---
Este documento cubre el Entregable 2: Documentación de los algoritmos de transformación.

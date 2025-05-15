# Data Transformer AI Agent

Este proyecto implementa un agente inteligente capaz de transformar datos entre múltiples formatos (CSV, JSON, XML) sin perder su estructura semántica. Utiliza análisis estructural, embeddings semánticos y validadores de consistencia para permitir la interoperabilidad de datos en entornos financieros.

![Flujo del Agente](docs/flujo.excalidraw)

## Funcionalidades
- Carga y análisis de estructuras de datos desde distintos formatos.
- Transformación semántica entre esquemas diferentes.
- Validación de consistencia de datos.
- Visualización de estructuras antes y después de la transformación.

| Función                        | Descripción                            |
|--------------------------------|----------------------------------------|
| 📁 Carga de datos              | Archivos en CSV, JSON, XML              |
| 🧠 Mapeo semántico             | Usa embeddings para empatar columnas    |
| 🔀 Transformación              | Exporta al formato deseado              |
| ✅ Validación estructural      | Evalúa si se conservó el esquema        |
| 📥 Descarga                    | Permite guardar el archivo transformado |


## Tecnologías
- Python
- Streamlit
- pandas, xml.etree, json
- sentence-transformers

## Ejecución de la aplicación
```bash
streamlit run streamlit_app.py

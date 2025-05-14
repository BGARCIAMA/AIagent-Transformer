import streamlit as st
from io import StringIO
import pandas as pd
from app.parser import load_data
from app.transformer import semantic_transform, mapear_columnas_semanticas
from app.visualizer import visualize_structure
from app.validator import validate_structure_consistency

st.set_page_config(page_title="Data Transformer AI Agent", layout="wide")
st.title("🔄 Data Transformer AI Agent")

st.markdown("""
Esta herramienta utiliza inteligencia artificial para transformar datos entre distintos formatos (CSV, JSON, XML), 
preservando su estructura semántica.
""")

uploaded_file = st.file_uploader("📁 Carga un archivo CSV, JSON o XML", type=["csv", "json", "xml"])

if uploaded_file:
    # Paso 1: Análisis inicial
    df, original_structure = load_data(uploaded_file)
    # Detectar mapeo semántico antes de exportar
    st.subheader("🧠 Mapeo semántico sugerido entre columnas")
    mapeo = mapear_columnas_semanticas(original_structure, [
        "cliente_nombre", "transaction_date", "total_amount"  # Puedes ajustar estos valores estándar
    ])
    st.json(mapeo)
    st.table(pd.DataFrame(mapeo.items(), columns=["Columna original", "Columna destino sugerida"]))
    st.subheader("👀 Vista previa del archivo")
    st.dataframe(df.head())

    st.subheader("🧬 Estructura detectada")
    visualize_structure(original_structure)

    # Paso 2: Transformación
    st.subheader("🔀 Transformación semántica")
    target_format = st.selectbox("Selecciona el formato de salida", ["CSV", "JSON", "XML"])
    transformed_str = semantic_transform(df, target_format)

    st.success("Transformación completada")
    st.code(transformed_str, language=target_format.lower())

    # Paso 3: Validación de consistencia
    st.subheader("✅ Validación de consistencia estructural")

    try:
        # Parseamos el archivo transformado nuevamente
        df_transformed, transformed_structure = load_data(StringIO(transformed_str))
        validation = validate_structure_consistency(original_structure, transformed_structure)

        st.write("Columnas coincidentes:", validation["matched_columns"])
        st.metric("Porcentaje de coincidencia", f"{validation['match_ratio'] * 100:.2f}%")
        if validation["passed"]:
            st.success("✅ Validación aprobada")
        else:
            st.error("⚠️ Validación no aprobada")

    except Exception as e:
        st.error(f"No se pudo validar el archivo transformado: {e}")

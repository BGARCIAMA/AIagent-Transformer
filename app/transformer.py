from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

# Puedes ajustar este esquema estándar a tu caso de uso real
CAMPOS_DESTINO_ESTANDAR = ["cliente_nombre", "transaction_date", "total_amount"]

def mapear_columnas_semanticas(columnas_fuente, columnas_destino):
    emb_fuente = model.encode(columnas_fuente, convert_to_tensor=True)
    emb_destino = model.encode(columnas_destino, convert_to_tensor=True)

    sim_matrix = util.cos_sim(emb_fuente, emb_destino).cpu().numpy()

    mapeo = {}
    for i, fuente in enumerate(columnas_fuente):
        mejor_idx = sim_matrix[i].argmax()
        score = sim_matrix[i][mejor_idx]
        if score > 0.7:  # puedes ajustar este umbral
            mapeo[fuente] = columnas_destino[mejor_idx]
    return mapeo

def semantic_transform(df, target_format):
    # Paso 1: aplicar mapeo semántico
    columnas_originales = list(df.columns)
    mapeo = mapear_columnas_semanticas(columnas_originales, CAMPOS_DESTINO_ESTANDAR)
    df_renombrado = df.rename(columns=mapeo)

    # Paso 2: exportar al formato deseado
    if target_format.lower() == "json":
        return df_renombrado.to_json(orient="records", indent=2)
    elif target_format.lower() == "xml":
        return df_renombrado.to_xml(
            root_name="data",
            row_name="record",
            pretty_print=True,
            parser="etree"
        )
    else:
        return df_renombrado.to_csv(index=False)

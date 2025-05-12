from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_transform(df, target_format):
    # Por ahora, solo retorna el mismo dataframe como ejemplo
    if target_format.lower() == "json":
        return df.to_json(orient="records", indent=2)
    elif target_format.lower() == "xml":
        return df.to_xml(root_name="data", row_name="record", pretty_print=True)
    else:
        return df.to_csv(index=False)
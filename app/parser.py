import pandas as pd
import json
import xml.etree.ElementTree as ET
from io import StringIO

def load_data(file):
    file_type = file.name.split(".")[-1].lower()

    if file_type == "csv":
        df = pd.read_csv(file)
        structure = list(df.columns)
        return df, structure

    elif file_type == "json":
        data = json.load(file)
        df = pd.json_normalize(data)
        return df, list(df.columns)

    elif file_type == "xml":
        tree = ET.parse(file)
        root = tree.getroot()
        rows = []
        for child in root:
            row = {elem.tag: elem.text for elem in child}
            rows.append(row)
        df = pd.DataFrame(rows)
        return df, list(df.columns)

    else:
        raise ValueError("Formato no soportado")
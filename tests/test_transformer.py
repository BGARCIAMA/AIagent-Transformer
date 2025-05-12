import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from app.parser import load_data
from app.transformer import semantic_transform
from app.validator import validate_structure_consistency
from io import StringIO

# DataFrame de ejemplo
df_sample = pd.DataFrame({
    "nombre": ["Ana", "Luis"],
    "edad": [25, 30]
})

def test_semantic_transform_csv():
    output = semantic_transform(df_sample, "CSV")
    assert "nombre,edad" in output
    assert "Ana" in output

def test_semantic_transform_json():
    output = semantic_transform(df_sample, "JSON")
    assert '"nombre":"Ana"' in output  # Ajustado sin espacio

def test_semantic_transform_xml():
    output = semantic_transform(df_sample, "XML")
    assert "<nombre>Ana</nombre>" in output  # Requiere parser "etree" si no usas lxml

def test_structure_validation():
    original = ["nombre", "edad"]
    transformed = ["nombre", "edad", "extra"]
    result = validate_structure_consistency(original, transformed)
    assert result["passed"] is True
    assert result["match_ratio"] == 1.0

def test_load_data_csv():
    csv_str = "col1,col2\nA,1\nB,2"
    file_like = StringIO(csv_str)
    # Forzamos tipo CSV si no tiene .name
    file_like.name = "fake.csv"
    df, cols = load_data(file_like)
    assert df.shape == (2, 2)
    assert "col1" in cols
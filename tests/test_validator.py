
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.validator import validate_structure_consistency

def test_validacion_total():
    original = ["nombre", "edad", "correo"]
    transformado = ["nombre", "edad", "correo"]
    resultado = validate_structure_consistency(original, transformado)
    assert resultado["passed"] is True
    assert resultado["match_ratio"] == 1.0

def test_validacion_parcial():
    original = ["nombre", "edad", "correo"]
    transformado = ["nombre", "email"]
    resultado = validate_structure_consistency(original, transformado, threshold=0.3)
    assert resultado["passed"] is True
    assert resultado["match_ratio"] == 1/3

def test_validacion_fallida():
    original = ["id", "producto", "precio"]
    transformado = ["fecha", "cliente"]
    resultado = validate_structure_consistency(original, transformado, threshold=0.5)
    assert resultado["passed"] is False

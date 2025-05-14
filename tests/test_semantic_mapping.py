
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from app.transformer import mapear_columnas_semanticas

def test_mapeo_semantico_basico():
    columnas_fuente = ["nombre_cliente", "fecha_transacción", "monto_total"]
    columnas_destino = ["cliente_nombre", "transaction_date", "total_amount"]
    
    mapeo = mapear_columnas_semanticas(columnas_fuente, columnas_destino)
    
    assert mapeo["nombre_cliente"] == "cliente_nombre"
    assert mapeo["monto_total"] == "total_amount"
    assert "fecha_transacción" in mapeo

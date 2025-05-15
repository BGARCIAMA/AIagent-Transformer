def validate_structure_consistency(original_cols, transformed_cols, threshold=0.5):
    """
    Compara las columnas originales y transformadas para evaluar si se mantienen consistentes.

    Parámetros:
    - original_cols: lista de nombres de columnas del archivo original.
    - transformed_cols: lista de nombres de columnas del archivo transformado.
    - threshold: umbral mínimo (entre 0 y 1) de columnas coincidentes requerido para considerar válida la transformación.

    Retorna:
    Diccionario con:
        - matched_columns: columnas que se encuentran en ambos esquemas.
        - match_ratio: porcentaje de coincidencia.
        - passed: booleano indicando si supera el umbral.
    """

    original_set = set(original_cols)
    transformed_set = set(transformed_cols)
    
    matched = original_set.intersection(transformed_set)
    match_ratio = len(matched) / len(original_set) if original_set else 0

    return {
        "matched_columns": list(matched),
        "match_ratio": match_ratio,
        "passed": match_ratio >= threshold
    }
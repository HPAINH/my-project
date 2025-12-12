import pandas as pd

def compute_quality_flags(df: pd.DataFrame) -> dict:
    flags = {}

    # Базовые флаги
    flags["has_missing_values"] = df.isna().any().any()

    # Новая эвристика 1 — константные колонки
    flags["has_constant_columns"] = any(df.nunique() == 1)

    # Новая эвристика 2 — высокая кардинальность категорий
    high_card_cols = []
    for col in df.select_dtypes(include=["object"]):
        if df[col].nunique() > 50:
            high_card_cols.append(col)
    flags["high_cardinality_categoricals"] = len(high_card_cols) > 0

    # Новая эвристика 3 — дубликаты ID
    if "user_id" in df.columns:
        flags["has_id_duplicates"] = df["user_id"].duplicated().any()
    else:
        flags["has_id_duplicates"] = False

    # Евристика 4 — много нулей
    many_zero_cols = []
    for col in df.select_dtypes(include=["number"]):
        share = (df[col] == 0).mean()
        if share > 0.5:
            many_zero_cols.append(col)
    flags["many_zero_values"] = len(many_zero_cols) > 0

    return flags

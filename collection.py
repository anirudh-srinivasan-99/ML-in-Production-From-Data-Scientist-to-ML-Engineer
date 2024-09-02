import pandas as pd

def get_data_from_excel(path: str = "Data.xlsx") -> pd.DataFrame:
    return pd.read_excel(path)
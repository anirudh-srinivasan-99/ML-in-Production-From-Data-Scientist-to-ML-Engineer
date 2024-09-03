import pandas as pd
from typing import List

from collection import get_data_from_excel
from config import settings

def prepare_data(path: str = settings.data_path) -> pd.DataFrame:
    df = get_data_from_excel(path)

    df['HS'] = df['HS'].map(get_clean_high_score)
    df['Avg'] = df['Avg'].map(get_clean_average) 

    df = drop_columns(['NO', 'SR', 100, 'PLAYER'], df)

    return df

def get_clean_high_score(high_score: int|str) -> int:
    if isinstance(high_score, int):
        return high_score
    return int(high_score.replace("*", ""))

def get_clean_average(average: float|str) -> float:
    if average == '-':
        return 0.0
    return float(average)

def drop_columns(
    list_of_columns: List[str], df: pd.DataFrame
) -> pd.DataFrame:
    df = df.drop(list_of_columns, axis = 1)
    return df
from typing import List
import pandas as pd
from loguru import logger

from app.model.pipeline.collection import get_data_from_db


def prepare_data() -> pd.DataFrame:
    logger.info("Starting prepare_data() function !!")
    df = get_data_from_db()
    logger.info("Cleaned HS and Avg columns !!")
    df['HS'] = df['HS'].map(get_clean_high_score)
    df['Avg'] = df['Avg'].map(get_clean_average) 
    df = drop_columns(['NO', 'SR', 100, 'PLAYER'], df)
    logger.info("Dropped ['NO', 'SR', 100, 'PLAYER'] columns !!")
    logger.info("Completed prepare_data() function !!")
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
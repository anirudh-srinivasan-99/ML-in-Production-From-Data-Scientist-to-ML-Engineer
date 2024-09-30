"""This file is used to prepare the dataset for training."""

from typing import List

import pandas as pd
from loguru import logger

from app.model.pipeline.collection import get_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepare the data.

    :return: Cleaned data.
    :rtype: pd.DataFrame
    """
    logger.info('Starting prepare_data() function !!')
    df = get_data_from_db()
    logger.info('Cleaned HS and Avg columns !!')
    df['HS'] = df['HS'].map(_get_clean_high_score)
    df['Avg'] = df['Avg'].map(_get_clean_average)
    drop_columns = ['NO', 'SR', 100, 'PLAYER']
    df = _drop_columns(drop_columns, df)
    logger.info(f'Dropped {drop_columns} columns !!')
    logger.info('Completed prepare_data() function !!')
    return df


def _get_clean_high_score(high_score: int | str) -> int:
    """
    Clean Highscore column by removing * which indicates not-out.

    :param high_score: Highscore value.
    :type high_score: int | str
    :return: Cleaned Highscore value.
    :rtype: int
    """
    if isinstance(high_score, int):
        return high_score
    return int(high_score.replace('*', ''))


def _get_clean_average(average: float | str) -> float:
    """
    Clean Average column by converting '-' to 0.0 and typecasting to float.

    :param average: Average value.
    :type average: float | str
    :return: Cleaned Average value.
    :rtype: float
    """
    if average == '-':
        return 0.0  # noqa: WPS358
    return float(average)


def _drop_columns(
    list_of_columns: List[str], df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Drop unnecessary columns.

    :param list_of_columns: List of columns to be dropped.
    :type list_of_columns: List[str]
    :param df: Data.
    :type df: pd.DataFrame
    :return: Pruned Dataframe
    :rtype: pd.DataFrame
    """
    df = df.drop(list_of_columns, axis=1)
    return df

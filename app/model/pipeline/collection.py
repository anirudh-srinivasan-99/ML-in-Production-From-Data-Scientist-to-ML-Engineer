"""This file is used for loading IPL Data."""
from typing import Optional

import pandas as pd
from loguru import logger
from sqlalchemy import select

from app.config.db_config import engine
from app.config.model_config import model_settings
from app.database.db_model import IPLData


def get_data_from_excel(
    path: Optional[str] = model_settings.data_path,
) -> pd.DataFrame:
    """
    Load data from excel into a dataframe.

    :param path: Path to the excel file, defaults to model_settings.data_path
    :type path: Optional[str]
    :return: Loaded Data.
    :rtype: pd.DataFrame
    """
    logger.info('Starting get_data_from_excel() function !!')
    logger.debug(f'Input path: {path}')
    df = pd.read_excel(path)
    logger.info('Completed get_data_from_excel() function !!')
    return df


def get_data_from_db() -> pd.DataFrame:
    """
    Load data from database into a dataframe.

    :return: Loaded Data.
    :rtype: pd.DataFrame
    """
    logger.info('Starting get_data_from_db() function !!')
    query = select(IPLData)
    df = pd.read_sql(query, engine)
    logger.info('Completed get_data_from_excel() function !!')
    return df

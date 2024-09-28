import pandas as pd

from app.config.config import settings, engine
from loguru import logger
from app.database.db_model import IPLData
from sqlalchemy import select

def get_data_from_excel(path: str = settings.data_path) -> pd.DataFrame:
    logger.info("Starting get_data_from_excel() function !!")
    logger.debug(f"Input path: {path}")
    df = pd.read_excel(path)
    logger.info("Completed get_data_from_excel() function !!")
    return df

def get_data_from_db():
    logger.info("Starting get_data_from_db() function !!")
    query = select(IPLData)
    df = pd.read_sql(query, engine)
    logger.info("Completed get_data_from_excel() function !!")
    return df
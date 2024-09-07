import pandas as pd

from config import settings
from loguru import logger


def get_data_from_excel(path: str = settings.data_path) -> pd.DataFrame:
    logger.info("Starting get_data_from_excel() fucntion !!")
    logger.debug(f"Input path: {path}")
    df = pd.read_excel(path)
    logger.info("Completed get_data_from_excel() fucntion !!")
    return df
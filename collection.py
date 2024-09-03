import pandas as pd

from config import settings


def get_data_from_excel(path: str = settings.data_path) -> pd.DataFrame:
    return pd.read_excel(path)
"""This file is used for setting up DB Configurations."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DBSettings(BaseSettings):
    """DB Settings Class."""

    model_config = SettingsConfigDict(
        env_file='app/config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )
    db_conn_str: str
    ipl_data_table_name: str


db_settings = DBSettings()
engine = create_engine(db_settings.db_conn_str)

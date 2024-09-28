from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from loguru import logger
from sqlalchemy import create_engine

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = 'app/config/.env', env_file_encoding='utf-8', extra='ignore')
    data_path: FilePath
    model_dir: DirectoryPath
    model_name: str
    db_conn_str: str
    ipl_data_table_name: str

settings = Settings()

logger.add(
    "app/log/app.log", retention='1 week', rotation = '1 day',
    level = 'INFO'
)

engine = create_engine(settings.db_conn_str)

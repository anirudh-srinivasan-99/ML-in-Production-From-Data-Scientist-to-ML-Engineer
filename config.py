from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from loguru import logger

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = '.env', env_file_encoding='utf-8')
    
    data_path: FilePath
    model_dir: DirectoryPath
    model_name: str

settings = Settings()

logger.add(
    "app.log", retention='1 week', rotation = '1 day',
    level = 'INFO'
)
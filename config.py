from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = '.env', env_file_encoding='utf-8')
    
    data_path: FilePath
    model_dir: DirectoryPath
    model_name: str

settings = Settings()
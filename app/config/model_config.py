"""This file is for Model Configuration."""
from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """Model Configuration."""

    model_config = SettingsConfigDict(
        env_file='app/config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )
    data_path: FilePath
    model_dir: DirectoryPath
    model_name: str


model_settings = ModelSettings()

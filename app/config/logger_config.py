"""This file is used for Logger Configuration."""

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """Logger Configuration."""

    model_config = SettingsConfigDict(
        env_file='app/config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )
    logger_level: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging application.

    :param log_level: Log Level.
    :type log_level: str
    """
    logger.remove()
    logger.add(
        r'app/log/app.log',
        retention='1 week',
        rotation='1 day',
        level=log_level,
    )


configure_logging(log_level=LoggerSettings().logger_level)

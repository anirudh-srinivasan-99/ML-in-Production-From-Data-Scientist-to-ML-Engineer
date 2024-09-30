"""This file is used for DB Table Models."""
from sqlalchemy import INTEGER, REAL, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.config.db_config import db_settings


class Base(DeclarativeBase):
    """Base class for SQL Alchemy."""

    pass  # noqa: WPS420, WPS604


class IPLData(Base):
    """SQLAlchemy model class for IPL Data."""

    __tablename__ = db_settings.ipl_data_table_name

    id: Mapped[int] = mapped_column(INTEGER(), primary_key=True)
    player_name: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    matches: Mapped[int] = mapped_column(INTEGER())
    innings: Mapped[int] = mapped_column(INTEGER())
    not_out: Mapped[int] = mapped_column(INTEGER())
    runs_in_2018: Mapped[int] = mapped_column(INTEGER())  # noqa:WPS114
    high_score: Mapped[str] = mapped_column(VARCHAR())
    average_score: Mapped[int] = mapped_column(INTEGER())
    balls_faced: Mapped[str] = mapped_column(VARCHAR())
    strike_rate: Mapped[float] = mapped_column(REAL())
    hundreds_scored: Mapped[int] = mapped_column(INTEGER())
    fifties_scored: Mapped[int] = mapped_column(INTEGER())
    fours_scored: Mapped[int] = mapped_column(INTEGER())
    sixes_scored: Mapped[int] = mapped_column(INTEGER())
    runs_in_2019: Mapped[int] = mapped_column(INTEGER())  # noqa:WPS114

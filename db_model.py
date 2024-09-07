from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import settings


class Base(DeclarativeBase):
    pass

class IPLData(Base):
    __tablename__ = settings.ipl_data_table_name

    id: Mapped[int] = mapped_column(INTEGER(), primary_key=True)
    player_name: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    matches: Mapped[int] = mapped_column(INTEGER())
    innings: Mapped[int] = mapped_column(INTEGER())
    not_out: Mapped[int] = mapped_column(INTEGER())
    runs_in_2018: Mapped[int] = mapped_column(INTEGER())
    high_score: Mapped[str] = mapped_column(VARCHAR())
    average_score: Mapped[int] = mapped_column(INTEGER())
    balls_faced: Mapped[str] = mapped_column(VARCHAR())
    strike_rate: Mapped[float] = mapped_column(REAL())
    hundreds_scored: Mapped[int] = mapped_column(INTEGER())
    fifties_scored: Mapped[int] = mapped_column(INTEGER())
    fours_scored: Mapped[int] = mapped_column(INTEGER())
    sixes_scored: Mapped[int] = mapped_column(INTEGER())
    runs_in_2019: Mapped[int] = mapped_column(INTEGER())


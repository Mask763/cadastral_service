from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean, func


class Base(DeclarativeBase):
    pass


class Query(Base):
    __tablename__ = "queries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cadastral_number: Mapped[str] = mapped_column(String, index=True)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    response: Mapped[bool] = mapped_column(Boolean)
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        index=True
    )

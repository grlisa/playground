from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field


class TimeStampMixin(BaseModel):
    __config__ = None
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False,
        )
    )

    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
            nullable=False,
        )
    )

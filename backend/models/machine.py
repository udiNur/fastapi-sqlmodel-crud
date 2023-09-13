from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from sqlalchemy import Enum as SAEnum

from sqlmodel import (
    SQLModel,
    Field,
    Column,
    String,
)

from models.enums import StateEnum


# SQLModel Definitions
class MachineBase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(10)))
    location: str
    email: EmailStr
    number: int
    float_number: float
    enum: StateEnum = Field(sa_column=Column(SAEnum(StateEnum)))
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    edited_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    password: str


class MachineBaseData(BaseModel):
    name: str
    location: str
    email: EmailStr
    number: int
    float_number: float
    enum: StateEnum


class MachineCreate(MachineBaseData):
    password: str


class MachineUpdate(MachineBaseData):
    pass


class MachineRead(MachineBaseData):
    id: Optional[int]
    created_at: datetime
    edited_at: datetime

from typing import Union
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class DeviceEnum(str, Enum):
    smartphone = 'smartphone'
    pc = 'pc'

class SearchEngineEnum(str, Enum):
    yandex = 'yandex'
    google = 'google'

class Position(BaseModel):
    key: str
    pos: int
    url: str
    date: datetime
    region: int
    device: DeviceEnum
    search_engine: SearchEngineEnum
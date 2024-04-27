from pydantic import BaseModel
from datetime import datetime
import enum
from typing import List, Dict


class DeviceEnum(enum.Enum):
    SMARTPHONE = "smartphone"
    PC = "pc"


class SearchEngineEnum(enum.Enum):
    YANDEX = "yandex"
    GOOGLE = "google"


class Position(BaseModel):
    key: str
    position: int
    url: str
    date: datetime
    region: int
    device: DeviceEnum
    search_engine: SearchEngineEnum


class SearchResult(BaseModel):
    pos: int
    url: str


class Data(BaseModel):
    results: List[SearchResult]


class TaskResult(BaseModel):
    status: str
    is_finished: bool
    created_at: datetime
    started_at: datetime
    finished_at: datetime
    data: Dict[str, Data]


class APIResponse(BaseModel):
    success: bool
    result: TaskResult

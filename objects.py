from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class Stop(BaseModel):
    departure: datetime
    delay: Optional[int]

class Stationboard(BaseModel):
    stop: Stop
    category: str
    number: Optional[int]
    to: str

class StationboardResponse(BaseModel):
    stationboard: List[Stationboard] = []

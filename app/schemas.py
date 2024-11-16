from pydantic import BaseModel
from datetime import datetime

class DomainCreate(BaseModel):
    domain_name: str

class DomainOut(BaseModel):
    id: int
    domain_name: str
    created_time: datetime
    https_enabled: bool

    class Config:
        orm_mode = True
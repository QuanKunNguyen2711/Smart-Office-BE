from pydantic import BaseModel, Field, ConfigDict
from .enums import Home

class Record(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: str = Field(...)
    value: int = Field(...)
    model_config = ConfigDict(
        populate_by_name=True
    )
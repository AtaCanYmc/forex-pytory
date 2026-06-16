from typing import Optional
from pydantic import BaseModel, Field


class EconomicEvent(BaseModel):
    id: Optional[str] = Field(default=None, alias="ID")
    time: Optional[str] = Field(default=None, alias="Time")
    currency: Optional[str] = Field(default=None, alias="Currency")
    event: Optional[str] = Field(default=None, alias="Event")
    forecast: Optional[str] = Field(default=None, alias="Forecast")
    actual: Optional[str] = Field(default=None, alias="Actual")
    previous: Optional[str] = Field(default=None, alias="Previous")
    impact: Optional[str] = Field(default=None, alias="Impact")

    model_config = {
        "populate_by_name": True,
    }

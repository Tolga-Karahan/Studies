from typing import List

from pydantic import BaseModel, Field, validator


class Features(BaseModel):
    features: List[float] = Field(...)

    @validator("features")
    def validate_features(cls, v: List[float]):
        if len(v) != 2:
            raise ValueError(
                "Inadequate number of features! You should provide two values!"
            )
        return v


class Prediction(BaseModel):
    prediction: int = Field(...)

import pytest

from adjoe_task.schemas.prediction_schemas import Features
from adjoe_task.routers.predictions_router import prediction


def test_prediction():
    input = Features(**{"features": [10, 15]})
    assert {"prediction": 0} == prediction(input)

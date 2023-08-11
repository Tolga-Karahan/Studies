from http.client import HTTPException
from catboost import CatBoostClassifier
from fastapi import APIRouter, Response, status
import logging

from adjoe_task.schemas.prediction_schemas import Features, Prediction

predictions_router = APIRouter(prefix="/predictions", tags=["Predictions"])
model = CatBoostClassifier().load_model("adjoe_task/model/example_model")
logger = logging.getLogger(__name__)


@predictions_router.post("/", status_code=status.HTTP_200_OK, response_model=Prediction)
def prediction(features: Features):
    try:
        feats = list(features.features)
        return {"prediction": model.predict(feats)}
    except ValueError:
        msg = "Invalid input format!"
        logger.exception(msg)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

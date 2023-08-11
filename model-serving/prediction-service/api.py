from fastapi import FastAPI

from adjoe_task.routers.predictions_router import predictions_router

api = FastAPI()


@api.get("/")
async def root():
    return {"api-version": "0.1.0"}


api.include_router(predictions_router)

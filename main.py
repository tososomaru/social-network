from fastapi import FastAPI

from src.social_network.api import router

app = FastAPI()
app.include_router(router)

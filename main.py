from fastapi import FastAPI

from api import router as api_router

app = FastAPI(
    title='Тайный Санта'
)
app.include_router(api_router)

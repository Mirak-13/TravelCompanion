from fastapi import FastAPI
from places_api.views import router as places_router
from hotels_api.views import router as hotels_router
app = FastAPI()
app.include_router(places_router)
app.include_router(hotels_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


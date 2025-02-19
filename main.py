from fastapi import FastAPI
from places_api.places_requests import router as places_router
app = FastAPI()
app.include_router(places_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

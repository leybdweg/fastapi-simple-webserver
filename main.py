from fastapi import FastAPI
from api.routes.main import api_router

app = FastAPI(
    title="we rock"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

print(f"aaaa")
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.routes.main import api_router
from app.di import availableStays


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialization: Start background task
    print("Starting up the application...")
    background_task = asyncio.create_task(availableStays.init())

    yield  # Application is running

    # Cleanup: Stop background task
    availableStays.keep_quote_loop_alive = False
    background_task.cancel()
    print("Shutting down the application...")
    try:
        await background_task
    except asyncio.CancelledError:
        print("Background task was cancelled.")


async def run_background_task():
    try:
        i = 0
        while i < 10:
            print("Background task is running...", i)
            await asyncio.sleep(5)  # Simulate periodic work
            i += 1
    except asyncio.CancelledError:
        print("Background task exiting gracefully...")

app = FastAPI(
    title="we rock",
    lifespan=lifespan
)

app.include_router(api_router)
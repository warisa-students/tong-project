import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI


async def continuous_monitor():
    """A background process that runs forever while the app is alive."""
    try:
        while True:
            print("Fetching telemetry data...")
            # Your continuous background logic here (e.g., database polling)

            # CRITICAL: Always use non-blocking asyncio.sleep
            await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Background task was cleanly cancelled.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Start the continuous process on app startup
    task = asyncio.create_task(continuous_monitor())
    yield
    # 2. Gracefully cancel the process when the app shuts down
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)

"""FastAPI application for the trip planner API."""
from fastapi import FastAPI

from server.routes import router

app = FastAPI(
    title="MtnBot API",
    description="API for generating mountaineering trip plans",
    version="0.1.0",
)

app.include_router(router)


@app.get("/healthz")
def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}

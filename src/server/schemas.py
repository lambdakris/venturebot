"""API request/response schemas for the trip planner API."""

from pydantic import BaseModel, Field

from server.models import TripPlan


class GeneratePlanRequest(BaseModel):
    """Request body for generating a trip plan."""

    trip_request: str = Field(
        description="Natural language trip planning request",
        examples=["Plan a winter climb of Mount Yale via East Ridge for January 25, 2026"],
    )


class GeneratePlanResponse(BaseModel):
    """Response body containing the generated trip plan."""

    trip_plan_data: TripPlan = Field(description="Structured trip plan")
    trip_plan_text: str = Field(description="Rendered markdown representation of the plan")


class ErrorResponse(BaseModel):
    """Error response body."""

    detail: str = Field(description="Error message")
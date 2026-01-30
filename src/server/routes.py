"""API routes for the trip planner."""

from fastapi import APIRouter, HTTPException

from server.agent import OrchestratorAgent
from server.renderer import render_to_markdown
from server.schemas import GeneratePlanRequest, GeneratePlanResponse
from server.settings import configure_dspy

router = APIRouter(prefix="/api", tags=["plans"])

# Initialize agent on module load
configure_dspy()
agent = OrchestratorAgent()


@router.post("/plans", response_model=GeneratePlanResponse)
def generate_plan(request: GeneratePlanRequest) -> GeneratePlanResponse:
    """Generate a trip plan from a natural language request.

    Args:
        request: The trip planning request

    Returns:
        Structured plan and rendered markdown

    Raises:
        HTTPException: If plan generation fails
    """
    try:
        result = agent(trip_request=request.trip_request)

        plan_data = result.trip_plan
        plan_text = render_to_markdown(plan_data)

        return GeneratePlanResponse(
            plan_data=plan_data, 
            plan_text=plan_text
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""DSPy agent for generating mountaineering trip plans."""

import dspy
from server.models import TripPlan


class ConstructTripPlan(dspy.Signature):
    """Cosntruct a comprehensive mountaineering trip plan.

    Formulate a detailed, safety-focused trip plan for the requested objective.
    Include all required sections and conditional sections as appropriate for the 
    trip type (winter routes need avalanche info, technical routes need special gear and obstacle details, etc.).
    """

    trip_request: str = dspy.InputField(
        desc="Free form trip request, typically including things like peak, route, date, season, and any preferences or constraints"
    )
    trip_plan: TripPlan = dspy.OutputField(
        desc="Complete structured trip plan with relevant sections"
    )


class OrchestratorAgent(dspy.Module):
    """Agent that constructs structured mountaineering trip plans."""

    def __init__(self):
        super().__init__()
        self.construct_trip_plan = dspy.ChainOfThought(ConstructTripPlan)

    def forward(self, trip_request: str) -> dspy.Prediction:
        """Construct a trip plan for the given trip request.

        Args:
            trip_request: Natural language trip planning request

        Returns:
            Prediction with a trip_plan
        """
        prediction = self.construct_trip_plan(trip_request=trip_request)
        return prediction
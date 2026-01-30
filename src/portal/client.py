"""HTTP client for the MtnBot API."""

import httpx


class MtnBotClient:
    """Client for interacting with the MtnBot API."""

    def __init__(self, base_url: str, timeout: float | None = None):
        """Initialize the client.

        Args:
            base_url: Base URL of the API server
            timeout: Request timeout in seconds (default 120s for LLM calls)
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def generate_plan(self, trip_request: str) -> dict:
        """Generate a trip plan.

        Args:
            trip_request: Natural language trip planning request

        Returns:
            Dict with 'plan_data' (structured) and 'plan_text' (rendered) keys

        Raises:
            httpx.HTTPStatusError: If the API returns an error status
            httpx.RequestError: If the request fails
        """
        with httpx.Client(timeout=self.timeout) as client:
            response = client.post(
                f"{self.base_url}/api/plans",
                json={"trip_request": trip_request},
            )
            response.raise_for_status()
            return response.json()

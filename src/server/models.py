"""Pydantic models for structured trip plan output."""

from pydantic import BaseModel, Field
from typing import List, Optional


class TripMetrics(BaseModel):
    """Quantitative trip measurements."""
    distance_miles: float = Field(description="Round trip distance in miles")
    elevation_gain_ft: int = Field(description="Total elevation gain in feet")
    elevation_summit_ft: int = Field(description="Summit elevation in feet")
    elevation_trailhead_ft: int = Field(description="Trailhead elevation in feet")
    duration_hours: str = Field(description="Estimated duration range, e.g. '8-10'")


class RouteSegment(BaseModel):
    """A segment of the route with timing details."""
    segment: str = Field(description="Segment name, e.g. 'Trailhead to Treeline'")
    destination: str = Field(description="Waypoint name and elevation")
    distance: str = Field(description="Segment distance, e.g. '3.2 mi'")
    elevation_change: str = Field(description="Elevation change, e.g. '+1,500 ft'")
    description: str = Field(description="Brief description of terrain and navigation")
    duration: str = Field(description="Estimated time, e.g. '1.5 hrs'")
    start_time: str = Field(description="Expected start time, e.g. '7:00 AM'")
    end_time: str = Field(description="Expected end time, e.g. '8:30 AM'")


class Participant(BaseModel):
    """Trip participant with emergency contact info."""
    name: str = Field(description="Participant's full name")
    phone: str = Field(description="Participant's phone number")
    emergency_contact: str = Field(description="Emergency contact name")
    emergency_phone: str = Field(description="Emergency contact phone number")


class WeatherConditions(BaseModel):
    """Weather forecast information."""
    forecast_links: List[str] = Field(
        description="URLs to weather forecasts (NOAA, Mountain Forecast, etc.)"
    )
    summary: str = Field(
        description="Brief summary of expected conditions and key concerns"
    )


class AvalancheConditions(BaseModel):
    """Avalanche forecast for winter/spring routes."""
    forecast_link: str = Field(description="URL to avalanche forecast (e.g. CAIC)")
    risk_level: str = Field(description="Overall risk: Low, Moderate, Considerable, High, Extreme")
    problems: List[str] = Field(description="Avalanche problems: wind slab, persistent slab, etc.")
    key_concerns: str = Field(description="Specific concerns for this route and aspect")


class EmergencyContact(BaseModel):
    """Emergency service contact information."""
    service: str = Field(description="Type of service: Emergency, Dispatch, Medical, Overdue")
    agency: str = Field(description="Agency or contact name")
    phone: str = Field(description="Phone number")
    notes: str = Field(description="Additional info: address, hours, links")


class TripPlan(BaseModel):
    """Complete structured trip plan."""

    # Metadata
    title: str = Field(description="Trip title, e.g. 'Mount Yale - East Ridge (Winter)'")
    date: str = Field(description="Trip date in YYYY-MM-DD format")
    objective: str = Field(description="Primary objective: peak name, elevation, route")
    trip_type: str = Field(
        description="Trip type: day_trip, multi_day, winter, spring_snow, technical, rock_scramble"
    )

    # Metrics
    metrics: TripMetrics

    # Location
    county: str = Field(description="County jurisdiction for SAR")
    area: str = Field(description="Wilderness area or recreation area name")

    # Timing
    sunrise: str = Field(description="Sunrise time for trip date, e.g. '7:15 AM'")
    sunset: str = Field(description="Sunset time for trip date, e.g. '5:00 PM'")
    turnaround_time: str = Field(description="Hard turnaround time, e.g. '12:00 PM'")

    # Summary
    summary: str = Field(description="Brief trip summary: objective, approach, key considerations")
    difficulty: str = Field(description="Difficulty: class rating, technical requirements, fitness level")

    # Logistics
    carpool_time: str = Field(description="Expected carpool departure time")
    carpool_name: str = Field(description="Carpool location name")
    carpool_location: str = Field(description="Carpool location pin or coordinates")
    trailhead_time: str = Field(description="Expected trailhead arrival time")
    trailhead_name: str = Field(description="Trailhead location name")
    trailhead_location: str = Field(description="Trailhead location pin or coordinates")

    # Route
    route_map_link: str = Field(description="URL to route map (CalTopo, GaiaGPS, Google Maps, etc.)")
    route_overview: str = Field(description="High-level route description and navigation notes")
    route_segments: List[RouteSegment] = Field(description="Detailed route segments with timing")

    # Conditions
    weather: WeatherConditions
    avalanche: Optional[AvalancheConditions] = Field(
        default=None,
        description="Avalanche conditions - include for winter/spring snow routes"
    )

    # Equipment
    personal_gear: List[str] = Field(description="Required personal gear items")
    group_gear: List[str] = Field(description="Required group gear items")
    winter_gear: Optional[List[str]] = Field(
        default=None,
        description="Winter-specific gear - include for winter routes"
    )
    technical_gear: Optional[List[str]] = Field(
        default=None,
        description="Technical gear - include for technical routes"
    )

    # Emergency
    emergency_action_plan: str = Field(
        description="Step-by-step emergency procedures"
    )
    emergency_contacts: List[EmergencyContact] = Field(
        description="Emergency contacts: 911, dispatch, hospital, overdue contact"
    )

    # Optional sections
    technical_sections: Optional[str] = Field(
        default=None,
        description="Detailed information for technical sections (rappels, etc.)"
    )
    bailout_options: Optional[str] = Field(
        default=None,
        description="Escape routes and when to use them"
    )
    objective_hazards: Optional[str] = Field(
        default=None,
        description="Significant hazards and mitigation strategies"
    )

    # Participants (often filled in later, but structure is defined)
    participants: List[Participant] = Field(
        default_factory=list,
        description="Trip participants - may be empty if not yet determined"
    )
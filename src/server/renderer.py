"""Render structured TripPlan to markdown format using Jinja2."""

from pathlib import Path

import jinja2

from server.models import TripPlan


# Set up Jinja2 environment
template_dir = Path(__file__).parent / "templates"
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_to_markdown(plan: TripPlan) -> str:
    """Render a structured TripPlan to markdown with YAML frontmatter.

    Args:
        plan: Structured TripPlan object

    Returns:
        Complete markdown document with YAML frontmatter
    """
    template = template_env.get_template("trip_plan.md.j2")
    return template.render(plan=plan)

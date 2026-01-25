# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MtnBot is a DSPy-based AI agent that helps users create trip plans for mountaineering activities. The agent transforms "I want to climb something" into comprehensive, safety-conscious trip plans.

## Current Status

**Phase 0 (Discovery and Framing): COMPLETE**
- Canonical trip plan templates created
- META/EVENT planning distinction established
- Example plans created (Mount Yale East Ridge - Winter)

**Phase 1 (Baseline Agent + Error Analysis): IN PROGRESS**
- Structured output agent implemented (Pydantic models + Jinja2 renderer)
- Client-server architecture (FastAPI + Streamlit)
- Docker Compose for local development
- Next: Generate 20-30 trip plans, manual review, discover failure modes

**Architecture decision:** Unified agent with structured output. Single `TripPlan` model contains both stable (META-like) and temporal (EVENT-like) information.

## Commands

```bash
# Install dependencies
uv sync

# Start the Server and GUI using docker compose
docker compose up

# Run tests
pytest
```

## Architecture

### Client-Server Architecture

```
┌─────────────────┐       HTTP        ┌─────────────────┐
│  Streamlit App  │  ──────────────>  │   FastAPI API   │
│   (src/portal/)    │  POST /api/plans  │  (src/server/)  │
└─────────────────┘                   └─────────────────┘
```

### Server Components (`src/server/`)

- **`main.py`**: FastAPI application entry point
- **`routes.py`**: API endpoints (`POST /api/plans`)
- **`schemas.py`**: Request/response Pydantic models
- **`agent.py`**: DSPy agent with `OrchestratorAgent` and `ConstructTripPlan` signature
- **`models.py`**: Pydantic models for structured trip plan output (`TripPlan`, etc.)
- **`renderer.py`**: Jinja2-based markdown renderer
- **`templates/`**: Jinja2 templates for rendering
- **`settings.py`**: DSPy and LangWatch configuration
- **`cli.py`**: CLI entry point (bypasses API)

### Portal Components (`src/portal/`)

- **`main.py`**: Streamlit web interface
- **`client.py`**: HTTP client for the API

### Key Concepts

**META vs EVENT Planning**: Trip planning divides into two phases:
- **META Plans**: Stable blueprints for a peak/route/season (e.g., "Mount Yale East Ridge - Winter"). Created once, reused.
- **EVENT Plans**: Temporal details for a specific attempt (e.g., "Mount Yale East Ridge on January 17"). Created per trip.

### Development Methodology

This project follows Hamel Husain's error-analysis-first approach:
- Error analysis before infrastructure (manually review 20-50 outputs first)
- Custom evaluators for specific failure modes (not generic metrics)
- Binary pass/fail criteria (no Likert scales)
- Expect 60-80% of development time on error analysis

## Environment Variables

Required in `.env`:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4o-mini
- `LANGWATCH_API_KEY`: LangWatch API key for monitoring (optional)

## Project Assets

**Templates & Examples** (`assets/templates/`):
- `trip_plan_template.md`: Canonical template with YAML frontmatter + markdown
- `schema.yaml`: Machine-readable schema for validation
- `trip_planning_process.md`: Complete planning workflow documentation
- `examples/mount_yale_east_ridge_winter_META.md`: Example META plan
- `examples/mount_yale_east_ridge_winter_EVENT_2026-01-17.md`: Example EVENT plan

**Documentation** (`docs/`):
- `project_overview.md`: Project overview, phases, methodology, terminology

**Archive** (`archive/`):
- Historical session summaries from completed phases

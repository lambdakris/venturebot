# MtnBot

An AI agent built with DSPy to help create mountaineering trip plans.

## What It Does

MtnBot transforms "I want to climb something" into comprehensive, safety-conscious trip plans. It understands two planning phases:

- **META Plans** - Reusable blueprints for a peak/route/season (e.g., "Mount Yale East Ridge - Winter")
- **EVENT Plans** - Specific attempt details with date, conditions, forecast, participants, etc.

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- Docker and Docker Compose (optional)

### Setup

1. Clone the repository
2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

### Usage

**Start the Server and Portal using docker compose:**
```bash
docker compose up
```
- Server: http://localhost:8000
- Portal: http://localhost:8501

## Docker Compose Architecture

The system runs as two containerized services defined in `compose.yml`:

| Service | Port | Dockerfile | Description |
|---------|------|------------|-------------|
| `server_service` | 8000 | `src/server/Dockerfile` | FastAPI backend |
| `portal_service` | 8501 | `src/portal/Dockerfile` | Streamlit frontend |

### Container Structure

Each service has its own Dockerfile and runs in an isolated container:

```
src/
├── server/
│   ├── Dockerfile      # WORKDIR /src/server
│   ├── main.py         # FastAPI app
│   └── ...
└── portal/
    ├── Dockerfile      # WORKDIR /src/portal
    ├── main.py         # Streamlit app
    └── ...
```

### Import Path Nuance

The container working directory structure affects Python imports:

- **FastAPI (server)**: Uses `WORKDIR /src/server`. Imports are relative to the parent (`/src`), so use `from server.models import TripPlan`.
- **Streamlit (portal)**: Uses `WORKDIR /src/portal`. Imports within the portal are relative (e.g., `from client import MtnBotClient`).

This means the container's working directory name must match the module name used in imports.

### Common Commands

```bash
# Start all services
docker compose up

# Start in background
docker compose up -d

# Rebuild after code changes
docker compose up --build

# View logs
docker compose logs -f

# Stop all services
docker compose down
```

## Project Status

**Phase 1: Baseline Agent + Error Analysis** (current)

- Phase 0 (Discovery and Framing - define the problem to be solved or jobs to be done, frame the baseline inputs, outputs, and process): Complete
- Phase 1: Generate trip plans, manual review, discover failure modes
- Phase 2: Custom DSPy evaluators (upcoming)
- Phase 3: Optimization with DSPy (upcoming)

## Documentation

- [Project Overview](docs/project_overview.md) - Methodology, phases, architecture decisions
- [Trip Planning Process](assets/templates/trip_planning_process.md) - Complete planning workflow
- [Templates](assets/templates/) - Trip plan templates, schema, and examples

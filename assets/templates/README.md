# Trip Plan Templates

Templates and schema for mountaineering trip plans.

## Contents

- **`trip_plan_template.md`** - Canonical trip plan template with YAML frontmatter and markdown sections
- **`schema.yaml`** - Machine-readable schema for validation and DSPy integration
- **`trip_planning_process.md`** - Complete planning workflow documentation
- **`examples/`** - Example plans demonstrating the template

## Template Structure

The template uses:
- **YAML frontmatter** for structured metadata (machine-readable)
- **Markdown sections** for narrative content (human-readable)

### Required Sections
- Summary
- Participants
- Transportation & Logistics
- Route (with map, overview, detailed plan)
- Conditions (weather, avalanche if applicable)
- Equipment (personal + group)
- Emergency Information

### Conditional Sections (include when relevant)
- **Avalanche Forecast** - Winter/spring snow routes
- **Technical Sections** - Routes with rappels, exposed climbing
- **Bailout Options** - Technical routes with commitment
- **Objective Hazards** - Explicit hazard analysis
- **Sources** - Attribution to beta sources

## Usage

### For Manual Trip Planning

1. Copy `trip_plan_template.md`
2. Fill in YAML frontmatter with trip metadata
3. Complete required sections
4. Add conditional sections as needed
5. Replace all `[brackets]` with actual data

### For Agent Development

1. Use template as few-shot example in DSPy signature
2. Reference `schema.yaml` for validation criteria
3. Use examples as reference outputs

## Examples

| Example | Type | Demonstrates |
|---------|------|--------------|
| `mount_yale_east_ridge_winter_META.md` | META plan | Reusable objective blueprint |
| `mount_yale_east_ridge_winter_EVENT_2026-01-17.md` | EVENT plan | Specific attempt with conditions |
| `quandary_peak_winter_reformatted.md` | Full plan | Winter trip, decision points |
| `citadel_pettingell_traverse_reformatted.md` | Full plan | Technical route with rappel |

## Formatting Guidelines

- Use **specific times** ("6:30 AM" not "morning")
- Use **specific numbers** ("10.2 mi" not "about 10 miles")
- Include **coordinates** for key waypoints (decimal degrees)
- Use **tables** for participants, route segments, emergency contacts
- Include **links** to all maps and forecasts

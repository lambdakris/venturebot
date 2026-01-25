# MtnBot: Project Overview

**Project Name:** MtnBot
**Purpose:** An agentic system to help users create trip plans for mountaineering activities
**Framework:** DSPy (Python)
**Methodology:** Error-analysis-first approach (Hamel Husain)

---

## Intent

Build an AI-powered agent that assists with planning mountaineering trips. The agent should help users go from "I want to climb something" to a complete, safety-conscious trip plan.

**The final artifact:** A comprehensive trip plan document that a mountaineer could use to safely execute an objective.

---

## Target Capabilities

The agent should be able to:

1. **Suggest mountaineering routes** based on user experience and preferences
2. **Provide gear and packing lists** for specific trips
3. **Check weather conditions and forecasts** for mountain regions
4. **Inform users about permit requirements and regulations**
5. **Plan multi-day itineraries** including camp spots

---

## Key Constraints & Decisions

### 1. Trip Plans as Final Artifact

Trip plans (examples in `assets/plans/`) are the target output. The agent's success is measured by the quality of the trip plans it produces.

### 2. DSPy as Primary Framework

Use DSPy for:
- Structured signatures and modules (not free-form prompts)
- Datasets and examples
- Evaluation framework
- Optimization (teleprompters like BootstrapFewShot, MIPRO)

### 3. Error-Analysis-First Methodology

Following Hamel Husain's approach from [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/):

**Core principles:**
- **Error analysis first:** Manually review 20-50 outputs before building infrastructure
- **Custom evaluators:** Build evaluators for YOUR specific failure modes, not generic metrics
- **Binary pass/fail:** Avoid Likert scales, use clear pass/fail criteria
- **Validate evaluators:** Test against human judgment
- **Resource allocation:** Expect 60-80% of time on error analysis, not coding
- **Iterate on data:** Not on theory or intuition

**What to avoid:**
- Generic evaluation metrics (waste time, create false confidence)
- Outsourcing error analysis (breaks feedback loop)
- Eval-driven development (writing tests before understanding failures)
- Building infrastructure before seeing real failures

### 4. User Highly Involved

The user (an experienced mountaineer) is deeply involved in:
- Reviewing agent outputs
- Identifying failure modes
- Validating evaluator accuracy
- Providing domain expertise

---

## Key Discovery: META vs EVENT Planning

Through our Phase 0 work, we discovered that trip planning naturally divides into two phases:

### META Planning (Objective Blueprint)

**What:** Stable, reusable information about a peak/route/season combination

**Example:** "Mount Yale East Ridge - Winter"

**Contains:**
- Route description and navigation
- Typical hazards for that season
- Standard gear requirements
- Baseline timing estimates
- Emergency information (jurisdiction, hospital)
- Where to check conditions (links to forecasts, trip reports)

**Characteristics:**
- Created once, referenced many times
- Updated as new information emerges
- Season-specific (winter ≠ summer)

### EVENT Planning (Specific Attempt)

**What:** Temporal information for a specific attempt

**Example:** "Mount Yale East Ridge - Winter on January 17, 2026"

**Contains:**
- Specific date and participants
- Current weather forecast
- Current avalanche forecast
- Recent trip reports
- Specific timing (sunrise/sunset for that date)
- Go/no-go decision framework

**Characteristics:**
- Created for each attempt
- References the META plan
- Disposable after the trip (archived for learning)

---

## Scope

### In Scope

- Trip plan generation (META and EVENT)
- Objective discovery (find peaks matching criteria)
- Information synthesis from multiple sources
- Conditions monitoring guidance
- Gear recommendations
- Safety information

### Out of Scope (User Responsibility)

- Plan B/C/D development (user uses agent again for different objective)
- Final go/no-go decisions (agent provides info, user decides)
- Real-time field decisions (this is a planning tool, not field guide)
- Booking/reservations
- Social coordination (finding partners)

---

## Development Phases

### Phase 0: Discovery and Framing ✅ COMPLETE

**Goal:** Define what "good" looks like

**Deliverables:**
- Canonical trip plan template
- Machine-readable schema
- Example plans (META and EVENT)
- Documented planning process

### Phase 1: Baseline Agent + Error Analysis (NEXT)

**Goal:** Generate outputs and discover failure modes

**Activities:**
- Enhance DSPy agent with META/EVENT awareness
- Generate 20-30 trip plans
- Manual review of ALL outputs
- Document failure taxonomy

### Phase 2: Custom DSPy Evaluators

**Goal:** Build evaluators for persistent failure modes

**Activities:**
- Create evaluators for specific failures (not generic)
- Validate against human judgment
- Integrate with DSPy evaluation framework

### Phase 3: Optimization with DSPy

**Goal:** Improve agent using DSPy teleprompters

**Activities:**
- Manual improvements first
- DSPy optimization (BootstrapFewShot, MIPRO, COPRO)
- Validation and iteration

### Phase 4: Production Readiness (Future)

**Goal:** Deploy with proper monitoring

**Activities:**
- Guardrails for safety-critical info
- Async evaluation of outputs
- Ongoing error analysis
- Multi-turn conversation capabilities

---

## User Context

### Primary Use Case

Planning mountaineering trips in Colorado, primarily:
- 14ers (peaks over 14,000 ft)
- Winter, spring, and summer objectives
- Day trips and multi-day trips
- Technical and non-technical routes

### User Profile

- Experienced winter mountaineer
- Comfortable with Class 2-3 scrambling
- Avalanche awareness trained
- GPS navigation proficient
- Conservative safety approach ("mountains will be there tomorrow")

### Geographic Focus

- **Primary:** Colorado (Sawatch, Front Range, San Juans, etc.)
- **Secondary:** Pacific Northwest, other regions
- **Resources:** 14ers.com, CAIC, SummitPost, regional sources

---

## Design Principles

### Safety First

- Emergency information always prominent
- Turnaround times enforced
- Abort criteria clear
- Hazards identified and mitigated
- "Check and see" mindset supported

### Judgment Support, Not Replacement

- Agent provides information and analysis
- User makes final decisions
- Uncertainty acknowledged ("conditions may vary")
- Multiple information sources provided

### Real-World Workflow

- Match how experienced mountaineers actually plan
- Acknowledge information fragmentation
- Support iterative refinement
- Embrace incomplete information

### Specific Over Vague

- Specific times ("6:30 AM" not "morning")
- Specific distances ("10.5 mi" not "about 10 miles")
- Specific coordinates for waypoints
- Specific sources cited

---

## Key Resources

### Route Information
- 14ers.com (Colorado-specific)
- SummitPost (broader coverage)
- Mountain Project (technical)
- Regional guidebooks

### Weather
- NOAA Point Forecast
- Mountain Forecast
- OpenSnow

### Avalanche
- CAIC (Colorado)
- Regional avalanche centers

### Conditions
- SNOTEL (snow depth)
- Trip reports (14ers.com, Reddit, Facebook, blogs)
- Road conditions (CoTrip)

---

## Success Metrics

### Phase 1 Success

- Agent generates plausible META and EVENT plans
- Failure modes documented and understood
- Foundation for custom evaluators established

### Overall Success

- Trip plans are usable by real mountaineers
- Safety-critical information is complete and accurate
- Plans match the quality of hand-crafted examples
- Agent saves significant planning time while maintaining quality

---

## Template Design Decision

Three approaches were considered for handling META vs EVENT plans:

**Option 1: Two Separate Templates**
- Separate META template (route, difficulty, hazards, gear, timing) and EVENT template (date, participants, conditions, logistics)
- Pros: Clear separation, independent evaluation
- Cons: Two templates to maintain, event must reference meta

**Option 2: Unified Template with Markers**
- Single template with `[META]`, `[EVENT]`, `[BOTH]` section tags
- Pros: Single template, clear relationship between meta/event
- Cons: Could be confusing which sections to fill when

**Option 3: Inheritance Model**
- Event plans "inherit" from meta plans as diffs/overlays
- Pros: Elegant, shows what changed for specific attempt
- Cons: More complex to implement, requires tooling

**Decision:** Unified approach with structured output. A single `TripPlan` Pydantic model contains both stable (META-like) and temporal (EVENT-like) information. The agent generates complete plans; the META/EVENT distinction is conceptual knowledge, not separate artifacts.

---

## Terminology

- **Objective** - A specific peak/route/season combination (e.g., "Quandary East Ridge - Winter")
- **Event/Attempt** - A specific planned ascent with date, people, conditions
- **Meta Plan** - Reusable objective blueprint with stable information
- **Event Plan** - Temporal plan for a specific attempt
- **14er** - A peak with summit elevation above 14,000 feet
- **Class Rating** - Yosemite Decimal System difficulty rating (Class 1-5)
- **Bailout** - Alternative descent or escape route if conditions deteriorate
- **Turnaround Time** - Hard deadline for reaching summit or turning back
- **Beta** - Route information, tips, and tricks from other climbers

---

## References

- [Hamel's LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) - Methodology
- [DSPy Documentation](https://dspy.ai/) - Framework
- [LangWatch](https://langwatch.ai/) - Evaluation and monitoring
- `assets/templates/trip_planning_process.md` - Detailed planning workflow
- `assets/templates/trip_plan_template.md` - Canonical template
- `assets/templates/schema.yaml` - Validation schema

---

## Document History

**Created:** 2026-01-05
**Last Updated:** 2026-01-05
**Status:** Living document

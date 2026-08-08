# Anduril Air Defense Human Factors Interview System

A dedicated Lead/Staff interview coach for **Dr. Brandon Fluegel**, targeting a **Human Factors Research Lead / Staff Human Factors Engineer** role with Anduril Industries' Air Defense team.

The system pressure-tests Brandon's central thesis, **Calibrated Cognitive Friction**, against four interviewer perspectives: Dr. Daniella Kim (Research Head), Systems/ML Engineering, Product, and Design. It preserves the repository's five-dimension scoring and calibration mechanics while removing general job-search workflows.

## What Is Preloaded

- `data/candidate_profile.json`: canonical education, experience, philosophy, and evidence limits
- `data/target_anduril_air_defense.json`: Air Defense target, mission, panel, and uplevel priorities
- `data/storybank_6_pillars.json`: six STAR pillars with explicit earned secrets
- `coaching_state.md`: active Anduril loop, story details, readiness assessment, and coaching strategy
- `references/role-drills.md`: four specialized interviewer personas

Claims with incomplete evidence are explicitly marked for validation. The coach must not invent company details, study outcomes, operational facts, or prior interactions with Dr. Kim.

## Scoring

Every answer receives the five core 1-5 scores:

- Substance
- Structure
- Relevance
- Credibility
- Differentiation

It also evaluates eight Lead/Staff criteria when evidenced:

- Research Thesis
- Empirical Rigor
- Research Velocity
- Systems Integration
- Cross-Functional Influence
- Standard Setting
- Operational Judgment
- Executive Communication

Missing evidence receives `N/E`, not an artificial low score.

## Gradio App

The app accepts clean text dictated through Superwhisper, sends the loaded `SKILL.md` and `coaching_state.md` context to OpenAI `gpt-4o`, and returns concise in-character pushback followed by a structured scorecard.

### Setup

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OPENAI_API_KEY="your-key"
python src\app.py
```

The app launches on `0.0.0.0:7860` and requests a public Gradio share URL for remote access from an iPhone. Treat the share URL as public: anyone with the link can reach the interface while the process is running.

## Focused Commands

| Command | Purpose |
|---|---|
| `research` | Verify Anduril, Air Defense, interviewer, and process claims |
| `decode` | Extract Lead/Staff signals from the target requisition |
| `prep` | Build the panel strategy and story mapping |
| `stories` | Improve and validate the six canonical pillars |
| `concerns` | Rank likely uplevel objections and counter-evidence |
| `questions` | Prepare questions for Dr. Kim and cross-functional leads |
| `practice kim` | Research thesis, rigor, telemetry, and velocity |
| `practice systems` | Failure modes, system requirements, standards, and uFMEA |
| `practice product` | Shipping speed, ROI, risk, and tradeoffs |
| `practice design` | C2 workflow, ergonomics, modalities, and density |
| `mock panel` | Run a full cross-functional interview simulation |
| `present` | Prepare a research or case presentation |
| `analyze` | Score an answer or transcript |
| `debrief` | Capture same-day interview evidence |
| `feedback` | Record feedback, corrections, and outcomes |
| `progress` | Review score trends and Lead/Staff readiness |
| `salary` | Handle pre-offer compensation questions |
| `thankyou` | Draft an evidence-specific follow-up |
| `reflect` | Archive the interview cycle and lessons learned |
| `help` | Show focused recommendations from current state |

## Recommended Starting Sequence

1. Verify the exact requisition and Dr. Kim keynote source with `research`.
2. Pressure-test the research thesis with `practice kim`.
3. Convert it into requirements and failure controls with `practice systems`.
4. Defend speed and ROI with `practice product`.
5. Translate it into C2 workflow decisions with `practice design`.
6. Run `mock panel`, then review trends with `progress`.

## Architecture

`SKILL.md` is the global router. Command workflows live in `references/commands/`; scoring and calibration remain in the shared reference files. The JSON files are canonical source data, while `coaching_state.md` is mutable session state. The Gradio app reloads prompt and state context for every evaluation so edits are picked up without changing application code.

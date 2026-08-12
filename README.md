# Anduril Voice Interview Coach

A continuous multi-turn interview simulator for Brandon Fluegel, PhD, targeting Anduril Industries' Air Defense team. The Gradio interface supports Superwhisper dictation, browser speech playback, four interviewer personas, and a holistic Senior-versus-Lead/Staff debrief at the end of the session.

The interviewer stays fully in character for every live turn. The conversation runs for as many turns as you want, and **no grading appears until you finalize the session** — the persona probes, pushes back, and re-probes thin answers instead of scoring them in the moment.

## Interview Arc

The first four turns follow an arc used as stage direction, not as a hard cutoff:

1. Technical and domain core
2. Deep-dive pushback and probe
3. Behavioral and cross-functional friction
4. Leadership, scaling, and vision

The persona is locked for the duration of a session and held in state. An optional target-pillar drill narrows the ground the session covers. Every live turn receives the full transcript plus the running claim ledger and covered-pillar list, so a covered pillar is never repeated except when the interviewer is deliberately holding the same ground.

On finalize, the session is scored on **Substance, Structure, Relevance, Credibility, and Differentiation**, plus separate Lead/Staff criteria where evidenced. `N/E` means not evidenced and is never converted into a low score. STAR/STARE is applied to behavioral and experience answers only; technical and research-craft answers are judged on claim, method, evidence and limits, threshold or decision, and what would change it.

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:OPENAI_API_KEY="your-key"
python src\app.py
```

Open http://localhost:7860.

Public sharing is disabled by default. To request a temporary public Gradio URL, set `$env:GRADIO_SHARE="true"` before launch and treat the resulting URL as public.

## Tabs

- **🛡️ Interview Simulator** — persona and optional pillar selection, question playback, dictated or typed answers, *Submit Answer / Continue Conversation*, and *Wrap Up & Finalize Session*.
- **📈 Progress & 1-Week Sprint Tracker** — mock-session averages, upleveling readiness, bottlenecks, next actions, the Pillar Coverage matrix derived from persisted pillar IDs, recent-session history, and the seven-day intensive sprint checklist.

Finalized session summaries, including the turn count and the covered pillar IDs, persist to `data/coaching_state.md`.

## Runtime Context

`src/app.py` reloads these files for each model request.

| File | Contents |
|---|---|
| `data/candidate_profile.json` | Canonical resume evidence and closed logistics topics |
| `data/target_anduril_air_defense.json` | Role requirements and the upleveling bar |
| `data/storybank_6_pillars.json` | Nine approved stories (S001–S009), each tagged with an evidence tier and a do-not-claim boundary |
| `data/technical_questions.json` | Ten technical and research-craft pillars |
| `data/behavioral_questions.json` | Ten defense-tech behavioral and fit pillars |
| `data/culture_questions.json` | Ten culture, mission-fit, and stakeholder-collaboration pillars with named stakeholder groups |
| `data/positioning_questions.json` | Ten positioning, scope, and close pillars for the hiring-manager conversation and the end of any session |
| `data/coaching_state.md` | Mutable readiness and session state |
| `references/role-drills.md` | The four interviewer persona definitions |
| `references/rubrics-detailed.md` | Detailed scoring anchors |

Every question bank carries persona adaptations, follow-up probes, and a Lead/Staff bar for each pillar.

### Evidence boundaries

The coach never invents metrics, outcomes, clearance status, classified details, team structure, or prior familiarity with an interviewer. Candidate claims are context to probe, not evidence that a competency was demonstrated.

The recruiter screen is complete: **location, compensation, travel, and clearance are settled** and are never asked about or treated as gaps. Level is the only open item, and it is argued from scope rather than title.

## Practice Set

`practice/` holds the written answer bank — 40 pillars with one model answer each, all follow-ups answered at follow-up length, and the Senior → Lead/Staff delta per pillar.

- `00-response-architecture.md` — the two answer structures, length discipline, uplevel moves, evidence boundaries, drill protocol, and a one-page cheat sheet
- `01-technical-track.md` — TQ01–TQ10
- `02-behavioral-track.md` — BQ01–BQ10
- `03-culture-stakeholder-track.md` — CQ01–CQ10
- `04-positioning-close-track.md` — PQ01–PQ10

Placeholders in `[brackets]` mark facts only the candidate can supply. Fill them in or cut the sentence — never improvise a number, a name, or an outcome.

### Printing

```powershell
python scripts\build_practice_html.py
```

Renders each markdown file plus a combined `ALL-tracks.html` into `practice/print/`, styled for two-column printing at 10.5pt. Open the combined file in a browser and `Ctrl+P` with **Background graphics** enabled. Generated output is gitignored; regenerate after editing any practice markdown.

## Validation

```powershell
python -m py_compile src\app.py
python -m pip check
python scripts\smoke_check.py              # offline: scorecard rendering, persistence, dashboard reads
python scripts\check_env.py                # verifies OPENAI_API_KEY authenticates
python scripts\live_integration_test.py    # live multi-turn run against the real API
```

`smoke_check.py` needs no API key. `check_env.py` and `live_integration_test.py` both call OpenAI.

## Notes

The application requires `OPENAI_API_KEY` for question generation and answer evaluation. Browser speech playback uses the Web Speech API; `pyttsx3` remains available for local or offline speech extensions.

OpenAI requests use structured responses with complete score-set validation, run under a bounded timeout, and preserve in-browser session state when a timeout, connection failure, rate limit, or API error occurs.

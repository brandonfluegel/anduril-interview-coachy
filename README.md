# Anduril Voice Interview Coach

A focused four-question interview simulator for Brandon Fluegel, PhD, targeting Anduril Industries' Air Defense team. The Gradio interface supports Superwhisper dictation, browser speech playback, four adaptive interviewer personas, structured answer scoring, and a final Senior-versus-Lead/Staff debrief.

## Interview Arc

1. Technical and Domain Core
2. Deep-Dive Pushback and Probe
3. Behavioral and Cross-Functional Collaboration
4. Leadership, Scaling, and Vision

Every answer is scored on Substance, Structure, Relevance, Credibility, and Differentiation, plus eight Lead/Staff criteria when evidenced.

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

## Runtime Context

- `data/candidate_profile.json`: canonical resume evidence
- `data/target_anduril_air_defense.json`: canonical role requirements
- `data/storybank_6_pillars.json`: six approved interview stories
- `data/coaching_state.md`: active readiness and session context
- `references/role-drills.md`: interviewer persona definitions
- `references/rubrics-detailed.md`: detailed scoring anchors

`src/app.py` reloads these files for each model request. It never treats unsupported resume claims, clearance status, classified details, or interviewer familiarity as established facts.

## Validation

```powershell
python -m py_compile src\app.py
python -m pip check
```

The application requires `OPENAI_API_KEY` for question generation and answer evaluation. Browser speech playback uses the Web Speech API; `pyttsx3` remains available for local/offline speech extensions.

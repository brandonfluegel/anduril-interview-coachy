---
title: Anduril Human Factors Interview Coach
emoji: 🛡️
colorFrom: gray
colorTo: red
sdk: gradio
sdk_version: 6.22.0
app_file: src/app.py
pinned: false
short_description: Lead/Staff interview pressure testing for Air Defense Human Factors
---

# Anduril Voice Interview Coach

A continuous multi-turn interview simulator for Brandon Fluegel, PhD, targeting Anduril Industries' Air Defense team. The Gradio interface records your spoken answer, transcribes it verbatim through the OpenAI API, plays the interviewer's questions back in each persona's own voice, and produces a holistic Senior-versus-Lead/Staff debrief at the end of the session. No third-party dictation tool is involved: everything runs on `OPENAI_API_KEY`.

The interviewer stays fully in character for every live turn. The conversation runs for as many turns as you want, and **no grading appears until you finalize the session** — the persona probes, pushes back, and re-probes thin answers instead of scoring them in the moment.

## Interview Arc

The first four turns follow an arc used as stage direction, not as a hard cutoff:

1. Technical and domain core
2. Deep-dive pushback and probe
3. Behavioral and cross-functional friction
4. Leadership, scaling, and vision

The persona is locked for the duration of a session and held in state. An optional target-pillar drill narrows the ground the session covers. Every live turn receives the full transcript plus the running claim ledger and covered-pillar list, so a covered pillar is never repeated except when the interviewer is deliberately holding the same ground.

On finalize, the session is scored on **Substance, Structure, Relevance, Credibility, and Differentiation**, plus separate Lead/Staff criteria where evidenced. `N/E` means not evidenced and is never converted into a low score. STAR/STARE is applied to behavioral and experience answers only; technical and research-craft answers are judged on claim, method, evidence and limits, threshold or decision, and what would change it. Structure is graded against the beats and length targets in `practice/00-response-architecture.md`, including follow-up answers that re-narrate the original story.

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

- **🛡️ Interview Simulator** — persona and optional pillar selection, spoken question playback, the recorder, and *Wrap Up & Finalize Session*. Playback works on headphones or a phone speaker: touching the transcript cuts the interviewer off mid-sentence so the mic never picks up the question while you speak. The transcript, the typed-answer submit, and the audio controls sit in collapsed panels so the question and the recorder own the screen.

Stopping the recording submits it: the answer is transcribed verbatim, stamped with its real spoken duration, and sent straight to the interviewer. With **Hands-free turn taking** on, the mic opens on its own when the interviewer finishes speaking and closes after about two seconds of silence, so a whole session runs without touching a button. The first recording of a session still needs one manual press to grant microphone permission. Typed answers use *Submit typed answer* and have their length estimated at 150 words per minute instead of measured.

> **On a phone, use the share URL.** Browsers only grant microphone access in a secure context. `https://…gradio.live` (via `GRADIO_SHARE`) and `localhost` qualify; a plain `http://192.168.…` LAN address does not, and the recorder will silently fail to start.
- **📈 Progress & 1-Week Sprint Tracker** — mock-session averages, upleveling readiness, bottlenecks, next actions, the Pillar Coverage matrix derived from persisted pillar IDs, recent-session history, and the seven-day intensive sprint checklist.

Finalized session summaries, including the turn count and the covered pillar IDs, persist to `data/coaching_state.md`. **⬇︎ Download grades & feedback** appears after you finalize and saves the full debrief — scores, quoted evidence, pacing, and the Lead/Staff read — as a markdown file. Keep those files to track performance over time; they are the record that survives a host with no persistent disk.

## Running It Without a PC

The repo is configured as a Gradio Space (see the front matter at the top of this file).

1. Create a **private** Space on Hugging Face with the Gradio SDK.
2. Push this repo to it.
3. In *Settings → Variables and secrets*, add `OPENAI_API_KEY`.

The Space serves real HTTPS, so Safari grants microphone access, and being private means your Hugging Face login is the only way in. Note that a free Space has an ephemeral filesystem: interviews and grading work normally, but `data/coaching_state.md` resets when the Space rebuilds — which is what the download button is for.

To run it from your own machine instead, `python src\app.py` and reach it at `http://localhost:7860`. For phone access from a local run you need an HTTPS tunnel, since browsers block the microphone on plain `http://` LAN addresses.

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
| `practice/00-response-architecture.md` | Answer-structure beats and length discipline the debrief grades against |

`references/` also holds the candidate's source artifacts — the granted patent, the written response to Dr. Kim's Learners Conference questions, and two former-employer research reports. The reports are **confidential**: `data/candidate_profile.json` records what each one establishes and how it may be used. Method and structure are discussable; internal codenames, competitor benchmarking, and any dollar figure other than the ~$50M on the resume are not, and must not even be alluded to.

Every question bank carries persona adaptations, follow-up probes, and a Lead/Staff bar for each pillar. Live turns keep each bank question's construct and demand intact so the wording stays recognizable against the practice set; framing varies by persona style and a rotating probe stance rather than by rewriting the pillar.

### Evidence boundaries

The coach never invents metrics, outcomes, clearance status, classified details, team structure, or acquaintance with an interviewer. Candidate claims are context to probe, not evidence that a competency was demonstrated.

The recruiter screen is complete: **location, compensation, travel, and clearance are settled** and are never asked about or treated as gaps. Level is the only open item, and it is argued from scope rather than title.

The remaining loop is a **45-minute conversation with Dr. Daniella Kim built around a single case study**, which gates an onsite of four back-to-back 1:1 interviews. One boundary is narrowed rather than absolute: the candidate may state that Dr. Kim posed three questions publicly at the Learners Conference in May 2026 and that he wrote a research response to them. No acquaintance, no private exchange, and nothing characterized beyond those three questions.

## Practice Set

`practice/` holds the written answer bank — 40 question pillars with one model answer each, all follow-ups answered at follow-up length, and the Senior → Lead/Staff delta per pillar — plus two case-study files built for the single-case hiring-manager conversation.

**Which file is for which conversation.** The hiring-manager screen is one case study probed in depth, so `06` carries it and `05` supplies a 55-second module inside it. The four question tracks are the onsite material: the loop only happens if Friday goes well, and the banks cover ground the case study deliberately doesn't — field craft, facilitation, quantitative breadth, service blueprints, mentorship.

- `00-response-architecture.md` — the two answer structures, length discipline, uplevel moves, evidence boundaries, drill protocol, and a one-page cheat sheet
- `01-technical-track.md` — TQ01–TQ10 · onsite
- `02-behavioral-track.md` — BQ01–BQ10 · onsite
- `03-culture-stakeholder-track.md` — CQ01–CQ10 · onsite
- `04-positioning-close-track.md` — PQ01–PQ10 · onsite and the close of any conversation
- `05-nasa-case-study.md` — NC01–NC08, the NASA Langley case: a 55-second module inside the hiring-manager conversation, and the full deep-dive for the onsite loop
- `06-amazon-case-study.md` — AC01–AC11, **the primary case for the 45-minute hiring-manager conversation.** A counted three-minute presentation, five drilled deep-dive layers, the rigor follow-ups, the evidence-tier ladder, the off-case answers for when she leaves the case, and a minute-by-minute run sheet
- `08-design-partner-screen.md` — DS01–DS14, **the 30-minute embedded design screen with the Air Defense principal designer.** A minute-by-minute block plan, three alignment pillars with STAR bullets, the anticipated questions at 60–75s, three current-role answers, and a reverse-question set

Every spoken block is **counted at 150 words per minute**, not estimated, so the stated timings are real.

Placeholders in `[brackets]` mark facts only the candidate can supply. Fill them in or cut the sentence — never improvise a number, a name, or an outcome.

### Printing

```powershell
python scripts\build_practice_html.py
```

Renders each markdown file plus a combined `ALL-tracks.html` into `practice/print/`, styled for two-column printing at 9.6pt. Open a file in a browser and `Ctrl+P` with **Background graphics** enabled; if a document spills one page past where you want it, set **Scale: 95%**. Generated output is gitignored — regenerate after editing any practice markdown rather than keeping a stale PDF around.

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

The application requires `OPENAI_API_KEY` for question generation, transcription, speech, and evaluation.

| Purpose | Model | Settings |
|---|---|---|
| Live interviewer turns | `gpt-5.4-mini` | reasoning effort `low` — about 1.5s per turn |
| End-of-session debrief | `gpt-5.4` | reasoning effort `high`, 5-minute timeout |
| Answer transcription | `gpt-4o-transcribe` | domain-term prompt, verbatim output |
| Interviewer speech | `gpt-4o-mini-tts` | per-persona voice and delivery instruction |

Question framing is varied deliberately rather than randomly: each persona carries a speech style, and one of six probe stances is drawn per turn. The pillar's construct and demand stay fixed so the wording remains recognizable against the practice set.

OpenAI requests use structured responses with complete score-set validation, run under a bounded timeout, and preserve in-browser session state when a timeout, connection failure, rate limit, or API error occurs.

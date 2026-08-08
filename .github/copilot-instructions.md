# Anduril Voice Interview Coach Instructions

## Scope

This repository is a single-purpose interview system for Brandon Fluegel, PhD, targeting Anduril Industries' Air Defense team. Keep changes focused on the four-question Gradio interview arc, evidence-grounded persona probing, and Senior-to-Lead/Staff calibration.

## Canonical Context

- `data/candidate_profile.json`: resume facts and evidence boundaries
- `data/target_anduril_air_defense.json`: role requirements and upleveling bar
- `data/storybank_6_pillars.json`: approved stories and earned secrets
- `data/coaching_state.md`: mutable interview readiness and session state
- `references/rubrics-detailed.md`: scoring anchors
- `references/role-drills.md`: four interviewer personas

Never invent metrics, outcomes, clearance status, classified details, team structure, or prior familiarity with an interviewer. Candidate claims are context to probe, not evidence that an answer demonstrated a competency.

## Product Contract

- Preserve the mandatory four-question arc in `src/app.py`.
- Keep questions and pushback concise and voice-friendly.
- Maintain all five core scores: Substance, Structure, Relevance, Credibility, and Differentiation.
- Maintain separate Lead/Staff criteria and explicit Senior UXR versus Lead/Staff calibration.
- Treat `N/E` as not evidenced; do not convert missing evidence into a low score.
- Keep the four native personas: Dr. Daniella Kim, Systems/ML Engineering Lead, Product Manager, and Design Lead.
- Preserve structured OpenAI responses and validate their complete score sets.

## Engineering

Use the existing Python, Gradio, OpenAI, and Pydantic patterns. Keep dependencies minimal, never commit keys or runtime artifacts, and run `python -m py_compile src/app.py` plus focused tests or callback checks after behavioral changes.

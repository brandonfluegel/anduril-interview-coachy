# Anduril Voice Interview Coach Instructions

## Scope

This repository is a single-purpose interview system for Brandon Fluegel, PhD, targeting Anduril Industries' Air Defense team. Keep changes focused on the continuous multi-turn Gradio interview, evidence-grounded persona probing, and Senior-to-Lead/Staff calibration.

## Canonical Context

- `data/candidate_profile.json`: resume facts and evidence boundaries
- `data/target_anduril_air_defense.json`: role requirements and upleveling bar
- `data/storybank_6_pillars.json`: approved stories and earned secrets
- `data/behavioral_questions.json`: ten behavioral/fit pillars and four persona adaptations
- `data/technical_questions.json`: ten technical and research-craft pillars, four persona adaptations, follow-up probes, and Lead/Staff bars
- `data/culture_questions.json`: ten Anduril culture, mission-fit, and stakeholder-collaboration pillars with stakeholder groups, persona adaptations, follow-up probes, and Lead/Staff bars
- `data/positioning_questions.json`: ten positioning, scope, and close pillars for the hiring manager conversation and the end of any session
- `data/coaching_state.md`: mutable interview readiness and session state
- `references/rubrics-detailed.md`: scoring anchors
- `references/role-drills.md`: four interviewer personas

Never invent metrics, outcomes, clearance status, classified details, team structure, or prior familiarity with an interviewer. Candidate claims are context to probe, not evidence that an answer demonstrated a competency.

## Product Contract

- Keep the interview loop continuous in `src/app.py`: the persona stays fully in character for every live turn, the conversation runs for as many turns as the candidate wants, and no grading appears until the session is finalized.
- Keep the first four turns' arc guidance (technical core, technical pushback, behavioral friction, leadership and scaling) as stage direction, not as a hard cutoff.
- Select the third question from the behavioral bank and retain STAR/STARE behavioral calibration in the holistic evaluation. Apply STAR/STARE to behavioral and experience answers only; score technical and research-craft answers on claim, method, evidence and limits, threshold or decision, and what would change it.
- Anchor the opening, pushback, and leadership turns to the technical bank, and use each bank entry's follow-ups as the escalation ladder. Keep both banks at exactly ten pillars with all four persona adaptations, follow-ups, and a Lead/Staff bar.
- Offer the culture and stakeholder-collaboration bank on the behavioral, leadership, and open turns. Keep it at exactly ten pillars and keep every question grounded in the posted job description: never assert internal Anduril process, team structure, or program details, and never state or imply clearance status.
- Keep the four session formats: 30-minute hiring manager, onsite 1:1 panel, research design case, and portfolio deep dive. Each has its own arc and open stage; all four share the personas, the banks, and the holistic scorecard.
- The recruiter screen is complete. Location, compensation, travel, and clearance are settled: never ask about them, never treat them as gaps, and never assert a compensation number or an active clearance status.
- Persist the session format and the covered pillar IDs with every finalized session, and keep the Pillar Coverage matrix on the progress dashboard derived from those records.
- Keep questions and pushback concise and voice-friendly.
- Maintain all five core scores: Substance, Structure, Relevance, Credibility, and Differentiation.
- Maintain separate Lead/Staff criteria and explicit Senior UXR versus Lead/Staff calibration.
- Treat `N/E` as not evidenced; do not convert missing evidence into a low score.
- Keep the four native personas: Dr. Daniella Kim, Systems/ML Engineering Lead, Product Manager, and Design Lead.
- Preserve structured OpenAI responses and validate their complete score sets.
- Persist finalized multi-turn session summaries, including the turn count, to `data/coaching_state.md` and keep the Progress Tracker derived from those records.
- Preserve the seven-day intensive sprint checklist and both Gradio tabs.

## Engineering

Use the existing Python, Gradio, OpenAI, and Pydantic patterns. Keep dependencies minimal, never commit keys or runtime artifacts, and run `python -m py_compile src/app.py` plus focused tests or callback checks after behavioral changes.

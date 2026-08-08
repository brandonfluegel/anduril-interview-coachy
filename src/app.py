from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import gradio as gr
from openai import OpenAI
from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-4o"
CORE_DIMENSIONS = (
    "Substance",
    "Structure",
    "Relevance",
    "Credibility",
    "Differentiation",
)
LEAD_STAFF_CRITERIA = (
    "Research Thesis",
    "Empirical Rigor",
    "Research Velocity",
    "Systems Integration",
    "Cross-Functional Influence",
    "Standard Setting",
    "Operational Judgment",
    "Executive Communication",
)
PERSONAS = {
    "Dr. Daniella Kim — Research Head": "Dr. Daniella Kim",
    "Systems / ML Engineering Lead": "Systems / ML Engineering Lead",
    "Product Manager": "Product Manager",
    "Design Lead": "Design Lead",
}
PERSONA_FOCUS = {
    "Dr. Daniella Kim": "research velocity, biometric telemetry, NASA-TLX, and Calibrated Cognitive Friction",
    "Systems / ML Engineering Lead": "non-deterministic failure modes, latency thresholds, system specifications, MIL-STD compliance, and software/hardware integration",
    "Product Manager": "shipping speed, operational ROI, cross-functional alignment, and trade-off prioritization",
    "Design Lead": "interaction architecture, C2 operator workflow, UI information density, and physical ergonomics",
}
INTERVIEW_ARC = {
    1: (
        "Technical & Domain Core",
        "foundational Human Factors expertise, psychophysics, uFMEA, and evidence aligned with the candidate's whitepaper and resume",
    ),
    2: (
        "Deep-Dive Pushback & Probe",
        "direct technical pushback on the first answer that challenges assumptions and demands falsifiable metrics",
    ),
    3: (
        "Behavioral & Collaboration",
        "friction with PMs and ML/software engineers, execution under extreme startup ambiguity, and conflict resolution without compromising safety standards",
    ),
    4: (
        "Leadership, Scaling & Vision",
        "org-wide standards, scalable Human Factors frameworks, team culture, and alignment with Anduril Air Defense's fast-paced mission",
    ),
}


class InterviewQuestion(BaseModel):
    question: str


class CoreScore(BaseModel):
    dimension: Literal[
        "Substance",
        "Structure",
        "Relevance",
        "Credibility",
        "Differentiation",
    ]
    score: int = Field(ge=1, le=5)
    evidence: str


class UplevelScore(BaseModel):
    criterion: Literal[
        "Research Thesis",
        "Empirical Rigor",
        "Research Velocity",
        "Systems Integration",
        "Cross-Functional Influence",
        "Standard Setting",
        "Operational Judgment",
        "Executive Communication",
    ]
    score: int | None = Field(default=None, ge=1, le=5)
    evidence: str


class Evaluation(BaseModel):
    interviewer_pushback: str
    core_scores: list[CoreScore]
    uplevel_scores: list[UplevelScore]
    strongest_signal: str
    primary_gap: str
    priority_move: str
    next_question: str | None = None
    end_of_session_debrief: str | None = None
    uplevel_verdict: Literal["Below Lead Bar", "Lead", "Lead/Staff Borderline", "Staff"] | None = None
    confidence: Literal["High", "Medium", "Low"]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def load_system_context() -> str:
    sections = {
        "SYSTEM ROUTER": read_text("SKILL.md"),
        "CURRENT COACHING STATE": read_text("coaching_state.md"),
        "INTERVIEW PERSONAS": read_text("references/role-drills.md"),
        "DETAILED RUBRIC": read_text("references/rubrics-detailed.md"),
    }
    return "\n\n".join(f"## {name}\n{content}" for name, content in sections.items())


def validate_evaluation(evaluation: Evaluation) -> None:
    core_names = [item.dimension for item in evaluation.core_scores]
    if len(core_names) != len(CORE_DIMENSIONS) or set(core_names) != set(CORE_DIMENSIONS):
        raise ValueError("The model did not return all five core dimensions exactly once.")

    uplevel_names = [item.criterion for item in evaluation.uplevel_scores]
    if len(uplevel_names) != len(LEAD_STAFF_CRITERIA) or set(uplevel_names) != set(LEAD_STAFF_CRITERIA):
        raise ValueError("The model did not return all eight Lead/Staff criteria exactly once.")


def render_scorecard(
    evaluation: Evaluation,
    turn: int,
    cumulative_scores: list[dict[str, object]],
) -> str:
    core_rows = "\n".join(
        f"| {item.dimension} | **{item.score}/5** | {item.evidence} |"
        for item in evaluation.core_scores
    )
    uplevel_rows = "\n".join(
        f"| {item.criterion} | **{item.score}/5** | {item.evidence} |"
        if item.score is not None
        else f"| {item.criterion} | **N/E** | {item.evidence} |"
        for item in evaluation.uplevel_scores
    )
    scorecard = f"""## Question {turn} Scorecard

**Confidence:** {evaluation.confidence}

| Core dimension | Score | Evidence |
|---|---:|---|
{core_rows}

### Lead/Staff Read

| Criterion | Rating | Evidence |
|---|---:|---|
{uplevel_rows}

**Strongest signal:** {evaluation.strongest_signal}

**Primary gap:** {evaluation.primary_gap}

**Priority move:** {evaluation.priority_move}
"""
    if turn < 4:
        return scorecard

    core_averages = {
        dimension: sum(
            item["score"]
            for result in cumulative_scores
            for item in result["core_scores"]
            if item["dimension"] == dimension
        )
        / len(cumulative_scores)
        for dimension in CORE_DIMENSIONS
    }
    uplevel_averages = {}
    for criterion in LEAD_STAFF_CRITERIA:
        ratings = [
            item["score"]
            for result in cumulative_scores
            for item in result["uplevel_scores"]
            if item["criterion"] == criterion and item["score"] is not None
        ]
        uplevel_averages[criterion] = sum(ratings) / len(ratings) if ratings else None

    core_summary = "\n".join(
        f"| {dimension} | **{average:.1f}/5** |" for dimension, average in core_averages.items()
    )
    uplevel_summary = "\n".join(
        f"| {criterion} | **{average:.1f}/5** |" if average is not None else f"| {criterion} | **N/E** |"
        for criterion, average in uplevel_averages.items()
    )
    return f"""# End of Session Debrief

**Lead/Staff verdict: {evaluation.uplevel_verdict}**

{evaluation.end_of_session_debrief}

## Four-Turn Averages

| Core dimension | Average |
|---|---:|
{core_summary}

| Lead/Staff criterion | Average |
|---|---:|
{uplevel_summary}

---

{scorecard}
"""


def turn_indicator(turn: int) -> str:
    title, _ = INTERVIEW_ARC[turn]
    return f"**Question {turn} of 4: {title}**"


def require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise gr.Error("OPENAI_API_KEY is not set. In PowerShell, run: $env:OPENAI_API_KEY='your-key'")
    return api_key


def generate_question(
    persona_label: str,
    turn: int,
    history: list[dict[str, str]],
) -> str:
    persona = PERSONAS[persona_label]
    title, objective = INTERVIEW_ARC[turn]
    prior_context = history[-8:] if history else "No prior turns; open the interview without preamble."
    prompt = f"""Generate Question {turn} of a mandatory four-question interview as {persona}.

Arc stage: {title}
Stage objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}
Prior conversation: {prior_context}

Ask exactly one concise, voice-friendly question in character. Make it answerable aloud. For Turn 2, directly challenge a specific assumption or missing falsifiable metric from Turn 1. Do not provide coaching, an answer, or a question number. Do not invent candidate evidence or classified Anduril details.
"""
    response = OpenAI(api_key=require_api_key()).responses.parse(
        model=MODEL,
        instructions=load_system_context(),
        input=prompt,
        text_format=InterviewQuestion,
        temperature=0.3,
        max_output_tokens=350,
    )
    result = response.output_parsed
    if result is None:
        raise gr.Error("The model returned no interview question. Please try again.")
    return result.question.strip()


def start_interview(
    persona_label: str,
) -> tuple[str, str, str, int, list[dict[str, str]], list[dict[str, object]], str]:
    question = generate_question(persona_label, 1, [])
    history = [{"role": "assistant", "content": question}]
    return turn_indicator(1), f"## {PERSONAS[persona_label]}\n\n{question}", "Scorecards will appear after each answer.", 1, history, [], ""


def evaluate_answer(
    answer: str,
    persona_label: str,
    turn: int,
    history: list[dict[str, str]] | None,
    cumulative_scores: list[dict[str, object]] | None,
) -> tuple[str, str, str, int, list[dict[str, str]], list[dict[str, object]], str]:
    answer = answer.strip()
    if not answer:
        raise gr.Error("Dictate or paste an answer first.")

    if turn not in INTERVIEW_ARC:
        raise gr.Error("Start a new four-question interview before submitting an answer.")

    persona = PERSONAS[persona_label]
    prior_turns = history or []
    prior_scores = cumulative_scores or []
    title, objective = INTERVIEW_ARC[turn]
    next_stage = INTERVIEW_ARC.get(turn + 1)
    next_instruction = (
        f"Generate next_question for Question {turn + 1}, '{next_stage[0]}': {next_stage[1]}."
        if next_stage
        else "Set next_question to null. Produce a comprehensive end_of_session_debrief and a clear uplevel_verdict using all four answers and prior scorecards."
    )
    prompt = f"""Act as {persona} for the immediate response, then switch to the independent coach scorecard.

This is Question {turn} of 4: {title}.
Arc objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}

Evaluate the candidate answer below. Apply all five core dimensions and every Lead/Staff criterion. Use null for a Lead/Staff score when this answer does not provide evidence for that criterion; missing evidence is not automatically poor performance.

The interviewer_pushback must be in character, voice-friendly, and no more than two short sentences. It should acknowledge the answer only as needed and identify its highest-leverage weakness. The detailed evidence belongs in the scorecard.

{next_instruction}
The next question must be exactly one concise, voice-friendly question in character. For Question 2, directly challenge a specific assumption or request a falsifiable metric from the first answer. Do not invent facts about Anduril, Dr. Kim, the candidate, classified systems, study outcomes, or prior interactions.

Conversation so far:
{prior_turns[-8:]}

Prior structured scorecards:
{prior_scores}

Candidate answer:
{answer}
"""

    response = OpenAI(api_key=require_api_key()).responses.parse(
        model=MODEL,
        instructions=load_system_context(),
        input=prompt,
        text_format=Evaluation,
        temperature=0.2,
        max_output_tokens=2200,
    )
    evaluation = response.output_parsed
    if evaluation is None:
        raise gr.Error("The model returned no structured evaluation. Please try again.")

    validate_evaluation(evaluation)
    if turn < 4 and not evaluation.next_question:
        raise gr.Error("The model did not return the next interview question. Please try again.")
    if turn == 4 and (not evaluation.end_of_session_debrief or not evaluation.uplevel_verdict):
        raise gr.Error("The model did not return the final debrief and verdict. Please try again.")

    updated_scores = [*prior_scores, evaluation.model_dump()]
    updated_history = [
        *prior_turns,
        {"role": "user", "content": answer},
        {"role": "assistant", "content": evaluation.interviewer_pushback},
    ]
    scorecard = render_scorecard(evaluation, turn, updated_scores)
    if turn == 4:
        return (
            "**Interview Complete: End of Session Debrief**",
            f"## {persona}\n\n{evaluation.interviewer_pushback}\n\nThe four-question interview is complete.",
            scorecard,
            0,
            updated_history,
            updated_scores,
            "",
        )

    next_turn = turn + 1
    next_question = evaluation.next_question or ""
    updated_history.append({"role": "assistant", "content": next_question})
    interviewer_output = f"## {persona}\n\n{evaluation.interviewer_pushback}\n\n### Your Next Question\n\n{next_question}"
    return turn_indicator(next_turn), interviewer_output, scorecard, next_turn, updated_history, updated_scores, ""


def clear_session() -> tuple[str, str, str, int, list[dict[str, str]], list[dict[str, object]], str]:
    return (
        "**No interview in progress**",
        "Select an interviewer and start a new four-question interview.",
        "Scorecards will appear after each answer.",
        0,
        [],
        [],
        "",
    )


HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

CSS = """
:root {
  --ink: #171717;
  --paper: #f4f1e9;
  --signal: #d43b2f;
  --steel: #35505a;
  --line: #c9c3b7;
}

body,
body.dark {
    color-scheme: light;
    background: var(--paper) !important;
    --body-background-fill: var(--paper);
    --background-fill-primary: #fffdf7;
    --background-fill-secondary: #ebe7dd;
    --block-background-fill: #fffdf7;
    --input-background-fill: #fffdf7;
    --button-secondary-background-fill: #e1ddd3;
    --button-secondary-text-color: var(--ink);
    --body-text-color: var(--ink);
    --block-label-text-color: var(--ink);
    --input-placeholder-color: #6f736f;
    --border-color-primary: var(--line);
    --block-border-color: var(--line);
}

.gradio-container {
  font-family: 'IBM Plex Sans', sans-serif !important;
  color: var(--ink);
  background:
    linear-gradient(rgba(53, 80, 90, 0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(53, 80, 90, 0.055) 1px, transparent 1px),
    var(--paper);
  background-size: 28px 28px;
}

#shell { max-width: 1120px; margin: 0 auto; padding: 20px 16px 40px; }
#masthead { border-top: 7px solid var(--signal); border-bottom: 1px solid var(--line); padding: 18px 0 16px; margin-bottom: 18px; }
#masthead h1 { font-family: 'IBM Plex Mono', monospace; font-size: clamp(1.55rem, 4vw, 2.5rem); line-height: 1.05; letter-spacing: 0; margin: 0; color: var(--ink) !important; }
#masthead p { max-width: 760px; color: #4b5354; margin: 9px 0 0; }
#shell .form { background: transparent !important; border-color: var(--line) !important; }
#shell .block { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; }
#shell .block span { color: var(--ink) !important; }
#shell textarea { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; }
#shell textarea::placeholder { color: #6f736f !important; }
#shell input[type='radio'] { accent-color: var(--signal) !important; }
#shell input[type='radio'] + span,
#shell label:has(input[type='radio']) { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; }
#shell label.selected:has(input[type='radio']) { background: #ebe7dd !important; border-color: var(--signal) !important; }
#answer textarea { min-height: 190px; font-size: 1.05rem; line-height: 1.55; }
#turn-indicator { border-left: 5px solid var(--steel); background: #ebe7dd; padding: 7px 14px; }
#pushback { border-left: 5px solid var(--signal); background: #fffdf7; padding: 8px 16px; min-height: 126px; }
#scorecard { border-top: 3px solid var(--steel); background: rgba(255, 253, 247, 0.86); padding: 10px 16px; min-height: 360px; }
#pushback *, #scorecard * { color: var(--ink) !important; }
#evaluate { background: var(--signal); border-color: var(--signal); color: white; font-weight: 700; }
#evaluate:hover { background: #b92e24; border-color: #b92e24; }
footer { display: none !important; }
@media (max-width: 700px) {
  #shell { padding: 8px 8px 28px; }
  #answer textarea { min-height: 230px; }
  #masthead { padding-top: 12px; }
}
"""


with gr.Blocks(title="Anduril Human Factors Interview System") as demo:
    turn_state = gr.State(0)
    conversation_history = gr.State([])
    cumulative_scores = gr.State([])
    with gr.Column(elem_id="shell"):
        gr.HTML(
            """
            <header id="masthead">
              <h1>HUMAN FACTORS // AIR DEFENSE</h1>
              <p>Lead/Staff interview pressure testing for Dr. Brandon Fluegel. Dictate through Superwhisper, then evaluate against the core rubric and the Anduril uplevel bar.</p>
            </header>
            """
        )
        persona = gr.Radio(
            choices=list(PERSONAS),
            value="Dr. Daniella Kim — Research Head",
            label="Interviewer",
        )
        start_button = gr.Button("Start New 4-Question Interview")
        indicator = gr.Markdown("**No interview in progress**", elem_id="turn-indicator")
        interviewer = gr.Markdown(
            "Select an interviewer and start a new four-question interview.",
            elem_id="pushback",
        )
        listen_button = gr.Button("Listen to Interviewer")
        answer = gr.Textbox(
            label="Candidate answer",
            placeholder="Place the cursor here, dictate with Superwhisper, then submit.",
            lines=8,
            max_lines=18,
            autofocus=True,
            elem_id="answer",
        )
        with gr.Row():
            evaluate_button = gr.Button("Submit Answer", variant="primary", elem_id="evaluate")
            clear_button = gr.Button("Clear Session")
        scorecard = gr.Markdown("Scorecards will appear after each answer.", elem_id="scorecard")

    session_outputs = [indicator, interviewer, scorecard, turn_state, conversation_history, cumulative_scores, answer]
    start_button.click(start_interview, inputs=[persona], outputs=session_outputs)
    listen_button.click(
        fn=None,
        inputs=[interviewer],
        js="(text) => { window.speechSynthesis.cancel(); const voice = new SpeechSynthesisUtterance(text.replaceAll('#', '').replaceAll('*', '')); voice.rate = 0.96; window.speechSynthesis.speak(voice); }",
        queue=False,
    )
    submit_inputs = [answer, persona, turn_state, conversation_history, cumulative_scores]
    submit_outputs = session_outputs
    evaluate_button.click(evaluate_answer, submit_inputs, submit_outputs)
    answer.submit(evaluate_answer, submit_inputs, submit_outputs)
    clear_button.click(clear_session, outputs=session_outputs)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True, css=CSS, head=HEAD)

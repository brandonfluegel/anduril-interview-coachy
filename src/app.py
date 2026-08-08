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
    next_question: str
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


def render_scorecard(evaluation: Evaluation) -> str:
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
    return f"""## Coach Scorecard

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

### Next Question

{evaluation.next_question}
"""


def evaluate_answer(
    answer: str,
    persona_label: str,
    history: list[dict[str, str]] | None,
) -> tuple[str, str, list[dict[str, str]], str]:
    answer = answer.strip()
    if not answer:
        raise gr.Error("Dictate or paste an answer first.")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise gr.Error("OPENAI_API_KEY is not set. In PowerShell, run: $env:OPENAI_API_KEY='your-key'")

    persona = PERSONAS[persona_label]
    prior_turns = history or []
    compact_history = prior_turns[-6:]
    prompt = f"""Act as {persona} for the immediate pushback, then switch to the independent coach scorecard.

Evaluate the candidate answer below. Apply the five core dimensions and every Lead/Staff criterion. Use null for a Lead/Staff score when the answer does not provide evidence for that criterion; missing evidence is not automatically poor performance.

The pushback must be in character, voice-friendly, and no more than two short sentences. It must challenge the answer's highest-leverage weakness, not summarize it. The detailed evidence belongs in the scorecard.

Do not invent facts about Anduril, Dr. Kim, the candidate, classified systems, study outcomes, or prior interactions. Treat the supplied system context as the evidence boundary. End with exactly one incisive next question from the selected persona.

Recent practice context:
{compact_history}

Candidate answer:
{answer}
"""

    client = OpenAI(api_key=api_key)
    response = client.responses.parse(
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
    pushback = f"## {persona}\n\n{evaluation.interviewer_pushback}"
    scorecard = render_scorecard(evaluation)
    updated_history = [
        *compact_history,
        {"role": "user", "content": answer},
        {"role": "assistant", "content": evaluation.interviewer_pushback},
    ]
    return pushback, scorecard, updated_history, ""


def clear_session() -> tuple[str, str, list[dict[str, str]], str]:
    return (
        "Select an interviewer, then dictate an answer through Superwhisper.",
        "Your scored evidence will appear here.",
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
    history_state = gr.State([])
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
        answer = gr.Textbox(
            label="Candidate answer",
            placeholder="Place the cursor here, dictate with Superwhisper, then submit.",
            lines=8,
            max_lines=18,
            autofocus=True,
            elem_id="answer",
        )
        with gr.Row():
            evaluate_button = gr.Button("Evaluate Answer", variant="primary", elem_id="evaluate")
            clear_button = gr.Button("Clear Session")
        pushback = gr.Markdown(
            "Select an interviewer, then dictate an answer through Superwhisper.",
            elem_id="pushback",
        )
        scorecard = gr.Markdown("Your scored evidence will appear here.", elem_id="scorecard")

    submit_inputs = [answer, persona, history_state]
    submit_outputs = [pushback, scorecard, history_state, answer]
    evaluate_button.click(evaluate_answer, submit_inputs, submit_outputs)
    answer.submit(evaluate_answer, submit_inputs, submit_outputs)
    clear_button.click(clear_session, outputs=submit_outputs)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True, css=CSS, head=HEAD)

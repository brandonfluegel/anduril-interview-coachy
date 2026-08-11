from __future__ import annotations

import os
import re
import threading
from datetime import datetime
from pathlib import Path
from typing import Literal, TypeVar

import gradio as gr
from openai import APIConnectionError, APIStatusError, APITimeoutError, OpenAI, RateLimitError
from pydantic import BaseModel, Field, ValidationError


ROOT = Path(__file__).resolve().parents[1]
COACHING_STATE_PATH = ROOT / "data" / "coaching_state.md"
MODEL = "gpt-4o"
OPENAI_TIMEOUT_SECONDS = 45.0
SESSION_LOG_END = "<!-- FOUR_TURN_SESSION_LOG_END -->"
SESSION_RECORD_PATTERN = re.compile(r"<!-- FOUR_TURN_SESSION_JSON (.+?) -->")
SESSION_WRITE_LOCK = threading.Lock()
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
SYSTEM_PROMPT = """You are the evidence-grounded Anduril Air Defense Voice Interview Coach for Brandon Fluegel, PhD.

Run a mandatory four-question interview, one question at a time, using the selected interviewer persona. Cross-examine canonical resume evidence against the posted Senior User Experience Researcher requirements and the Lead/Staff upleveling bar. Never invent metrics, outcomes, team details, classified information, clearance status, or familiarity with an interviewer.

Score every answer on Substance, Structure, Relevance, Credibility, and Differentiation. Separately evaluate Research Thesis, Empirical Rigor, Research Velocity, Systems Integration, Cross-Functional Influence, Standard Setting, Operational Judgment, and Executive Communication. Use N/E when a Lead/Staff criterion is not evidenced.

Senior UXR baseline means expertly designing and executing studies that produce actionable insights. Lead/Staff signal means setting reusable standards, bridging human perception to engineering requirements, establishing frameworks before policy exists, defining Research Operations, influencing decisions across functions, and translating HSI evidence into hard hardware/software specifications.

Keep interviewer questions and pushback concise and voice-friendly. Treat prior resume claims as context to probe, not proof that the spoken answer demonstrated a competency. Preserve Meaningful Human Control, operational tempo, and evidence integrity throughout.

For Question 3, select a behavioral/fit pillar from the canonical behavioral question bank using the active persona's adaptation. Grade behavioral answers for STAR/STARE completeness, concrete ownership, interpersonal maturity, and Lead/Staff organizational impact.
"""
PERSONA_FOCUS = {
    "Dr. Daniella Kim": (
        "Cross-examine how Brandon's Ph.D. dissertation on high-stress interruptions, Amazon fNIRS and eye-tracking work, "
        "and ACM CSCW 2026 Principles for Agentic Trust framework translate into rapid ethnography, service blueprints, "
        "research repositories, research velocity, NASA-TLX, and Calibrated Cognitive Friction for Air Defense operators using Lattice OS."
    ),
    "Systems / ML Engineering Lead": (
        "Cross-examine how Brandon's $50M Amazon psychophysics program, NASA uFMEA work, and MIL-STD-1472 experience "
        "translate into falsifiable non-deterministic C2 latency thresholds, system specifications, counter-drone autonomous "
        "feedback loops, standards compliance, and software/hardware integration."
    ),
    "Product Manager": (
        "Cross-examine how Brandon balances academic rigor with Anduril's startup shipping velocity measured in months, "
        "drives product-roadmap trade-offs, proves operational ROI, aligns cross-functional partners, and scales Research Operations."
    ),
    "Design Lead": (
        "Cross-examine how Brandon's Echo Hub and multimodal architecture work, reach-envelope modeling, physical ergonomics, "
        "and hardware/software validation translate into high-stress 3D C2 tactical operator workflows, information density, "
        "interaction architecture, and physical fit."
    ),
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


class BehavioralQuestion(BaseModel):
    id: str
    pillar: str
    question: str
    resume_and_role_links: list[str]
    persona_adaptations: dict[str, str]


class BehavioralQuestionBank(BaseModel):
    schema_version: str
    purpose: str
    personas: list[str]
    questions: list[BehavioralQuestion]


class SessionRecord(BaseModel):
    timestamp: str
    date: str
    persona: str
    core_averages: dict[str, float]
    uplevel_rating: Literal["Pass", "Strategic Upgrade Needed"]
    readiness_rating: Literal["Senior UXR Baseline", "Lead/Staff Upleveled"]
    primary_bottleneck: str
    actionable_fix: str


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
    senior_uxr_baseline_assessment: str
    lead_staff_uplevel_assessment: str
    demonstrated_level: Literal[
        "Below Senior UXR Baseline",
        "Meets Senior UXR Baseline",
        "Lead/Staff Upleveling Signal",
    ]
    next_question: str | None = None
    end_of_session_debrief: str | None = None
    uplevel_verdict: Literal["Below Lead Bar", "Lead", "Lead/Staff Borderline", "Staff"] | None = None
    confidence: Literal["High", "Medium", "Low"]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def load_behavioral_question_bank() -> BehavioralQuestionBank:
    bank = BehavioralQuestionBank.model_validate_json(read_text("data/behavioral_questions.json"))
    expected_personas = set(PERSONAS.values())
    if len(bank.questions) != 10:
        raise ValueError("The behavioral question bank must contain exactly 10 questions.")
    if len({question.id for question in bank.questions}) != 10:
        raise ValueError("Behavioral question IDs must be unique.")
    if set(bank.personas) != expected_personas:
        raise ValueError("The behavioral question bank must declare all four interviewer personas.")
    for question in bank.questions:
        if set(question.persona_adaptations) != expected_personas:
            raise ValueError(f"{question.id} must define an adaptation for every interviewer persona.")
    return bank


BEHAVIORAL_QUESTION_BANK = load_behavioral_question_bank()
ResponseModel = TypeVar("ResponseModel", bound=BaseModel)


def behavioral_question_options(persona: str) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {question.persona_adaptations[persona]}"
        for question in BEHAVIORAL_QUESTION_BANK.questions
    )


def load_system_context() -> str:
    sections = {
        "SYSTEM CONTRACT": SYSTEM_PROMPT,
        "CANONICAL CANDIDATE RESUME": read_text("data/candidate_profile.json"),
        "CANONICAL AIR DEFENSE JOB REQUIREMENTS": read_text("data/target_anduril_air_defense.json"),
        "CANONICAL STORYBANK": read_text("data/storybank_6_pillars.json"),
        "BEHAVIORAL AND FIT QUESTION BANK": read_text("data/behavioral_questions.json"),
        "CURRENT COACHING STATE": read_text("data/coaching_state.md"),
        "INTERVIEW PERSONAS": read_text("references/role-drills.md"),
        "DETAILED RUBRIC": read_text("references/rubrics-detailed.md"),
    }
    return "\n\n".join(f"## {name}\n{content}" for name, content in sections.items())


def parse_openai_response(
    prompt: str,
    response_format: type[ResponseModel],
    temperature: float,
    max_output_tokens: int,
) -> ResponseModel:
    try:
        response = OpenAI(
            api_key=require_api_key(),
            timeout=OPENAI_TIMEOUT_SECONDS,
            max_retries=1,
        ).responses.parse(
            model=MODEL,
            instructions=load_system_context(),
            input=prompt,
            text_format=response_format,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
    except (APITimeoutError, TimeoutError) as exc:
        raise gr.Error("The interview request timed out. Your session is intact; please submit again.") from exc
    except APIConnectionError as exc:
        raise gr.Error("The interview service is unreachable. Check your connection and try again.") from exc
    except RateLimitError as exc:
        raise gr.Error("The interview service is temporarily busy. Wait a moment and try again.") from exc
    except APIStatusError as exc:
        raise gr.Error(f"The interview service returned an error ({exc.status_code}). Please try again.") from exc
    except ValidationError as exc:
        raise gr.Error("The model response did not match the required score format. Please try again.") from exc

    parsed = response.output_parsed
    if parsed is None:
        raise gr.Error("The model returned no structured response. Please try again.")
    return parsed


def calculate_core_averages(cumulative_scores: list[dict[str, object]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    for dimension in CORE_DIMENSIONS:
        ratings = [
            float(item["score"])
            for result in cumulative_scores
            for item in result["core_scores"]
            if item["dimension"] == dimension
        ]
        averages[dimension] = round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    return averages


def persist_session(
    persona: str,
    evaluation: Evaluation,
    cumulative_scores: list[dict[str, object]],
) -> SessionRecord:
    timestamp = datetime.now().astimezone()
    passed_uplevel = evaluation.uplevel_verdict in {"Lead", "Lead/Staff Borderline", "Staff"}
    primary_bottleneck = " ".join(evaluation.primary_gap.split()).replace("-->", "->")
    actionable_fix = " ".join(evaluation.priority_move.split()).replace("-->", "->")
    record = SessionRecord(
        timestamp=timestamp.isoformat(timespec="seconds"),
        date=timestamp.date().isoformat(),
        persona=persona,
        core_averages=calculate_core_averages(cumulative_scores),
        uplevel_rating="Pass" if passed_uplevel else "Strategic Upgrade Needed",
        readiness_rating="Lead/Staff Upleveled" if passed_uplevel else "Senior UXR Baseline",
        primary_bottleneck=primary_bottleneck,
        actionable_fix=actionable_fix,
    )
    averages = "; ".join(
        f"{dimension}: {record.core_averages[dimension]:.2f}" for dimension in CORE_DIMENSIONS
    )
    entry = f"""

### Mock Session — {record.timestamp}
- **Date:** {record.date}
- **Interviewer:** {record.persona}
- **Core averages:** {averages}
- **Lead/Staff upleveling:** {record.uplevel_rating}
- **Primary bottleneck:** {record.primary_bottleneck}
- **Actionable fix:** {record.actionable_fix}
<!-- FOUR_TURN_SESSION_JSON {record.model_dump_json()} -->
"""
    with SESSION_WRITE_LOCK:
        state = COACHING_STATE_PATH.read_text(encoding="utf-8")
        if SESSION_LOG_END not in state:
            state = f"{state.rstrip()}\n\n## Persistent Four-Turn Mock Sessions\n{SESSION_LOG_END}\n"
        updated_state = state.replace(SESSION_LOG_END, f"{entry}\n{SESSION_LOG_END}", 1)
        temporary_path = COACHING_STATE_PATH.with_suffix(".md.tmp")
        temporary_path.write_text(updated_state, encoding="utf-8")
        temporary_path.replace(COACHING_STATE_PATH)
    return record


def load_session_records() -> list[SessionRecord]:
    state = COACHING_STATE_PATH.read_text(encoding="utf-8")
    records: list[SessionRecord] = []
    for match in SESSION_RECORD_PATTERN.finditer(state):
        try:
            record = SessionRecord.model_validate_json(match.group(1))
        except ValidationError:
            continue
        if set(record.core_averages) == set(CORE_DIMENSIONS):
            records.append(record)
    return records


def load_progress_dashboard() -> tuple[str, list[list[object]]]:
    records = load_session_records()
    if records:
        overall = {
            dimension: sum(record.core_averages[dimension] for record in records) / len(records)
            for dimension in CORE_DIMENSIONS
        }
        weakest_dimension = min(overall, key=overall.get)
        readiness = records[-1].readiness_rating
    else:
        overall = {dimension: 0.0 for dimension in CORE_DIMENSIONS}
        weakest_dimension = "Not yet measured"
        readiness = "Senior UXR Baseline"

    score_rows = "\n".join(
        f"| {dimension} | **{overall[dimension]:.2f}/5** |" for dimension in CORE_DIMENSIONS
    )
    summary = f"""## Sprint Readiness

**Total mock sessions completed:** {len(records)}

**Weakest dimension alert:** {weakest_dimension}

**Readiness rating:** {readiness}

| Core dimension | Overall average |
|---|---:|
{score_rows}
"""
    history = [
        [
            record.timestamp,
            record.persona,
            *[record.core_averages[dimension] for dimension in CORE_DIMENSIONS],
            record.uplevel_rating,
            record.primary_bottleneck,
            record.actionable_fix,
        ]
        for record in reversed(records[-10:])
    ]
    return summary, history


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

### Senior vs. Lead/Staff Calibration

**Demonstrated level:** {evaluation.demonstrated_level}

**Senior UXR baseline:** {evaluation.senior_uxr_baseline_assessment}

**Lead/Staff upleveling signal:** {evaluation.lead_staff_uplevel_assessment}
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
    behavioral_instruction = ""
    if turn == 3:
        behavioral_instruction = f"""
Select the strongest non-duplicative behavioral pillar from these persona-adapted options. Use its adapted question directly or tailor it to the prior conversation without changing the pillar's intent:
{behavioral_question_options(persona)}
"""
    prompt = f"""Generate Question {turn} of a mandatory four-question interview as {persona}.

Arc stage: {title}
Stage objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}
Prior conversation: {prior_context}
{behavioral_instruction}

Ask exactly one concise, voice-friendly question in character. Make it answerable aloud. For Turn 2, directly challenge a specific assumption or missing falsifiable metric from Turn 1. Do not provide coaching, an answer, or a question number. Do not invent candidate evidence or classified Anduril details.

The spoken question must be one conversational sentence of at most 35 words. Lead with the challenge; avoid stacked clauses, lists, jargon preambles, and written-report language.

Cross-examine a concrete claim from the canonical resume against a concrete Air Defense responsibility or qualification. Do not ask a generic interview question. Distinguish evidence that merely meets the Senior UXR baseline from evidence that could prove Lead/Staff scope.
"""
    result = parse_openai_response(prompt, InterviewQuestion, temperature=0.3, max_output_tokens=350)
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
    if turn == 2:
        next_instruction = f"""Generate next_question for Question 3, 'Behavioral & Collaboration'.
Select the strongest non-duplicative pillar from the following persona-adapted behavioral bank. Use the adapted question directly or tailor it to the candidate's prior answers without changing the pillar's intent:
{behavioral_question_options(persona)}"""
    elif next_stage:
        next_instruction = f"Generate next_question for Question {turn + 1}, '{next_stage[0]}': {next_stage[1]}."
    else:
        next_instruction = "Set next_question to null. Produce a comprehensive end_of_session_debrief and a clear uplevel_verdict using all four answers and prior scorecards."
    behavioral_evaluation = ""
    if turn == 3:
        behavioral_evaluation = """
This is the behavioral/fit response. Evaluate its STAR/STARE evidence explicitly:
- Situation: specific defense-tech, safety-critical, startup, or cross-functional context and stakes.
- Task: the candidate's mandate, constraints, and decision responsibility.
- Action: concrete first-person ownership, choices, influence tactics, and trade-offs rather than vague "we" activity.
- Result: observable decision, safety, operator, product, team, or business outcome with bounded evidence.
- Evaluation/Reflection: what the candidate learned, would change, or converted into a reusable practice.

Penalize missing concrete ownership in Substance and Credibility. Assess interpersonal maturity through directness, listening, conflict handling, ethical judgment, and respect for engineering/product constraints. Award Lead/Staff signal only when the answer demonstrates organizational impact such as a reusable standard, escalation protocol, research-ops mechanism, mentoring system, cross-team decision model, or durable culture change.
"""
    prompt = f"""Act as {persona} for the immediate response, then switch to the independent coach scorecard.

This is Question {turn} of 4: {title}.
Arc objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}
{behavioral_evaluation}

Evaluate the candidate answer below. Apply all five core dimensions and every Lead/Staff criterion. Use null for a Lead/Staff score when this answer does not provide evidence for that criterion; missing evidence is not automatically poor performance.

Explicitly classify demonstrated_level using this bar:
- Senior UXR baseline: expertly designs and executes studies that produce actionable product and program insights.
- Lead/Staff upleveling signal: sets company-wide standards, bridges engineering latency with human perception, establishes frameworks before policy exists, defines Research Operations tools, and translates complex HSI into hard hardware/software specifications.

For senior_uxr_baseline_assessment and lead_staff_uplevel_assessment, cite specific evidence from this answer and compare it with the canonical resume and Air Defense job requirements. Prior resume claims are context to probe, not proof that the spoken answer demonstrated the competency.

The interviewer_pushback must be in character, conversational, and no more than 28 words across at most two short sentences. Lead with the challenge and identify the highest-leverage weakness. The detailed evidence belongs in the scorecard.

{next_instruction}
The next question must be exactly one concise, voice-friendly question in character. For Question 2, directly challenge a specific assumption or request a falsifiable metric from the first answer. Do not invent facts about Anduril, Dr. Kim, the candidate, classified systems, study outcomes, or prior interactions.

Conversation so far:
{prior_turns[-8:]}

Prior structured scorecards:
{prior_scores}

Candidate answer:
{answer}
"""

    evaluation = parse_openai_response(prompt, Evaluation, temperature=0.2, max_output_tokens=2200)

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
        try:
            persist_session(persona, evaluation, updated_scores)
        except OSError as exc:
            gr.Warning(f"Interview completed, but progress could not be saved: {exc}")
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

SPRINT_CHECKLIST = [
    "Day 1: Foundational STAR Calibration — Pillars 1 & 2: Agentic Trust and Amazon $50M",
    "Day 2: Systems Safety & MIL-STD Deep Dive — Pillars 3 & 5: NASA uFMEA and Hardware/Software HMI",
    "Day 3: Ethics, Friction & Warfare Philosophy — Pillars 4 & 6: Calibrated Friction and Keynote Unanswerable Questions",
    "Day 4: Cross-Functional Pressure Tests — PM and ML Engineering Personas",
    "Day 5: Behavioral & Operator Fit Drill — 10 Behavioral/Military Operator Scenarios",
    "Day 6: Full 4-Turn Dynamic Loop Runs — Dr. Daniella Kim Persona",
    "Day 7: Final Polish & Peak Performance Simulation",
]

SESSION_HISTORY_HEADERS = [
    "Timestamp",
    "Interviewer",
    *CORE_DIMENSIONS,
    "Lead/Staff Rating",
    "Primary Bottleneck",
    "Actionable Fix",
]

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

#shell { max-width: 1120px; margin: 0 auto; padding: 20px 16px 40px; overflow-x: hidden; }
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
#answer textarea { min-height: 190px; font-size: 1.05rem; line-height: 1.55; overflow-y: auto; }
#turn-indicator { border-left: 5px solid var(--steel); background: #ebe7dd; padding: 7px 14px; }
#pushback { border-left: 5px solid var(--signal); background: #fffdf7; padding: 8px 16px; min-height: 126px; }
#scorecard { border-top: 3px solid var(--steel); background: rgba(255, 253, 247, 0.86); padding: 10px 16px; min-height: 360px; overflow-x: auto; }
#scorecard table { display: block; max-width: 100%; overflow-x: auto; }
#history-table { max-width: 100%; overflow-x: auto; }
#sprint-checklist label { align-items: flex-start; }
#pushback *, #scorecard * { color: var(--ink) !important; }
#evaluate { background: var(--signal); border-color: var(--signal); color: white; font-weight: 700; }
#evaluate:hover { background: #b92e24; border-color: #b92e24; }
footer { display: none !important; }
@media (max-width: 700px) {
  #shell { padding: 8px 8px 28px; }
  #answer textarea { min-height: 230px; }
  #masthead { padding-top: 12px; }
    #shell button { white-space: normal; }
    #shell .tab-nav { overflow-x: auto; }
}
"""


initial_dashboard, initial_history = load_progress_dashboard()


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
        with gr.Tabs():
            with gr.Tab("🛡️ Interview Simulator"):
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
                    lines=10,
                    max_lines=30,
                    autofocus=True,
                    elem_id="answer",
                )
                with gr.Row():
                    evaluate_button = gr.Button("Submit Answer", variant="primary", elem_id="evaluate")
                    clear_button = gr.Button("Clear Session")
                scorecard = gr.Markdown("Scorecards will appear after each answer.", elem_id="scorecard")

            with gr.Tab("📈 Progress & 1-Week Sprint Tracker"):
                dashboard = gr.Markdown(initial_dashboard, elem_id="progress-dashboard")
                refresh_dashboard = gr.Button("Refresh Progress")
                gr.Markdown("## 7-Day Intensive Sprint Checklist")
                gr.CheckboxGroup(
                    choices=SPRINT_CHECKLIST,
                    label="Complete each practice block before interview day",
                    elem_id="sprint-checklist",
                )
                gr.Markdown("## Recent Mock Sessions")
                session_history = gr.Dataframe(
                    value=initial_history,
                    headers=SESSION_HISTORY_HEADERS,
                    datatype=["str", "str", "number", "number", "number", "number", "number", "str", "str", "str"],
                    interactive=False,
                    elem_id="history-table",
                )

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
    evaluate_event = evaluate_button.click(evaluate_answer, submit_inputs, submit_outputs)
    evaluate_event.then(load_progress_dashboard, outputs=[dashboard, session_history])
    answer_event = answer.submit(evaluate_answer, submit_inputs, submit_outputs)
    answer_event.then(load_progress_dashboard, outputs=[dashboard, session_history])
    clear_button.click(clear_session, outputs=session_outputs)
    refresh_dashboard.click(load_progress_dashboard, outputs=[dashboard, session_history])


if __name__ == "__main__":
    share_enabled = os.getenv("GRADIO_SHARE", "false").lower() == "true"
    demo.launch(server_name="0.0.0.0", server_port=7860, share=share_enabled, css=CSS, head=HEAD)

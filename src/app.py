from __future__ import annotations

import contextlib
import json
import os
import random
import re
import tempfile
import threading
import time
import wave
from datetime import datetime
from pathlib import Path
from typing import Literal, TypeVar

import gradio as gr
from openai import APIConnectionError, APIStatusError, APITimeoutError, OpenAI, RateLimitError
from pydantic import BaseModel, Field, ValidationError


ROOT = Path(__file__).resolve().parents[1]
COACHING_STATE_PATH = ROOT / "data" / "coaching_state.md"
TEMP_AUDIO_DIR = ROOT / "temp_audio"
EXPORT_DIR = ROOT / "exports"
LIVE_MODEL = "gpt-5.4-mini"
DEBRIEF_MODEL = "gpt-5.4"
LIVE_REASONING_EFFORT = "low"
DEBRIEF_REASONING_EFFORT = "high"
TTS_MODEL = "gpt-4o-mini-tts"
TRANSCRIBE_MODEL = "gpt-4o-transcribe"
TRANSCRIPTION_HINT = (
    "Human factors interview answer. Likely terms: psychophysics, perceptual threshold, staircase, psychometric "
    "function, fNIRS, NASA-TLX, uFMEA, MIL-STD-1472, NASA-STD-3001, Lattice OS, counter-drone, command and control, "
    "Meaningful Human Control, Calibrated Cognitive Friction, Principles for Agentic Trust, Anduril, Mercedes-Benz, "
    "Lunar Gateway, Sling, Brigham, CSCW."
)
AUDIO_RETENTION_SECONDS = 3600.0
OPENAI_TIMEOUT_SECONDS = 45.0
DEBRIEF_TIMEOUT_SECONDS = 300.0
OPENAI_MAX_RETRIES = 3
SESSION_LOG_END = "<!-- FOUR_TURN_SESSION_LOG_END -->"
SPEAKING_WORDS_PER_MINUTE = 150
SESSION_RECORD_PATTERN = re.compile(r"<!-- FOUR_TURN_SESSION_JSON (.+?) -->")
SPRINT_PROGRESS_PATTERN = re.compile(r"<!-- SPRINT_CHECKLIST_JSON (.*?) -->")
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
PUSHBACK_WORD_LIMIT = 18
QUESTION_WORD_LIMIT = 25
SCORECARD_PLACEHOLDER = (
    "The interview runs uninterrupted. Press **Wrap Up & Finalize Session** when you are done "
    "and the full holistic scorecard appears here."
)
HARD_EVIDENCE_ANCHORS = """Canonical hard-evidence anchors the answer may legitimately draw on:
- $50M operational value from the Amazon psychophysics program that replaced arbitrary latency targets with perceptual thresholds
- 30% task-time reduction and eliminated critical input errors on NASA Lunar Gateway clinical workstations
- fNIRS neuroimaging plus eye-tracking objective cognitive load framework
- uFMEA risk analysis for high-consequence use errors
- NASA-STD-3001 and MIL-STD-1472 standards application
- Principles for Agentic Trust, accepted to ACM CSCW 2026 Industry Perspectives
- US Patent US-12532040-B1 for context-aware multimodal interaction architectures
- Calibrated Cognitive Friction thesis and Meaningful Human Control
Credit an anchor only when the spoken answer actually invokes and uses it. Never invent an anchor, a new number, or an outcome that is not in the canonical record."""
SPOKEN_STYLE_RULES = """Say it like a person, not like a written question read out loud. This is a conversation.
- Plain, everyday language. Contractions. Short words over long ones. One idea per sentence.
- Ask for one thing. A single walkthrough with a couple of named parts is fine; two separate questions in one breath is not. No lists, no "and also", no parentheses, no semicolons.
- Say instrument and standard names the way they are said aloud: functional near-infrared spectroscopy, the NASA Task Load Index, military standard 1472, use-error failure modes and effects analysis. Acronyms people genuinely say out loud in this world are fine as they are: C2, AI, ML, PM, UX. Never speak a citation, a patent number, or a pillar code.
- Write numbers, money, and units the way they are spoken: fifty million dollars, not $50M; twenty-four percent, not 24%; a hundred and twenty milliseconds, not 120ms.
- Never use written-report verbs: articulate, delineate, elucidate, expound, enumerate, leverage, utilize, operationalize. Say tell me, walk me through, how did you, what made you, where does that break, who decided that.
- Real interviewers open like people: "Okay, so...", "Hang on.", "Let me push on that one." Use at most a few words of that, and not on every turn.
- Plain language changes the wording only. The thing you are asking for stays exactly what the bank specifies."""
PROBE_STANCES = (
    "Cold open — lead with the demand, no preamble.",
    "Quote-back — open by repeating the candidate's own words, then press on them.",
    "Scenario — put the demand inside one concrete Air Defense moment.",
    "Inversion — ask for the case where their own position fails.",
    "Narrow demand — ask for one number, one threshold, or one named method.",
    "Forced choice — make them choose between their approach and the cheaper alternative.",
)
UPLEVEL_BAR = """Senior UXR signal: expertly plans and executes research studies with clear timelines and actionable tactical insights.
Lead/Staff upleveling signal: establishes company-wide AI safety and trust frameworks before regulations exist, bridges engineering latency targets with human psychophysics, translates complex Human Systems Integration findings into hard hardware and software specifications, defines Research Operations, and drives multi-million-dollar business impact.
Executing an excellent study is the Senior baseline, not the uplevel. Reserve Lead/Staff signal for durable, reusable, organization-scale mechanisms."""
PERSONAS = {
    "Dr. Daniella Kim — Research Head": "Dr. Daniella Kim",
    "Systems / ML Engineering Lead": "Systems / ML Engineering Lead",
    "Product Manager": "Product Manager",
    "Design Lead": "Design Lead",
}
PERSONA_VOICES = {
    "Dr. Daniella Kim": "nova",
    "Systems / ML Engineering Lead": "onyx",
    "Product Manager": "alloy",
    "Design Lead": "fable",
}
PERSONA_SPEECH = {
    "Dr. Daniella Kim": "Senior research director talking across a table, not reading. Measured, precise, unhurried. Curious rather than warm, and completely unimpressed by fluency.",
    "Systems / ML Engineering Lead": "Blunt engineer in a real conversation. Clipped, fast, a little impatient. Flat affect, no pleasantries, lands hard on the word that matters.",
    "Product Manager": "Brisk product lead thinking out loud. Direct and time-pressured, conversational but pointed, like a meeting starts in five minutes.",
    "Design Lead": "Thoughtful design lead in an easy back-and-forth. Warmer and collaborative, but pressing — asks the awkward question in a friendly tone.",
}
DEFAULT_TTS_VOICE = "nova"
DEFAULT_TTS_STYLE = "Professional interviewer. Direct and conversational."
SYSTEM_PROMPT = """You are the evidence-grounded Anduril Air Defense Voice Interview Coach for Brandon Fluegel, PhD.

You operate in two separate modes and never mix them in a single response.

LIVE MODE: you are the selected interviewer persona in a continuous spoken interview that runs for as many turns as the candidate wants. Stay fully in character. Never grade, score, coach, praise, or narrate the rubric while the conversation is live. React to what the candidate just said and keep probing.

DEBRIEF MODE: after the candidate ends the session, you drop the persona and act as the independent coach, scoring the entire transcript holistically on Substance, Structure, Relevance, Credibility, and Differentiation, plus a separate Tone & Authority read. Separately evaluate Research Thesis, Empirical Rigor, Research Velocity, Systems Integration, Cross-Functional Influence, Standard Setting, Operational Judgment, and Executive Communication. Use N/E when a Lead/Staff criterion is not evidenced anywhere in the transcript.

Cross-examine canonical resume evidence against the posted Senior User Experience Researcher requirements and the Lead/Staff upleveling bar. Never invent metrics, outcomes, team details, classified information, clearance status, or familiarity with an interviewer.

Senior UXR baseline means expertly designing and executing studies that produce actionable insights. Lead/Staff signal means setting reusable standards, bridging human perception to engineering requirements, establishing frameworks before policy exists, defining Research Operations, influencing decisions across functions, and translating HSI evidence into hard hardware/software specifications.

This is one continuous spoken conversation, not a set of isolated prompts. Every question after the first must reference something the candidate actually said. You are given the full transcript and a running claim ledger on every live turn: hold later answers against earlier ones and name contradictions, walked-back numbers, and retold stories. Keep interviewer questions and pushback concise and voice-friendly, and equally clear whether the candidate hears them aloud or reads them on screen. Treat prior resume claims as context to probe, not proof that a spoken answer demonstrated a competency. Preserve Meaningful Human Control, operational tempo, and evidence integrity throughout.

For the third question, select a behavioral/fit pillar from the canonical behavioral question bank using the active persona's adaptation. Judge behavioral answers on STAR/STARE completeness, concrete ownership, interpersonal maturity, and Lead/Staff organizational impact. STAR/STARE is the standard for behavioral and experience answers only. Do not impose it on technical, methodological, or research-craft answers; judge those on the claim, the method or mechanism, the evidence and its limits, the threshold or decision it drives, and what would change it.

Anchor technical and research-craft turns to the canonical technical question bank, which maps every posted Air Defense responsibility and qualification onto the candidate's resume evidence: research thesis and falsifiability, psychophysics to system requirements, objective workload and measure selection, safety analysis and military standards, non-deterministic autonomy and trust calibration, operator workflow and interaction architecture, hardware ergonomics and physical-digital integration, quantitative methods including scaled surveys and max-diff, field craft and facilitation including service blueprints and co-creation workshops, and Research Operations including repositories and storytelling. Use each bank entry's follow-ups as the escalation ladder when an answer leaves that pillar's gap open, and never cover the same pillar twice in one session.

A third canonical bank covers Anduril culture, mission fit, and collaboration with likely stakeholders: mission motivation, ownership with little oversight, months-not-years delivery cadence, engineering partnership, hardware and field-test collaboration, product and roadmap partnership, design partnership and critique, military operator and customer access, security-conscious collaboration under access restrictions, and teammate behavior, culture, and mentorship. Draw from it on the behavioral, leadership, and open turns. Keep every culture question grounded in the posted job description and canonical resume: never assert internal Anduril process, tooling, team structure, headcount, or program details, never imply the candidate has any acquaintance or private exchange with anyone on the panel, and never state or imply the candidate's clearance status. The candidate may reference the three questions Dr. Kim posed publicly at the Learners Conference in San Francisco in May 2026 and the written research response he produced; treat any characterization of her remarks beyond those three questions, and any claimed result from that response's proposed studies, as an evidence violation. Also treat any former-employer internal codename, competitor benchmark, or dollar or interaction-count figure other than the roughly fifty million in projected operational value as a confidentiality violation worth probing, including any allusion to a larger unnamed internal figure or any inflation of the number under pressure.

A fourth canonical bank covers positioning, scope, and close: the ninety-second pitch, why leave and why here, the first ninety days, research vision, the level and scope argument, working with research leadership, cross-panel message discipline, portfolio framing, the candidate's questions for the interviewer, and objection handling. Draw from it in the hiring manager conversation and at the close of any session.

The recruiter screen is already complete. Location preference, compensation expectations, travel, and clearance eligibility are settled and closed: never ask about them, never treat them as gaps, and never assert a compensation number or an active clearance status. The remaining loop is a forty-five-minute conversation with Dr. Daniella Kim built around a single case study presented and then probed in depth, which gates a subsequent onsite of four back-to-back 1:1 interviews with engineering, design, and product partners; the portfolio presentation is being prepared later. Every rehearsal runs as one continuous conversation with a single selected persona, so any of the four personas may draw from any bank when the transcript calls for it.
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
PERSONA_STYLE = {
    "Dr. Daniella Kim": (
        "Speaks in method vocabulary and wants the falsifier and the boundary of the evidence. "
        "Refuses abstract framing that carries no testable claim."
    ),
    "Systems / ML Engineering Lead": (
        "Blunt and requirements-shaped, wants thresholds, failure modes, and observable signals. "
        "Refuses any recommendation that cannot be verified in a test harness."
    ),
    "Product Manager": (
        "Speaks in cost, tempo, and consequence, and wants the decision that changed and the price of being wrong. "
        "Refuses answers that sound like a gate on shipping."
    ),
    "Design Lead": (
        "Speaks in workflow states, modality, and information density, and wants the point where the interaction itself changes. "
        "Refuses verdicts handed down instead of co-ownership."
    ),
}
INTERVIEW_ARC = {
    1: (
        "Positioning & Technical Core",
        "the persona sets the stage in one breath, then probes either the candidate's positioning for this role or a specific claim from the Principles for Agentic Trust whitepaper or resume for foundational Human Factors, psychophysics, and uFMEA depth",
    ),
    2: (
        "Dynamic Technical Pushback",
        "direct pushback on the weakest claim or unquantified assumption in the candidate's Turn 1 answer, demanding a falsifiable metric",
    ),
    3: (
        "Behavioral & Cross-Functional Friction",
        "friction with PMs, ML/software engineers, or military operators in a fast-paced startup, and conflict resolution without compromising safety standards",
    ),
    4: (
        "Leadership, Scope & Scaling",
        "org-wide standards, scaling Research Operations, the scope the candidate intends to own, team culture, and alignment with Anduril Air Defense's counter-drone Lattice OS mission",
    ),
}
OPEN_STAGE = (
    "Live Cross-Examination",
    "free-flowing follow-up that hunts the thinnest evidence still standing in the transcript, whether that is an unquantified claim, "
    "a leadership scope gap, an Air Defense translation gap, a behavioral ownership gap, or an untested positioning and close pillar",
)


class InterviewQuestion(BaseModel):
    question: str
    pillar_id: str


class InterviewerTurn(BaseModel):
    reaction: str
    question: str
    pillar_id: str
    claim_ledger_entry: str
    interjection: bool
    held_same_pillar: bool


class BehavioralQuestion(BaseModel):
    id: str
    pillar: str
    question: str
    resume_and_role_links: list[str]
    persona_adaptations: dict[str, str]
    follow_ups: list[str]
    lead_staff_bar: str


class BehavioralQuestionBank(BaseModel):
    schema_version: str
    purpose: str
    usage_policy: str
    personas: list[str]
    questions: list[BehavioralQuestion]


class TechnicalQuestion(BaseModel):
    id: str
    pillar: str
    arc_stages: list[Literal["opening", "pushback", "leadership"]]
    question: str
    resume_and_role_links: list[str]
    persona_adaptations: dict[str, str]
    follow_ups: list[str]
    lead_staff_bar: str


class TechnicalQuestionBank(BaseModel):
    schema_version: str
    purpose: str
    usage_policy: str
    personas: list[str]
    questions: list[TechnicalQuestion]


class CultureQuestion(BaseModel):
    id: str
    pillar: str
    arc_stages: list[Literal["behavioral", "leadership", "open"]]
    stakeholders: list[str]
    question: str
    resume_and_role_links: list[str]
    persona_adaptations: dict[str, str]
    follow_ups: list[str]
    lead_staff_bar: str


class CultureQuestionBank(BaseModel):
    schema_version: str
    purpose: str
    usage_policy: str
    personas: list[str]
    questions: list[CultureQuestion]


class PositioningQuestion(BaseModel):
    id: str
    pillar: str
    arc_stages: list[Literal["opening", "midpoint", "close"]]
    question: str
    resume_and_role_links: list[str]
    persona_adaptations: dict[str, str]
    follow_ups: list[str]
    lead_staff_bar: str


class PositioningQuestionBank(BaseModel):
    schema_version: str
    purpose: str
    usage_policy: str
    personas: list[str]
    questions: list[PositioningQuestion]


class SessionRecord(BaseModel):
    timestamp: str
    date: str
    persona: str
    turns_completed: int = Field(default=4, ge=1)
    core_averages: dict[str, float]
    pillars_covered: list[str] = Field(default_factory=list)
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
    evidence: str = Field(
        description="Quote at least one verbatim phrase from the transcript and name the rubric band it matches."
    )


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


class ToneAuthority(BaseModel):
    score: int = Field(ge=1, le=5)
    voice_register: Literal[
        "Executing IC",
        "Emerging Lead",
        "Standard-Setting Lead/Staff",
    ]
    evidence: str = Field(
        description="Quote the verbatim phrasing, including any hedges, that drove the register call."
    )


class Evaluation(BaseModel):
    core_scores: list[CoreScore]
    tone_and_authority: ToneAuthority
    uplevel_scores: list[UplevelScore]
    pillars_covered: list[str]
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
    end_of_session_debrief: str
    uplevel_verdict: Literal["Below Lead Bar", "Lead", "Lead/Staff Borderline", "Staff"]
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
        if not question.follow_ups:
            raise ValueError(f"{question.id} must define at least one follow-up probe.")
    return bank


def load_technical_question_bank() -> TechnicalQuestionBank:
    bank = TechnicalQuestionBank.model_validate_json(read_text("data/technical_questions.json"))
    expected_personas = set(PERSONAS.values())
    if len(bank.questions) != 10:
        raise ValueError("The technical question bank must contain exactly 10 questions.")
    if len({question.id for question in bank.questions}) != 10:
        raise ValueError("Technical question IDs must be unique.")
    if set(bank.personas) != expected_personas:
        raise ValueError("The technical question bank must declare all four interviewer personas.")
    covered_stages: set[str] = set()
    for question in bank.questions:
        if set(question.persona_adaptations) != expected_personas:
            raise ValueError(f"{question.id} must define an adaptation for every interviewer persona.")
        if not question.follow_ups:
            raise ValueError(f"{question.id} must define at least one follow-up probe.")
        if not question.arc_stages:
            raise ValueError(f"{question.id} must map to at least one arc stage.")
        covered_stages.update(question.arc_stages)
    if covered_stages != {"opening", "pushback", "leadership"}:
        raise ValueError("The technical question bank must cover the opening, pushback, and leadership stages.")
    return bank


def load_culture_question_bank() -> CultureQuestionBank:
    bank = CultureQuestionBank.model_validate_json(read_text("data/culture_questions.json"))
    expected_personas = set(PERSONAS.values())
    if len(bank.questions) != 10:
        raise ValueError("The culture and stakeholder question bank must contain exactly 10 questions.")
    if len({question.id for question in bank.questions}) != 10:
        raise ValueError("Culture question IDs must be unique.")
    if set(bank.personas) != expected_personas:
        raise ValueError("The culture question bank must declare all four interviewer personas.")
    covered_stages: set[str] = set()
    for question in bank.questions:
        if set(question.persona_adaptations) != expected_personas:
            raise ValueError(f"{question.id} must define an adaptation for every interviewer persona.")
        if not question.follow_ups:
            raise ValueError(f"{question.id} must define at least one follow-up probe.")
        if not question.stakeholders:
            raise ValueError(f"{question.id} must name at least one stakeholder group.")
        if not question.arc_stages:
            raise ValueError(f"{question.id} must map to at least one arc stage.")
        covered_stages.update(question.arc_stages)
    if covered_stages != {"behavioral", "leadership", "open"}:
        raise ValueError("The culture question bank must cover the behavioral, leadership, and open stages.")
    return bank


def load_positioning_question_bank() -> PositioningQuestionBank:
    bank = PositioningQuestionBank.model_validate_json(read_text("data/positioning_questions.json"))
    expected_personas = set(PERSONAS.values())
    if len(bank.questions) != 10:
        raise ValueError("The positioning question bank must contain exactly 10 questions.")
    if len({question.id for question in bank.questions}) != 10:
        raise ValueError("Positioning question IDs must be unique.")
    if set(bank.personas) != expected_personas:
        raise ValueError("The positioning question bank must declare all four interviewer personas.")
    covered_stages: set[str] = set()
    for question in bank.questions:
        if set(question.persona_adaptations) != expected_personas:
            raise ValueError(f"{question.id} must define an adaptation for every interviewer persona.")
        if not question.follow_ups:
            raise ValueError(f"{question.id} must define at least one follow-up probe.")
        if not question.arc_stages:
            raise ValueError(f"{question.id} must map to at least one arc stage.")
        covered_stages.update(question.arc_stages)
    if covered_stages != {"opening", "midpoint", "close"}:
        raise ValueError("The positioning question bank must cover the opening, midpoint, and close stages.")
    return bank


BEHAVIORAL_QUESTION_BANK = load_behavioral_question_bank()
TECHNICAL_QUESTION_BANK = load_technical_question_bank()
CULTURE_QUESTION_BANK = load_culture_question_bank()
POSITIONING_QUESTION_BANK = load_positioning_question_bank()
PILLAR_REGISTRY = {
    question.id: (bank_name, question)
    for bank_name, bank in (
        ("Technical", TECHNICAL_QUESTION_BANK),
        ("Behavioral", BEHAVIORAL_QUESTION_BANK),
        ("Culture", CULTURE_QUESTION_BANK),
        ("Positioning", POSITIONING_QUESTION_BANK),
    )
    for question in bank.questions
}
AUTO_PILLAR = "Auto — let the interviewer choose"
PILLAR_CHOICES = [AUTO_PILLAR] + [
    f"{pillar_id} | {question.pillar}" for pillar_id, (_, question) in PILLAR_REGISTRY.items()
]
ResponseModel = TypeVar("ResponseModel", bound=BaseModel)


def behavioral_question_options(persona: str) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {question.persona_adaptations[persona]}\n"
        f"  Follow-ups: {' / '.join(question.follow_ups)}\n"
        f"  Lead/Staff bar: {question.lead_staff_bar}"
        for question in BEHAVIORAL_QUESTION_BANK.questions
    )


def technical_question_options(persona: str, stage: str) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {question.persona_adaptations[persona]}\n"
        f"  Follow-ups: {' / '.join(question.follow_ups)}\n"
        f"  Lead/Staff bar: {question.lead_staff_bar}"
        for question in TECHNICAL_QUESTION_BANK.questions
        if stage in question.arc_stages
    )


def technical_follow_up_probes(stage: str | None = None) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {' / '.join(question.follow_ups)}"
        for question in TECHNICAL_QUESTION_BANK.questions
        if stage is None or stage in question.arc_stages
    )


def culture_question_options(persona: str, stage: str) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar} (stakeholders: {', '.join(question.stakeholders)}): "
        f"{question.persona_adaptations[persona]}\n"
        f"  Follow-ups: {' / '.join(question.follow_ups)}\n"
        f"  Lead/Staff bar: {question.lead_staff_bar}"
        for question in CULTURE_QUESTION_BANK.questions
        if stage in question.arc_stages
    )


def culture_follow_up_probes(stage: str | None = None) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {' / '.join(question.follow_ups)}"
        for question in CULTURE_QUESTION_BANK.questions
        if stage is None or stage in question.arc_stages
    )


def positioning_question_options(persona: str, stage: str) -> str:
    return "\n".join(
        f"- {question.id} | {question.pillar}: {question.persona_adaptations[persona]}\n"
        f"  Follow-ups: {' / '.join(question.follow_ups)}\n"
        f"  Lead/Staff bar: {question.lead_staff_bar}"
        for question in POSITIONING_QUESTION_BANK.questions
        if stage in question.arc_stages
    )


def selected_pillar_id(pillar_choice: str) -> str:
    return pillar_choice.split("|", 1)[0].strip() if "|" in pillar_choice else ""


def pillar_index() -> str:
    return "\n".join(
        f"- {pillar_id} | {question.pillar} ({bank_name})"
        for pillar_id, (bank_name, question) in PILLAR_REGISTRY.items()
    )


def pillar_brief(pillar_id: str, persona: str) -> str:
    entry = PILLAR_REGISTRY.get(pillar_id)
    if entry is None:
        return ""
    bank_name, question = entry
    return (
        f"The candidate has requested a targeted drill on {bank_name} pillar {question.id} — {question.pillar}. "
        f"Build this turn on it and nothing else.\n"
        f"Persona-adapted question: {question.persona_adaptations[persona]}\n"
        f"Escalation probes: {' / '.join(question.follow_ups)}\n"
        f"Lead/Staff bar (never read aloud): {question.lead_staff_bar}"
    )


def probe_stance() -> str:
    """Varies surface framing per turn so the rehearsed pillar spine can stay fixed."""
    return random.choice(PROBE_STANCES)


OPENING_ANCHOR = (
    "Anchor this opener to exactly one pillar from the canonical banks below. The persona-adapted line gives you the substance: "
    "the thing it names and the thing it asks for both have to survive. Say that substance in your own plain spoken words rather "
    "than reading the line — the bank wording is written, and you are talking. Never swap in a different subject or a different "
    "ask. Do not blend pillars and do not read the Lead/Staff bar aloud."
)


def opening_bank(persona: str) -> str:
    return "\n".join(
        [
            technical_question_options(persona, "opening"),
            positioning_question_options(persona, "opening"),
        ]
    )


def stage_instruction(next_turn: int, persona: str) -> str:
    instructions = {
        2: f"""Find the single weakest link in the answer you just heard: the claim with no falsifiable metric, the causal leap, the borrowed team credit, the unstated assumption, or the number with no measurement method behind it. Attack exactly that weak link and demand the missing falsifiable evidence, in the style of "What falsifiable metric proved that latency threshold degraded operator trust?" Quote or paraphrase the candidate's own words so the question is unmistakably about what they just said.

Escalate using the canonical probe library below when one of these probes targets the exact gap the candidate left open. Keep what the probe asks for, but say it in your own plain spoken words and point it at what the candidate actually said. Never read a probe out as written:
{technical_follow_up_probes("pushback")}""",
        3: f"""Move the conversation to behavioral and cross-functional friction. Select the strongest non-duplicative pillar from the following persona-adapted behavioral bank, then frame it so it directly tests handling friction with a PM, an ML/software engineer, or a military operator under fast-paced startup constraints. Use the adapted question directly or tailor it to what the candidate just said, without changing the pillar's intent. Hold that pillar's follow-ups in reserve for later turns and never read the Lead/Staff bar aloud:
{behavioral_question_options(persona)}

If the transcript already covered the friction the behavioral bank targets, you may instead take one non-duplicative pillar from the culture, mission-fit, and stakeholder-collaboration bank below. Keep it grounded in the posted job description and never assert internal Anduril process, team structure, program details, or the candidate's clearance status:
{culture_question_options(persona, "behavioral")}""",
        4: f"""Test whether the candidate can set org-wide Human Factors standards, scale Research Operations beyond their own hands, name the scope they intend to own, and tie that to Anduril Air Defense's counter-drone Lattice OS mission. Build the question off a specific commitment or gap the candidate revealed earlier. Anchor it to one non-duplicative pillar from this leadership-stage bank:
{technical_question_options(persona, "leadership")}

When the stronger gap is culture, ownership without oversight, delivery cadence, or collaboration with a specific stakeholder group, anchor to one of these instead:
{culture_question_options(persona, "leadership")}

When the stronger gap is scope, research vision, the first ninety days, or how the candidate works with research leadership, anchor to one of these instead:
{positioning_question_options(persona, "midpoint")}""",
        "open": f"""Stay in the flow of the live conversation. Hunt the thinnest evidence still standing across the whole transcript and press it, or follow a genuinely interesting thread the candidate just opened. Do not restart the interview, summarize it, or signal that it is ending. If the conversation has reached a natural close, you may hand the floor over and ask what questions the candidate has for you.

Draw from the full canonical probe libraries below, or from a behavioral pillar not yet covered, whenever it sharpens the hunt. Never repeat a pillar the transcript already covered, and never raise location, compensation, travel, or clearance.
Technical and research-craft probes:
{technical_follow_up_probes()}
Culture and stakeholder-collaboration probes:
{culture_follow_up_probes()}
Positioning and close pillars:
{positioning_question_options(persona, "close")}""",
    }
    return instructions.get(next_turn, instructions["open"])


def load_live_context() -> str:
    """Live turns get only what the persona needs in the room; the banks arrive per-turn in the prompt."""
    sections = {
        "SYSTEM CONTRACT": SYSTEM_PROMPT,
        "CANONICAL CANDIDATE RESUME": read_text("data/candidate_profile.json"),
        "CANONICAL AIR DEFENSE JOB REQUIREMENTS": read_text("data/target_anduril_air_defense.json"),
        "CANONICAL STORYBANK AND EVIDENCE TIERS": read_text("data/storybank_6_pillars.json"),
    }
    return "\n\n".join(f"## {name}\n{content}" for name, content in sections.items())


def load_debrief_context() -> str:
    sections = {
        "SYSTEM CONTRACT": SYSTEM_PROMPT,
        "CANONICAL CANDIDATE RESUME": read_text("data/candidate_profile.json"),
        "CANONICAL AIR DEFENSE JOB REQUIREMENTS": read_text("data/target_anduril_air_defense.json"),
        "CANONICAL STORYBANK AND EVIDENCE TIERS": read_text("data/storybank_6_pillars.json"),
        "CANONICAL PILLAR INDEX": pillar_index(),
        "CANONICAL RESPONSE ARCHITECTURE": read_text("practice/00-response-architecture.md"),
        "CURRENT COACHING STATE": read_text("data/coaching_state.md"),
        "INTERVIEW PERSONAS": read_text("references/role-drills.md"),
        "DETAILED RUBRIC": read_text("references/rubrics-detailed.md"),
    }
    return "\n\n".join(f"## {name}\n{content}" for name, content in sections.items())


def parse_openai_response(
    prompt: str,
    response_format: type[ResponseModel],
    max_output_tokens: int,
    instructions: str,
    model: str = LIVE_MODEL,
    reasoning_effort: str = LIVE_REASONING_EFFORT,
    timeout: float = OPENAI_TIMEOUT_SECONDS,
) -> ResponseModel:
    try:
        response = OpenAI(
            api_key=require_api_key(),
            timeout=timeout,
            max_retries=OPENAI_MAX_RETRIES,
        ).responses.parse(
            model=model,
            instructions=instructions,
            input=prompt,
            text_format=response_format,
            reasoning={"effort": reasoning_effort},
            max_output_tokens=max_output_tokens,
        )
    except (APITimeoutError, TimeoutError) as exc:
        raise gr.Error("The interview request timed out. Your session is intact; please submit again.") from exc
    except APIConnectionError as exc:
        raise gr.Error("The interview service is unreachable. Check your connection and try again.") from exc
    except RateLimitError as exc:
        if "quota" in str(exc).lower():
            raise gr.Error(
                "OpenAI reports no remaining quota on this API key. Check billing, then try again."
            ) from exc
        raise gr.Error(
            "OpenAI rate-limited this request after 3 retries. Wait about a minute, then submit again — "
            "your session is intact."
        ) from exc
    except APIStatusError as exc:
        raise gr.Error(f"The interview service returned an error ({exc.status_code}). Please try again.") from exc
    except ValidationError as exc:
        raise gr.Error("The model response did not match the required score format. Please try again.") from exc

    parsed = response.output_parsed
    if parsed is None:
        if getattr(response, "status", "") == "incomplete":
            raise gr.Error("The model ran out of output budget before finishing. Please submit again.")
        raise gr.Error("The model returned no structured response. Please try again.")
    return parsed


def calculate_core_averages(evaluation: Evaluation) -> dict[str, float]:
    scores = {item.dimension: float(item.score) for item in evaluation.core_scores}
    return {dimension: scores.get(dimension, 0.0) for dimension in CORE_DIMENSIONS}


def known_pillars(raw_ids: list[str]) -> list[str]:
    seen: list[str] = []
    for raw in raw_ids:
        pillar_id = raw.split("|", 1)[0].strip().upper()
        if pillar_id in PILLAR_REGISTRY and pillar_id not in seen:
            seen.append(pillar_id)
    return seen


def persist_session(
    persona: str,
    evaluation: Evaluation,
    turns_completed: int,
    pillars_covered: list[str] | None = None,
) -> SessionRecord:
    timestamp = datetime.now().astimezone()
    passed_uplevel = evaluation.uplevel_verdict in {"Lead", "Lead/Staff Borderline", "Staff"}
    primary_bottleneck = " ".join(evaluation.primary_gap.split()).replace("-->", "->")
    actionable_fix = " ".join(evaluation.priority_move.split()).replace("-->", "->")
    record = SessionRecord(
        timestamp=timestamp.isoformat(timespec="seconds"),
        date=timestamp.date().isoformat(),
        persona=persona,
        turns_completed=turns_completed,
        core_averages=calculate_core_averages(evaluation),
        pillars_covered=known_pillars(
            pillars_covered if pillars_covered is not None else evaluation.pillars_covered
        ),
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
- **Turns completed:** {record.turns_completed}
- **Pillars covered:** {', '.join(record.pillars_covered) or 'None recorded'}
- **Core averages:** {averages}
- **Lead/Staff upleveling:** {record.uplevel_rating}
- **Primary bottleneck:** {record.primary_bottleneck}
- **Actionable fix:** {record.actionable_fix}
<!-- FOUR_TURN_SESSION_JSON {record.model_dump_json()} -->
"""
    with SESSION_WRITE_LOCK:
        state = COACHING_STATE_PATH.read_text(encoding="utf-8")
        if SESSION_LOG_END not in state:
            state = f"{state.rstrip()}\n\n## Persistent Mock Sessions\n{SESSION_LOG_END}\n"
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


def load_sprint_progress() -> list[str]:
    state = COACHING_STATE_PATH.read_text(encoding="utf-8")
    match = SPRINT_PROGRESS_PATTERN.search(state)
    if not match:
        return []
    try:
        stored = json.loads(match.group(1))
    except json.JSONDecodeError:
        return []
    return [item for item in stored if item in SPRINT_CHECKLIST]


def save_sprint_progress(selected: list[str] | None) -> None:
    payload = json.dumps([item for item in (selected or []) if item in SPRINT_CHECKLIST])
    marker = f"<!-- SPRINT_CHECKLIST_JSON {payload} -->"
    with SESSION_WRITE_LOCK:
        state = COACHING_STATE_PATH.read_text(encoding="utf-8")
        if SPRINT_PROGRESS_PATTERN.search(state):
            updated_state = SPRINT_PROGRESS_PATTERN.sub(lambda _: marker, state, count=1)
        else:
            updated_state = f"{state.rstrip()}\n\n## Sprint Checklist Progress\n{marker}\n"
        temporary_path = COACHING_STATE_PATH.with_suffix(".md.tmp")
        temporary_path.write_text(updated_state, encoding="utf-8")
        temporary_path.replace(COACHING_STATE_PATH)


def render_coverage_matrix(records: list[SessionRecord]) -> str:
    drilled = [pillar for record in records for pillar in record.pillars_covered]
    banks = (
        ("Technical & research craft", TECHNICAL_QUESTION_BANK),
        ("Behavioral & friction", BEHAVIORAL_QUESTION_BANK),
        ("Culture & stakeholders", CULTURE_QUESTION_BANK),
        ("Positioning & close", POSITIONING_QUESTION_BANK),
    )
    rows = []
    untested_all: list[str] = []
    for label, bank in banks:
        untested = [question.id for question in bank.questions if question.id not in drilled]
        untested_all.extend(untested)
        covered = len(bank.questions) - len(untested)
        rows.append(f"| {label} | {covered}/{len(bank.questions)} | {', '.join(untested) or '—'} |")
    matrix = "\n".join(rows)
    headline = (
        "**Every pillar has been drilled at least once.**"
        if not untested_all
        else f"**{len(untested_all)} pillars still untested.** Use the target-pillar picker to drill them directly."
    )
    return f"""### Pillar Coverage

{headline}

| Bank | Covered | Still untested |
|---|---:|---|
{matrix}
"""


def load_progress_dashboard() -> tuple[str, list[list[object]]]:
    records = load_session_records()
    if records:
        overall = {
            dimension: sum(record.core_averages[dimension] for record in records) / len(records)
            for dimension in CORE_DIMENSIONS
        }
        weakest_dimension = min(overall, key=overall.get)
        readiness = records[-1].readiness_rating
        total_turns = sum(record.turns_completed for record in records)
        turns_line = f"{total_turns} ({total_turns / len(records):.1f} per session)"
    else:
        overall = {dimension: 0.0 for dimension in CORE_DIMENSIONS}
        weakest_dimension = "Not yet measured"
        readiness = "Senior UXR Baseline"
        turns_line = "0"

    score_rows = "\n".join(
        f"| {dimension} | **{overall[dimension]:.2f}/5** |" for dimension in CORE_DIMENSIONS
    )
    summary = f"""## Sprint Readiness

**Total mock sessions completed:** {len(records)}

**Total conversation turns practiced:** {turns_line}

**Weakest dimension alert:** {weakest_dimension}

**Readiness rating:** {readiness}

| Core dimension | Overall average |
|---|---:|
{score_rows}

{render_coverage_matrix(records)}
"""
    history = [
        [
            record.timestamp,
            record.persona,
            record.turns_completed,
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


def render_scorecard(evaluation: Evaluation, turns_completed: int) -> str:
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
    core_average = sum(item.score for item in evaluation.core_scores) / len(evaluation.core_scores)
    return f"""# End of Session Debrief

**Lead/Staff verdict: {evaluation.uplevel_verdict}**

**Turns completed:** {turns_completed} | **Session core average:** {core_average:.2f}/5 | **Confidence:** {evaluation.confidence}

{evaluation.end_of_session_debrief}

## Holistic Session Scorecard

| Core dimension | Score | Evidence |
|---|---:|---|
{core_rows}

### Tone & Authority

**{evaluation.tone_and_authority.voice_register} — {evaluation.tone_and_authority.score}/5**

{evaluation.tone_and_authority.evidence}

### Lead/Staff Read

| Criterion | Rating | Evidence |
|---|---:|---|
{uplevel_rows}

**Strongest signal:** {evaluation.strongest_signal}

**Primary growth area:** {evaluation.primary_gap}

**Priority move:** {evaluation.priority_move}

### Senior vs. Lead/Staff Calibration

**Demonstrated level:** {evaluation.demonstrated_level}

**Senior UXR baseline:** {evaluation.senior_uxr_baseline_assessment}

**Lead/Staff upleveling signal:** {evaluation.lead_staff_uplevel_assessment}
"""


def conversation_stage(turn: int) -> tuple[str, str]:
    return INTERVIEW_ARC.get(turn, OPEN_STAGE)


def turn_indicator(turn: int, interjection: bool = False, held: bool = False) -> str:
    title, _ = conversation_stage(turn)
    if interjection:
        title = f"{title} — interjection"
    elif held:
        title = f"{title} — same ground, sharper"
    return f"**Question {turn}: {title}** — keep going or wrap up whenever you are ready."


def render_transcript_review(history: list[dict[str, str]]) -> str:
    if not history:
        return ""
    lines = []
    for message in history:
        speaker = "**Interviewer**" if message["role"] == "assistant" else "**You**"
        lines.append(f"{speaker}: {message['content']}")
    body = "\n\n".join(lines)
    return f"\n\n---\n\n## Transcript Review\n\nRead your own phrasing back against the critique above.\n\n{body}\n"


def require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise gr.Error("OPENAI_API_KEY is not set. In PowerShell, run: $env:OPENAI_API_KEY='your-key'")
    return api_key


def strip_markdown(text: str) -> str:
    lines = [
        re.sub(r"^\s*(?:[-+*]|\d+\.)\s+", "", line)
        for line in str(text or "").splitlines()
        if not line.lstrip().startswith("#")
    ]
    spoken = " ".join(lines)
    spoken = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", spoken)
    spoken = re.sub(r"[*_`>|~]+", " ", spoken)
    return re.sub(r"\s+", " ", spoken).strip()


def resolve_voice(persona: str) -> str:
    name = PERSONAS.get(persona, persona)
    return PERSONA_VOICES.get(name, DEFAULT_TTS_VOICE)


def resolve_speech_style(persona: str) -> str:
    name = PERSONAS.get(persona, persona)
    return PERSONA_SPEECH.get(name, DEFAULT_TTS_STYLE)


def prune_temp_audio() -> None:
    cutoff = time.time() - AUDIO_RETENTION_SECONDS
    for stale in TEMP_AUDIO_DIR.glob("*.mp3"):
        try:
            if stale.stat().st_mtime < cutoff:
                stale.unlink()
        except OSError:
            continue


def generate_interviewer_audio(text: str, persona: str) -> str:
    spoken = strip_markdown(text)
    if not spoken:
        return ""

    TEMP_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    prune_temp_audio()
    try:
        response = OpenAI(
            api_key=require_api_key(),
            timeout=OPENAI_TIMEOUT_SECONDS,
            max_retries=1,
        ).audio.speech.create(
            model=TTS_MODEL,
            voice=resolve_voice(persona),
            instructions=resolve_speech_style(persona),
            input=spoken,
        )
        with tempfile.NamedTemporaryFile(
            suffix=".mp3", dir=TEMP_AUDIO_DIR, delete=False
        ) as handle:
            handle.write(response.read())
            return handle.name
    except (APITimeoutError, TimeoutError, APIConnectionError, RateLimitError, APIStatusError, OSError) as exc:
        gr.Warning(f"Interviewer audio unavailable: {exc}")
        return ""


def speak_interviewer(markdown_text: str, persona_label: str, audio_enabled: bool = True) -> str:
    if not audio_enabled:
        return ""
    return generate_interviewer_audio(markdown_text, persona_label)


def replay_interviewer(markdown_text: str, persona_label: str, existing_path: str) -> str:
    """Plays on demand even when auto-play is off, so silent sessions can still hear a question."""
    if existing_path and Path(existing_path).exists():
        return existing_path
    return generate_interviewer_audio(markdown_text, persona_label)


def render_transcript(history: list[dict[str, str]], limit: int | None = None) -> str:
    messages = history[-limit:] if limit else history
    if not messages:
        return "No prior turns."
    speakers = {"assistant": "INTERVIEWER", "user": "CANDIDATE"}
    return "\n\n".join(
        f"{speakers.get(message['role'], message['role'].upper())}: {message['content']}"
        for message in messages
    )


def completed_turns(history: list[dict[str, str]]) -> int:
    return sum(1 for message in history if message["role"] == "user")


def render_claims_ledger(claims: list[str]) -> str:
    if not claims:
        return "No claims recorded yet."
    return "\n".join(f"- Turn {index}: {claim}" for index, claim in enumerate(claims, start=1))


def render_covered_pillars(pillars: list[str]) -> str:
    if not pillars:
        return "None yet."
    return ", ".join(
        f"{pillar} ({PILLAR_REGISTRY[pillar][1].pillar})" if pillar in PILLAR_REGISTRY else pillar
        for pillar in pillars
    )


def audio_duration_seconds(audio_path: str) -> float:
    """Header frame counts can be wrong on streamed clips, so trust whichever length is shorter."""
    try:
        with contextlib.closing(wave.open(audio_path)) as clip:
            frame_size = clip.getnchannels() * clip.getsampwidth()
            payload_frames = max(Path(audio_path).stat().st_size - 44, 0) / frame_size
            return round(min(clip.getnframes(), payload_frames) / clip.getframerate(), 1)
    except (OSError, wave.Error, ZeroDivisionError):
        return 0.0


def transcribe_answer(audio_path: str | None) -> tuple[str, float]:
    """Verbatim transcription: hedges and filler survive because the register call depends on them."""
    if not audio_path:
        return "", 0.0
    try:
        with open(audio_path, "rb") as clip:
            result = OpenAI(
                api_key=require_api_key(),
                timeout=OPENAI_TIMEOUT_SECONDS,
                max_retries=OPENAI_MAX_RETRIES,
            ).audio.transcriptions.create(
                model=TRANSCRIBE_MODEL,
                file=clip,
                prompt=TRANSCRIPTION_HINT,
            )
    except (APITimeoutError, TimeoutError) as exc:
        raise gr.Error("Transcription timed out. The recording is still there — press stop and try again.") from exc
    except APIConnectionError as exc:
        raise gr.Error("Transcription is unreachable. Check your connection and try again.") from exc
    except (RateLimitError, APIStatusError) as exc:
        raise gr.Error(f"Transcription failed ({exc.__class__.__name__}). Record again or type your answer.") from exc
    except OSError as exc:
        raise gr.Error("The recording could not be read. Please record again.") from exc
    return result.text.strip(), audio_duration_seconds(audio_path)


def render_pacing_log(history: list[dict[str, str]]) -> str:
    answers = [message for message in history if message["role"] == "user"]
    if not answers:
        return "No answers recorded."
    lines = []
    for index, message in enumerate(answers, start=1):
        spoken_words = len(message["content"].split())
        measured = float(message.get("seconds") or 0)
        timing = (
            f"{measured:.0f}s measured"
            if measured
            else f"~{round(spoken_words / SPEAKING_WORDS_PER_MINUTE * 60)}s estimated from word count"
        )
        lines.append(f"- Answer {index}: {spoken_words} words, {timing}")
    return "\n".join(lines)


def answer_meter(text: str, spoken_seconds: float = 0.0) -> str:
    words = len((text or "").split())
    if not words:
        return "0 words — technical answers run 160-230 words, behavioral 200-265, follow-up probes 45-90."
    measured = float(spoken_seconds or 0)
    seconds = round(measured) if measured else round(words / SPEAKING_WORDS_PER_MINUTE * 60)
    source = "spoken" if measured else "estimated"
    if seconds < 20:
        verdict = "too short to carry evidence, even for a follow-up"
    elif seconds <= 35:
        verdict = "follow-up length — right for a scalpel answer, short for a main answer"
    elif seconds <= 90:
        verdict = "technical main-answer range"
    elif seconds <= 110:
        verdict = "behavioral main-answer range — long for a technical answer"
    else:
        verdict = "past the hard ceiling — an interviewer would cut in"
    return f"**{words} words · {seconds}s {source}** — {verdict}."


def merge_pillars(covered: list[str], pillar_id: str) -> list[str]:
    cleaned = (pillar_id or "").split("|", 1)[0].strip().upper()
    if cleaned in PILLAR_REGISTRY and cleaned not in covered:
        return [*covered, cleaned]
    return list(covered)


LIVE_MEMORY_RULES = """You have the complete transcript and a running ledger of every concrete claim the candidate has made. Use them. Hold their later answers against their earlier ones and name any contradiction, walked-back number, retold story, or claim that shrank under pressure.

Answer-quality rule: if the answer you just heard was short, hedged, or carried no mechanism, no number, and no first-person ownership, do NOT advance the interview. Stay on the same ground and ask the narrower version of the same question. Set held_same_pillar to true when you do this. Real interviewers do not move on just because the candidate spoke.

Interjection rule: when the answer hinged on an unsupported causal leap or a number with no method behind it, cut in instead of asking a full question. An interjection is a reaction of at most 10 words naming the flaw plus a question of at most 12 words demanding the missing piece. Set interjection to true. Use this sparingly, at most once every three turns.

Return pillar_id as the canonical bank ID this turn tested, such as TQ02, BQ04, CQ07, or PQ05, or an empty string when the turn tests no specific bank pillar.

Return claim_ledger_entry as one short line recording what the candidate just claimed, in the form "claim - mechanism or method - number or outcome - ownership". Write "no substantive claim" when the answer contained none."""


def generate_question(
    persona_label: str,
    turn: int,
    history: list[dict[str, str]],
    pillar_choice: str,
) -> tuple[str, str]:
    persona = PERSONAS[persona_label]
    title, objective = conversation_stage(turn)
    prior_context = render_transcript(history)
    pillar_id = selected_pillar_id(pillar_choice)
    if pillar_id:
        anchor = pillar_brief(pillar_id, persona)
    else:
        anchor = f"""{OPENING_ANCHOR}
{opening_bank(persona)}"""
    prompt = f"""Open a live spoken interview as {persona}. This is Question {turn}.

Arc stage: {title}
Stage objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}
Persona speech style: {PERSONA_STYLE[persona]}
Framing stance for this turn (vary the wording, never the pillar): {probe_stance()}
Prior conversation: {prior_context}

{HARD_EVIDENCE_ANCHORS}

{anchor}

{SPOKEN_STYLE_RULES}

Ask exactly one concise, voice-friendly question in character. Make it answerable aloud. Set the stage in at most one short clause that signals who you are and what you own, then immediately probe one named claim from the Principles for Agentic Trust whitepaper or the canonical resume. Do not provide coaching, an answer, a score, or a question number. Do not invent candidate evidence or classified Anduril details.

The spoken question must be one conversational sentence of at most {QUESTION_WORD_LIMIT} words that lands in a single pass, whether it is heard aloud or read on screen. Lead with the challenge, in plain words a person would actually say out loud.

Cross-examine a concrete claim from the canonical resume against a concrete Air Defense responsibility or qualification. Do not ask a generic interview question. Distinguish evidence that merely meets the Senior UXR baseline from evidence that could prove Lead/Staff scope.

Return pillar_id as the canonical bank ID this question tests, such as TQ02 or PQ01.
"""
    result = parse_openai_response(
        prompt,
        InterviewQuestion,
        max_output_tokens=1600,
        instructions=load_live_context(),
    )
    return result.question.strip(), result.pillar_id.strip()


def render_interviewer(persona: str, question: str, reaction: str = "") -> str:
    body = f"{reaction}\n\n{question}" if reaction.strip() else question
    return f"## {persona}\n\n{body}"


def start_interview(
    persona_label: str,
    pillar_choice: str,
) -> tuple[str, str, str, int, list[dict[str, str]], str, list[str], list[str], str]:
    question, pillar_id = generate_question(persona_label, 1, [], pillar_choice)
    history = [{"role": "assistant", "content": question}]
    return (
        turn_indicator(1),
        render_interviewer(PERSONAS[persona_label], question),
        SCORECARD_PLACEHOLDER,
        1,
        history,
        "",
        [],
        merge_pillars([], pillar_id),
        persona_label,
    )


def continue_conversation(
    answer: str,
    turn: int,
    history: list[dict[str, str]] | None,
    claims: list[str] | None,
    covered: list[str] | None,
    active_persona: str,
    spoken_seconds: float = 0.0,
) -> tuple[str, str, str, int, list[dict[str, str]], str, list[str], list[str], str]:
    answer = answer.strip()
    if not answer:
        raise gr.Error("Record or type an answer first.")

    prior_turns = history or []
    if turn < 1 or not prior_turns or not active_persona:
        raise gr.Error("Start a new interview before submitting an answer.")

    persona = PERSONAS[active_persona]
    claims_ledger = list(claims or [])
    covered_pillars = list(covered or [])
    next_turn = turn + 1
    title, objective = conversation_stage(next_turn)
    stage_directive = stage_instruction(next_turn, persona)

    prompt = f"""You are {persona} in a live spoken interview. LIVE MODE only.

This is your response to the candidate's answer to Question {turn}. Your next question is Question {next_turn}.
Conversation stage: {title}
Stage objective: {objective}
Persona lens: {PERSONA_FOCUS[persona]}
Persona speech style: {PERSONA_STYLE[persona]}
Framing stance for this turn (vary the wording, never the pillar): {probe_stance()}

{LIVE_MEMORY_RULES}

Claim ledger so far:
{render_claims_ledger(claims_ledger)}

Pillars already covered this session — do not repeat one unless you are deliberately holding the same ground because the last answer was thin:
{render_covered_pillars(covered_pillars)}

{stage_directive}

{HARD_EVIDENCE_ANCHORS}

{SPOKEN_STYLE_RULES}

Return the fields below and nothing else.
- reaction: your immediate in-character reaction to what the candidate just said, at most {PUSHBACK_WORD_LIMIT} words across at most two short sentences, or at most 10 words when this is an interjection. Say it the way a person reacts out loud. Name the specific thing you are pushing on, or acknowledge the strongest concrete detail in one clause. It may be empty only if the follow-up question carries the pushback on its own.
- question: exactly one concise, plain-spoken follow-up question of at most {QUESTION_WORD_LIMIT} words, or at most 12 words when this is an interjection, in character, that builds on what the candidate actually just said so the interview reads as one continuous conversation.
- pillar_id, claim_ledger_entry, interjection, and held_same_pillar per the memory rules above.

Absolute rules for LIVE MODE: never score, never grade, never mention rubrics, dimensions, STAR, Senior versus Lead/Staff calibration, or coaching advice. Never praise generically. Never announce how many questions remain or that the interview is over. Never invent facts about Anduril, Dr. Kim, the candidate, classified systems, study outcomes, or prior interactions. Write the spoken fields as speech that also reads cleanly on screen: no markdown, no bullet lists, no headings, and no parenthetical asides.

Full conversation so far:
{render_transcript(prior_turns)}

Candidate's newest answer:
{answer}
"""

    result = parse_openai_response(
        prompt,
        InterviewerTurn,
        max_output_tokens=2000,
        instructions=load_live_context(),
    )
    question = result.question.strip()
    if not question:
        raise gr.Error("The interviewer returned no follow-up question. Please submit again.")
    reaction = result.reaction.strip()
    entry = result.claim_ledger_entry.strip()
    if entry:
        claims_ledger.append(entry)

    updated_history = [
        *prior_turns,
        {"role": "user", "content": answer, "seconds": f"{float(spoken_seconds or 0):.0f}"},
    ]
    if reaction:
        updated_history.append({"role": "assistant", "content": reaction})
    updated_history.append({"role": "assistant", "content": question})
    return (
        turn_indicator(next_turn, interjection=result.interjection, held=result.held_same_pillar),
        render_interviewer(persona, question, reaction),
        SCORECARD_PLACEHOLDER,
        next_turn,
        updated_history,
        "",
        claims_ledger,
        merge_pillars(covered_pillars, result.pillar_id),
        active_persona,
    )


def finalize_session(
    turn: int,
    history: list[dict[str, str]] | None,
    claims: list[str] | None,
    covered: list[str] | None,
    active_persona: str,
) -> tuple[str, str, str, int, list[dict[str, str]], str, list[str], list[str], str]:
    prior_turns = history or []
    turns_completed = completed_turns(prior_turns)
    if turns_completed < 1:
        raise gr.Error("Answer at least one question before wrapping up the session.")
    if not active_persona:
        raise gr.Error("Start a new interview before wrapping up a session.")

    persona = PERSONAS[active_persona]
    claims_ledger = list(claims or [])
    covered_pillars = list(covered or [])
    prompt = f"""DEBRIEF MODE. Drop the persona and act as the independent coach.

The candidate just ended a live interview with {persona} after {turns_completed} answered turns. Evaluate the ENTIRE transcript holistically as one performance, not turn by turn. Weigh the whole arc: how the candidate opened, how they held up under pushback, whether they escalated their evidence when pressed, and where they ended.

Running claim ledger captured live during the session:
{render_claims_ledger(claims_ledger)}

Bank pillars the interviewer recorded as covered: {render_covered_pillars(covered_pillars)}

Measured pacing, one line per answer. "measured" is the real spoken length of a dictated answer; "estimated" is derived from word count for a typed answer. Grade pacing on the measured numbers where they exist:
{render_pacing_log(prior_turns)}

Persona lens used in the room: {PERSONA_FOCUS[persona]}

Apply all five core dimensions once for the session, rate Tone & Authority once for the session, and apply every Lead/Staff criterion once for the session. Use null for a Lead/Staff score when the transcript provides no evidence for that criterion; missing evidence is not automatically poor performance.

Scoring discipline, which overrides any instinct to be even-handed:
- Every core score, the Tone & Authority score, and every non-null Lead/Staff score must quote at least one verbatim phrase from the transcript in its evidence field and name the rubric band that phrase matches. An evidence field with no quotation is invalid.
- Score each dimension independently against its own rubric row. A weak dimension must not drag an unrelated one down, and a strong one must not lift the rest.
- Use the full 1-5 range. When the transcript contains concrete support at the 4 or 5 band for one dimension, award it even if every other dimension is weak.
- If all five core scores land on the same value, state explicitly in end_of_session_debrief why the session was genuinely uniform on every dimension. Identical scores are a finding that must be defended, never a default.
- The transcript is verbatim spoken text, including hedges and filler. Quote hedges such as "sort of", "we", "I was involved in", or "they let me" directly when they drive the Tone & Authority register call.

Grade the core dimensions with this calibration. The CANONICAL RESPONSE ARCHITECTURE section in your instructions is the structure and length contract the candidate is rehearsing against; grade to it.
- STRUCTURE: judge each answer by its type. Apply STAR plus STARE — Situation, Task, Action, Result, and an explicit Earned Secret — to behavioral, experience, and cross-functional friction answers only. Judge technical, methodological, and research-craft answers on technical reasoning structure instead: the claim or recommendation stated up front, the method or mechanism behind it, the evidence and its limits, the threshold or decision it drives, and the condition that would change it. Name which of the five technical beats or six behavioral beats were missing, using those beat names. Never mark a technical answer down for lacking a Situation and Task narrative, and never let a rambling technical answer pass because STAR did not apply. Across the whole session at least one answer of either type must deliver an Earned Secret, meaning a non-obvious lesson only someone who actually ran this work could state; cap Structure at 3 when none does. Penalize generic textbook process instead of specific lived sequences.
- PACING AND FOLLOW-UP DISCIPLINE, scored inside STRUCTURE: use the measured pacing lines above rather than your own estimate. Main technical answers should land at 160-230 words and 65-90 seconds, behavioral at 200-265 words and 90-110 seconds, culture and stakeholder at 170-220 words, and answers to a narrow follow-up probe at 45-90 words and 20-35 seconds. Flag any answer past its ceiling and any follow-up that re-narrated the original story instead of answering the one thing asked; re-narration on a follow-up is a Structure and Relevance penalty on both answers.
- SUBSTANCE: audit for hard data across the session. {HARD_EVIDENCE_ANCHORS}
- RELEVANCE: reward direct connection to Lattice OS, counter-drone command and control, 3D operator workflows, and startup execution speed. Abstract Human Factors theory with no Air Defense translation caps Relevance at 3.
- CREDIBILITY: verify first-person ownership, plausible mechanism, and named method. Downgrade borrowed team credit and unverifiable causal leaps, especially claims that stayed unquantified after direct pushback. Reward volunteering the boundary of the evidence before being asked. Treat these as hard boundary violations and name any that occurred: attributing functional near-infrared spectroscopy to Brigham or Harvard rather than Amazon, claiming any head-to-head result where a biometric measure beat the NASA Task Load Index, or describing Calibrated Cognitive Friction as deployed rather than as an untested thesis.
- DIFFERENTIATION: award the top band only for seamless, load-bearing use of the Calibrated Cognitive Friction thesis or the Principles for Agentic Trust framework. Name-dropping either without applying it is a 2.

If the transcript contains a behavioral or cross-functional friction answer, judge it explicitly on STAR/STARE completeness, concrete first-person ownership, real friction rather than smooth agreement, interpersonal maturity, and whether it produced organizational impact such as a reusable standard, escalation protocol, research-ops mechanism, mentoring system, or durable culture change. If the answer describes agreement rather than a concrete disagreement with a PM, an ML or software engineer, or a military operator, cap Substance and Differentiation at 3 and say so.

Rate tone_and_authority once for the whole session, choosing the voice_register that matches how the candidate speaks:
- 1-2 'Executing IC': narrates assigned usability tests, defers trade-offs upward, hedges, seeks permission.
- 3 'Emerging Lead': owns projects end to end but frames impact locally.
- 4-5 'Standard-Setting Lead/Staff': speaks as the person who sets the standard, names the trade-offs they owned and why, states the bar for the organization, and disagrees with engineering or product from evidence rather than authority.
Quote the specific phrasing that drove the register call.

Explicitly classify demonstrated_level using this bar:
{UPLEVEL_BAR}

For strongest_signal, name the single most convincing moment in the transcript and quote it. For primary_gap, name the single highest-leverage growth area for the next session. For priority_move, give one concrete rehearsal action.

For senior_uxr_baseline_assessment, state plainly what across this session clears or misses the Senior baseline of expertly planned and executed studies with clear timelines and actionable tactical insights. For lead_staff_uplevel_assessment, state whether the session showed pre-regulation framework setting, latency-to-psychophysics bridging, HSI translated into hard system specs, Research Operations definition, or multi-million-dollar business impact, and name the one upgrade that would convert it. Cite specific evidence from the transcript and compare it with the canonical resume and Air Defense job requirements. Prior resume claims are context to probe, not proof that a spoken answer demonstrated the competency.

Produce a comprehensive end_of_session_debrief covering how the candidate performed across all {turns_completed} turns, and a clear uplevel_verdict. In the debrief, name the highest-priority posted Air Defense requirement that went untested so the next session can target it.

Return pillars_covered as the list of canonical bank pillar IDs this session actually probed, using bare IDs such as TQ02, BQ04, CQ07, or PQ05. Include an ID only when the transcript genuinely tested that pillar. Return an empty list if none applies.

Full interview transcript:
{render_transcript(prior_turns)}
"""

    evaluation = parse_openai_response(
        prompt,
        Evaluation,
        max_output_tokens=16000,
        instructions=load_debrief_context(),
        model=DEBRIEF_MODEL,
        reasoning_effort=DEBRIEF_REASONING_EFFORT,
        timeout=DEBRIEF_TIMEOUT_SECONDS,
    )
    validate_evaluation(evaluation)
    session_pillars = covered_pillars + [
        pillar for pillar in known_pillars(evaluation.pillars_covered) if pillar not in covered_pillars
    ]

    try:
        persist_session(persona, evaluation, turns_completed, session_pillars)
    except OSError as exc:
        gr.Warning(f"Interview completed, but progress could not be saved: {exc}")

    return (
        f"**Session complete — {turns_completed} turns with {persona}**",
        f"## {persona}\n\nThat is where we will stop. Thanks for the conversation.",
        render_scorecard(evaluation, turns_completed) + render_transcript_review(prior_turns),
        0,
        prior_turns,
        "",
        claims_ledger,
        session_pillars,
        active_persona,
    )


def clear_session() -> tuple[str, str, str, int, list[dict[str, str]], str, list[str], list[str], str]:
    return (
        "**No interview in progress**",
        "Select an interviewer and start a new interview.",
        SCORECARD_PLACEHOLDER,
        0,
        [],
        "",
        [],
        [],
        "",
    )


def export_session(scorecard_markdown: str, history: list[dict[str, str]] | None, persona_label: str):
    """Writes the debrief to a file so grades survive a host that does not keep a disk."""
    turns = history or []
    if not scorecard_markdown or scorecard_markdown == SCORECARD_PLACEHOLDER or not turns:
        return gr.DownloadButton(visible=False)
    persona = PERSONAS.get(persona_label, persona_label or "Interviewer")
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    slug = re.sub(r"[^a-z0-9]+", "-", persona.lower()).strip("-")
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = EXPORT_DIR / f"session_{stamp}_{slug}.md"
    body = "\n".join(
        [
            f"# Mock Interview Debrief — {persona}",
            f"_{datetime.now().strftime('%Y-%m-%d %H:%M')} · {completed_turns(turns)} turns_",
            "",
            "## Pacing",
            render_pacing_log(turns),
            "",
            scorecard_markdown,
        ]
    )
    path.write_text(body, encoding="utf-8")
    return gr.DownloadButton(value=str(path), visible=True)


def lock_setup() -> tuple[gr.Accordion, gr.Radio]:
    return gr.Accordion(open=False), gr.Radio(interactive=False)


def reset_capture() -> tuple[None, float]:
    return None, 0.0


def unlock_setup() -> tuple[gr.Accordion, gr.Radio]:
    return gr.Accordion(open=True), gr.Radio(interactive=True)


HEAD = r"""
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#f4f1e9">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<script>
// iOS follows the system theme unless the app pins it, and the palette here is light-only.
(function () {
  try {
    var url = new URL(window.location.href);
    if (url.searchParams.get("__theme") !== "light") {
      url.searchParams.set("__theme", "light");
      window.location.replace(url.toString());
    }
  } catch (error) { /* older browsers keep the system theme */ }
})();
</script>
<script>
(function () {
  // A 0.05s silent WAV. iOS grants an element permission to play audible media
  // only after a real, audible-capable play() inside a user gesture; a muted
  // play does not count, so the unlock clip must be genuinely silent instead.
  var SILENT = "data:audio/wav;base64,UklGRkQDAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YSADAAAA";
  var player = null;
  var unlocked = false;
  var lastUrl = "";

  function ensurePlayer() {
    if (!player) {
      player = new Audio();
      player.preload = "auto";
    }
    return player;
  }

  function unlock() {
    if (unlocked) { return; }
    var element = ensurePlayer();
    if (!element.paused) { unlocked = true; return; }
    if (!element.src) { element.src = SILENT; }
    var attempt = element.play();
    if (attempt && attempt.then) {
      attempt.then(function () {
        unlocked = true;
        if (element.src === SILENT) {
          element.pause();
          element.currentTime = 0;
        }
      }).catch(function () {});
    } else {
      unlocked = true;
    }
  }

  ["pointerdown", "touchend", "keydown"].forEach(function (name) {
    document.addEventListener(name, unlock, { capture: true });
  });

  window.playInterviewer = function (path) {
    if (!path) { return; }
    lastUrl = "gradio_api/file=" + encodeURIComponent(String(path));
    var element = ensurePlayer();
    element.src = lastUrl;
    element.currentTime = 0;
    element.onended = function () { window.setTimeout(openMic, 400); };
    element.play().catch(function () {});
  };

  // Turn-taking. The recorder is one toggle button whose label flips
  // between Record and Stop, so the label is the state.
  function recorderButton(label) {
    var host = document.getElementById("recorder");
    if (!host) { return null; }
    var buttons = host.querySelectorAll("button");
    for (var index = 0; index < buttons.length; index += 1) {
      if (buttons[index].textContent.trim() === label && !buttons[index].disabled) {
        return buttons[index];
      }
    }
    return null;
  }

  function handsFree() {
    var box = document.querySelector("#handsfree input[type='checkbox']");
    return !!(box && box.checked);
  }

  function openMic() {
    if (!handsFree()) { return; }
    var indicator = document.getElementById("turn-indicator");
    if (!indicator || indicator.textContent.indexOf("Question ") === -1) { return; }
    var button = recorderButton("Record");
    if (button) { button.click(); }
  }

  function closeMic() {
    var button = recorderButton("Stop");
    if (button) { button.click(); }
  }

  // Voice activity detection. Wrapping getUserMedia lets the meter read the
  // very stream the recorder is using, instead of opening a second mic.
  var SPEECH_RMS = 0.018;
  var MIN_SPEECH_MS = 700;
  var TRAILING_SILENCE_MS = 2200;

  function watchLevels(stream) {
    var Ctx = window.AudioContext || window.webkitAudioContext;
    if (!Ctx) { return; }
    var context = new Ctx();
    var analyser = context.createAnalyser();
    analyser.fftSize = 1024;
    context.createMediaStreamSource(stream).connect(analyser);
    var samples = new Float32Array(analyser.fftSize);
    var spokeAt = 0;
    var quietSince = 0;
    var started = Date.now();

    function tick() {
      var track = stream.getAudioTracks()[0];
      if (!track || track.readyState !== "live") {
        context.close().catch(function () {});
        return;
      }
      analyser.getFloatTimeDomainData(samples);
      var sum = 0;
      for (var index = 0; index < samples.length; index += 1) {
        sum += samples[index] * samples[index];
      }
      var rms = Math.sqrt(sum / samples.length);
      var now = Date.now();
      if (rms > SPEECH_RMS) {
        if (!spokeAt) { spokeAt = now; }
        quietSince = 0;
      } else if (spokeAt && now - spokeAt > MIN_SPEECH_MS) {
        if (!quietSince) { quietSince = now; }
        if (handsFree() && now - quietSince > TRAILING_SILENCE_MS && now - started > 3000) {
          closeMic();
          context.close().catch(function () {});
          return;
        }
      }
      window.requestAnimationFrame(tick);
    }
    window.requestAnimationFrame(tick);
  }

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    var openStream = navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices);
    navigator.mediaDevices.getUserMedia = function (constraints) {
      return openStream(constraints).then(function (stream) {
        if (constraints && constraints.audio && stream.getAudioTracks().length) {
          stopInterviewer();
          try { watchLevels(stream); } catch (error) { /* level metering is optional */ }
        }
        return stream;
      });
    };
  }

  // Half-duplex: touching the answer field cuts the interviewer off, so a
  // phone speaker never bleeds into the mic while dictating.
  function stopInterviewer() {
    if (!player || player.paused) { return; }
    player.pause();
  }

  function inAnswerField(target) {
    var box = document.getElementById("answer");
    return !!(box && target && box.contains(target));
  }

  ["pointerdown", "focusin", "keydown"].forEach(function (name) {
    document.addEventListener(name, function (event) {
      if (inAnswerField(event.target)) { stopInterviewer(); }
    }, { capture: true });
  });

  // After each turn, drop the iOS keyboard and bring the new question into view.
  window.focusInterviewer = function () {
    var active = document.activeElement;
    if (active && typeof active.blur === "function") { active.blur(); }
    var target = document.getElementById("pushback");
    if (!target) { return; }
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.setTimeout(function () {
      target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    }, 60);
  };
})();
</script>
"""

FOCUS_INTERVIEWER_JS = "() => { if (window.focusInterviewer) { window.focusInterviewer(); } }"
PLAY_AUDIO_JS = "(path) => { if (window.playInterviewer) { window.playInterviewer(path); } }"

SPRINT_CHECKLIST = [
    "Block 1: Dr. Kim — positioning and thesis (PQ01, PQ02, TQ01)",
    "Block 2: Dr. Kim — scope, research vision, and close (PQ03, PQ04, PQ05, PQ09)",
    "Block 3: Systems / ML Engineering Lead — requirements and safety (TQ02, TQ04, TQ07)",
    "Block 4: Product Manager — velocity, ROI, and prioritization (TQ08, CQ03, CQ06)",
    "Block 5: Design Lead — workflow, density, and partnership (TQ06, CQ07, TQ09)",
    "Block 6: Behavioral friction across all four personas (BQ04, BQ07, BQ09)",
    "Block 7: Cross-panel message discipline and objection handling (PQ07, PQ10)",
]

SESSION_HISTORY_HEADERS = [
    "Timestamp",
    "Interviewer",
    "Turns",
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
  color-scheme: light;
}

html,
html.dark {
  background: var(--paper) !important;
  color-scheme: light;
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
  max-width: 100% !important;
  overflow-x: hidden;
  background:
    linear-gradient(rgba(53, 80, 90, 0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(53, 80, 90, 0.055) 1px, transparent 1px),
    var(--paper);
  background-size: 28px 28px;
}

html, body {
  max-width: 100%;
  overflow-x: hidden;
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  overscroll-behavior-y: contain;
  -webkit-tap-highlight-color: transparent;
}

@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}

#shell {
  max-width: 1120px;
  margin: 0 auto;
  padding: 20px 16px calc(40px + env(safe-area-inset-bottom));
  padding-left: max(16px, env(safe-area-inset-left));
  padding-right: max(16px, env(safe-area-inset-right));
  overflow-x: clip;
}
#shell *, #masthead * { overflow-wrap: anywhere; word-break: break-word; }
#masthead { border-top: 7px solid var(--signal); border-bottom: 1px solid var(--line); padding: 18px 0 16px; margin-bottom: 18px; }
#masthead h1 { font-family: 'IBM Plex Mono', monospace; font-size: clamp(1.55rem, 4vw, 2.5rem); line-height: 1.05; letter-spacing: 0; margin: 0; color: var(--ink) !important; }
#masthead p { max-width: 760px; color: #4b5354; margin: 9px 0 0; }
#shell .form { background: transparent !important; border-color: var(--line) !important; }
#shell .block { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; max-width: 100%; }
#shell .block span { color: var(--ink) !important; }
#shell textarea { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; max-width: 100%; overflow-wrap: anywhere; white-space: pre-wrap; resize: vertical; }
#shell textarea::placeholder { color: #6f736f !important; }
#shell input[type='radio'] { accent-color: var(--signal) !important; }
#shell input:not([type='radio']):not([type='checkbox']),
#target-pillar input {
  background: #fffdf7 !important;
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
  border-color: var(--line) !important;
  opacity: 1 !important;
}
#target-pillar,
#target-pillar .wrap,
#target-pillar .wrap-inner,
#target-pillar .secondary-wrap,
#target-pillar .token,
#target-pillar span {
  background-color: #fffdf7 !important;
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#target-pillar svg { color: #0f172a !important; fill: #0f172a !important; }
ul.options,
.gradio-container ul.options {
  background: #fffdf7 !important;
  border: 1px solid #94a3b8 !important;
  color: #0f172a !important;
  max-height: 46vh !important;
  z-index: 9999 !important;
}
ul.options li,
ul.options li.item,
ul.options li span,
ul.options .item span {
  background-color: #fffdf7 !important;
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
  opacity: 1 !important;
  font-size: 1rem;
  line-height: 1.4;
  padding: 12px 12px;
  min-height: 44px;
}
ul.options li.selected,
ul.options li.active,
ul.options li:hover,
ul.options li.selected span,
ul.options li.active span,
ul.options li:hover span {
  background-color: #ebe7dd !important;
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#shell input[type='radio'] + span,
#shell label:has(input[type='radio']) { background: #fffdf7 !important; color: var(--ink) !important; border-color: var(--line) !important; }
#shell label.selected:has(input[type='radio']) { background: #ebe7dd !important; border-color: var(--signal) !important; }
#answer textarea {
  min-height: 190px;
  max-height: 55dvh;
  font-size: 16px;
  line-height: 1.55;
  overflow-y: auto;
  overflow-x: hidden;
}
/* iOS zooms the page whenever a focused field is under 16px. */
#shell textarea,
#shell input:not([type='radio']):not([type='checkbox']),
ul.options input {
  font-size: 16px !important;
}
#shell button {
  min-height: 46px;
  transition: background-color 120ms ease, border-color 120ms ease, transform 80ms ease;
  touch-action: manipulation;
}
#shell button:active { transform: scale(0.985); }
#shell label:has(input[type='radio']),
#sprint-checklist label {
  min-height: 44px;
  display: flex;
  align-items: center;
  padding: 10px 12px;
}
#shell [role='tab'] {
  flex: 1 1 auto;
  min-height: 48px;
  font-size: 0.95rem;
}
#replay {
  min-height: 40px !important;
  font-size: 0.9rem;
  background: #ebe7dd !important;
  border-color: var(--line) !important;
}
#recorder {
  background: #fffdf7 !important;
  border: 1px solid var(--line) !important;
}
#recorder,
#recorder span,
#recorder button,
#recorder select,
#recorder option,
#recorder .label-wrap span,
#recorder [data-testid='block-info'] {
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#recorder button {
  min-height: 46px !important;
  background: #ebe7dd !important;
  border: 1px solid var(--line) !important;
}
#handsfree {
  background: #ebe7dd !important;
  border: 1px solid var(--line) !important;
  border-radius: 6px;
  padding: 6px 10px;
}
#handsfree,
#handsfree span,
#handsfree label,
#handsfree label span,
#handsfree [data-testid='block-info'] {
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#audio-row { flex-wrap: wrap; }
#recorder .label-wrap span,
#recorder > .block > span {
  font-weight: 700 !important;
}
#answer-panel,
#audio-panel {
  background: #ebe7dd !important;
  border: 1px solid var(--line) !important;
}
#answer-panel .label-wrap span,
#audio-panel .label-wrap span,
#answer-panel button.label-wrap,
#audio-panel button.label-wrap {
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
  font-size: 0.9rem;
}
#finalize {
  background: var(--steel) !important;
  border-color: var(--steel) !important;
  color: #ffffff !important;
  font-weight: 700;
  min-height: 46px !important;
}
#clear { min-height: 40px !important; font-size: 0.85rem; opacity: 0.85; }
@media (max-width: 560px) {
  #audio-row { flex-direction: column; align-items: stretch; }
  #audio-row > * { min-width: 100% !important; }
}
@media (prefers-reduced-motion: reduce) {
  #shell *, #shell *::before, #shell *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
#turn-indicator { border-left: 5px solid var(--steel); background: #ebe7dd; padding: 7px 14px; }
#answer-meter { padding: 2px 2px 6px; font-size: 0.9rem; }
#answer-meter * { color: #475569 !important; }
#setup-panel,
#setup-panel .label-wrap,
#setup-panel .label-wrap span,
#setup-panel button.label-wrap {
  background: #ebe7dd !important;
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#setup-panel .label-wrap span { font-weight: 700 !important; }
#pushback { border-left: 5px solid var(--signal); background: #fffdf7; padding: 8px 16px; min-height: 126px; }
#scorecard { border-top: 3px solid var(--steel); background: rgba(255, 253, 247, 0.86); padding: 10px 16px; min-height: 360px; overflow-x: auto; }
#scorecard table { display: block; max-width: 100%; overflow-x: auto; }
#scorecard pre, #scorecard code, #pushback pre, #pushback code { white-space: pre-wrap; overflow-wrap: anywhere; max-width: 100%; }
#history-table { max-width: 100%; overflow-x: auto; }
#shell .block > .label-wrap span,
#shell .block > label > span,
#shell h1, #shell h2, #shell h3, #shell h4, #shell h5, #shell h6,
#shell p, #shell li, #shell strong, #shell em { color: #0f172a !important; }
#progress-dashboard,
#progress-dashboard *,
#mobile-note,
#mobile-note * { color: #0f172a !important; }
#progress-dashboard h1,
#progress-dashboard h2,
#progress-dashboard h3,
#progress-dashboard h4 { color: #0f172a !important; font-weight: 700 !important; }
#shell table { border-collapse: collapse !important; width: 100%; }
#shell table th,
#shell table th * {
  color: #0f172a !important;
  background: #e6e2d8 !important;
  font-weight: 700 !important;
}
#shell table td,
#shell table td * { color: #1e293b !important; }
#shell table th,
#shell table td { border: 1px solid #94a3b8 !important; padding: 6px 9px !important; }
#history-table table,
#history-table th,
#history-table td,
#history-table span,
#history-table .cell-wrap,
#history-table input,
#history-table textarea {
  color: #0f172a !important;
  background-color: #fffdf7 !important;
  -webkit-text-fill-color: #0f172a !important;
  opacity: 1 !important;
}
#history-table th,
#history-table th span {
  background-color: #e6e2d8 !important;
  font-weight: 700 !important;
}
#sprint-checklist label { align-items: flex-start; }
#sprint-checklist,
#sprint-checklist span,
#sprint-checklist label,
#sprint-checklist label span,
#sprint-checklist .label-wrap span,
#sprint-checklist [data-testid='block-info'] {
  color: #0f172a !important;
  -webkit-text-fill-color: #0f172a !important;
}
#sprint-checklist label {
  background: #fffdf7 !important;
  border: 1px solid var(--line) !important;
  line-height: 1.45;
}
#sprint-checklist label.selected,
#sprint-checklist label:has(input:checked) {
  background: #35505a !important;
  border-color: #35505a !important;
}
#sprint-checklist label.selected,
#sprint-checklist label.selected span,
#sprint-checklist label:has(input:checked),
#sprint-checklist label:has(input:checked) span {
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
}
#sprint-checklist input[type='checkbox'] { accent-color: var(--signal) !important; }
#pushback *, #scorecard * { color: var(--ink) !important; }
#evaluate { background: var(--signal); border-color: var(--signal); color: white; font-weight: 700; }
#evaluate:hover { background: #b92e24; border-color: #b92e24; }
footer { display: none !important; }
@media (max-width: 700px) {
  #shell { padding: 8px 8px calc(28px + env(safe-area-inset-bottom)); }
  #answer textarea { min-height: 26dvh; }
  /* Reclaim the fold: the masthead blurb and practice note are read once, not every turn. */
  #masthead { padding: 8px 0 10px; margin-bottom: 10px; border-top-width: 5px; }
  #masthead p { display: none; }
  #mobile-note { font-size: 0.78rem; opacity: 0.75; margin: 0; }
  #shell button { white-space: normal; }
  #shell .tab-container { display: flex; overflow-x: visible; }
  #shell [role='tab'] { font-size: 0.82rem; padding: 8px 4px; }
  #shell .gap,
  #shell .column,
  #shell .row { gap: 10px !important; }
  #shell .block { padding: 10px !important; }
  #mobile-note { padding: 0 !important; }
  ul.options { max-height: 38dvh !important; }
  /* The recorder is the only control that matters mid-session, so give it the thumb zone. */
  #recorder button { min-height: 54px !important; font-size: 1rem !important; flex: 1 1 auto; }
  #recorder select { max-width: 45% !important; }
  #pushback { font-size: 1.05rem; }
  /* Keep Submit reachable with one thumb while the keyboard is up. */
  #evaluate {
    position: sticky;
    bottom: calc(10px + env(safe-area-inset-bottom));
    z-index: 40;
    box-shadow: 0 8px 20px rgba(23, 23, 23, 0.22);
  }
  /* Clears the sticky turn indicator when a new question is scrolled into view. */
  #pushback { scroll-margin-top: 58px; }
  #turn-indicator { position: sticky; top: 0; z-index: 30; }
}
@media (max-width: 440px) {
  #shell { padding: 6px 6px calc(24px + env(safe-area-inset-bottom)); }
  #shell .gap, #shell .form { gap: 8px !important; }
  #pushback, #scorecard, #turn-indicator { padding-left: 10px; padding-right: 10px; }
  #scorecard { min-height: 240px; }
  #shell .block { padding: 8px !important; }
  #masthead h1 { font-size: 1.4rem; }
}
"""


initial_dashboard, initial_history = load_progress_dashboard()


with gr.Blocks(title="Anduril Human Factors Interview System") as demo:
    turn_state = gr.State(0)
    conversation_history = gr.State([])
    claims_state = gr.State([])
    pillars_state = gr.State([])
    active_persona = gr.State("")
    spoken_seconds = gr.State(0.0)
    with gr.Column(elem_id="shell"):
        gr.HTML(
            """
            <header id="masthead">
              <h1>HUMAN FACTORS // AIR DEFENSE</h1>
              <p>Lead/Staff interview pressure testing for Dr. Brandon Fluegel. Pick an interviewer, optionally target a specific pillar, answer out loud, then finalize for one holistic scorecard.</p>
            </header>
            """
        )
        with gr.Tabs():
            with gr.Tab("🛡️ Interview Simulator"):
                gr.Markdown(
                    "📱 Keep this tab in the foreground — iOS reloads background tabs.",
                    elem_id="mobile-note",
                )
                with gr.Accordion("Session setup", open=True, elem_id="setup-panel") as setup_panel:
                    persona = gr.Radio(
                        choices=list(PERSONAS),
                        value="Dr. Daniella Kim — Research Head",
                        label="Interviewer",
                    )
                    target_pillar = gr.Dropdown(
                        choices=PILLAR_CHOICES,
                        value=AUTO_PILLAR,
                        label="Target pillar (optional drill)",
                        filterable=True,
                        elem_id="target-pillar",
                    )
                    start_button = gr.Button("Start New Interview", variant="primary")
                indicator = gr.Markdown("**No interview in progress**", elem_id="turn-indicator")
                interviewer = gr.Markdown(
                    "Select an interviewer and start a new interview.",
                    elem_id="pushback",
                )
                audio_path = gr.Textbox(visible=False, elem_id="audio-path")
                answer_recorder = gr.Audio(
                    sources=["microphone"],
                    type="filepath",
                    label="Your turn — speak",
                    elem_id="recorder",
                )
                answer_readout = gr.Markdown(answer_meter(""), elem_id="answer-meter")
                with gr.Accordion("Transcript · type instead", open=False, elem_id="answer-panel"):
                    answer = gr.Textbox(
                        label="Candidate answer",
                        placeholder="Your spoken answer lands here. You can also type one.",
                        lines=8,
                        max_lines=30,
                        elem_id="answer",
                    )
                    continue_button = gr.Button(
                        "Submit typed answer", variant="secondary", elem_id="evaluate"
                    )
                with gr.Accordion("Audio & turn taking", open=False, elem_id="audio-panel"):
                    replay_button = gr.Button("🔊 Play question again", elem_id="replay")
                    hands_free = gr.Checkbox(
                        value=True,
                        label="Hands-free turn taking",
                        info="The mic opens when the interviewer stops talking and closes when you stop.",
                        elem_id="handsfree",
                    )
                    audio_enabled = gr.Checkbox(
                        value=True,
                        label="Speak questions aloud",
                        info="Turn off to run silently. Touching the transcript always cuts the interviewer off.",
                        elem_id="audio-toggle",
                    )
                finalize_button = gr.Button("Wrap Up & Finalize Session", elem_id="finalize")
                download_button = gr.DownloadButton(
                    "⬇︎ Download grades & feedback", visible=False, elem_id="download"
                )
                clear_button = gr.Button("Clear Session", variant="stop", elem_id="clear")
                scorecard = gr.Markdown(SCORECARD_PLACEHOLDER, elem_id="scorecard")

            with gr.Tab("📈 Progress & 1-Week Sprint Tracker"):
                dashboard = gr.Markdown(initial_dashboard, elem_id="progress-dashboard")
                refresh_dashboard = gr.Button("Refresh Progress")
                gr.Markdown("## 7-Day Intensive Sprint Checklist")
                sprint_checklist = gr.CheckboxGroup(
                    choices=SPRINT_CHECKLIST,
                    value=load_sprint_progress(),
                    label="Complete each practice block before interview day",
                    elem_id="sprint-checklist",
                )
                gr.Markdown("## Recent Mock Sessions")
                session_history = gr.Dataframe(
                    value=initial_history,
                    headers=SESSION_HISTORY_HEADERS,
                    datatype=[
                        "str",
                        "str",
                        "number",
                        "number",
                        "number",
                        "number",
                        "number",
                        "number",
                        "str",
                        "str",
                        "str",
                    ],
                    interactive=False,
                    elem_id="history-table",
                )

    session_outputs = [
        indicator,
        interviewer,
        scorecard,
        turn_state,
        conversation_history,
        answer,
        claims_state,
        pillars_state,
        active_persona,
    ]
    setup_outputs = [setup_panel, persona]
    capture_outputs = [answer_recorder, spoken_seconds]
    speak_inputs = [interviewer, active_persona, audio_enabled]
    submit_inputs = [
        answer,
        turn_state,
        conversation_history,
        claims_state,
        pillars_state,
        active_persona,
        spoken_seconds,
    ]
    finalize_inputs = [turn_state, conversation_history, claims_state, pillars_state, active_persona]

    start_event = start_button.click(
        start_interview, inputs=[persona, target_pillar], outputs=session_outputs
    )
    start_event.then(lock_setup, outputs=setup_outputs, queue=False)
    start_event.then(reset_capture, outputs=capture_outputs, queue=False)
    start_speak = start_event.then(speak_interviewer, speak_inputs, audio_path)
    start_speak.then(fn=None, inputs=audio_path, js=PLAY_AUDIO_JS, queue=False)
    start_event.then(fn=None, js=FOCUS_INTERVIEWER_JS, queue=False)
    continue_event = continue_button.click(continue_conversation, submit_inputs, session_outputs)
    continue_event.then(reset_capture, outputs=capture_outputs, queue=False)
    continue_speak = continue_event.then(speak_interviewer, speak_inputs, audio_path)
    continue_speak.then(fn=None, inputs=audio_path, js=PLAY_AUDIO_JS, queue=False)
    continue_event.then(fn=None, js=FOCUS_INTERVIEWER_JS, queue=False)
    submit_event = answer.submit(continue_conversation, submit_inputs, session_outputs)
    submit_event.then(reset_capture, outputs=capture_outputs, queue=False)
    submit_speak = submit_event.then(speak_interviewer, speak_inputs, audio_path)
    submit_speak.then(fn=None, inputs=audio_path, js=PLAY_AUDIO_JS, queue=False)
    submit_event.then(fn=None, js=FOCUS_INTERVIEWER_JS, queue=False)
    replay_event = replay_button.click(
        replay_interviewer, [interviewer, active_persona, audio_path], audio_path
    )
    replay_event.then(fn=None, inputs=audio_path, js=PLAY_AUDIO_JS, queue=False)
    finalize_event = finalize_button.click(finalize_session, finalize_inputs, session_outputs)
    finalize_event.then(unlock_setup, outputs=setup_outputs, queue=False)
    finalize_event.then(
        export_session,
        inputs=[scorecard, conversation_history, active_persona],
        outputs=download_button,
        queue=False,
    )
    finalize_event.then(load_progress_dashboard, outputs=[dashboard, session_history])
    clear_event = clear_button.click(clear_session, outputs=session_outputs)
    clear_event.then(unlock_setup, outputs=setup_outputs, queue=False)
    clear_event.then(reset_capture, outputs=capture_outputs, queue=False)
    clear_event.then(lambda: gr.DownloadButton(visible=False), outputs=download_button, queue=False)
    transcribe_event = answer_recorder.stop_recording(
        transcribe_answer, inputs=answer_recorder, outputs=[answer, spoken_seconds]
    )
    spoken_turn = transcribe_event.then(continue_conversation, submit_inputs, session_outputs)
    spoken_turn.then(reset_capture, outputs=capture_outputs, queue=False)
    spoken_speak = spoken_turn.then(speak_interviewer, speak_inputs, audio_path)
    spoken_speak.then(fn=None, inputs=audio_path, js=PLAY_AUDIO_JS, queue=False)
    spoken_turn.then(fn=None, js=FOCUS_INTERVIEWER_JS, queue=False)
    answer.change(answer_meter, inputs=[answer, spoken_seconds], outputs=answer_readout, queue=False)
    refresh_dashboard.click(load_progress_dashboard, outputs=[dashboard, session_history])
    sprint_checklist.change(save_sprint_progress, inputs=sprint_checklist, outputs=None)


def tunnel_auth() -> tuple[str, str] | None:
    """A tunnelled URL is public, so gate it with COACH_AUTH='user:password' before exposing the API key."""
    credentials = os.getenv("COACH_AUTH", "")
    if ":" not in credentials:
        return None
    user, _, password = credentials.partition(":")
    return (user.strip(), password) if user.strip() and password else None


if __name__ == "__main__":
    share_enabled = os.getenv("GRADIO_SHARE", "false").lower() == "true"
    TEMP_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
        share=share_enabled,
        auth=tunnel_auth(),
        css=CSS,
        head=HEAD,
        allowed_paths=[str(TEMP_AUDIO_DIR), str(EXPORT_DIR)],
    )

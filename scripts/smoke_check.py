"""Offline verification of holistic scorecard rendering, session persistence, and dashboard reads."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app  # noqa: E402
from openai.lib._parsing._responses import type_to_text_format_param  # noqa: E402


def build_evaluation() -> app.Evaluation:
    return app.Evaluation(
        core_scores=[
            app.CoreScore(dimension=name, score=4, evidence=f"{name} evidence across the session.")
            for name in app.CORE_DIMENSIONS
        ],
        tone_and_authority=app.ToneAuthority(
            score=4,
            voice_register="Standard-Setting Lead/Staff",
            evidence="Named the trade-off he owned and set the bar for the org.",
        ),
        uplevel_scores=[
            app.UplevelScore(criterion=name, score=None if name == "Research Velocity" else 4, evidence="Cited.")
            for name in app.LEAD_STAFF_CRITERIA
        ],
        pillars_covered=["TQ02", "BQ04", "PQ01", "NOPE99"],
        strongest_signal="Bridged latency targets to perceptual thresholds.",
        primary_gap="No falsifiable trust metric.",
        priority_move="Name the measurement instrument.",
        senior_uxr_baseline_assessment="Clears the baseline.",
        lead_staff_uplevel_assessment="Approaching the uplevel bar.",
        demonstrated_level="Lead/Staff Upleveling Signal",
        end_of_session_debrief="Strong systems framing; tighten metric ownership.",
        uplevel_verdict="Lead/Staff Borderline",
        confidence="High",
    )


def build_transcript(turns: int) -> list[dict[str, str]]:
    history: list[dict[str, str]] = [{"role": "assistant", "content": "Opening question."}]
    for index in range(1, turns + 1):
        history.append({"role": "user", "content": f"Answer {index}."})
        history.append({"role": "assistant", "content": f"Follow-up question {index + 1}."})
    return history


def main() -> None:
    type_to_text_format_param(app.Evaluation)
    type_to_text_format_param(app.InterviewerTurn)
    print("OK  structured-output schemas build for Evaluation and InterviewerTurn")

    transcript = build_transcript(7)
    turns = app.completed_turns(transcript)
    assert turns == 7, f"expected 7 completed turns, got {turns}"
    assert "CANDIDATE: Answer 7." in app.render_transcript(transcript)
    assert app.conversation_stage(9)[0] == app.OPEN_STAGE[0], "turns past 4 must fall back to the open stage"
    print("OK  multi-turn transcript helpers handle unlimited turns")

    evaluation = build_evaluation()
    app.validate_evaluation(evaluation)
    card = app.render_scorecard(evaluation, turns)
    assert "End of Session Debrief" in card
    assert "### Tone & Authority" in card
    assert "**Turns completed:** 7" in card
    review = app.render_transcript_review(transcript)
    assert "## Transcript Review" in review and "Answer 7." in review
    print("OK  holistic scorecard renders with Tone & Authority, the turn count, and a transcript review")

    ledger = app.render_claims_ledger(["latency threshold - staircase - 120ms - owned"])
    assert "Turn 1:" in ledger
    assert app.render_covered_pillars(["TQ02"]).startswith("TQ02 (")
    assert app.merge_pillars(["TQ02"], "bq04 | whatever") == ["TQ02", "BQ04"]
    assert app.merge_pillars(["TQ02"], "TQ02") == ["TQ02"], "covered pillars must not duplicate"
    assert app.merge_pillars([], "ZZ99") == []
    assert "0 words" in app.answer_meter("")
    assert "cut in" in app.answer_meter(" ".join(["word"] * 400))
    assert "technical main-answer range" in app.answer_meter(" ".join(["word"] * 200))
    assert "behavioral main-answer range" in app.answer_meter(" ".join(["word"] * 250))
    assert "follow-up length" in app.answer_meter(" ".join(["word"] * 70))
    assert "interjection" in app.turn_indicator(3, interjection=True)
    assert "same ground" in app.turn_indicator(3, held=True)
    print("OK  claim ledger, coverage merge, answer meter, and turn states behave")

    with tempfile.TemporaryDirectory() as tmp:
        sandbox = Path(tmp) / "coaching_state.md"
        shutil.copyfile(app.COACHING_STATE_PATH, sandbox)
        original = app.COACHING_STATE_PATH
        app.COACHING_STATE_PATH = sandbox
        try:
            before = len(app.load_session_records())
            record = app.persist_session("Dr. Daniella Kim", evaluation, turns, ["TQ02", "BQ04", "PQ01"])
            records = app.load_session_records()
            assert len(records) == before + 1
            assert records[-1].timestamp == record.timestamp
            assert records[-1].turns_completed == 7
            assert records[-1].pillars_covered == ["TQ02", "BQ04", "PQ01"], "unknown pillar IDs must be dropped"
            assert set(records[-1].core_averages) == set(app.CORE_DIMENSIONS)
            summary, history = app.load_progress_dashboard()
            assert f"**Total mock sessions completed:** {before + 1}" in summary
            assert "**Total conversation turns practiced:**" in summary
            assert "### Pillar Coverage" in summary
            assert history[0][0] == record.timestamp
            assert history[0][2] == 7
            assert len(history[0]) == len(app.SESSION_HISTORY_HEADERS)
        finally:
            app.COACHING_STATE_PATH = original
    print("OK  multi-turn session persistence round-trips into the progress dashboard")

    for persona_name in app.PERSONAS.values():
        for stage_turn in (2, 3, 4, 9):
            assert app.stage_instruction(stage_turn, persona_name).strip(), (
                f"{persona_name} turn {stage_turn} produced an empty stage instruction"
            )
        assert app.opening_bank(persona_name).strip(), f"{persona_name} has no opening pillars"

    settled_topics = ("relocat", "salary", "compensation", "25-30%", "clearance status")
    for pillar_id, (_, question) in app.PILLAR_REGISTRY.items():
        spoken = " ".join(
            [question.question, *question.persona_adaptations.values(), *question.follow_ups]
        ).lower()
        for banned in settled_topics:
            assert banned not in spoken, f"{pillar_id} asks about the settled recruiter topic '{banned}'"
    print("OK  all four personas build every stage instruction and no pillar re-opens settled topics")

    live_context = app.load_live_context()
    debrief_context = app.load_debrief_context()
    for bank_file in ("technical_questions", "culture_questions", "positioning_questions"):
        assert bank_file not in live_context, f"{bank_file} must not ship in the live instruction payload"
    assert "DETAILED RUBRIC" not in live_context, "grading rubric must not ship on live turns"
    assert "DETAILED RUBRIC" in debrief_context, "debrief still needs the rubric"
    assert "TQ01 | Research Thesis" in debrief_context, "debrief needs the compact pillar index"
    assert len(live_context) < len(debrief_context)
    assert len(live_context) // 4 < 12000, "live instructions exceed the per-turn token budget"
    print(
        f"OK  instruction payloads split: live ~{len(live_context) // 4} tok, "
        f"debrief ~{len(debrief_context) // 4} tok"
    )

    summary, history = app.load_progress_dashboard()
    assert "Sprint Readiness" in summary
    print(f"OK  live dashboard reads {len(history)} prior session rows")


if __name__ == "__main__":
    main()

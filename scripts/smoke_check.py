"""Offline verification of scorecard rendering, session persistence, and dashboard reads."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app  # noqa: E402
from openai.lib._parsing._responses import type_to_text_format_param  # noqa: E402


def build_evaluation(turn: int) -> app.Evaluation:
    return app.Evaluation(
        interviewer_pushback="That number is unowned. What measurement proved the threshold?",
        core_scores=[
            app.CoreScore(dimension=name, score=4, evidence=f"{name} evidence for turn {turn}.")
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
        strongest_signal="Bridged latency targets to perceptual thresholds.",
        primary_gap="No falsifiable trust metric.",
        priority_move="Name the measurement instrument.",
        senior_uxr_baseline_assessment="Clears the baseline.",
        lead_staff_uplevel_assessment="Approaching the uplevel bar.",
        demonstrated_level="Lead/Staff Upleveling Signal",
        next_question=None if turn == 4 else "What falsifiable metric proved operator trust degraded?",
        end_of_session_debrief="Strong systems framing; tighten metric ownership." if turn == 4 else None,
        uplevel_verdict="Lead/Staff Borderline" if turn == 4 else None,
        confidence="High",
    )


def main() -> None:
    type_to_text_format_param(app.Evaluation)
    print("OK  structured-output schema builds for Evaluation")

    cumulative: list[dict[str, object]] = []
    for turn in (1, 2, 3, 4):
        evaluation = build_evaluation(turn)
        app.validate_evaluation(evaluation)
        cumulative.append(evaluation.model_dump())
        card = app.render_scorecard(evaluation, turn, cumulative)
        assert "Tone & Authority" in card, f"turn {turn} scorecard missing Tone & Authority"
    assert "End of Session Debrief" in card
    assert "| Tone & Authority | **4.0/5** |" in card
    print("OK  four-turn scorecards render with Tone & Authority")

    with tempfile.TemporaryDirectory() as tmp:
        sandbox = Path(tmp) / "coaching_state.md"
        shutil.copyfile(app.COACHING_STATE_PATH, sandbox)
        original = app.COACHING_STATE_PATH
        app.COACHING_STATE_PATH = sandbox
        try:
            before = len(app.load_session_records())
            record = app.persist_session("Dr. Daniella Kim", build_evaluation(4), cumulative)
            records = app.load_session_records()
            assert len(records) == before + 1
            assert records[-1].timestamp == record.timestamp
            assert set(records[-1].core_averages) == set(app.CORE_DIMENSIONS)
            summary, history = app.load_progress_dashboard()
            assert f"**Total mock sessions completed:** {before + 1}" in summary
            assert history[0][0] == record.timestamp
            assert len(history[0]) == len(app.SESSION_HISTORY_HEADERS)
        finally:
            app.COACHING_STATE_PATH = original
    print("OK  session persistence round-trips into the progress dashboard")

    summary, history = app.load_progress_dashboard()
    assert "Sprint Readiness" in summary
    print(f"OK  live dashboard reads {len(history)} prior session rows")


if __name__ == "__main__":
    main()

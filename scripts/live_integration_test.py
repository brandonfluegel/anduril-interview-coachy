"""Live end-to-end 4-turn integration test against the real OpenAI API.

Backs up data/coaching_state.md, runs a full interview, validates scorecards,
persistence, and the dashboard, then restores the file byte-for-byte.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import app  # noqa: E402

PERSONA_LABEL = "Dr. Daniella Kim — Research Head"

ANSWERS = [
    # Turn 1 — technical core
    """At Amazon I ran a multi-year psychophysics program because our latency targets were arbitrary
    engineering guesses. I measured actual human perceptual thresholds for response delay and replaced the
    guessed numbers with those thresholds, which produced about fifty million dollars in operational value.
    That work is where Calibrated Cognitive Friction came from. The insight is that removing all friction
    is not the goal. In an autonomous system you deliberately place friction at the exact moment where an
    operator would otherwise accept an automated recommendation without checking it, because that is where
    automation bias does its damage and where Meaningful Human Control actually lives.""",
    # Turn 2 — response to falsifiability pushback
    """Fair challenge. The falsifiable claim was operationalized three ways. First, a just-noticeable-difference
    threshold from a staircase procedure, so the latency number was a measured perceptual boundary with a
    confidence interval, not an opinion. Second, an objective cognitive load index built from fNIRS
    prefrontal oxygenation and eye-tracking fixation dispersion, which meant I could falsify the claim if load
    did not move when I crossed the threshold. Third, task-level error and time data. At NASA I used the same
    logic on Lunar Gateway clinical workstations, where the redesign cut task time thirty percent and eliminated
    the critical input errors uFMEA had flagged as highest consequence.""",
    # Turn 3 — behavioral / cross-functional friction
    """Our engineering lead wanted to ship a latency budget I knew crossed the perceptual threshold, and we
    were two weeks from a launch. I did not escalate and I did not block. I asked for one instrumented build
    and ran the discrimination test on his own hardware, so the disagreement moved from my judgment against
    his to a number we both trusted. He was right that my original spec was over-conservative for one modality
    and I moved it. He moved on the other two. The earned secret is that engineers do not resist Human Factors,
    they resist unfalsifiable requirements. Once I started writing specs as testable thresholds with a
    measurement method attached, the friction mostly disappeared. I turned that into the standard template our
    team now uses.""",
    # Turn 4 — leadership, standard setting, scaling
    """At Sling I own Human Factors strategy across software, hardware, and AI, and the leverage is not in the
    studies I personally run. I wrote Principles for Agentic Trust, accepted to ACM CSCW 2026, covering
    alignment, execution, control, and calibration, because there is no regulation yet for agentic systems and
    waiting for one means shipping unsafe defaults. For Air Defense I would do three things. Define trust
    calibration acceptance criteria that a Lattice OS release has to clear before it ships, the same way it
    clears a performance budget. Stand up a research repository and a rapid ethnography cadence so an engineer
    can answer an operator question in a day without waiting on me. And instrument the counter-drone
    engagement workflow so we can detect automation bias in the field rather than inferring it in a lab.""",
]


def words(text: str) -> int:
    return len(text.split())


def strip_spoken(markdown: str) -> str:
    return " ".join(
        line for line in markdown.splitlines() if not line.strip().startswith("#")
    ).strip()


def main() -> int:
    state_path = app.COACHING_STATE_PATH
    original_bytes = state_path.read_bytes()
    original_hash = hashlib.sha256(original_bytes).hexdigest()
    backup_path = state_path.with_suffix(".md.integration-backup")
    backup_path.write_bytes(original_bytes)
    print(f"→ Backed up coaching_state.md ({len(original_bytes)} bytes, sha256 {original_hash[:12]}…)")

    sessions_before = len(app.load_session_records())
    summary_before, history_before = app.load_progress_dashboard()
    print(f"→ Baseline: {sessions_before} logged sessions, {len(history_before)} dashboard rows\n")

    failures: list[str] = []
    new_timestamp: str | None = None

    try:
        indicator, interviewer, _, turn, history, scores, answer_box = app.start_interview(PERSONA_LABEL)
        question = strip_spoken(interviewer)
        print(f"[Q1] {question}")
        print(f"     words={words(question)} turn_state={turn} answer_box_cleared={answer_box == ''}\n")
        if words(question) > 45:
            failures.append(f"Q1 spoken length {words(question)} exceeds the 45-word voice budget")

        for index, candidate_answer in enumerate(ANSWERS, start=1):
            indicator, interviewer, scorecard, turn, history, scores, answer_box = app.evaluate_answer(
                candidate_answer, PERSONA_LABEL, index, history, scores
            )
            evaluation = scores[-1]
            spoken = strip_spoken(interviewer)

            core = {item["dimension"]: item["score"] for item in evaluation["core_scores"]}
            tone = evaluation["tone_and_authority"]
            evidenced = sum(1 for item in evaluation["uplevel_scores"] if item["score"] is not None)

            print(f"--- TURN {index} EVALUATED ---")
            print(f"  core: {core}")
            print(f"  tone_and_authority: {tone['score']}/5 — {tone['voice_register']}")
            print(f"  demonstrated_level: {evaluation['demonstrated_level']}")
            print(f"  uplevel criteria evidenced: {evidenced}/8   confidence: {evaluation['confidence']}")
            print(f"  pushback ({words(evaluation['interviewer_pushback'])}w): {evaluation['interviewer_pushback']}")
            if evaluation["next_question"]:
                print(f"  next Q ({words(evaluation['next_question'])}w): {evaluation['next_question']}")
            print(f"  spoken block: {words(spoken)}w | answer box cleared: {answer_box == ''}")
            print(f"  scorecard has Tone & Authority section: {'### Tone & Authority' in scorecard}")

            if set(core) != set(app.CORE_DIMENSIONS):
                failures.append(f"Turn {index} missing core dimensions")
            if not tone.get("voice_register") or not tone.get("evidence"):
                failures.append(f"Turn {index} Tone & Authority incomplete")
            if "### Tone & Authority" not in scorecard:
                failures.append(f"Turn {index} scorecard omitted Tone & Authority")
            if words(spoken) > 45:
                failures.append(f"Turn {index} spoken block {words(spoken)}w exceeds the 45-word voice budget")
            if answer_box != "":
                failures.append(f"Turn {index} did not auto-clear the dictation box")

            if index < 4:
                if not evaluation["next_question"]:
                    failures.append(f"Turn {index} returned no next question")
                if turn != index + 1:
                    failures.append(f"Turn {index} advanced to turn {turn}, expected {index + 1}")
            else:
                print(f"  verdict: {evaluation['uplevel_verdict']}")
                print(f"  debrief: {(evaluation['end_of_session_debrief'] or '')[:220]}…")
                if "End of Session Debrief" not in scorecard:
                    failures.append("Turn 4 scorecard is missing the end-of-session debrief")
                if not evaluation["uplevel_verdict"]:
                    failures.append("Turn 4 returned no uplevel verdict")
            print()

        print("--- PERSISTENCE & DASHBOARD ---")
        records = app.load_session_records()
        print(f"  session records: {sessions_before} -> {len(records)}")
        if len(records) != sessions_before + 1:
            failures.append("Turn 4 did not append exactly one session record")
        else:
            record = records[-1]
            new_timestamp = record.timestamp
            print(f"  persona: {record.persona}")
            print(f"  core averages: {record.core_averages}")
            print(f"  uplevel: {record.uplevel_rating} | readiness: {record.readiness_rating}")
            print(f"  bottleneck: {record.primary_bottleneck}")
            if set(record.core_averages) != set(app.CORE_DIMENSIONS):
                failures.append("Persisted record has an incomplete core-average set")
            if record.persona != "Dr. Daniella Kim":
                failures.append("Persisted record has the wrong persona")

        summary_after, history_after = app.load_progress_dashboard()
        print(f"  dashboard rows: {len(history_before)} -> {len(history_after)}")
        expected_line = f"**Total mock sessions completed:** {sessions_before + 1}"
        print(f"  dashboard reports new total: {expected_line in summary_after}")
        if expected_line not in summary_after:
            failures.append("Dashboard did not report the new session total")
        if len(history_after) != len(history_before) + 1:
            failures.append("Dashboard history did not gain the new row")
        if history_after and len(history_after[0]) != len(app.SESSION_HISTORY_HEADERS):
            failures.append("Dashboard row width does not match the table headers")
        nonzero = any(
            isinstance(cell, (int, float)) and cell > 0 for cell in (history_after[0] if history_after else [])
        )
        print(f"  non-zero statistics present: {nonzero}\n")
        if not nonzero:
            failures.append("Dashboard returned all-zero statistics")

    finally:
        print("--- CLEANUP ---")
        if new_timestamp:
            print(f"  removing test entry {new_timestamp}")
        shutil.copyfile(backup_path, state_path)
        restored = state_path.read_bytes()
        restored_hash = hashlib.sha256(restored).hexdigest()
        print(f"  restored sha256 {restored_hash[:12]}… matches original: {restored_hash == original_hash}")
        if restored_hash != original_hash:
            failures.append("coaching_state.md was NOT restored to its original bytes")
        backup_path.unlink(missing_ok=True)
        leftover = re.findall(app.SESSION_RECORD_PATTERN, state_path.read_text(encoding="utf-8"))
        print(f"  residual session records in file: {len(leftover)} (baseline {sessions_before})")
        if len(leftover) != sessions_before:
            failures.append("Test session entry was left behind in coaching_state.md")
        print(f"  temp/backup artifacts remaining: {[p.name for p in state_path.parent.glob('*.integration-backup')]}\n")

    if failures:
        print("❌ INTEGRATION TEST FAILED")
        for failure in failures:
            print(f"   - {failure}")
        return 1

    print("🎉 System is 100% authenticated, operational, and ready for live voice practice!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

import os
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import app


class FakeResponses:
    prompts: list[str] = []

    def parse(self, **kwargs: object) -> SimpleNamespace:
        prompt = str(kwargs["input"])
        self.prompts.append(prompt)
        if prompt.startswith("Generate Question 1"):
            return SimpleNamespace(
                output_parsed=app.InterviewQuestion(
                    question="How would you establish a falsifiable Human Factors baseline for an Air Defense workflow?"
                )
            )

        turn = next(number for number in app.INTERVIEW_ARC if f"This is Question {number} of 4" in prompt)
        core_scores = [
            app.CoreScore(dimension=dimension, score=4, evidence=f"Turn {turn} evidence")
            for dimension in app.CORE_DIMENSIONS
        ]
        uplevel_scores = [
            app.UplevelScore(criterion=criterion, score=4, evidence=f"Turn {turn} evidence")
            for criterion in app.LEAD_STAFF_CRITERIA
        ]
        evaluation = app.Evaluation(
            interviewer_pushback=f"Turn {turn} pushback.",
            core_scores=core_scores,
            uplevel_scores=uplevel_scores,
            strongest_signal="Rigorous operational framing.",
            primary_gap="More quantified thresholds are needed.",
            priority_move="State the falsification criterion first.",
            senior_uxr_baseline_assessment="The answer converts a study into an actionable product decision.",
            lead_staff_uplevel_assessment="The answer defines a reusable standard across teams.",
            demonstrated_level="Lead/Staff Upleveling Signal",
            next_question=f"Question {turn + 1}?" if turn < 4 else None,
            end_of_session_debrief="Consistent evidence across all four turns." if turn == 4 else None,
            uplevel_verdict="Staff" if turn == 4 else None,
            confidence="High",
        )
        return SimpleNamespace(output_parsed=evaluation)


class FakeOpenAI:
    def __init__(self, **_: object) -> None:
        self.responses = FakeResponses()


class InterviewArcTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeResponses.prompts.clear()

    def test_complete_four_question_arc(self) -> None:
        persona = "Dr. Daniella Kim — Research Head"
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch.object(app, "OpenAI", FakeOpenAI):
            indicator, _, _, turn, history, scores, _ = app.start_interview(persona)
            self.assertEqual(turn, 1)
            self.assertIn("Question 1 of 4", indicator)

            for answered_turn in range(1, 5):
                result = app.evaluate_answer(
                    f"Answer {answered_turn}", persona, turn, history, scores
                )
                indicator, _, scorecard, turn, history, scores, cleared_answer = result
                self.assertEqual(cleared_answer, "")
                self.assertEqual(len(scores), answered_turn)
                if answered_turn < 4:
                    self.assertEqual(turn, answered_turn + 1)
                    self.assertIn(f"Question {turn} of 4", indicator)
                else:
                    self.assertEqual(turn, 0)
                    self.assertIn("End of Session Debrief", scorecard)
                    self.assertIn("Lead/Staff verdict: Staff", scorecard)
                    self.assertIn("Senior UXR baseline", scorecard)
                    self.assertIn("Lead/Staff upleveling signal", scorecard)

        self.assertTrue(any("Deep-Dive Pushback & Probe" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(any("Behavioral & Collaboration" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(any("Leadership, Scaling & Vision" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(all("NASA-TLX" in prompt for prompt in FakeResponses.prompts))

    def test_canonical_resume_and_job_requirements_are_in_system_context(self) -> None:
        context = app.load_system_context()

        self.assertIn("Brandon Fluegel, PhD", context)
        self.assertIn("Working memory, spatial processing, and reaction times", context)
        self.assertIn("US-12532040-B1", context)
        self.assertIn("Senior User Experience Researcher", context)
        self.assertIn('"minimum": 166000', context)
        self.assertIn("service blueprints", context)
        self.assertIn("max-diff", context)

    def test_all_personas_receive_specific_resume_to_job_probe(self) -> None:
        expected_evidence = {
            "Dr. Daniella Kim — Research Head": "fNIRS",
            "Systems / ML Engineering Lead": "$50M Amazon psychophysics",
            "Product Manager": "startup shipping velocity",
            "Design Lead": "Echo Hub",
        }
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch.object(app, "OpenAI", FakeOpenAI):
            for persona, evidence in expected_evidence.items():
                FakeResponses.prompts.clear()
                app.generate_question(persona, 1, [])
                self.assertIn(evidence, FakeResponses.prompts[-1])
                self.assertIn("Senior UXR baseline", FakeResponses.prompts[-1])
                self.assertIn("Lead/Staff scope", FakeResponses.prompts[-1])

    def test_canonical_json_has_complete_supplied_collections(self) -> None:
        data_root = Path(__file__).resolve().parents[1] / "data"
        candidate = json.loads((data_root / "candidate_profile.json").read_text(encoding="utf-8"))
        target = json.loads((data_root / "target_anduril_air_defense.json").read_text(encoding="utf-8"))

        self.assertEqual(candidate["schema_version"], "2.0")
        self.assertEqual(len(candidate["experience"]), 6)
        self.assertEqual(len(candidate["education"]), 2)
        self.assertEqual(target["position"]["base_salary_usd"], {"minimum": 166000, "maximum": 220000})
        self.assertEqual(len(target["key_responsibilities"]), 5)
        self.assertIn("Eligibility for a Top Secret clearance.", target["qualifications"]["required"])


if __name__ == "__main__":
    unittest.main()
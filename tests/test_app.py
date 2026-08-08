from __future__ import annotations

import os
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

        self.assertTrue(any("Deep-Dive Pushback & Probe" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(any("Behavioral & Collaboration" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(any("Leadership, Scaling & Vision" in prompt for prompt in FakeResponses.prompts))
        self.assertTrue(all("NASA-TLX" in prompt for prompt in FakeResponses.prompts))


if __name__ == "__main__":
    unittest.main()
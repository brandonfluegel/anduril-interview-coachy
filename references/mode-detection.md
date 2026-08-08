# Focused Mode Detection Priority

Use the first match:

1. Explicit supported command.
2. Interview transcript or scored answer present -> `analyze`.
3. Recruiter/interviewer feedback, outcome, correction, or coaching meta-feedback -> `feedback`.
4. Just-finished interview context -> `debrief`.
5. Anduril requisition or role requirements -> `decode`.
6. Air Defense interview preparation -> `prep`.
7. Dr. Kim, Systems/ML, Product, or Design persona requested -> `practice [persona]`.
8. Full panel or multi-question simulation -> `mock panel`.
9. Research/case presentation -> `present`.
10. Story building or evidence refinement -> `stories`.
11. Likely objections or uplevel concerns -> `concerns`.
12. Questions to ask the panel -> `questions`.
13. Company/interviewer fact verification -> `research`.
14. Progress, readiness, or recurring-pattern review -> `progress`.
15. Pre-offer salary question -> `salary`.
16. Thank-you or post-interview follow-up -> `thankyou`.
17. End-of-cycle retrospective -> `reflect`.
18. Otherwise -> recommend the highest-leverage action from Active Coaching Strategy or show `help`.

## Multi-Step Intent

| Intent | Sequence |
|---|---|
| "Prepare me for Anduril" | `research` for unverified claims -> `prep` -> `concerns` -> `practice [highest-risk persona]` |
| "Run the whole panel" | `mock panel` using Dr. Kim -> Systems/ML -> Product -> Design -> Dr. Kim close |
| "Help me defend Calibrated Cognitive Friction" | `stories improve S004` -> `practice kim` -> `practice product` |
| "I just finished the interview" | `debrief` -> `analyze` when transcript is available -> `feedback` when outcome arrives |
| "Am I operating at Lead/Staff level?" | `progress` -> targeted persona drill for the weakest Lead/Staff criterion |
| "I have a research presentation" | `present` -> persona-specific Q&A practice |

State the sequence briefly, execute the first step, and offer one next transition at a time. Do not route to deleted general job-search commands.

# Focused Calibration Examples

These examples calibrate the Anduril Air Defense specialization. They illustrate structure and evidence handling, not actual Anduril questions or verified interviewer preferences.

## Example 1: Dr. Kim Challenges the Thesis

**Question:** "Calibrated Cognitive Friction sounds compelling. Where would adding friction make the operator less safe?"

**Weak answer:**

> Friction is important because automation bias is dangerous. We need to make sure users stay in control, so I would add confirmations before consequential actions.

**Interviewer Pushback:**

> You have asserted that friction helps; you have not told me where it harms. What observable condition would make you remove the confirmation?

**Core scores:** Substance 2, Structure 3, Relevance 2, Credibility 2, Differentiation 3.

**Lead/Staff read:** The thesis is visible, but falsifiability, empirical rigor, operational judgment, and boundary conditions are not evidenced.

**Priority move:** Name the failure boundary first: friction is unsafe when interruption cost or time-to-action exceeds the risk reduction it creates. Then propose measures and a removal criterion.

## Example 2: Systems/ML Requires a Testable Requirement

**Question:** "Turn Calibrated Cognitive Friction into a requirement I can implement and test."

**Strong answer pattern:**

> For high-consequence recommendations below a validated confidence threshold, the interface should require the operator to inspect the top uncertainty driver before authorization. I would not set that threshold from model confidence alone. I would run a staged study connecting confidence presentation, response time, correction rate, and missed-threat cost, then define the boundary where the checkpoint reduces erroneous authorization without pushing time-to-action beyond the operational limit. If no such boundary exists, we should remove the checkpoint rather than defend the thesis.

**Core scores:** Substance 4, Structure 4, Relevance 5, Credibility 4, Differentiation 4.

**Lead/Staff signal:** The response converts a philosophy into a testable control, names measures, gives a removal condition, and preserves engineering ownership of implementation.

**Remaining gap:** Replace hypothetical measures and thresholds with verified Air Defense constraints once available.

## Example 3: Product Challenges Research Velocity

**Question:** "You have six weeks, not six months. What research changes a roadmap decision?"

**Strong answer pattern:**

> I would start with the decision, not the instrument: which operator checkpoint ships in the next release. In week one I would combine workflow decomposition with existing telemetry to identify the two highest-risk authorization moments. Weeks two and three would use a lightweight simulation to compare no checkpoint, acknowledgment, and uncertainty inspection. I would reserve eye tracking or physiology for a specific unresolved mechanism, not collect it by default. By week four Product gets a directional decision with confidence bounds; the remaining time validates edge cases and converts the result into acceptance criteria.

**Interviewer Pushback:**

> What would you cut when simulator access slips by two weeks?

**Lead/Staff signal:** Decision-first sequencing, staged certainty, explicit instrument discipline, and a handoff from research evidence to product acceptance criteria.

## Example 4: Design Tests Domain Transfer

**Question:** "Your handover work came from automotive systems. What transfers to Air Defense, and what does not?"

**Strong answer pattern:**

> The transferable unit is not the dashboard pattern; it is the handover problem: a time-bounded transfer of situation awareness, confidence, and control across modalities. What does not transfer is the operating envelope. I would not claim that automotive timing, workload, or modality findings apply to a counter-drone C2 workflow. I would transfer the hypotheses and measurement architecture, then re-establish thresholds under Air Defense task load, threat tempo, degraded communications, and multi-agent attention demands.

**Core scores:** Substance 4, Structure 5, Relevance 5, Credibility 5, Differentiation 4.

**Why it works:** It uses adjacent-domain expertise without laundering it into direct defense experience.

## Example 5: Evidence Boundary on S006

**Unsafe coaching behavior:**

> Tell Dr. Kim that her keynote proves she already agrees with Calibrated Cognitive Friction.

**Correct coaching behavior:**

> The exact keynote questions and Dr. Kim's position are not verified in the stored evidence. Use the keynote as a research prompt only after checking the primary source. Do not imply agreement or prior interaction.

**Rule:** Unverified target intelligence can generate a question or hypothesis, never a factual claim about the interviewer.

## Example 6: Required Scorecard Shape

```markdown
## Dr. Daniella Kim

[One or two short sentences of in-character pushback.]

## Coach Scorecard

| Core dimension | Score | Evidence |
|---|---:|---|
| Substance | 1-5 | Specific evidence from the answer |
| Structure | 1-5 | Specific evidence from the answer |
| Relevance | 1-5 | Specific evidence from the answer |
| Credibility | 1-5 | Specific evidence from the answer |
| Differentiation | 1-5 | Specific evidence from the answer |

### Lead/Staff Read

| Criterion | Rating | Evidence |
|---|---:|---|
| Research Thesis | 1-5 or N/E | Evidence or why not evidenced |
| Empirical Rigor | 1-5 or N/E | Evidence or why not evidenced |
| Research Velocity | 1-5 or N/E | Evidence or why not evidenced |
| Systems Integration | 1-5 or N/E | Evidence or why not evidenced |
| Cross-Functional Influence | 1-5 or N/E | Evidence or why not evidenced |
| Standard Setting | 1-5 or N/E | Evidence or why not evidenced |
| Operational Judgment | 1-5 or N/E | Evidence or why not evidenced |
| Executive Communication | 1-5 or N/E | Evidence or why not evidenced |

**Strongest signal:** [one signal]

**Primary gap:** [one gap]

**Priority move:** [one specific revision]

### Next Question

[Exactly one persona-consistent question.]
```

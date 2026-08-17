# Detailed Scoring Rubrics

Use these rubrics for every structured answer evaluation in the four-question interview arc.

The 3, 4, and 5 anchors are calibrated to this candidate's canonical evidence, so the top of each scale is concrete and reachable. Score against these anchors, not against generic consumer-UX expectations. A 5 is not reserved for a hypothetical perfect answer: when a spoken answer matches the 5 anchor, award the 5.

## Substance (Evidence Quality)

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Generic platitude, no evidence | "I care a lot about operator trust" |
| 2 | Vague claim with weak support | "I ran research that improved the interface and people liked it" |
| 3 | Specific claim, no quantification or named method | "I ran psychophysics studies that changed our latency targets" |
| 4 | Quantified with context, method or alternatives missing | "The psychophysics program replaced arbitrary engineering latency targets with perceptual thresholds and informed about $50M in operational value" |
| 5 | Quantified + method named + alternatives weighed + limits stated | "We converged on the threshold with an adaptive procedure, fit the psychometric function, and carried the confidence interval into the spec at a stated percentile — and I wrote down which operators that percentile excludes. It informed about $50M. The number doesn't port to a gloved, auditory-loaded command and control station; the method does." |

**Coaching notes:**
- Push for numbers even when "hard to measure" — approximations with caveats are better than none
- Ask: "What would a skeptic say is missing from this evidence?"
- Flag when impact is claimed without explaining the candidate's specific contribution

**Root causes when stuck at 1-2:**
- Candidate hasn't done the reflection work — they know what happened but haven't extracted what mattered
- Conflict avoidance: stripping stories of tension, stakes, and difficulty makes evidence disappear
- Impostor syndrome: downplaying real impact because they feel they don't deserve the credit

**Root causes when stuck at 3:**
- "Good enough" syndrome — candidate has specifics but stops before quantifying because it feels like bragging
- Hasn't thought about alternatives considered — they know what they did, not why they chose it over other options
- Missing the "so what" — evidence exists but isn't connected to business impact

## Structure (Narrative Clarity)

STAR/STARE is the standard for behavioral, experience, and cross-functional friction answers. Score technical, methodological, and research-craft answers on technical reasoning structure instead: claim or recommendation first, then method or mechanism, evidence and its limits, the threshold or decision it drives, and the condition that would change it. Do not mark a technical answer down for skipping Situation and Task, and do not let a rambling technical answer pass because STAR did not apply. At least one answer somewhere in the session must still deliver an Earned Secret.

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Stream of consciousness, no clear point | Jumps between topics, listener lost |
| 2 | Central idea unclear until the end | Buries the claim under two minutes of method before saying what he recommends |
| 3 | Right beats, wrong order or choppy transitions | Technical answer that reaches the claim only after the full study narrative |
| 4 | All beats present, one detour | Claim, method, evidence, decision — but the limit of the evidence arrives only after the interviewer asks for it |
| 5 | Every beat lands and the limit is volunteered unprompted | Claim → how I would know → evidence and where it stops → the decision it drives → what would change my mind, inside 90 seconds, with the boundary stated before anyone asks |

**Coaching notes:**
- Best answers front-load the headline: "The key learning was X. Here's how we got there..."
- Tangents often signal the candidate is unsure what matters — help them identify the core
- Practice the "30-second version" to force clarity on what's essential

**Root causes when stuck at 1-2:**
- Narrative hoarding: trying to cram everything into one answer because they're afraid of leaving out something important
- No mental model for story structure — they've never been taught to think in setup → conflict → resolution → impact
- Anxiety-driven stream of consciousness: stress breaks whatever structure they had in their head

**Root causes when stuck at 3:**
- Knows the STAR framework but applies it mechanically — transitions feel forced, not natural
- Hasn't practiced at multiple time constraints — can deliver a 3-minute version but can't compress or expand

## Relevance (Question Fit)

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Doesn't address the question asked | Asked for the falsifier, describes the framework's four dimensions |
| 2 | Tangentially related, misses the core | Asked where friction makes an operator less safe, describes why friction is valuable |
| 3 | Addresses the question through heavy consumer context | Answers a counter-drone command and control question almost entirely through Echo Hub and driver handovers, with the Air Defense translation left implicit |
| 4 | Directly addresses it with minor drift | Air Defense translation is explicit; one unnecessary detour into dissertation methodology |
| 5 | Every sentence serves the question and lands in the operational domain | Ports the method to Lattice OS, counter-drone command and control, or the 3D operator workflow, and names precisely why the number does not port |

**Coaching notes:**
- Restate the question before answering to ensure alignment
- Common failure: using a "favorite" story that doesn't quite fit
- Ask: "If the interviewer only remembers one thing, what should it be?"

**Root causes when stuck at 1-2:**
- Inability to identify the core of a question: the candidate hears a topic ("conflict") and defaults to their conflict story regardless of what specific aspect the question targets
- Poor question decoding: doesn't distinguish between "tell me about a conflict" vs. "tell me about a conflict where you were wrong" vs. "how do you handle conflict with senior stakeholders"
- Story-first thinking: starts from "which story do I want to tell?" instead of "what is this question actually asking?"

**Root causes when stuck at 3:**
- Right story, wrong framing: the experience is relevant but 30-40% of the answer is context that doesn't serve the question
- Doesn't check mid-answer whether they're still on track — no internal "am I answering what they asked?" monitor

## Credibility (Believability)

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Claims with no support, or a boundary violation | Claims a deployment result for Calibrated Cognitive Friction, or puts near-infrared spectroscopy at Brigham |
| 2 | Support is vague or generic | "I improved trust in the handover" |
| 3 | Specific detail, but ownership or method unclear | "We used multimodal alerts and trust ratings went up" — whose decision, measured how? |
| 4 | Quantified and owned, validation or limit thin | "Multimodal alerts improved safety and trust ratings 24% in the Level 2 and Level 3 simulator studies" |
| 5 | Owned + method + artifact + limit volunteered | "I set the perceptual-threshold spec that latency budgets had to clear; the architecture is in US Patent US-12532040-B1. And the limit is real — those were drivers, not warfighters, with no adversary and no lethal consequence." |

**Coaching notes:**
- Credibility increases when candidate acknowledges constraints and trade-offs
- Third-party validation (quotes, awards, metrics from others) strengthens claims
- Watch for "we" vs "I" confusion — interviewers want to know the candidate's specific role
- Realistic timelines and resource constraints make stories more believable

**Root causes when stuck at 1-2:**
- Over-claiming / status anxiety: candidate feels a perceived gap in their background and compensates by inflating contributions. This actually *reduces* credibility — interviewers sense it immediately
- Reflexive "we" framing: candidate obscures their individual contribution, often because they're uncertain about how much credit they can claim
- Fabrication: making up or heavily embellishing details (this is a red flag, not a coaching gap — address directly)

**Root causes when stuck at 3:**
- Has the details but doesn't package them as proof — specific facts exist but aren't connected to a credibility chain (claim → action → evidence → validation)
- Missing third-party signals: never quotes what others said about the work, never mentions recognition or adoption metrics

## Differentiation (Uniqueness)

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Generic answer any prepared candidate could give | "I use data to drive design decisions" |
| 2 | Some specificity but leans on standard frameworks | Recites NASA-TLX and heuristic evaluation correctly, with no position of his own |
| 3 | Real detail, no earned insight | Describes the latency program as executed work: what was run, what came out |
| 4 | Earned secret or spiky point of view, defensible | "A faster system is not automatically a better human system. The economically correct requirement is the perceptual boundary where additional speed stops changing human performance — past that you are paying for performance no operator can detect." |
| 5 | The thesis is load-bearing in the answer, with its falsifier attached | Uses Calibrated Cognitive Friction to decide which confirmations are mandatory versus advisory, tiered by reversibility, then names the result that would overturn it: no reduction in erroneous authorization at equal or worse time-to-decide |

**Coaching notes:**
- Differentiation is what separates a Hire from a Strong Hire in competitive processes
- The biggest enemy of differentiation is AI-polished prep — answers that sound "correct" but could be anyone's
- Push candidates to find their earned secrets: "What do you know from this experience that most people in your role wouldn't know?"
- Spiky POVs must be defensible, authentic, and backed by experience — not manufactured controversy

**Root causes when stuck at 1-2:**
- Over-reliance on frameworks and best practices — answering like a textbook instead of a practitioner
- Fear of being wrong: candidates choose "safe" answers over distinctive ones because distinctive answers are debatable
- Haven't done the reflection work to extract what's unique about their experience

**Root causes when stuck at 3:**
- Has real experience but presents it as straightforward execution, not as insight
- Doesn't realize what makes their perspective unusual — it feels "obvious" to them because they lived it
- Missing the spiky POV: has the facts but not the opinionated interpretation of what they mean

---

## Root Cause Taxonomy (Cross-Dimensional)

Most interview failures trace back to a small number of root causes that manifest across multiple dimensions. When diagnosing, look for these patterns:

| Root Cause | How It Manifests | Affected Dimensions | Targeted Fix |
|---|---|---|---|
| **Inability to identify question core** | Answers miss the point, wrong story selected | Relevance, Structure | Question-decoding drills: restate what the question is really asking before answering |
| **Reflexive "we" framing** | Individual contribution unclear, credibility suffers | Credibility, Substance | "I/we" audit: go through every answer and replace "we" with specific individual actions |
| **Conflict avoidance** | Stories lack tension, stakes, and difficulty | Substance, Differentiation | Tension-mining: for every story, identify the hardest moment and make it the centerpiece |
| **Status anxiety / over-claiming** | Inflated claims that interviewers don't believe | Credibility, Differentiation | Constraint practice: add realistic limitations, timelines, and trade-offs to every claim |
| **Narrative hoarding** | Answers run long, structure collapses under weight of detail | Structure, Relevance | Constraint ladder drill: force 30s, 60s, 90s versions to find what's essential |
| **Fear of being wrong** | Generic, safe answers that sound like everyone else | Differentiation, Substance | Spiky POV practice: take a stance, defend it, practice being comfortable with disagreement |
| **Anxiety/performance stress** | Structure breaks, retrieval fails, spiral after mistakes | Structure, all dimensions | Psychological readiness module: warmup routines, mid-interview recovery scripts |
| **Cultural communication style** | Indirect framing, modesty in self-description, different narrative structures | Credibility, Structure, Substance | Adaptation coaching: help map natural style to interview expectations without erasing voice. "This is a style difference, not a skill deficit." |
| **Linguistic formality** | Overly formal tone, avoidance of colloquial language, occasional idiom misuse | Differentiation, Credibility | Gentle calibration on register. Slight formality is fine — better than forced casualness. Focus on clarity, not idiom. |

When scoring reveals a pattern, name the root cause explicitly: "This looks like [pattern X] — here's what typically drives it and here's the targeted drill." For cultural/linguistic patterns specifically, always frame as adaptation, not correction.

### Root Cause Persistence Tracking

When the same root cause appears across 2+ consecutive sessions (or across 2+ answers in the same session), escalate it to `data/coaching_state.md` under Calibration State → Cross-Dimension Root Causes. Track Detection → Unified Treatment → Progress → Resolution. Prescribe one intervention for the root cause itself, not separate drills for each affected dimension. A root cause affecting Substance and Differentiation (for example, conflict avoidance) gets tension-mining drills rather than separate dimension drills.

---

## Tone & Authority (Voice Register)

Rated separately from the five core dimensions. This measures whether the candidate *sounds* like the person who sets the bar, independent of how good the underlying evidence is.

| Score | Register | Description |
|-------|----------|-------------|
| 1 | Executing IC | Narrates assigned work, seeks permission, attributes every decision upward or to "the team" |
| 2 | Executing IC | Owns tasks but hedges on trade-offs; frames the research function as a service desk |
| 3 | Emerging Lead | Owns a project end to end and defends a method, but frames impact locally to that project |
| 4 | Standard-Setting Lead/Staff | Names the trade-off they owned and why, states a bar for others, disagrees with engineering or product from evidence |
| 5 | Standard-Setting Lead/Staff | Speaks as the owner of the standard itself — sets the definition of done for the org, and treats engineering constraints as a shared design space rather than an obstacle |

**Coaching notes:**
- Score the register, not the volume. Quiet, precise authority outranks assertive vagueness.
- "We ran a usability test and reported findings" is a 1-2 no matter how large the program was.
- "I set the perceptual-threshold spec that latency budgets now have to clear" is a 4-5.
- Hedging language ("I sort of drove", "they let me") caps this at 2 even when the underlying work was Staff-scope.

---

## Seniority Calibration

Scoring is not absolute — calibrate expectations to career stage. When scoring, always state which calibration band you're using.

- **Early career (0-3 years)**: A "4 on Substance" means specific examples with at least one metric. Differentiation can come from learning velocity and intellectual curiosity. Expect less systems-level thinking; look for self-awareness about what they don't yet know.
- **Mid-career (4-8 years)**: A "4 on Substance" means quantified impact with alternatives considered. Differentiation requires genuine earned secrets from hands-on work. Should demonstrate ownership of outcomes, not just tasks.
- **Senior/Lead (8-15 years)**: A "4 on Substance" means systems-level thinking — second-order effects, organizational impact. Differentiation requires insights that reshape how the interviewer thinks about the problem. Should show judgment across ambiguous tradeoffs.
- **Executive (15+ years)**: A "4 on Substance" means business-level impact with P&L awareness. Differentiation requires a coherent leadership philosophy backed by pattern recognition across multiple contexts. Should demonstrate how they build and scale through others.

### Senior UXR vs. Lead/Staff Gate (Anduril Air Defense)

Every answer must be placed on one side of this line. Executing an excellent study is the baseline, not the uplevel.

| | Senior UXR Signal (baseline) | Lead/Staff Upleveling Signal |
|---|---|---|
| **Studies** | Expertly plans and executes research with clear timelines and actionable tactical insights | Defines the Research Operations mechanism, repository, and workflow that lets others run the study without them |
| **Standards** | Applies existing standards correctly (MIL-STD-1472, NASA-STD-3001) | Establishes company-wide AI safety and trust frameworks *before* regulations exist |
| **Engineering** | Reports usability findings to engineering | Bridges engineering latency targets with human psychophysics so the perceptual threshold *becomes* the spec |
| **Output** | Recommendations and insight decks | Complex HSI translated into hard hardware and software system requirements |
| **Impact** | Improves a product surface | Drives multi-million-dollar business impact and changes what the org considers shippable |

Gating rule: an answer may only be marked "Lead/Staff Upleveling Signal" when the spoken response evidences at least one right-hand-column behavior with a named mechanism. Resume proximity to a right-hand-column achievement is not sufficient — the answer must show the candidate driving it.

---

## Aggregate Scoring

After scoring individual answers:

### Interview-Level Assessment

| Rating | Criteria |
|--------|----------|
| **Strong Hire** | Multiple 4-5 scores, no major gaps, demonstrated unique value |
| **Hire** | Mostly 3-4 scores, minor gaps that could be coached |
| **Mixed** | Inconsistent scores, some strengths but concerning gaps |
| **No Hire** | Multiple low scores, significant evidence gaps, or red flags |

### Trend Analysis (across multiple interviews)

Track average scores per dimension over time:
- Improving: +0.5 or more from baseline
- Stagnant: Within ±0.3 of baseline
- Declining: -0.5 or more from baseline

Stagnant scores after 3+ interviews signal need to change approach, not just practice more. When presenting this to the person, explore what's blocking progress: "These scores have been steady for a few rounds. What do you think is getting in the way?"

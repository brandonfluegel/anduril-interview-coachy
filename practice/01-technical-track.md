# 01 — Technical & Research-Craft Track (TQ01–TQ10)

Ten pillars. Each has the base question, the four ways it may be phrased, one model answer, all three follow-ups with scoped answers, and the Senior → Lead/Staff delta.

The **persona variants** are the same question worded four ways. They are there so you recognize the question, not so you tailor the answer. One answer per question, every time.

**Structure for this entire track: CMELT** — Claim → Method/mechanism → Evidence + limits → Line (threshold/decision) → Turn (falsifier). Do **not** use STAR here. STAR on a technical question is a Relevance penalty.

**Target length: 160–230 words ≈ 65–90 seconds.** Follow-ups: 45–90 words ≈ 20–35 seconds.

`[brackets]` = a fact only you can supply. Fill it in or delete the sentence. Never improvise a number.

---

## TQ01 — Research Thesis & Falsifiability

**Arc:** opening, leadership · **Structure:** CMELT · **Target:** ~80s

> **Base:** State your Human Factors thesis for autonomous Air Defense in one sentence, and tell me what evidence would falsify it.

**Persona variants**

- **Kim:** "Give me your one-sentence thesis for Human Factors in autonomous Air Defense, and the single result that would force you to abandon it."
- **Systems/ML:** "Calibrated Cognitive Friction is a philosophy. What measurable claim inside it can I actually test on a counter-drone C2 build?"
- **Product:** "In one sentence, what is your Human Factors bet for Air Defense, and what would it cost us if you are wrong?"
- **Design:** "What is your thesis about operator authority in autonomous C2, and where would it visibly change an interaction, not just a research memo?"

### Model answer (~190 words / 78s)

**Claim.** In autonomous air defense the design goal is not the fastest interaction, it is the best-authorized one. My thesis — Calibrated Cognitive Friction — is that at irreversible decision boundaries, a small amount of risk-proportional friction that exposes system uncertainty produces better authorization quality than a frictionless flow, without materially costing engagement tempo.

**Method.** The testable core is trust calibration, not trust. I'd measure operator acceptance rate conditioned on autonomy correctness and on the system's own confidence band. Over-trust shows up as flat acceptance across confidence bands — the operator approves a low-confidence recommendation as fast as a high-confidence one. That is measurable in decision latency distributions and acceptance-by-confidence curves before it is ever measurable in an incident.

**Evidence and limits.** My Mercedes L2/L3 handover work improved safety and trust ratings 24% using multimodal alerts to prepare a disengaged operator before transfer. The limit is real: those were drivers, not warfighters, with no adversary and no lethal consequence. And Calibrated Cognitive Friction is a thesis — I have not deployed it. What I have shipped is the audit structure behind it, *Principles for Agentic Trust*, accepted to CSCW 2026.

**Line.** It governs one decision: where a confirmation step is mandatory versus advisory, tiered by reversibility.

**Turn.** It's falsified if friction at the authorization boundary shows no reduction in erroneous authorization while pushing time-to-decide outside the threat's kinematic window. Same acceptance-by-confidence curve, worse timeline — I abandon it.

### Follow-ups

**F1 — "Which of your four Agentic Trust dimensions fails first in a non-deterministic C2 system, and how would you detect it?"** *(~70 words)*

> Calibration fails first. Alignment, Execution, and Control are mostly design-time properties — you can specify and verify them. Calibration is a running property of the human-system pair, and it drifts every time the model updates or the operator gets a streak of correct recommendations. Detection signal: acceptance rate flattening across the system's own confidence bands, plus decision latency collapsing toward zero on low-confidence items.

**F2 — "Name the specific study result that would falsify Calibrated Cognitive Friction rather than merely complicate it."** *(~65 words)*

> A within-subjects study where the friction condition shows no significant reduction in erroneous authorizations against a matched no-friction condition, at equal or worse time-to-decide, under realistic workload. Not a null in one scenario — a null with adequate power across the consequence tiers where I claim the effect is strongest. If the effect isn't there at the irreversible boundary, the thesis is wrong.

**F3 — "Where would adding friction make an Air Defense operator less safe, and how would you know you crossed that line?"** *(~75 words)*

> Two places. Under saturation — multiple simultaneous threats — where a confirmation step serializes an operator who needs to work in parallel. And in degraded comms, where friction can strand a decision the operator can no longer complete. I'd know I crossed it when added dwell time stops buying error reduction and starts producing abandoned or timed-out decisions. That ratio is the governing metric, and it should be a monitored number, not a design opinion.

### Senior → Lead/Staff

- **Senior:** states a defensible, well-articulated thesis.
- **Lead/Staff:** states the falsifier, the detection measure, and the organizational decision the thesis governs.
- **Say this:** *"The reason I state it as a falsifiable claim is that it has to govern a decision — which confirmations are mandatory and which are advisory. If it isn't falsifiable it can't govern anything, it can only be argued about."*

---

## TQ02 — Psychophysics to System Requirements

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~85s

> **Base:** You replaced arbitrary engineering latency targets with human perceptual thresholds. Walk me from the psychophysics to the written specification.

**Persona variants**

- **Kim:** "Take me through the psychophysical method behind your latency thresholds: stimuli, staircase or method of limits, sample, and how you defended the threshold estimate."
- **Systems/ML:** "Your threshold came from a population distribution. How do you turn that distribution into a single acceptance criterion I can verify in a test harness?"
- **Product:** "How did the perceptual threshold work actually change what engineering shipped, and what was the dollar consequence of the old arbitrary target?"
- **Design:** "Where does a perceptual latency threshold change the interaction itself — feedback timing, modality choice, or the moment we show uncertainty?"

### Model answer (~210 words / 84s)

**Claim.** A latency target is a perceptual claim, so it should be written as a threshold with a stated population percentile and a defined degradation behavior — not as a round number someone liked.

**Method.** Four steps. One: define the perceptual event precisely — not "system latency" but the interval between the operator's input and the first system feedback in a named modality. Two: estimate the threshold with an adaptive procedure, converging on the detection point rather than sampling a fixed grid, because the interesting region is narrow and non-linear. Three: fit the psychometric function and carry the confidence interval forward — the spec inherits the uncertainty. Four: choose the population percentile deliberately and write down who that excludes.

**Evidence and limits.** At Amazon I ran a multi-year psychophysics program that replaced arbitrary engineering latency targets with human perceptual thresholds; it informed roughly $50M in operational value, and the multimodal interaction architecture is captured in US Patent US-12532040-B1. At Sling I now define latency, auditory and visual feedback, and spatial layout criteria against perceptual thresholds. The limit: thresholds are modality- and workload-specific. A visual-feedback threshold from a consumer device does not port to a gloved, high-tempo, auditory-loaded C2 station. The method ports; the number does not.

**Line.** The spec reads as an acceptance test: end-to-end feedback latency at [percentile] of the operator population, verified under worst-case system load, with a named fallback if the hardware cannot hit it.

**Turn.** If operators under realistic workload show no performance or trust difference across the threshold band, latency isn't the binding constraint and I re-derive it under load.

### Follow-ups

**F1 — "Which percentile of the operator population did you specify to, and who did that choice exclude?"** *(~70 words)*

> I specify to [percentile] and I write the exclusion down explicitly, because that's the part that gets lost. A central-tendency spec silently designs for the median operator and fails the tails — and in this domain the tails aren't edge cases, they're the fatigued operator at hour nine and the one with degraded hearing from the environment. If I can't cover a tail, it becomes a documented residual risk, not an omission.

**F2 — "What measurement method produced that number, and what was its confidence interval?"** *(~60 words)*

> An adaptive threshold procedure with the psychometric function fit per participant, then aggregated — so the spec carries an interval, not a point. My rule is that the specification takes the conservative bound of that interval, not the mean. If someone wants the mean, that's a deliberate risk acceptance with a name attached to it, which is a different conversation than a measurement one.

**F3 — "If the hardware cannot hit your threshold, what is the fallback specification and what degrades?"** *(~75 words)*

> Fallback is a modality substitution, not a relaxation. If the visual path can't confirm inside the threshold, you acknowledge the input in a faster channel — an auditory or haptic onset cue — so the operator's sense of system responsiveness is preserved while the visual result resolves. What degrades is information completeness in that first window: the operator knows the system heard them before they know what it decided. That's an acceptable trade; silence is not.

### Senior → Lead/Staff

- **Senior:** reports a threshold and the study behind it.
- **Lead/Staff:** shows the population-to-specification translation, makes the tail-risk decision explicit and owned, and leaves a reusable method other teams inherit.
- **Say this:** *"The durable output wasn't the number. It was that latency arguments in that org stopped being opinion — anyone proposing a target had to say which percentile and which modality."*

---

## TQ03 — Objective Workload & Measure Selection

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~80s

> **Base:** When is fNIRS, eye tracking, or ECG worth the cost over NASA-TLX and behavioral performance data for an Air Defense operator study?

**Persona variants**

- **Kim:** "Defend your measure selection: what decision would fNIRS or eye tracking support for Air Defense that NASA-TLX and task performance would not?"
- **Systems/ML:** "Which of those signals could be instrumented in a fielded system, and which only survive in a lab? What do we lose in the field version?"
- **Product:** "Why should I fund biometric telemetry instead of another round of operator workflow testing this quarter?"
- **Design:** "What did eye tracking tell you about attention allocation that changed a layout, and how would that transfer to a dense 3D C2 display?"

### Model answer (~195 words / 78s)

**Claim.** Instrument choice follows the decision, not the prestige of the signal. Objective measures earn their cost in exactly two cases: when you need *within-task* dynamics — where in the task the load spikes — or when self-report is structurally compromised by the task itself.

**Method.** I work down a ladder and stop at the cheapest rung that answers the question. Behavioral performance and system telemetry first — errors, mode confusions, time-to-acknowledge. Then eye tracking, when the question is attention allocation and specifically *what the operator never looked at*, which no post-task rating can recover. Then continuous physiological measures when I need a time-series of state across a long, uneven task. NASA-TLX stays in the kit as a cheap, comparable post-task summary — it just can't tell me *when*.

**Evidence and limits.** At Amazon I built an objective cognitive load framework using fNIRS and eye tracking. Separately, at Brigham and Women's I processed fMRI, ECG, and telemetry for acute-stress research. Two different toolkits in two different settings — I keep them separate. And I want to be precise: I do not have a head-to-head result showing a biometric measure outperformed NASA-TLX. My claim is about the *class of question* each answers, not a bake-off I can cite.

**Line.** The rule I'd bring: a biometric measure gets funded only when it's pre-committed to a decision. If no plausible result changes a decision, it's expensive theater and I'd kill it myself.

**Turn.** If the biometric signal never dissociates from behavioral performance across conditions, it's redundant and I drop it.

### Follow-ups

**F1 — "Take fNIRS away. What is your next-best measure, and what claim can you no longer make?"** *(~65 words)*

> Next best is eye tracking plus task-embedded performance probes — secondary-task decrement and time-to-acknowledge. What I lose is the claim about internal load *when behavior looks fine*. That's the compensating-operator case: performance holds while effort climbs, and the only visible signal is the collapse later. Without a continuous physiological measure I can infer that from degradation over time, but I can't assert it in the moment.

**F2 — "What is your evidence that the biometric signal tracked the operational failure you cared about, not just arousal?"** *(~70 words)*

> You establish it by dissociation, and it's the right challenge — arousal confounds are the standard failure of this method class. The design requirement is conditions matched on arousal but differing in the cognitive demand you care about. If the signal moves with demand and not with the arousal manipulation, you have something. If it moves with both, you have a stress detector, which is a much weaker claim, and I'd report it as one.

**F3 — "How do you handle motion, noise, and gloves degrading those signals during in-field testing?"** *(~75 words)*

> I assume degradation and design the field version around it, rather than trying to force lab fidelity into the field. Optical and cardiac signals suffer motion artifact; eye tracking suffers sunlight and recalibration. So the field instrument set shifts toward system telemetry and observation — dwell, mode errors, corrections, sequence breakdowns — and the physiological work stays in the simulator, where I can control it. The field's job is validating that the lab effect exists in reality, not measuring it precisely.

### Senior → Lead/Staff

- **Senior:** selects a valid instrument and runs it well.
- **Lead/Staff:** states the decision the measure serves, offers the cheaper substitute unprompted, and names the point at which the measure becomes expensive theater.
- **Say this:** *"I've made a career out of objective measurement, which is exactly why I'll tell you when not to buy it."*

---

## TQ04 — Safety Analysis & Military Standards

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~85s

> **Base:** Walk me through a uFMEA for an autonomous threat recommendation that arrives with uncertain confidence, and where MIL-STD-1472 stops being enough.

**Persona variants**

- **Kim:** "How would you structure a use-error analysis for counter-drone authorization so it produces research priorities, not just a risk register?"
- **Systems/ML:** "Give me severity, occurrence, and detectability for one high-consequence use error in an autonomous engagement flow, plus the control that closes it."
- **Product:** "How do you keep a uFMEA from becoming a compliance ritual that slows every release by two weeks?"
- **Design:** "Which use-error modes are best mitigated by physical layout and control placement rather than by another confirmation dialog?"

### Model answer (~205 words / 82s)

**Claim.** MIL-STD-1472 governs the interface — control spacing, legibility, reach, labeling. It has essentially nothing to say about a *probabilistic recommendation*. That's the gap: the standard protects you from a mislabeled switch, not from a well-labeled switch attached to an inference the operator can't evaluate.

**Method.** I decompose the authorization sequence into use steps — detect, assess, authorize, intervene — and enumerate foreseeable use errors at each, including the omission errors, which teams routinely skip. Then severity, occurrence, and detectability. The critical discipline is that detectability in a *use*-FMEA means whether the operator or the system can catch the error before consequence — not whether a test catches it in the lab. Under uncertain confidence, the highest-severity mode is almost always the same one: authorizing a low-confidence recommendation at the same speed as a high-confidence one, with no independent path to catch it.

**Evidence and limits.** At NASA Langley I applied uFMEA to Lunar Gateway clinical workstations against NASA-STD-3001 and MIL-STD-1472. We reduced operator task time 30% and eliminated critical input errors. The honest read on that result: speed was a by-product. The errors were eliminated by physical layout and control-display redesign — separating controls whose consequence classes differed — not by making anything faster.

**Line.** My stop-ship criterion is a catastrophic-severity use error with no independent detection path before consequence. That's the one I escalate rather than document.

**Turn.** If field data shows my predicted top mode never occurs and an unmodeled one dominates, the analysis was mis-scoped and I redo the decomposition, not the ratings.

### Follow-ups

**F1 — "MIL-STD-1472 gives guidance, not product truth. Where would you deviate, and what evidence justifies the deviation?"** *(~75 words)*

> I'd deviate where the standard's assumption doesn't hold — it largely assumes deterministic system state, so its guidance on feedback and labeling under-specifies what to do with a confidence value. The justification has to be empirical and narrow: a test showing the deviation reduces the specific use error the clause was protecting against, plus a written rationale in the design record. A deviation without a documented rationale isn't engineering judgment, it's drift.

**F2 — "Your NASA work cut task time 30%. Was speed the safety metric, or did something else actually eliminate the critical errors?"** *(~60 words)*

> Something else. Speed was the visible number, but the error elimination came from physical layout and control-display changes — putting distance and dissimilarity between controls whose consequences differed. That's the lesson I carry into this domain: in safety-critical work, task time is a usability metric and use-error mode elimination is the safety metric. Conflating them is how teams optimize themselves into an incident.

**F3 — "What is your stop-ship criterion, and who at Anduril would you expect to overrule it?"** *(~70 words)*

> Criterion: a catastrophic-severity use error with no independent detection path before consequence. On who overrules — I don't know how authority is structured here and I won't pretend to. What I'd want is the thing agreed *before* the incident: a named risk-acceptance owner, in writing, at a level with the authority to take that risk. My job is to make the risk legible and the acceptance explicit, not to be the last word.

### Senior → Lead/Staff

- **Senior:** applies the standard correctly.
- **Lead/Staff:** decides where the standard is wrong for this system, and defines the evidence and escalation threshold governing the deviation.
- **Say this:** *"Standards compliance is table stakes. The Staff-level question is where the standard is silent, and who agreed in advance what we do there."*

---

## TQ05 — Non-Deterministic Autonomy & Trust Calibration

**Arc:** opening, pushback, leadership · **Structure:** CMELT · **Target:** ~85s

> **Base:** What is the failure mode when the autonomy is correct but the operator's trust calibration is wrong, and how would you detect it before an incident?

**Persona variants**

- **Kim:** "How do you measure trust calibration rather than trust, and what would over-trust look like in the telemetry before it looks like an incident?"
- **Systems/ML:** "The model changes after deployment. Which parts of your Human Factors validation must run again, and what signals must stay observable in production?"
- **Product:** "What would you measure after launch to decide whether to keep, remove, or increase a confirmation step?"
- **Design:** "How should the interface expose model uncertainty so an operator neither rubber-stamps nor second-guesses every recommendation?"

### Model answer (~200 words / 80s)

**Claim.** The dangerous state is a system that is right and an operator who is right for the wrong reason. Nothing fails visibly, so the organization banks confidence it hasn't earned — and the miscalibration is only revealed by the first case the system gets wrong.

**Method.** Trust is a rating; calibration is a relationship. I measure operator agreement *conditioned on* system correctness and on displayed confidence, which gives four cells: correct-accept, correct-reject, incorrect-reject, and incorrect-accept. The last one is the one that kills people, and its leading indicator is available long before it occurs — acceptance rate going flat across the system's own confidence bands, and decision latency collapsing toward zero on low-confidence items. An operator who takes the same 400 milliseconds on a 0.5-confidence track as on a 0.95 track is no longer evaluating.

**Evidence and limits.** Calibration is one of the four dimensions in *Principles for Agentic Trust*, accepted to CSCW 2026, and it's the one I argue fails first. My empirical grounding for handover and trust is the Mercedes L2/L3 work — 24% improvement in safety and trust ratings. The limit is that those were drivers with no adversary; what transfers is the mechanism of preparing a disengaged operator before transfer, not the numbers.

**Line.** Two concrete requirements. Production must log recommendation, displayed confidence, operator decision, latency, and outcome, so calibration is computable without a study. And any model change that shifts the confidence distribution triggers revalidation — the interface didn't change, but the human-system pair did.

**Turn.** If acceptance already tracks confidence cleanly and errors are dominated by system error rather than operator concurrence, I'm emphasizing the wrong problem.

### Follow-ups

**F1 — "Distinguish automation bias from complacency in your data. What separates them operationally?"** *(~70 words)*

> Automation bias is an error of commission: the operator acts on a recommendation that the available evidence contradicts. Complacency is an error of omission: the operator stops sampling the sources that would have caught it. They separate cleanly in the data — bias shows in the decision record, complacency shows in the monitoring record. Eye movement or interaction telemetry catches one; the authorization log catches the other. Different failures, different countermeasures.

**F2 — "What breaks when communications degrade, telemetry goes stale, or the operator is handling several simultaneous threats?"** *(~75 words)*

> Confidence itself becomes untrustworthy first, and that's the subtle one — a stale input can produce a *high*-confidence recommendation. So the display has to distinguish system confidence from input freshness, and treat staleness as a first-class state rather than a silent degradation. Under multi-threat saturation, the failure is serialization: any control that forces sequential handling turns a parallel problem into a queue. That's exactly where I'd expect friction to become harmful.

**F3 — "Your automotive handover evidence came from drivers, not warfighters. What transfers, and what absolutely does not?"** *(~80 words)*

> What transfers is the mechanism: a handover is a time-bounded transfer of situation awareness and control, not a notification, and multimodal pre-alerting reduces the re-orientation cost. That's a property of human attention. What does not transfer: the timelines, the trained-population baseline, the absence of an adversary, and the consequence structure. A driver's failure mode is a crash they're also inside of. I'd treat every automotive number as a hypothesis to re-test here, and I'd say so before anyone asked.

### Senior → Lead/Staff

- **Senior:** names automation bias and proposes a study.
- **Lead/Staff:** defines the observable production signal, the revalidation trigger after model change, and the control that survives degraded operations.
- **Say this:** *"I'd rather ship one logged field — displayed confidence next to operator decision — than run three studies. That field makes calibration measurable forever."*

---

## TQ06 — Operator Workflow & Interaction Architecture

**Arc:** opening, leadership · **Structure:** CMELT · **Target:** ~80s

> **Base:** Map an operator's attention across detection, assessment, authorization, and intervention. Where does a dense 3D C2 interface compete with the mission?

**Persona variants**

- **Kim:** "What research would you run first to model the operator's end-to-end workflow, and what artifact would outlive the study?"
- **Systems/ML:** "Which workflow states must the system expose as discrete, testable modes so we can verify the operator always knows who is in control?"
- **Product:** "Which single stage of that operator workflow would you fix first for the largest operational return, and why that one?"
- **Design:** "When does reducing information density hide the uncertainty the operator actually needs to see?"

### Model answer (~195 words / 78s)

**Claim.** Attention is the scarce resource, and it is most expensive at the *transitions* between stages, not inside them. Dense interfaces don't usually fail by showing too much; they fail by making the transition — from monitoring to deciding, from supervising to intervening — indistinguishable from steady state.

**Method.** I map each of the four stages against three questions: what must the operator know, what must they decide, and what must they physically do. Then I mark every point where authority moves between human and system. Those authority transitions are the design surface. The rule I apply: every one of them must be a discrete, observable state — the operator should never have to *infer* who is in control, because inference under load is where mode errors come from.

**Evidence and limits.** At Uber I ran urban field studies of mobile HMI and complex spatial navigation under live traffic and time pressure, contributing to a 5% retention increase; the finding I carry is that information density has to scale down during high-stress maneuvers or it produces visual overload. At Amazon I built multimodal interaction architecture — captured in patent US-12532040-B1 — and shaped strategy for a portfolio reaching 75M+ customers. The limit: neither population was operating under adversarial time pressure, and a 3D C2 display has spatial-reasoning demands neither of those studies touched.

**Line.** The output isn't a screen critique — it's a workflow model with named authority states that every downstream interaction has to be consistent with.

**Turn.** If operators tell me the binding constraint is upstream — getting the data at all, rather than interpreting it — I've scoped the problem wrong.

### Follow-ups

**F1 — "You found that density must scale down under stress. What triggers the scale-down, and who authorizes it?"** *(~75 words)*

> The trigger has to be a system-observable state — tempo, track count, time-to-intercept — not an inference about the operator's mental state, because we can't measure that reliably in the field. And the operator has to be able to see that the change happened and override it. An interface that silently reconfigures itself under load is a new mode error, not a solution. Adaptive by rule, visible by default, reversible by the operator.

**F2 — "Several autonomous agents demand attention at once. How do you preserve situation awareness without serializing the operator?"** *(~75 words)*

> You separate what must be attended from what must merely be *auditable*. Most agent activity needs a reviewable trace, not real-time attention. So the design job is aggregation with an escalation rule: agents report into a shared state the operator samples, and only cross into interruption when they hit a defined boundary — irreversibility, or disagreement between agents. Disagreement is the underrated trigger. Two agents conflicting is exactly when a human should be pulled in.

**F3 — "What belongs visually, what belongs auditorily, and what belongs haptically in a loud, gloved, high-tempo environment?"** *(~80 words)*

> Visual carries spatial and relational information — where, relative to what — because nothing else does that well. Auditory carries onset and urgency, and it's the channel that works when the eyes are committed elsewhere, but it degrades fast in noise and hearing protection. Haptic carries confirmation and alerting to a specific person, and it survives noise and gloves, but its bandwidth is tiny — it's a tap, not a sentence. My allocation rule is: what is the operator's most likely posture at that moment, and which channel is still free?

### Senior → Lead/Staff

- **Senior:** improves a screen with good evidence.
- **Lead/Staff:** produces a reusable workflow model or service blueprint that constrains every downstream interaction decision.
- **Say this:** *"The deliverable I'd defend is the authority-state map. Once the team agrees on the states, most screen arguments resolve themselves without me in the room."*

---

## TQ07 — Hardware Ergonomics & Physical-Digital Integration

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~80s

> **Base:** Before touching screen design, what physical and anthropometric constraints would you investigate for a fielded Air Defense operator station?

**Persona variants**

- **Kim:** "How do you generate physical-ergonomic evidence fast enough to influence hardware before the industrial design freezes?"
- **Systems/ML:** "Turn a reach envelope or anthropometric finding into a hardware requirement with a pass/fail acceptance test."
- **Product:** "Hardware changes are expensive and late changes are worse. How do you time ergonomic research so it is cheap to act on?"
- **Design:** "Where do physical constraints — gloves, vibration, sunlight, body armor, seated reach — override an otherwise clean interaction pattern?"

### Model answer (~195 words / 78s)

**Claim.** Physical constraints are the boundary conditions on every interaction decision, and they're the only ones you genuinely cannot patch later. So they get investigated first — not because they're more important, but because their cost curve is the steepest.

**Method.** Five things, in order. Reach and clearance in the *actual* posture with *actual* encumbrance — gloves, armor, vest, headset, restrained or standing, whichever is real. Anthropometric range using clothed and encumbered dimensions, not nude tables, which is where most reach specs quietly go wrong. Display legibility across the real luminance range, including night adaptation and vibration. Control discriminability by touch alone, because a gloved operator with eyes on the display is identifying controls by shape and location, not by label. And emergency access and egress, which is a use-error surface people forget is an ergonomics problem.

**Evidence and limits.** At Sling I define physical ergonomics, reach-envelope modeling, anatomical safety, and mechanical fit specifications. At NASA Langley I redesigned physical layouts and control displays for Lunar Gateway clinical workstations against NASA-STD-3001 and MIL-STD-1472, cutting task time 30% and eliminating critical input errors. The limit: simulated microgravity and consumer hardware are both different constraint sets from a fielded ground station. What ports is the method — encumbered anthropometry, mock-up-first, layout as a safety control.

**Line.** The output is a hardware requirement with a pass/fail test, not a report — for example, all primary controls actuable without torso translation across the specified encumbered anthropometric range, verified on a physical mock-up.

**Turn.** If the operators' real posture differs from the assumed one — they stand, or work from a vehicle — the envelope is wrong and everything built on it is wrong.

### Follow-ups

**F1 — "Which anthropometric percentile range did you design to, and what happens to the operators outside it?"** *(~70 words)*

> I design to a stated encumbered range — typically bounded so that reach is set by the smaller end and clearance by the larger — and I write down explicitly who falls outside. The mistake I actively avoid is the 50th-percentile composite operator, who doesn't exist: nobody is median on every dimension simultaneously. Anyone outside the range becomes a documented accommodation decision — adjustability, or a named residual risk — not a silent omission.

**F2 — "What use error did you catch through physical mock-up that no software prototype would have surfaced?"** *(~65 words)*

> The class that only exists in three dimensions: controls with different consequence classes that were adjacent and tactilely similar, so a gloved hand could actuate the wrong one without visual confirmation. On a screen prototype that's invisible — the cursor always goes where you intend. That's the NASA lesson I keep coming back to: separation and dissimilarity in physical space eliminated errors that no additional confirmation dialog would have caught.

**F3 — "How do you validate mechanical fit and anatomical safety without a full production unit?"** *(~75 words)*

> Layered fidelity. Digital human modeling with encumbered anthropometry to bound the envelope, then dimensionally accurate physical mock-ups — foam and printed parts get you real reach, clearance, and pinch-point findings without electronics. Anatomical safety questions like pinch points, sharp geometry, and sustained-posture load are answerable on a non-functional model. What you cannot get is anything thermal, vibrational, or duration-dependent. I'd scope those to the first functional article and say so up front rather than over-claim the mock-up.

### Senior → Lead/Staff

- **Senior:** runs an ergonomic evaluation when asked.
- **Lead/Staff:** writes the hard hardware specification and the acceptance test hardware engineering must pass.
- **Say this:** *"I don't want to review the enclosure. I want the encumbered reach criterion to be a requirement the mechanical team designs against from the start."*

---

## TQ08 — Quantitative Methods & Analysis

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~80s

> **Base:** Walk me through how you would use scaled surveys, max-diff, and your own analysis code to prioritize competing Air Defense operator needs.

**Persona variants**

- **Kim:** "With a small, hard-to-reach operator population, how do you keep a scaled survey or max-diff study statistically honest?"
- **Systems/ML:** "What sample size and effect size would you accept before I change a threshold in the system on your say-so?"
- **Product:** "How do you get a defensible prioritization signal out of a dozen operators in under two weeks?"
- **Design:** "How would max-diff results actually arbitrate between two competing interaction concepts without flattening the qualitative evidence?"

### Model answer (~200 words / 80s)

**Claim.** With a small, hard-to-reach population the honest move is to change the estimand, not to fake the power. I'm not trying to estimate a population parameter from twelve operators — I'm trying to recover a stable *preference structure*, and that's a question small samples can actually answer.

**Method.** Max-diff earns its place here for a structural reason: each respondent contributes many forced comparisons, so the information per participant is high even when participant count is low. I'd fit individual-level utilities hierarchically and report intervals, never a clean ranked list — a rank order with overlapping intervals is a false precision that will get quoted back at me for two years. Rating scales I use sparingly, because with a small expert population they compress toward the top and stop discriminating. And I pre-commit the decision rule before data collection: which result leads to which action.

**Evidence and limits.** My quantitative background is psychophysics — which is exactly the small-n, many-trials tradition — plus signal processing on fMRI, ECG, and telemetry data at Brigham and Women's, and formative and summative testing throughout. The limit is that max-diff tells me what operators trade off among the items *I chose*. It is completely blind to the thing I failed to put on the list, which is why it never runs without prior qualitative work.

**Line.** The bar I'd hold: prioritization-grade evidence can rank a backlog; only threshold-grade evidence can move a number in the system. Different questions, different bars, stated in advance.

**Turn.** If the top-ranked items don't survive a behavioral check in a realistic task, item framing drove the result and the ranking is an artifact.

### Follow-ups

**F1 — "State your power analysis assumptions. What effect size were you willing to miss?"** *(~70 words)*

> The assumption I make explicit is the smallest effect worth acting on — below which I wouldn't change anything anyway, so failing to detect it costs nothing. With a small operator pool, a within-subjects design and repeated trials per participant is how I recover power; between-subjects is usually unaffordable. And I state the miss up front: at this n, a small effect is invisible to me, so a null is not evidence of absence and I won't let it be quoted as one.

**F2 — "Where does max-diff mislead you, and what qualitative evidence do you pair with it?"** *(~70 words)*

> It misleads in three ways: it's blind to items you didn't list, it forces trade-offs operators would never actually face together, and it flattens the fact that a low-ranked item may be low-frequency and catastrophic. I pair it with contextual observation and critical-incident interviews — the qualitative work generates the item set going in, and explains the surprising rank orders coming out. Ranking without the *why* is how a team optimizes a real preference into a wrong roadmap.

**F3 — "Which analysis did you write code for, and what would break if someone else re-ran it?"** *(~70 words)*

> My analysis work has run from psychophysical threshold fitting to physiological signal processing on fMRI, ECG, and telemetry. The honest answer to what breaks: the preprocessing decisions. Filtering, artifact rejection, exclusion criteria — those are where reproducibility dies, because they're usually in someone's head rather than in the script. My standard is that the exclusion rule and the preprocessing chain live in the code with the raw data preserved, so a re-run is a re-run and not an approximation.

### Senior → Lead/Staff

- **Senior:** runs the analysis competently.
- **Lead/Staff:** defines the evidentiary bar the organization uses to accept a quantitative claim, and makes the pipeline reproducible by someone else.
- **Say this:** *"The thing I'd want to install isn't a method, it's a two-tier evidence bar — what's good enough to rank work versus what's good enough to change a system threshold. Most arguments I've seen are teams using one where they needed the other."*

---

## TQ09 — Field Craft, Facilitation & Service Blueprints

**Arc:** opening, pushback · **Structure:** CMELT · **Target:** ~80s

> **Base:** Design the first two weeks of rapid in-field ethnography with Air Defense operators. What do you run, and what artifact comes out?

**Persona variants**

- **Kim:** "Lay out a two-week rapid ethnography and contextual inquiry plan with operators, including how you protect validity under field constraints."
- **Systems/ML:** "Field observation produces stories. What is your protocol for converting them into requirements engineering can implement and verify?"
- **Product:** "You have one trip and limited operator access. What do you observe, what do you skip, and what decision does the trip unblock?"
- **Design:** "How would you facilitate a co-creation workshop with operators and engineers without letting the loudest participant design the system?"

### Model answer (~200 words / 80s)

**Claim.** Two weeks buys exactly one thing reliably: the true task sequence and where it breaks. I would not spend that access collecting opinions about features — opinions are cheap to get later and expensive to get right in the field.

**Method.** Week one is observation-first contextual inquiry. I shadow complete cycles including the parts teams skip — shift handoff, degraded operation, and dead time, because dead time is where vigilance failures are built. I anchor every interview to an artifact or a real event rather than a hypothetical, and I use retrospective decision probing on specific past incidents: what did you notice, what did you consider, what would have changed your call. Week two is targeted re-observation on the breakdowns I found, plus a validation session where I show operators my model of their work and let them correct it. Being wrong in front of them is the fastest credibility I know of.

**Evidence and limits.** At Uber I ran urban field studies in live driving conditions rather than in a lab; at NASA I validated workstations in simulated microgravity; at Mercedes I ran high-fidelity simulator studies of L2/L3 handovers. The limit is that none of those populations faced an adversary, and I have not done this with military operators. What transfers is field method under uncontrolled conditions, not domain familiarity.

**Line.** The artifact is a service blueprint with the operator's frontstage actions, the system and autonomy behavior backstage, and the failure and recovery lanes — plus a delta list of requirements it implies, each traceable to an observation.

**Turn.** If the breakdowns I find are training artifacts rather than design ones, I'm solving the wrong problem and I redirect the second week.

### Follow-ups

**F1 — "How do you cut through operator bravado or recall bias to get the true failure sequence?"** *(~80 words)*

> Three moves. I ask about the most recent instance, not the typical one — "typical" is where reconstruction lives. I anchor to artifacts: logs, screens, the physical station, walk me through what you actually touched. And I ask about near misses and workarounds rather than errors, because a workaround is something people are proud of and will show you, and every workaround is a design defect with a human patch on it. Bravado is not an obstacle to that question; it's the engine of it.

**F2 — "What does your service blueprint capture that a journey map does not, and who consumes it downstream?"** *(~70 words)*

> A journey map is the operator's experience. A blueprint adds the backstage — what the system, the autonomy, and other people are doing at each step, and the lines of visibility and interaction between them. That's what makes it useful to engineering: it exposes where a frontstage failure is caused by an invisible backstage state. Design consumes the frontstage lane, engineering consumes the backstage lane and the failure paths, and product uses it to see sequencing.

**F3 — "How do you run discovery and co-creation workshops when participants have unequal rank in the room?"** *(~75 words)*

> Structurally, not socially — you can't personality your way out of a rank problem. Individual silent generation before any discussion, so junior input exists on paper before anyone senior speaks. Contributions captured without attribution during clustering. And where the gap is severe, I run separate sessions and reconcile the outputs myself rather than pretend a mixed-rank room is a level one. Then the senior participant gets to react to a synthesis instead of shaping it in real time.

### Senior → Lead/Staff

- **Senior:** collects excellent field data.
- **Lead/Staff:** leaves behind a blueprint, protocol, or facilitation standard the team reuses without them.
- **Say this:** *"The trip is not the deliverable. The protocol is — so the next person who gets operator access, whether or not it's me, comes back with data that composes with mine."*

---

## TQ10 — Research Operations, Repositories & Storytelling

**Arc:** leadership · **Structure:** CMELT · **Target:** ~80s

> **Base:** How would you operationalize Air Defense research so insights are found, reused, and actually change decisions across Anduril?

**Persona variants**

- **Kim:** "What operating system would you build for Air Defense research — repository, standards, intake, and quality bar — so it survives after you leave?"
- **Systems/ML:** "How do you make Human Factors findings traceable into requirements and verification artifacts engineering already uses?"
- **Product:** "How would you build research operations that stop three product teams from repeating the same low-value study?"
- **Design:** "How do you connect insights, blueprints, and design patterns so operator knowledge compounds across Air Defense products?"

### Model answer (~195 words / 78s)

**Claim.** Research doesn't fail because insights are unfindable. It fails because insights aren't attached to a decision with an owner. So I'd index the repository by *decision*, not by study — a study nobody can trace to a decision is inventory, not evidence.

**Method.** Four components, and only four, because a heavy system dies. An intake that's one page: what decision, whose decision, by when, and what evidence tier it needs. Explicit evidence tiers, so the organization can consciously buy a fast answer or a rigorous one. A decision-indexed repository where the unit of record is "this call was made, here's what it rested on, here's what would reopen it." And a traceability link out — findings referenced inside engineering's own requirement and verification artifacts, because a finding that lives only in my system will be read by my team and nobody else.

**Evidence and limits.** At Sling I lead organizational Human Factors strategy across software, hardware, and AI platforms, and I authored *Principles for Agentic Trust* as a reusable audit framework rather than a one-off study — it was accepted to CSCW 2026. At Amazon my perceptual-threshold work outlived the studies because it became how latency targets were set. The limit: I don't know this organization's tooling or constraints, so I'd expect the first version of this to be shaped by what already exists here rather than imported wholesale.

**Line.** The measurable test is that a team about to commission a study can find in minutes whether the question is already answered, and if it is, they don't run it.

**Turn.** If teams keep re-running the same study anyway, the failure is intake, not search — and I'd fix intake rather than buy a better repository.

### Follow-ups

**F1 — "Storytelling aligns people once. What mechanism makes the insight stick after the room empties?"** *(~70 words)*

> A story changes a mind; a threshold changes a default. The mechanism is converting the insight into something that has to be cleared — an acceptance criterion, a review checkpoint, a required field, a spec value. That's the difference between my Amazon latency work and a well-received deck: afterward, anyone proposing a target had to state a percentile and a modality. Nobody had to remember my presentation for that to keep working.

**F2 — "What is the single artifact you would ship in your first 90 days, and who is forced to use it?"** *(~70 words)*

> The operator authority-state map and blueprint for one core Air Defense workflow — who is in control at each step, what the system is doing behind it, and where control transfers. It's forced on nobody by mandate; it's used because design needs it to be consistent, engineering needs it to enumerate modes, and product needs it to sequence. If it isn't being used at day 120, that's my signal it was the wrong artifact, and I'd say so.

**F3 — "How do you run research operations when some findings cannot be written down in a shared repository?"** *(~75 words)*

> Two-tier synthesis. The generalizable pattern — the human-factors principle, the failure mode class — is usually expressible at the lower level, and lives in the shared repository. The specific instance stays where it belongs, with a pointer that says a substantiating instance exists and who to talk to. That's the part people skip, and it's what prevents a team from concluding no evidence exists. I've worked under IRB and federal research constraints; the handling discipline is familiar, and I'd take direction here rather than assume.

### Senior → Lead/Staff

- **Senior:** documents studies thoroughly.
- **Lead/Staff:** defines intake, repository structure, quality bar, and the cross-functional workflow that makes evidence unavoidable in decisions.
- **Say this:** *"My test for a research function is simple: can a decision be made here without the evidence being visible? If yes, the function isn't operating yet, no matter how good the studies are."*

---

## Track drill sheet

| ID | Pillar | Hardest follow-up | Your weakest beat |
|---|---|---|---|
| TQ01 | Thesis & falsifiability | F2 — the specific falsifier | |
| TQ02 | Psychophysics → spec | F3 — fallback spec | |
| TQ03 | Measure selection | F2 — arousal confound | |
| TQ04 | uFMEA & MIL-STD | F3 — who overrules you | |
| TQ05 | Trust calibration | F3 — what doesn't transfer | |
| TQ06 | Workflow architecture | F3 — modality allocation | |
| TQ07 | Hardware ergonomics | F1 — percentile & exclusion | |
| TQ08 | Quant methods | F1 — power assumptions | |
| TQ09 | Field craft | F1 — bravado & recall bias | |
| TQ10 | ResearchOps | F1 — the sticking mechanism | |

**Three sentences that carry this entire track.** If you land these three, the technical bar is met before the follow-ups start.

1. *"The goal isn't the fastest interaction, it's the best-authorized one."*
2. *"That's resume-canonical; this next part is my thesis and I haven't deployed it."*
3. *"The durable output wasn't the finding, it was the criterion the team now has to clear."*


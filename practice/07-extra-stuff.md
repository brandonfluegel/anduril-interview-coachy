# 07 — Extra Stuff Track (EX01–EX07)

The seven answers that sit outside the four question banks and the two case studies: your patent framing, the physiological measurement toolkit, the NASA-TLX tradeoff, the Mercedes handover protocol, MaxDiff, your Python stack, and AI in your own workflow. None of these will be the main question. All of them are follow-up ground, and a thin answer here costs Credibility on a case you already landed.

**Targets:** main answer **150–200 words ≈ 60–80s**. Follow-ups 45–90 words. These are method answers, so they run on **Structure B** — claim, how you'd know, evidence and where it stops, the decision it drives, what would change your mind.

> ⚠️ **Two boundaries this track must not cross.** The Mercedes protocol details and the named trust scale in EX04 are *reconstructions*, not records — confirm them against your own memory or drop to the generic phrasing given there. And per `references/`, the fNIRS work is described as **converging** with subjective ratings. Never claim a head-to-head win over NASA-TLX, and never name the commercial interfaces compared.

---

## EX01 — The Patent: Multimodal Interaction in Non-Deterministic Contexts

**Arc:** technical core, or volunteered as the differentiator · **Target:** 70–80s

> **Base:** Tell me about your patent.

### Model answer (~190 words / 75s)

> US-12532040-B1 covers control inputs resolved against system context: the same physical actuation maps to a *different* control input depending on which interface is presented and where the user sits inside it. It's public, so I can go as deep as you want.
>
> The reason that's a hard human factors problem is that the action-to-effect mapping is no longer fixed at design time — it's resolved at runtime. The user can't lean on a memorized motor program; they have to hold a live model of system state. Three things have to be true for that to be safe: the current context has to be perceptible *before* the user commits, the input has to be reversible or confirmable when the stakes are high, and the mapping has to be predictable enough that people build a correct mental model instead of a superstitious one.
>
> I'd be precise about the word non-deterministic, though. The patent covers context-*dependent* mapping, which is still deterministic given state — it's the deterministic cousin of the agentic case. Genuinely stochastic systems are harder, and that gap is what my Principles for Agentic Trust work is aimed at.

### The Anduril bridge — say this unprompted if the room is engineering-heavy

> An autonomous system is the same class of problem at higher consequence. An operator's action means something different depending on autonomy mode, engagement state, and what the system currently believes about the world. That's the direct lineage into Calibrated Cognitive Friction: the checkpoint isn't there to slow anyone down, it's there to make context legible at the exact moment the mapping changes.

### Senior → Lead/Staff

- **Senior:** describes the claim and the product it shipped in.
- **Lead/Staff:** states the general problem class the claim belongs to, then *volunteers the limit of their own framing* — the deterministic/stochastic distinction. Drawing that line yourself is precision. Getting caught on it is overclaiming, and it is the single likeliest place you get caught in this track.

---

## EX02 — The Physiological Toolkit: fNIRS, GSR, HRV

**Arc:** method depth after any cognitive-load claim · **Target:** 60–75s, then let them pick one

### What each one actually measures — say it this plainly

| Measure | Plain mechanism | What it licenses you to claim |
|---|---|---|
| **fNIRS** | Light through the forehead reads how much oxygen the front of the brain is using. Harder thinking, more oxygen. | Continuous cortical effort the person can't self-report. |
| **GSR / EDA** | Two finger electrodes read micro-changes in sweat driven by the fight-or-flight system. | *Something spiked* — arousal, surprise, alarm. Not whether it was good or bad. |
| **HRV** | The gap between heartbeats. Relaxed people vary a lot; strained people get metronomic. | Sustained strain across minutes, not moments. |

### Setup, in one line each

- **fNIRS** — a headband of emitters and sensors about an inch apart across the forehead. Clean scalp contact, a still head, and a marker signal so you know exactly when each task began.
- **GSR** — two electrodes on two fingers, and you let them sit five to ten minutes before recording because the signal drifts until the skin settles. Stable room temperature, still hand.
- **HRV** — chest electrodes if you want accuracy, a wrist or finger optical sensor if you want convenience. Minutes per condition, not seconds.

### The analysis, without the jargon

> For all three, the raw signal is mostly garbage until it's cleaned — motion, blinking, breathing and postural shifts all masquerade as real responses, so artifact handling comes before anything else. Then you compare the task period against that same person's quiet baseline. For fNIRS you're looking for oxygen rising in the front of the brain during the hard condition, and the credible version has both blood signals moving in opposite directions together; if only one moves, it's probably scalp blood flow and not brain. For GSR you count how many spikes occurred and how large they were, remembering the response lags the event by a few seconds. For HRV you compute how much beat-to-beat variation there was, and less variation in the hard condition is the expected pattern.

### The five things that separate a practitioner from someone who read a paper

1. **These are relative, never absolute.** There is no "workload = 62." Everything is this person, this condition, against this person, that condition. Within-subject, counterbalanced, or it means nothing.
2. **Timing is the whole ballgame.** If the physiology clock and the task clock drift apart, the study is dead. One synchronized clock, hardware event markers.
3. **They measure a proxy, not the construct.** GSR says *aroused*, not *overloaded*. HRV says *strained*, not *confused*. Workload is an inference from the pattern plus the design.
4. **Some people simply don't respond.** Roughly one in ten produces almost no GSR response. Size the sample knowing you'll discard data.
5. **Never run physiology alone.** Pair it with behavior — task time, errors, gaze. When physiology and self-report disagree, behavior arbitrates. That disagreement is frequently the finding.

---

## EX03 — NASA-TLX vs. Your Objective Measures

**Arc:** the near-certain follow-up to any workload claim · **Target:** 60–70s

> **Base:** You've used both self-report and neuroimaging for workload. Which do you trust?

### Model answer (~175 words / 70s)

> I don't rank them, I use them as converging measures, because they fail in opposite directions.
>
> TLX is decades-validated, costs nothing, runs in the field, and its six subscales tell you *which kind* of load you're looking at — mental, temporal, effort, frustration. It's also the common language: an engineering audience accepts it without me having to defend the method first.
>
> Where it breaks is equally clear. It's retrospective, so it collapses a whole task into one memory-biased number and can't tell you when the load spiked. It saturates near the ceiling — an overloaded operator rates 85 whether the true demand is 85 or 140. And it can't detect load the operator isn't aware of, which is exactly the automation-bias case.
>
> So the rule I actually apply is: TLX for breadth and comparability, physiology when the design decision hinges on *when* the load occurred, or when I have reason to think self-report will be wrong. At Amazon the prefrontal activation differences converged with the subjective complexity ratings — and the convergence is what made either one usable.

**F1 — "So the neuroimaging beat the questionnaire?"** *(~55 words)*

> No, and I'd resist that framing. What I have is convergence, not a head-to-head — I didn't run the study that would license the stronger claim. The value was that two independent methods pointed the same way, plus gaze evidence of layout regions nobody was looking at, which neither method alone would have surfaced.

---

## EX04 — Mercedes L2/L3 Handover: Method and Trust Measurement

**Arc:** the automation-handover probe · **Target:** 70–80s

> ⚠️ **Reconstruction, not record.** Confirm the specifics below before you say them. If you can't, use the safe phrasing given at the end of each block — it's accurate and defensible without inventing a citation.

### The design

> Within-subjects, high-fidelity simulator, alert modality as the primary factor — auditory only, haptic only, multimodal combined, against a visual-only baseline — counterbalanced by Latin square. Drivers were occupied with a standardized non-driving task, an n-back or a tablet visual search, precisely so they were genuinely out of the loop when the takeover request fired. That's not a detail; if the driver is still monitoring, you're not studying a handover.

### The protocol beats

> Consent and brief, then about ten minutes of familiarization driving to stabilize behavior and cut simulator-sickness dropouts. Then automated highway driving with takeover requests at unpredictable intervals against scripted hazards — stopped vehicle, lane obstruction, a sensor-degradation event. The key manipulation is the time budget: roughly four to seven seconds of lead time, with the short budget as the stress condition.

### The measures

- **Takeover latency, decomposed** — hands-on-wheel, eyes-on-road, first control input. The decomposition is the point; a single reaction time hides which stage failed.
- **Takeover quality** — lateral deviation, minimum time-to-collision, brake and steer magnitude, collisions.
- **Biometrics** as the continuous load channel across the whole drive.

### Trust — the honest answer

> The field standard is a validated multi-item trust-in-automation scale, administered at baseline and after each modality block. **[Confirm before saying: Jian, Bisantz & Drury (2000), 12 items, 7-point — or Körber (2018) if that's what you used.]** If you cannot confirm which, say exactly this: *"a validated multi-item trust-in-automation scale, pre and post block."* Accurate, defensible, no fabricated citation.

### The move that upgrades this answer

> Self-reported trust and revealed trust routinely diverge, so I'd triangulate the scale against behavior — reliance rate, time to re-engage automation after a takeover, and monitoring gaze frequency. A driver who says they trust it and then never takes their eyes off the road has told you two different things, and the eyes are the one I'd design against.

---

## EX05 — MaxDiff

**Arc:** prioritization / survey-craft probe · **Target:** 60–70s

> **Base:** How do you prioritize requirements when every stakeholder says theirs is critical?

### Model answer (~180 words / 72s)

> For that specific failure mode I'd run MaxDiff rather than a rating scale. You show people small sets of four or five items and ask for best and worst, repeated across a balanced design so every item appears about equally often. It forces genuine tradeoffs, removes scale-use bias, and gives you real discrimination instead of everything landing at 4.2 out of 5.
>
> Analysis goes in three passes. Counting — best minus worst over appearances — as the quick descriptive. Multinomial logit for aggregate utilities. Then hierarchical Bayes for individual-level utilities, which is what I actually want, because that's what lets me segment and run simulations rather than just rank a list. I rescale to zero-centered or probability scores so a program lead can read it without me in the room.
>
> The limit I'd flag before anyone asks: standard MaxDiff gives *relative* importance only. It tells you A beats B; it doesn't tell you whether A clears any absolute bar. If that question matters — and for requirements it usually does — you need anchored MaxDiff with a dual-response item.

---

## EX06 — Python and the Analysis Stack

**Arc:** research-craft probe, often from the engineering lead · **Target:** 45–60s. Do not list libraries for a minute.

### Model answer (~150 words / 60s)

> Python end to end. pandas for wrangling, statsmodels for regression and choice models, PyMC when I need hierarchical or individual-level estimates, pingouin for repeated-measures work. For the physiological pipelines it's MNE and mne-nirs for fNIRS and NeuroKit2 for ECG, HRV and EDA. Jupyter for the analysis narrative, matplotlib and seaborn for output.
>
> The part that matters more than the stack: I write the analysis plan and the power analysis *before* collection, not after. And the pipeline is scripted, so the analysis is reproducible and auditable rather than a spreadsheet somebody has to take on faith. In a safety-critical program that's not a preference — if a threshold I recommend ends up in a requirement, someone has to be able to re-run how I got there two years from now without me.

---

## EX07 — AI in Your Workflow and Your Analysis

**Arc:** near-certain, from any persona · **Target:** 70–80s · **Frame first, tools second.**

> **Base:** How are you using AI in your own research work?

### Model answer (~195 words / 78s)

> I treat AI as leverage on the slow, low-judgment parts of research and never on the inference itself. It can generate and it can process; I own what counts as evidence.
>
> Concretely: first-pass thematic coding of transcripts, with a human validation pass on a held-out sample so I can check agreement between the model and myself rather than trusting it silently. Fast scoping across MIL-STD, NASA-STD and the trust literature — then verifying every citation by hand, because models fabricate references. Analysis scaffolding and stats implementation in Python, reviewed, since a plausible-looking wrong model specification is the dangerous failure mode. Drafting candidate probe and survey wording, then cutting it hard against construct validity. And generating scenario content and edge cases for test protocols.
>
> The lines I hold: no confidential or participant-identifying data into external models. No AI-generated finding without traceability to a specific participant utterance or data point. And AI never decides whether a threshold has been met.
>
> There's a symmetry I'm aware of — I study this class of system, so I apply my own Principles for Agentic Trust to my own tooling. I want observability into what the model did, not just its output.

### The close, if you have room

> The interesting question isn't whether I use AI. It's that research velocity and research rigor are now in tension in a genuinely new way, and the discipline is knowing which steps compress and which ones are load-bearing.

### Senior → Lead/Staff

- **Senior:** lists tools and reports a productivity gain.
- **Lead/Staff:** states the division of labor as a principle, names the specific failure modes each use invites, and states the hard lines *before* being asked whether there are any.

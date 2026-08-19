# 06 — Amazon Latency Case Study (AC01–AC10)

**This is the primary case for the 45-minute hiring manager conversation with Dr. Daniella Kim.** NASA moves to second position — a 45-second module you deploy yourself, covered in AC08.

**Why this case wins with Kim.** Her scorecard is empirical rigor, research velocity judgment, thesis-setting, standards that survive your departure, and executive influence. The latency program scores on all five, you owned it, and it has enough layers to survive forty minutes of probing without hitting the floor. The role record's definition of Lead/Staff — *"bridges engineering latency with human perception... translates HSI findings into hard specifications"* — is this program restated.

**Targets:** presentation 380–420 words ≈ 2:35–2:50 · deep-dive answers 160–230 words ≈ 90s · follow-ups 45–90 words.

---

> ## Read this before anything else: the confidentiality problem
>
> You now have the source report in `references/`. It contains internal program codenames, competitor benchmarking, percentile dashboards, and an economic model output far larger than the figure on your resume.
>
> **Do not bring any of it into the room.** Kim is a Head of Research evaluating whether you will be careful with *her* data. Reciting a former employer's confidential dollar figures and competitive benchmarks is the single fastest way to fail this conversation, and it fails it silently — you will never be told that's why.
>
> **The rule:** speak in method, structure, and sanitized magnitude. Never a codename, never the competitor comparison, never the internal economic model output, never the percentile dashboards.
>
> **Say the discretion out loud, once, early.** It converts a constraint into a credibility signal:
>
> > "I'll describe the method and the thresholds in detail, and I'll keep the internal figures and the competitive benchmarking out of it — the resume number is the sanitized one and it's the one I'll use."
>
> Kim will register that. It costs you nothing and it is the cheapest trust you will buy all day.

---

## AC01 — The 3-Minute Presentation

**Arc:** opening of the hiring manager conversation · **Target:** 2:35–2:50

> **Base:** Walk me through a piece of research you led, end to end. Take about three minutes.

### The beat spine

| # | Beat | Words | Time | The one job it does |
|---|---|---|---|---|
| 1 | **Claim first** | 40–50 | ~19s | The org was optimizing the wrong variable. State it flat. |
| 2 | **Ambiguity, not setup** | 45–55 | ~21s | Nobody could say what "fast enough" meant. That's the real problem. |
| 3 | **Your charge** | 25–35 | ~13s | First person. Thresholds engineering can hold as requirements. |
| 4 | **Method + the velocity call** | 100–120 | ~46s | Psychophysics design, and the sample-size decision you defend. |
| 5 | **The finding, including the counterintuitive one** | 60–70 | ~27s | Intent-dependence, and the floor. |
| 6 | **Earned secret** | 30–40 | ~15s | Latency isn't a quantity. It's an expectation violation. |
| 7 | **Mechanism** | 55–65 | ~25s | Thresholds became spec; ~$50M attributed; the metric got renamed. Level gate. |
| 8 | **Transfer + boundary** | 40–50 | ~19s | Air Defense, and where consumer evidence stops. |

Total **~415 words ≈ 2:50**.

### Model script (~415 words / 2:50)

> **[1]** The short version is that a large engineering organization was optimizing the wrong variable, and my job turned out to be proving that. Everyone was treating response latency as a number to drive down forever. What the research established is that there is no single acceptable latency — acceptable latency is a property of *what the user asked for*, and past a certain point, faster stops helping and starts hurting.
>
> **[2]** The ambiguity was the actual problem. The guidance in use predated the current hardware generation by years, and nobody could say what "fast enough" meant for any specific interaction. So latency targets were being set by engineering feasibility and argued about in reviews, and there was no evidentiary basis to settle any of it.
>
> **[3]** My charge was to produce perceptual thresholds defensible enough that an engineering organization would hold them as requirements rather than treat them as research opinion.
>
> **[4]** I ran it as psychophysics. Thirty participants, twelve high-priority interaction types, six latency levels from 500 milliseconds to three seconds, spanning everything from human conversational pace to the slow tail of what customers actually experienced. Around two thousand trials. The instrumentation mattered: I had a Wizard-of-Oz rig on a modified device that detected utterance termination and let me set the response delay per trial with millisecond control, so latency was a manipulated variable rather than an observed one. And I used a three-point scale — not slow, somewhat slow, too slow — instead of a seven-point Likert, because people don't perceive speed. They only notice slowness. Measuring the thing customers actually experience is what made the numbers behave.
>
> **[5]** Two findings. First, thresholds are interaction-dependent, not global — anything with a physical real-world analogue, a light switch, a notepad, has to land near half a second or it feels broken, while retrieval tasks got roughly twice the budget. Second, and this is the one I didn't expect: for conversational responses I had to recommend a *floor*. Faster than human conversational latency reads as unsettling rather than responsive.
>
> **[6]** The earned secret is that latency isn't a quantity, it's an expectation violation — and "faster is better" is false at both ends of the scale.
>
> **[7]** The mechanism is what I'd point at. Two thresholds per interaction type became the acceptance criteria the org designed against — roughly fifty million dollars in projected operational value was attributed to the program — and I got the internal metric renamed, because the old name conflated the objective interval with the subjective perception and that conflation was causing bad decisions. Both the criteria and the definition outlived my involvement.
>
> **[8]** Transfer to Air Defense is direct — a threshold is a threshold. Where it stops: my population was consumers, not trained operators under load, and the consequence of a violated expectation was annoyance, not an engagement.

### What each beat is buying you

- **[1]** *Decision first* + it opens on a claim Kim can disagree with, which is what makes her lean in.
- **[2]** **Ambiguity.** This beat exists because the JD asks for someone who can "work through ambiguity." Show the problem was undefined before you defined it.
- **[4]** *Alternatives + conditions* and instrumentation depth. The three-point-scale justification is a small detail that signals real method thinking.
- **[5]** The floor is your best single moment. It is *Calibrated Cognitive Friction with data behind it* — see AC07.
- **[7]** *Reusable mechanism.* Renaming an organizational metric is a Staff-level act. Do not leave it out.
- **[8]** *Evidence hygiene.* Name the population gap before she does.

### Senior → Lead/Staff

- **Senior:** describes a well-designed study and reports thresholds.
- **Lead/Staff:** reframes what the organization was measuring, defends a velocity tradeoff explicitly, produces a counterintuitive result that changes the design philosophy, and leaves behind both a specification and a corrected metric definition.
- **Structural test:** delete beat [7]. If the answer still feels finished, you told it as a Senior.

---

## AC02 — The Deep-Dive Layers

Three minutes is the presentation. The other forty are these. **Each layer is a separate answer you should be able to give cold.** Do not volunteer them all — hold them and deploy the one that answers the question asked.

### Layer 1 — Why psychophysics rather than analytics

> The organization already had behavioral telemetry at enormous scale, and telemetry can tell you what happened after a slow response. It cannot tell you where the perceptual boundary is, because the boundary isn't in the log data — it's in the person. Psychophysics is the method built exactly for that: manipulate the stimulus systematically, capture the subjective response, find the point where the judgment flips. Analytics gives you correlation at scale; psychophysics gives you a threshold you can write into a requirement. I needed the second thing.

### Layer 2 — The sample size, and the velocity call

**This is the answer Kim is most likely to press on. Have it word-perfect.**

> Thirty participants, roughly two thousand trials, ninety percent confidence with a margin of error that ranged by interaction type. I costed the alternative: getting to a five-percent margin across every interaction type needed on the order of three hundred participants, which was six to twelve months and several hundred thousand dollars. I recommended against it, in writing. The reason is that the decision the research had to serve was "which interaction types do we prioritize, and to what target" — and the effect sizes that mattered for that decision were large. Tightening the interval would have changed the error bars and changed no decision. So the honest framing is that I bought a decision, not a publication, and I said out loud which one I was buying.

### Layer 3 — The intent-dependence finding

> The result that reorganized the program was that acceptable latency isn't a system property, it's a property of the user's intent. Anything with a physical real-world analogue — flipping a switch, jotting on a notepad — has to complete near half a second, because the customer is benchmarking against the object, not against the software. Retrieval tasks got roughly double the budget. Participants said this directly and unprompted: if it isn't faster than the physical thing, the device isn't worth using. That killed the idea of one global latency SLA and replaced it with a per-intent specification, which is a very different engineering roadmap.

### Layer 4 — The floor, and non-monotonicity

**Your most valuable thirty seconds. See AC07 for how to spend it.**

> For conversational question-answering I recommended a lower bound as well as an upper one — responses should not be faster than roughly human conversational latency, because at that point the system stops reading as responsive and starts reading as uncanny. That's the finding that made me stop believing "faster is better." The response curve isn't monotonic. There's a band, and both edges are real, and if you only ever optimize one direction you will walk off the other edge without instrumentation to tell you.

### Layer 5 — The metric rename

> The organization used a metric name that described an objective time interval but was worded as though it described the customer's perception. That sounds like pedantry. It wasn't — it meant every conversation about the metric carried an embedded assumption that objective time and perceived time were the same quantity, which is precisely the assumption my data falsified. I recommended renaming it to describe the interval it actually measured, and separating perception into its own construct with its own thresholds. Getting a metric definition changed is slower than getting a study funded, and it's worth more, because the definition constrains every future argument.

### Layer 6 — Triangulation and the evidence gate

> There was a parallel economic model estimating downstream impact of slow responses, built by a partner team. Its estimates were large enough that people privately doubted it. My research was independent of it — different method, different data, no shared assumptions — and it corroborated the core claim that customers are genuinely sensitive to these differences. That's the useful structure: an observational model and a controlled perceptual study that fail in different directions. When they agree, the agreement is informative. I'd rather have two weak methods that fail independently than one strong method with a blind spot, and that's how I'd want to build an evidence base here.

### Layer 7 — The cognitive load framework

> Separately I co-established an objective cognitive-load capability using functional near-infrared spectroscopy and eye tracking. The application I'd describe is interface evaluation: we had participants view a set of comparable interfaces while measuring prefrontal activation associated with mental effort, alongside gaze. We found activation differences between interfaces that tracked the subjective complexity and density ratings, and gaze patterns that showed which regions of a layout were systematically never looked at. The value isn't that the neural measure is better than asking. It's that it's *non-reactive* — it doesn't require the person to introspect on effort while they're expending it, and it doesn't move when you change the wording of your question.

**Boundary — say it before she asks:** you have no head-to-head result showing the neural measure outperformed the NASA Task Load Index. Never imply one. The defensible claim is convergence and non-reactivity, not superiority.

### Layer 8 — The patent

> The patent came out of a different thread: context-based control inputs. The idea is that the same physical actuation maps to different control inputs depending on what the system is currently displaying and where the user is within it — the input is interpreted against context rather than fixed at the hardware. I'd describe it as the same intellectual move as the latency work. In both cases the meaning of a signal isn't a property of the signal; it's a property of the state the system and the human are in.

---

## AC03 — Kim Follow-Ups: Rigor and Velocity

**F1 — "Thirty people. Convince me that's not just a number you could afford."** *(~85 words)*

> It's a number I chose and costed, which isn't the same thing. The design carries the power, not the headcount: within-subjects, six latency levels, twelve interaction types, about two thousand trials — every participant is their own control, which is what makes small samples defensible in psychophysics and is exactly why the method exists. And I ran the counterfactual explicitly: three hundred participants, six to twelve months, high six figures, for a tighter interval on a decision that was already unambiguous. I recommend against studies that can't change a decision.

**F2 — "What's the weakest part of that study? Not the limitation section — the part that actually worries you."** *(~90 words)*

> The controlled setting. I isolated verbal response latency and stripped out everything that co-occurs with it in the real environment — the light ring, the earcons, ambient noise, the fact that people are usually doing something else. Those aren't nuisance variables, they're probably moderators, and my thresholds are almost certainly conservative in one direction and I can't tell you which. The second worry is that I measured a judgment, not behavior. People can report a response as acceptable and still disengage from the product, and my design cannot detect that gap.

**F3 — "If you re-ran it today with no constraints, what changes?"** *(~75 words)*

> I'd add the affordances back in as manipulated factors rather than removing them, because I now think the interaction between visual feedback and perceived latency is where the remaining budget is. I'd add a secondary task, so I'm measuring under load rather than at rest — that's much closer to the operational case and it's the version relevant here. And I'd pair the subjective threshold with a behavioral one, so I'm not relying on a single response class.

**F4 — "What did you get wrong?"** *(~70 words)*

> I framed the first version of the deliverable as a single global threshold, because that's what I'd been asked for and it's what would have been easiest to adopt. The data didn't support it and I had to go back and restructure the whole recommendation around interaction type. The lesson I took is that the shape of the deliverable is a research decision — I'd pre-committed to an answer format before I knew the answer's shape.

---

## AC04 — Ambiguity and Evidence Gates

**"How do you decide what research not to do?"** *(~95 words)*

> I run three gates before anything gets scoped. One: name the decision. If I can't write the sentence "this study will determine whether we do X or Y," it isn't a study, it's curiosity, and curiosity gets a literature review and a memo instead. Two: name the threshold in advance — what result changes the decision, and in which direction. If every possible outcome leads to the same action, I've found a very expensive way to feel confident. Three: cost the precision. Most requests for a bigger sample are requests for reassurance, and reassurance is cheaper to buy other ways.

**"You arrive and nobody can tell you what the research question is. What do you do in week one?"** *(~90 words)*

> I don't start with users, I start with the arguments. I go find the decisions that are currently being settled by seniority, by intuition, or by whoever is loudest in the review — those are the places where evidence has leverage, and they're visible within days if you sit in the right meetings. The latency work came from exactly that: the tell wasn't a research request, it was that the same argument kept recurring and never resolved, because there was no evidentiary basis on which it *could* resolve. A recurring unresolved argument is a research question with the label torn off.

**"How do you handle a stakeholder who wants a study to confirm a decision they've already made?"** *(~75 words)*

> I ask what they'll do if it comes back the other way. If the honest answer is "ship anyway," I say so plainly and offer to spend the money on something that's genuinely undecided — that's a better conversation than it sounds, because most people know they're doing it. If the answer is that they'd genuinely change course, then it's a real question and I'll run it. The gate is falsifiability of the decision, not of the hypothesis.

---

## AC05 — Stakeholder Management and the Multi-Year Arc

**"Walk me through how a multi-year program actually stayed alive."** *(~120 words)*

> Sequencing, mostly. The first study was deliberately the smallest one that could settle a live argument, because the fastest way to lose a multi-year program is to ask for multi-year funding at the start. Once thresholds existed for the highest-traffic interactions, the questions the thresholds *couldn't* answer generated the next phase, and by then engineering wanted them rather than tolerated them.
>
> The partnership structure mattered as much as the method. I ran it with the performance-engineering organization and with an economics team, and I made sure the economic modeling and my perceptual data were argued together rather than competing — two teams with the same recommendation is a different political object than two teams with adjacent findings.
>
> And I wrote down what I hadn't answered. The open-questions list is what made the program look like a roadmap rather than a series of requests.

**"Engineering says your threshold is not achievable this year. Now what?"** *(~85 words)*

> Then it's a prioritization problem, not a research disagreement, and I should hand them the tools to prioritize rather than defend my number. That's why I produced two thresholds instead of one — an acceptable band and a high-satisfaction band — and ranked the interaction types by the gap between where they were and where they needed to be. That turns "you're not meeting the spec" into "here are the three places the gap costs the most." I don't win those arguments by holding the line. I win them by making the line negotiable in a structured way.

**"How do you get a research finding to survive contact with a roadmap?"** *(~80 words)*

> By not shipping it as a finding. A finding is a fact about the past that competes for attention with everything else in the review. A threshold with an acceptance test attached is an artifact that gets embedded in how the thing is built, and then it doesn't need me to advocate for it. The rename is the purest version of that — once the metric definition is right, every future argument in the org inherits the correction whether or not anyone remembers where it came from.

**"Who disagreed with you, and how did that resolve?"** *(~75 words)*

> The real disagreement wasn't about the numbers, it was about whether perceptual data should be allowed to set an engineering requirement at all — the position being that this is a feasibility question and research should describe rather than constrain. I didn't win that on argument. I won it by producing thresholds precise enough to be testable, because the moment a criterion has a pass/fail test attached it stops looking like an opinion and starts looking like a spec.

---

## AC06 — The Level Move: The Mechanisms

Kim's own stated bar is *"how would you build a research function whose standards survive after you leave?"* You have three real answers. **Pick the two that fit the question — never recite all three as a list.**

> **The specification.** "Two thresholds per interaction type, with defined pass criteria — not a recommended target, an acceptance band with a test. That's the artifact engineering designs against, and it works without me in the room."

> **The metric definition.** "I got an organizational metric renamed because its name encoded an assumption my data had falsified. That's the one I'm proudest of, and it's the least impressive-sounding. A definition constrains every argument that comes after it."

> **The measurement capability.** "The cognitive-load setup was built as a capability, not a study — an instrumented method other researchers could run on their own questions. The point was to leave behind an instrument, not a result."

### The sentence that must be said out loud

> "The thing I'd want to be judged on isn't the thresholds. It's that the org's definition of the metric changed, and it stayed changed after I left."

### And the level claim, in one sentence

> "The scope I'm arguing for is the one where I own the criteria the organization designs against — which is what I did at Amazon, and it's the difference between running excellent studies and setting the bar those studies get measured against."

---

## AC07 — The Bridge: Kim's Three Questions

> **This section changed based on `references/Human Factors Response to Autonomous System Design`.** You wrote a four-page research response to three questions Dr. Kim posed publicly at the Learners Conference in San Francisco in May 2026. That document is the strongest asset you have for this specific conversation, and the previous guidance in this repo — which told you never to reference a panelist's talk — was written before it existed. See AC09 for the narrowed rule.

**How to use it: as a research agenda, not as flattery.** Never open with "I saw your talk." Deploy it when she asks what you'd work on, what you'd want to study, or why this role.

### The pivot from the latency case into the agenda (~110 words)

> The reason I keep coming back to that floor finding is that it's the same structure as the question you posed at the Learners Conference about whether better UX on autonomous systems reduces harm or just makes harm easier to authorize. In the consumer case, the answer was empirical and slightly absurd — past a point, faster made the system worse, and we could measure exactly where. I think the defense version of that is measurable too, and it's the thing I most want to work on. I actually wrote up a response to those three questions, with hypotheses and proposed methods, because I couldn't stop thinking about the third one.

### The three, compressed — one sentence of position, one of method

| Her question | Your position | Your proposed method |
|---|---|---|
| **Responsibility gap** — who keeps humans meaningfully in the loop when deployment outruns governance? | Responsibility defaults to the builder; if the interface permits it, operators infer it's authorized. | Vignette-based cognitive walkthrough, enforced-checklist vs. discretionary interface, measuring where operators locate accountability. |
| **Friction paradox** — does better UX reduce harm or make harm easier to authorize? | Testable directly: micro-frictions should cost completion time and buy a disproportionate reduction in false-positive authorizations. | A/B simulator study under time pressure with a friction gate requiring the operator to identify the justifying evidence before approval unlocks; eye tracking on data regions versus the approve button. |
| **Moral crumple zone at scale** — is a human evaluating 50 recommendations a minute actually in the loop? | There's a recommendation-rate threshold past which operators abandon verification and default to compliance. Past it, meaningful human control is nominal regardless of interface. | Ramp recommendation rate across a session with seeded false positives; measure error-catch rate, NASA Task Load Index, and physiological arousal to locate the inflection point. |

### The single best thing you can say in this conversation (~70 words)

> The third question is the one I'd want to answer first, because it's the only one that's falsifiable with a number. If there's a recommendation rate past which operators stop catching seeded errors, that's an inflection point you can measure, and once you have it, it becomes a design constraint on how fast the system is allowed to present decisions to a human. That's the same move as the latency thresholds, in a domain where it matters.

**Why this lands:** it converts your thesis from a philosophical position into a study with a dependent variable, and it uses your consumer work as method provenance rather than as domain evidence. That is precisely the transfer argument you need to make.

### Guardrails on this material

- The hypotheses in that document are **proposed, not run.** Say "I'd predict" and "the study I'd want," never "we found."
- The specific numbers in the friction hypothesis are **predictions you wrote down**, not results. Frame them as pre-registered expectations you'd be happy to be wrong about.
- Do not claim acquaintance, correspondence, or any private exchange with Dr. Kim. The honest and sufficient claim: she posed three questions publicly, and you wrote a response.
- Do not characterize anything she said beyond those three questions.

---

## AC08 — The NASA Module (45 seconds)

**Deploy this yourself, around minute 25, before she raises it.** The objection you are pre-empting is that everything above is consumer technology with recoverable consequences.

> The obvious hole in what I've described is that nothing in it was irreversible. Let me give you the version where it was. At NASA Langley I did human-systems integration for Lunar Gateway clinical workstations in simulated microgravity — a use-error analysis against NASA-STD-3001 and MIL-STD-1472 rather than a usability study, because the failures that matter there are rare and high-consequence and won't appear in any sample you can get. Enumerate the error modes, rank by consequence rather than frequency, redesign the physical layout so the irreversible action isn't adjacent to the routine one. Task time dropped thirty percent and the critical input errors were eliminated — and the layout is what eliminated them, not the speed. I was a Ph.D. intern on that, so the analysis and the redesign recommendation are the honest claim, not the program.

**~155 words ≈ 45 seconds.** Say it and stop. If she wants more, the full material is in [05-nasa-case-study.md](practice/05-nasa-case-study.md).

**Why it works here:** it supplies safety-criticality and military-standard fluency, it pre-empts the consumer-tech objection, and volunteering the intern caveat unprompted buys more credibility than the story costs.

---

## AC09 — Evidence Boundaries for This Case

### Assert freely

- Multi-year psychophysics program at Amazon Devices replacing arbitrary engineering latency targets with human perception-derived thresholds; ~$50M in projected operational value
- Method: within-subjects psychophysics, thirty participants, twelve high-priority interaction types, six latency levels from 500ms to 3000ms, ~2,000 trials, Wizard-of-Oz instrumentation with per-trial millisecond control, three-point slowness rating scale
- Two-tier threshold structure (acceptable band and high-satisfaction band) defined per interaction type, with stated pass criteria
- Findings: thresholds are intent-dependent; interactions with physical real-world analogues require ~500ms; the response curve is non-monotonic and conversational responses need a lower bound as well as an upper one
- The sample-size counterfactual you costed and recommended against
- The organizational metric rename separating objective interval from subjective perception
- Independent corroboration between your controlled study and a partner team's economic modeling
- Cognitive-load capability using functional near-infrared spectroscopy and eye tracking; prefrontal activation differences across comparable interfaces, converging with subjective complexity and density ratings; gaze evidence of systematically unattended layout regions
- US Patent US-12532040-B1, context-based control inputs — same actuation resolving to different control inputs depending on system state and interface position; 2023 Amazon Inventor Award
- Portfolio strategy influence across product lines reaching 75M+ customers

### Never assert

- **Any internal codename, dashboard, percentile table, or competitor benchmarking result.** These are in the source report and they stay there
- **Any dollar figure or interaction-count figure other than the ~$50M on your resume.** The internal economic modeling produced much larger numbers. Do not quote them, and **do not allude to them** — no "the internal number was higher," no "I'm being conservative," no raised eyebrow. Gesturing at a bigger figure you won't name is worse than either saying it or omitting it: it reads as a brag you're pretending not to make, and it invites exactly the follow-up you can't answer
- Any head-to-head result showing near-infrared spectroscopy outperformed the NASA Task Load Index. The defensible claims are convergence and non-reactivity
- Near-infrared spectroscopy at Brigham or Harvard — that instrument belongs to Amazon
- Any Echo-specific product metric beyond portfolio strategy influence at 75M+ customers
- Any result from the three autonomous-systems hypotheses. They are proposed studies
- Any deployment or adoption of Calibrated Cognitive Friction
- Any clearance status, classified detail, or Anduril-internal process, team, headcount, or program specifics

### The magnitude question, answered once

**$50M is the only number. It is also the better number** — not a compromise you're making for confidentiality reasons. A nine-figure or ten-figure claim from a single researcher triggers disbelief and forces the interviewer to spend their next question auditing you instead of engaging with the work. $50M is large enough to establish scope and small enough to stay believable, and believable is what converts.

When she asks where the number comes from, answer with **derivation, not size** (~75 words):

> That's the operational value attributed to the program, and the modeling behind it was done by an economics team, not by me — so I'd hold it loosely and I'd rather tell you the mechanism. Latency thresholds were missing on high-traffic interactions, slow responses measurably suppressed downstream engagement, and the thresholds gave the org a place to target. The part I'd actually defend is the threshold structure. The dollar figure is a consequence of it, and it isn't mine.

**Why this scores:** volunteering that the economic attribution belongs to someone else is the single most credible thing you can say about your own biggest number. It also moves the conversation back to method, which is the ground you want to be on with a Head of Research.

**The failure mode to drill out:** inflating under pressure. If she seems unimpressed, the instinct is to reach for the bigger figure. Don't. The recovery move is to go *smaller and more specific* — name the threshold, name the interaction type, name what changed — never larger.

### The narrowed panelist rule — this supersedes the old one

**Old rule:** never reference any panelist's talk or any prior interaction.

**Corrected rule:** you may state that Dr. Kim posed three questions publicly at the Learners Conference in San Francisco in May 2026, and that you wrote a research response to them. You may not claim acquaintance, private correspondence, or any exchange with her, and you may not characterize anything she said beyond those three questions.

### Facts to fill in before drilling

| Bracket | Where | What's needed |
|---|---|---|
| Trial count | AC01 beat [4] | "Around two thousand" is safe. Confirm the exact figure you're comfortable saying |
| Program duration | AC05 | The honest span of the latency program in years, and how many distinct phases |
| Team composition | AC05 | Who you partnered with, described by function only — never by internal org name |
| The disagreement | AC05 | The concrete instance behind "research should describe, not constrain." Have one real example |

---

## AC10 — The 45-Minute Run Sheet

You do not control the agenda. You do control what you have ready and what you volunteer. This is a plan for *your* half of it.

| Minutes | What's happening | What you're doing |
|---|---|---|
| 0–4 | Warm-up, then the case | Discretion line early. Then AC01, 2:45, and stop talking |
| 4–22 | Her probing | AC02 layers on demand. One layer per question. Never chain two |
| ~22 | The likely rigor attack | AC03 F1 and F2. Volunteer the weakness before she isolates it |
| ~25 | **Your move** | AC08 NASA module, unprompted, as the answer to the consumer-tech objection |
| 25–33 | Scope, stakeholders, mechanisms | AC05 and AC06. This is where level is actually decided |
| 33–40 | Why here, what you'd work on | AC07. The three questions, as an agenda |
| 40–45 | Your questions | Below |

### Three questions to ask her

Ask two. The third is a reserve.

1. "What's the research question in Air Defense right now that nobody has a defensible method for? That's usually where I'm most useful and I'd rather know it early."
2. "When research and engineering disagree about an acceptable risk level, how does that actually resolve on your team today?"
3. "What would have to be true in a year for you to say this hire cleared the bar you were hoping for rather than the one you posted?"

The third one raises level without ever saying the word. That is the correct way to argue it in this conversation.

### Drill sheet

| # | Drill | Pass condition |
|---|---|---|
| 1 | AC01 cold, recorded, no notes | Under 3:00, all eight beats, no internal codename spoken |
| 2 | Each AC02 layer, cold, isolated | Under 90s each, no re-narration of the case |
| 3 | AC03 F1 word-perfect | The sample-size defense with the costed counterfactual, under 40s |
| 4 | Confidentiality audit | Replay every recording; every dollar figure, codename, and competitor mention gets marked. Only ~$50M survives, and it is never hedged with "at least" or "publicly" |
| 5 | The AC08 pivot | Delivered unprompted, 45s, with the intern caveat intact |
| 6 | AC07 without flattery | Say the bridge without the words "your talk was interesting." Agenda, not admiration |
| 7 | Mechanism check | Answer any three questions in a row; at least two must land a mechanism, not a finding |

**The two failure modes on playback:** stacking layers — answering one question with three of AC02 at once, which reads as rehearsed and burns the material you'd need at minute 30 — and slipping a confidential figure in under pressure, which you will not notice yourself. That's what drill 4 is for.

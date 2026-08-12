<style>
@media print {
  @page { margin: 18mm 16mm; }
  html, body { font-size: 10.5pt; line-height: 1.5; font-family: Georgia, "Times New Roman", serif; }
  h1 { font-size: 19pt; margin-bottom: 4pt; }
  h2 { font-size: 15pt; page-break-before: always; margin-top: 0; }
  h2:first-of-type { page-break-before: avoid; }
  h3 { font-size: 12.5pt; margin-bottom: 4pt; }
  h4 { font-size: 11pt; margin-bottom: 3pt; }
  h1, h2, h3, h4 { page-break-after: avoid; page-break-inside: avoid; font-family: Helvetica, Arial, sans-serif; }
  p, li { orphans: 3; widows: 3; }
  blockquote { page-break-inside: avoid; border-left: 3px solid #666; padding-left: 11px; margin-left: 0; }
  table { page-break-inside: avoid; width: 100%; font-size: 9.5pt; border-collapse: collapse; }
  th, td { border: 1px solid #999; padding: 4px 6px; }
  hr { display: none; }
  a { color: inherit; text-decoration: none; }
}
</style>

# 02 — Behavioral & Fit Track (BQ01–BQ10)

Ten pillars. Base question, the four ways it may be phrased, one model answer, all three follow-ups, and the Senior → Lead/Staff delta.

The **persona variants** are the same question worded four ways. They are there so you recognize the question, not so you tailor the answer. One answer per question, every time.

**Structure for this entire track: STARE+M** — Situation → Task → Action → Result → Earned secret → Mechanism. **Target: 200–265 words ≈ 90–110 seconds.** Follow-ups: 45–90 words ≈ 20–35 seconds.

Three rules that decide this track:

1. **"I," not "we."** Every hedge — *"I was involved in," "they let me," "I helped drive"* — caps you at a 2 on Tone & Authority regardless of the work.
2. **The M beat is the level gate.** Result is Senior. What you left behind is Lead/Staff. Say it as its own sentence: *"What I left behind was X, and Y still has to clear it."*
3. **`[brackets]` are yours to fill.** Several pillars need a specific incident that only you can supply. Fill it in or cut the sentence — never improvise a number, a name, or an outcome.

---

## BQ01 — Warfare & Ethics

**Structure:** Position + mechanism (not STARE — this is a stance question) · **Target:** ~95s

> **Base:** How do you think about the moral and ethical responsibility of designing UX for autonomous weapons and counter-drone C2 systems?

**Persona variants**

- **Kim:** "What research philosophy would you use to define and test the moral boundaries of UX for autonomous weapons and counter-drone C2 systems without slowing responsible Air Defense delivery?"
- **Systems/ML:** "When a non-deterministic counter-drone system can act faster than an operator, what ethical constraints must become hard trust, intervention, and verification requirements?"
- **Product:** "How would you turn ethical concerns about autonomous weapons UX into product decisions that preserve mission value without becoming an open-ended reason not to ship?"
- **Design:** "Where should an Air Defense operator workflow introduce deliberate friction, confirmation, or control handoff so the physical-digital experience preserves meaningful human authority?"

### Model answer (~235 words / 95s)

**Position.** I don't think the hard ethical question here is whether the system should exist. It's whether the human who authorizes its action is genuinely in a position to be accountable for it. Accountability without comprehension is a fiction — and a UX that manufactures that fiction is the real ethical failure, because it launders a machine's decision through a human signature.

**So the responsibility is concrete.** Preserve the operator's capacity to form an independent judgment at the point of authorization, and tell the organization honestly when a design has stopped doing that.

**Mechanism.** That's why I wrote *Principles for Agentic Trust* as four auditable dimensions — Alignment, Execution, Control, and Calibration — rather than as values. Values can't be checked; dimensions can. And Calibrated Cognitive Friction is my position that at irreversible decision boundaries, risk-proportional friction is a control surface, not a usability defect. I'll be clear that it's a thesis — I haven't deployed it.

**The part people skip.** Risk-proportional cuts both ways. It means most of the system should be frictionless, and I have to be the one saying that out loud. An ethics position that only ever adds cost gets routed around within two quarters, and then it protects nothing.

**What I'd build.** A consequence classification agreed once — decisions tiered by reversibility — so the ethical conversation happens at design time about a *class* of decision, not at ship time about a feature. That converts a recurring argument into a standing rule.

### Follow-ups

**F1 — "Give me a concrete case where you personally declined to optimize something because of the ethical consequence, not the usability consequence."** *(~80 words)*

> I want to be precise rather than impressive: I've never been asked to design a weapon system, and I'm not going to dress a consumer example up as a moral stand. The closest real case is [your specific instance — the recommendation you declined to make, or the "improvement" you argued against because it would have removed a user's ability to notice something]. What made it ethical rather than usability was that the faster path was genuinely better for the metric and worse for the person's ability to catch an error.

**F2 — "Who decides when your ethical line becomes a shipping blocker, and what happens when they overrule you?"** *(~75 words)*

> Not me, and I think claiming otherwise is a red flag in a researcher. My job is to make the risk legible, name the severity, and make sure the acceptance is explicit and owned by someone with the authority to accept it. If I'm overruled, I document the residual risk, agree what we'd monitor to detect it, and move on without relitigating. The failure mode I avoid is quiet non-cooperation after losing a decision.

**F3 — "How do you keep an ethics position from becoming an open-ended veto that engineering learns to route around?"** *(~75 words)*

> By making it finite and pre-committed. A tiered rule agreed in advance — these decision classes require a control, these explicitly don't — means engineering can predict me, and predictability is what stops routing-around. The other half is spending the credibility in both directions: I should be visibly removing confirmations that don't earn their cost, not only adding them. A researcher who has never simplified anything doesn't get believed the day they ask for friction.

### Senior → Lead/Staff

- **Senior:** holds a coherent personal ethical position.
- **Lead/Staff:** converts it into a written principle, a review gate, or a control requirement the organization must satisfy.
- **Say this:** *"I'd rather have a boring rule about decision classes agreed in month two than a compelling ethics conversation every time we ship."*

---

## BQ02 — Military Operators

**Structure:** STARE+M, with an honest boundary up front · **Target:** ~105s

> **Base:** Describe your experience working directly with military operators or high-stress domain experts in field conditions. How do you cut through operator bias or bravado to get true operational data?

**Persona variants**

- **Kim:** "Using your NASA and field-research experience, how would you design rapid ethnography with Air Defense operators that separates genuine operational constraints from recall bias, status signaling, or bravado?"
- **Systems/ML:** "How would you convert conflicting operator accounts from stressful field conditions into falsifiable system requirements instead of anecdotes engineering cannot implement?"
- **Product:** "When field operators demand mutually incompatible changes, how do you identify the highest-value operational truth quickly enough to influence the next release?"
- **Design:** "How would you observe an operator's full physical-digital C2 workflow and reconcile what they say with breakdowns visible in posture, reach, attention, and interaction sequence?"

### Model answer (~250 words / 100s)

**Boundary first.** I have not worked with military operators. I've worked with high-stress domain experts under real conditions, and I'd rather be exact about that than blur it, because you'd find out in week one anyway.

**Situation.** At Uber I ran urban field studies of the driver interface — people doing complex spatial navigation in live traffic, with passengers, under time and income pressure. Classic conditions for the gap between what someone tells you and what they do.

**Task.** Mine was to find what the interface actually cost drivers in the moment, and connect it to whether they kept driving.

**Action.** I ran observation first and interviews second, so the conversation was anchored to something I'd watched rather than to a self-report. Three techniques did most of the work. I asked about the most recent instance, never the typical one — "typical" is reconstruction. I anchored every question to an artifact or a moment: show me, what did you touch. And I asked about workarounds instead of errors, which is the one that beats bravado. Nobody admits a mistake to a stranger with a notebook; everybody proudly demonstrates their clever hack. Every workaround is a design defect with a human patch over it.

**Result.** The work contributed to a 5% increase in driver retention, and the finding I still carry is that information density has to scale down during high-stress maneuvers or it becomes visual overload.

**Earned secret.** Bravado isn't an obstacle to truth, it's a channel to it — you just have to ask the question the person wants to answer.

**Mechanism.** What I'd bring is that as a protocol, not a personal skill: observe-then-ask, most-recent-instance, artifact-anchored, workaround-first. Written down, it means the next person who gets scarce operator access comes back with data that composes with mine instead of a different set of stories.

### Follow-ups

**F1 — "Name the moment an operator or domain expert told you something that turned out to be wrong. How did you find out?"** *(~75 words)*

> [Your specific instance — the stated behavior that observation contradicted.] The general shape, and the one I've seen repeatedly: people report the procedure they were trained on, not the one they run, and they aren't lying — the adapted version has become invisible to them. I found out by watching, then replaying it: "you did this here, walk me through that." The correction is almost always freely given, because they don't experience it as a contradiction.

**F2 — "What did you change about your protocol after that, and does it still work when you only get one field visit?"** *(~70 words)*

> I stopped scheduling interviews before observation. Ever. If I only get one visit, the interview becomes a debrief of what I just watched rather than an independent source, which is both faster and more accurate. The single-visit constraint actually enforces the discipline: you cannot afford to spend the access on hypotheticals, so you observe first and use every question to resolve a specific ambiguity you saw.

**F3 — "How do you earn credibility with an operator who thinks a researcher with a Ph.D. cannot understand their job?"** *(~75 words)*

> By being wrong in front of them on purpose. I show my model of their work early and let them correct it — people who think you don't understand their job are highly motivated to fix your description of it, and that's the fastest rapport I know. What loses it instantly is defending the model. The other half is showing them what changed because of the last visit; that's the difference between a participant and a partner.

### Senior → Lead/Staff

- **Senior:** runs credible field sessions.
- **Lead/Staff:** builds the elicitation protocol and access model that lets the whole team get truthful operator data.
- **Say this:** *"Operator access is the scarcest thing in this domain. I'd treat it as shared infrastructure with a protocol attached, not as my personal research budget."*

---

## BQ03 — Scrappiness vs. Rigor

**Structure:** STARE+M · **Target:** ~100s

> **Base:** You hold a Ph.D. and have published in academic tracks like ACM CSCW. How do you balance scientific rigor with Anduril's requirement to ship functional tech in months, not years?

**Persona variants**

- **Kim:** "Your Ph.D. and CSCW work show rigor; tell me how you would preserve validity while compressing an Air Defense research program into evidence that changes a decision in weeks, not years."
- **Systems/ML:** "What minimum evidence would you require before turning a psychophysics or trust finding into a latency threshold or verification test on a rapidly changing C2 system?"
- **Product:** "Give me an example of how you have traded methodological completeness for decision speed without making the resulting product recommendation intellectually dishonest."
- **Design:** "How would you combine fast prototype testing and service-blueprint work with enough rigor to prevent a rushed C2 interaction pattern from becoming an unsafe design standard?"

### Model answer (~245 words / 98s)

**Situation.** At Amazon I ran a multi-year psychophysics program, and it sounds like the least scrappy work imaginable. It was surrounded by product decisions that could not wait for it.

**Task.** Get decision-grade evidence at product cadence without letting the claim outrun the design that produced it.

**Action.** I stopped treating rigor as a duration and started treating it as a match between the claim and the design. Concretely: I separated the questions that needed threshold-grade evidence — the actual specification value, which would be inherited by every downstream team — from the ones that only needed direction, where a fast answer with a wide interval was completely sufficient. The rigorous work went where the cost of being wrong compounded. And on the fast work I made the boundary explicit in the deliverable itself: this is directional, do not build a spec on it.

**Result.** The program replaced arbitrary engineering latency targets with human perceptual thresholds, informed roughly $50M in operational value, and the interaction architecture became US Patent US-12532040-B1.

**Earned secret.** Most "rigor versus speed" fights aren't about method at all. They're about claim scope. The team wants a decision, the researcher hears a demand for certainty, and both sides argue past each other. Ninety percent of the time you can give them the decision fast if you're disciplined about what you refuse to claim alongside it.

**Mechanism.** What I'd install is explicit evidence tiers — directional, decision-grade, threshold-grade — with a stated bar for each. That lets an organization buy speed *on purpose* rather than by accident, and it lets me say yes quickly far more often than a rigor argument ever would.

### Follow-ups

**F1 — "Name the specific methodological compromise you made and the claim you refused to make because of it."** *(~75 words)*

> [Your specific instance.] The recurring shape for me is population coverage: I accept a sample that can't characterize the tails, and in exchange I refuse any claim about the tails — so the finding governs the central case and the extremes stay explicitly open. What I won't do is take a compromised sample and then quietly write a spec as though it were representative. The compromise is fine; the silent promotion of the compromised result is not.

**F2 — "What is the smallest study you have ever run that still changed a real decision?"** *(~65 words)*

> [Your specific instance — participants, days, decision changed.] The pattern worth knowing is that the smallest studies that change decisions are almost always the ones aimed at a binary: can operators do this at all, or does this control get confused with that one. Those need very few people, because a failure observed twice is real. Magnitude questions are what need scale, and they're rarer than teams assume.

**F3 — "Where is the line between a fast study and a dishonest one, and have you ever been asked to cross it?"** *(~75 words)*

> The line isn't speed, it's whether the write-up preserves the uncertainty the design actually left. A four-day study reported as a four-day study is honest. A four-day study reported with a clean number and no interval is not, and that's the same act regardless of how long it took. On being asked — the pressure I've encountered is rarely "fake it," it's "drop the caveat, it's confusing." That's the same request wearing a friendlier face, and I don't drop it; I make it shorter.

### Senior → Lead/Staff

- **Senior:** moves fast when asked.
- **Lead/Staff:** defines the evidentiary tiers the organization uses to decide how much rigor a given decision deserves.
- **Say this:** *"I'd rather the organization decide consciously that a question is worth four days than have me privately decide it's worth four weeks."*

---

## BQ04 — Cross-Functional Standoff

**Structure:** STARE+M · **Target:** ~105s

> **Base:** Tell me about a time an Engineering Lead or PM strongly resisted your research recommendations or wanted to strip a safety feature for speed. How did you resolve it?

**Persona variants**

- **Kim:** "Tell me about a time you protected the integrity of a research or safety recommendation under executive pressure while still preserving trust and delivery velocity across the team."
- **Systems/ML:** "Describe a technical standoff where engineering rejected your Human Factors threshold or safety control. What evidence, trade space, and verification criterion changed the decision?"
- **Product:** "Tell me about a time a PM wanted to remove a safety or usability control to hit a date. How did you frame the user risk, business cost, and reversible compromise?"
- **Design:** "Describe a conflict over an operator-workflow safeguard or physical-digital interaction. How did you keep research, design, product, and engineering aligned without diluting the safety intent?"

### Model answer (~250 words / 100s)

**Situation.** At Amazon, latency targets were already written into engineering specs and schedules. My psychophysics work said those numbers were wrong — in both directions. Some were tighter than anyone could perceive, so we were paying for performance nobody could detect. Others were looser than the point where users stopped trusting the system.

**Task.** Change a number that other teams' commitments were built on, without authority over any of them.

**Action.** My first attempt was the obvious one — here's the data, the target is wrong — and it went nowhere. So I stopped arguing about the number and asked what the number was protecting. The answer was risk: nobody knew what would break if it changed, so the safe move was to keep it. That reframed my job entirely. Instead of a finding, I brought a specification with three parts: the threshold, the population percentile it covered, and a defined fallback if the hardware couldn't hit it — substitute an earlier cue in a faster modality rather than relax the requirement. I also conceded the cases where the existing target was defensible, which mattered more than any single piece of evidence I presented.

**Result.** Arbitrary engineering targets were replaced with human perceptual thresholds. The program informed roughly $50M in operational value, and the multimodal interaction architecture became US Patent US-12532040-B1.

**Earned secret.** Engineers almost never resist evidence. They resist *unbounded* risk. A finding transfers risk to them; a specification with a fallback absorbs it. Same data, completely different reception.

**Mechanism.** What I left behind wasn't the threshold, it was the format — any proposed latency target had to state a percentile, a modality, and a fallback. That argument didn't have to happen again, and it happens without me now.

### Follow-ups

**F1 — "What exactly did the other person say, and what did you concede?"** *(~75 words)*

> The substance of it was: your data is interesting, my schedule is real, and if I change this and something breaks it's mine. Which was fair. What I conceded was scope — I dropped the targets where the existing number was defensible and stopped trying to win the whole spec, and I accepted their worst-case load condition for verification rather than my cleaner lab condition. That made the number harder to hit and much harder to argue with.

**F2 — "Did the decision go your way, and what did you do in the case where it did not?"** *(~75 words)*

> On the perceptual thresholds, yes — and it took a second attempt after the first framing failed. Where I've lost: I document the residual risk in their language, agree on what we'd watch to know whether I was right, and then genuinely drop it. The behavior that destroys a researcher's credibility isn't losing an argument, it's the quiet campaign afterward. If the monitoring signal later shows I was right, the data reopens it, not me.

**F3 — "What mechanism did you put in place so that argument never had to be relitigated?"** *(~65 words)*

> The spec format. A latency target without a stated percentile, modality, and fallback wasn't a complete proposal anymore. That's a small, almost bureaucratic thing, and it did more than any presentation I gave — it moved the burden from "convince the researcher" to "fill in the fields," and it kept working after I stopped being in the room for those conversations.

### Senior → Lead/Staff

- **Senior:** wins the argument with data.
- **Lead/Staff:** leaves behind a standard, threshold, or review gate that removes the need for the next argument.
- **Say this:** *"I count the win as the format, not the number. The number was one decision; the format was every decision after it."*

---

## BQ05 — Startup Intensity & Field Tempo

**Structure:** STARE+M · **Target:** ~95s

> **Base:** Defense tech requires high-intensity field testing and dynamic schedules. How do you stay effective and prevent burnout under high operational friction?

**Persona variants**

- **Kim:** "How would you build a high-performance research culture that can sustain field intensity and dynamic schedules without normalizing burnout or lowering evidence quality?"
- **Systems/ML:** "During repeated field-test cycles with shifting hardware and software builds, what operating practices keep your judgment and technical handoffs reliable under fatigue?"
- **Product:** "How do you protect the highest-value work and communicate capacity when travel, field failures, and release pressure collide in the same week?"
- **Design:** "How do you maintain observational quality and collaborative design judgment during intensive field studies where physical conditions, travel, and rapid redesign cycles create fatigue?"

### Model answer (~235 words / 95s)

**Situation.** My work has run on field and simulator cycles for most of a decade — live urban field studies at Uber, high-fidelity simulator programs at Mercedes, workstation validation at NASA. Compressed schedules, travel, and hardware that isn't ready when you arrive.

**Task.** Keep the evidence trustworthy when the conditions are actively hostile to it.

**Action.** I run four practices, and they're all about protecting judgment rather than energy. The protocol is written and reviewed *before* travel, so on site I'm executing a plan rather than designing one while tired — that single rule prevents most field data problems I've seen. Debrief happens the same day, before sleep, because observational detail decays overnight and no amount of discipline the next morning recovers it. Collection days and analysis days are separated, and I don't make an analysis decision on a field day. And where there's more than one of us, the observer role rotates, because sustained observation degrades faster than people believe.

**Result.** [Your specific instance — the field program where these practices held or where their absence cost you.]

**Earned secret.** Fatigue doesn't reduce output; that's why it's dangerous. It reduces the quality of your *methodological* judgment while your effort stays high. You keep working, and you start making quiet decisions — dropping a condition, accepting a bad session — that you'd never make rested. My dissertation was on performance under high-stress task interruption, so this isn't a wellness position for me, it's a measurement one.

**Mechanism.** Pre-committed protocols, same-day debriefs, and role rotation, written down as team practice. That's what makes a team's evidence survive tempo, rather than depending on who happened to be well-rested.

### Follow-ups

**F1 — "Walk me through your heaviest field-testing month. What actually happened to your evidence quality?"** *(~75 words)*

> [Your specific instance.] The honest general answer is that the first thing to degrade is never the data collection — it's the *notes*. Sessions still get run, but the observational richness thins out, and you don't notice because the recordings exist. Then analysis is three weeks later against thin notes and a lot of audio. That's the failure I now design against, and it's why the same-day debrief is non-negotiable for me rather than a nice practice.

**F2 — "Tell me about a week where the intensity degraded your work. What did you change afterward?"** *(~70 words)*

> [Your specific instance.] The change that came out of it for me was structural rather than personal — I stopped relying on being able to think clearly at the end of a field day, and moved every decision that required judgment to a pre-committed protocol or a next-morning slot. Willpower is not a method. If a practice only works when I'm rested, it isn't a practice, it's a hope.

**F3 — "How do you protect a team's sustainability without becoming the person who slows the deployment down?"** *(~75 words)*

> By spending the argument on quality rather than hours. "We shouldn't work this hard" loses in this environment, and honestly it should. "The last two sessions of a fourteen-hour day aren't usable data, so let's not pretend we ran twelve sessions" wins, because it's an evidence argument and it's true. Rotation and handoff practices let the tempo stay high while the observation stays good. I'd rather change the schedule's shape than its intensity.

### Senior → Lead/Staff

- **Senior:** manages their own capacity well.
- **Lead/Staff:** builds field-rotation, handoff, and quality-control practices that keep a team's evidence reliable under tempo.
- **Say this:** *"I don't want a slower program. I want one where the twelfth hour produces data we'd actually defend."*

---

## BQ06 — Extreme Ambiguity

**Structure:** STARE+M · **Target:** ~100s

> **Base:** How do you design a research strategy when hardware/software requirements are completely undefined and the product team is changing direction weekly?

**Persona variants**

- **Kim:** "How would you establish a coherent Air Defense research thesis and repository when product direction changes weekly and no stable policy or requirements exist yet?"
- **Systems/ML:** "When hardware interfaces, autonomy behavior, and software architecture are all moving, how do you create Human Factors hypotheses that can still mature into testable specifications?"
- **Product:** "What research do you fund first when the roadmap changes weekly, and how do you prevent discovery work from becoming obsolete before it changes a decision?"
- **Design:** "How would you use service blueprints and workflow models as stable artifacts when screens, hardware controls, and operator roles are all still changing?"

### Model answer (~245 words / 98s)

**Situation.** I joined Sling as the Human Factors function — there wasn't one before me — across core software, hardware, and AI platforms simultaneously. No precedent, no standing requirements, and non-deterministic AI behavior that conventional usability checks weren't built to evaluate.

**Task.** Produce something stable enough that design, engineering, and product could plan against it, while everything underneath was still moving.

**Action.** I looked for the slowest-moving layer and built there. Screens change weekly; what a person is physically capable of does not, and neither do the authority boundaries in a system — who decides what, and when control transfers. So I refused to spend my early time evaluating whatever interface existed that week. Instead I wrote the layer underneath it: usability criteria for system latency, auditory and visual feedback, and spatial layout, all grounded in perceptual thresholds; physical ergonomics, reach-envelope, anatomical safety, and mechanical fit specifications; and for the agentic side, *Principles for Agentic Trust* — Alignment, Execution, Control, Calibration — as an audit structure for systems whose behavior isn't deterministic.

**Result.** Those became the organization's Human Factors criteria, and the Agentic Trust work was accepted to ACM CSCW 2026 Industry Perspectives.

**Earned secret.** Ambiguity isn't a reason to wait for requirements. It's a signal about *which layer* to invest in. When the top layer is churning, the highest-leverage work is one layer down — and the artifacts you build there don't expire when the roadmap turns.

**Mechanism.** Those criteria are the mechanism. A moving roadmap now hits a fixed set of things it has to clear, which means product direction can change weekly without the human-factors floor moving with it.

### Follow-ups

**F1 — "What did you commit to in your first thirty days on an ambiguous program, and what did you deliberately leave undecided?"** *(~75 words)*

> I commit to the constraint layer — the physical and perceptual boundaries, and the map of who has authority at each step. Those are cheap to establish and expensive to discover late. What I deliberately leave undecided is anything about a specific interface or concept, and I say so out loud, because otherwise silence gets read as endorsement. The trap in month one is producing an opinion about the current design just to look useful.

**F2 — "How do you tell the difference between productive ambiguity and a team that has no strategy?"** *(~70 words)*

> Productive ambiguity has a stable question underneath the churn — the approach changes weekly, the problem doesn't. No strategy looks like the *problem* changing weekly. It's a simple test: ask three people what we're trying to make possible for the user. If you get one answer with three approaches, that's healthy. If you get three different answers, research isn't the intervention needed, and I'd say that rather than run a study into it.

**F3 — "What research did you fund that turned out to be obsolete before it landed, and what did that teach you?"** *(~70 words)*

> [Your specific instance.] The general lesson I hold, and it's the one behind my whole approach here: work indexed to a *concept* expires with the concept, and work indexed to the *user and the task* doesn't. Anything scoped to "does this design work" has a shelf life measured in sprints. Anything scoped to "what does this person have to do, and what are they capable of" is still true after three redesigns.

### Senior → Lead/Staff

- **Senior:** copes with ambiguity productively.
- **Lead/Staff:** imposes a research thesis and sequencing plan that gives other functions a stable frame to work against.
- **Say this:** *"I don't wait for requirements to stabilize. I go find the layer that was never going to move, and I make that the thing everything else has to clear."*

---

## BQ07 — Handling Ignored Insights

**Structure:** Protocol + example (the question asks for a protocol) · **Target:** ~95s

> **Base:** What is your protocol when leadership or engineering acknowledges your research findings but decides to ship an unsafe or sub-optimal UX anyway?

**Persona variants**

- **Kim:** "When leaders accept your evidence but choose a riskier design anyway, how do you document uncertainty, define escalation thresholds, and preserve the research function's influence?"
- **Systems/ML:** "If engineering ships despite a validated Human Factors failure mode, what severity, detectability, verification, and stop-ship criteria govern your response?"
- **Product:** "How do you respond when a roadmap owner accepts your data but chooses to ship a sub-optimal or unsafe workflow for schedule or mission reasons?"
- **Design:** "If an unsafe interaction survives design review, how do you preserve the evidence in the service blueprint, negotiate mitigations, and keep the operator workflow from silently normalizing the risk?"

### Model answer (~235 words / 95s)

**First, a distinction I hold hard.** Sub-optimal and unsafe are not the same thing and don't get the same response. Researchers who treat them the same lose the ability to be heard on the one that matters. Most of what I lose is sub-optimal, and that's a legitimate business call I don't fight.

**For sub-optimal:** I document it, agree with the owner on the signal we'd watch to know whether the call was wrong, and drop it. Genuinely drop it — no relitigating in the next review. Then the data reopens the question later, not me.

**For unsafe, the protocol is four steps.** One: restate it in the team's own risk language — severity, likelihood, and specifically whether there's an independent path to detect the error before consequence. Missing detectability is what makes something escalation-worthy, more than severity alone. Two: put it in writing, including what would change my assessment, so it's a risk statement rather than an objection. Three: ask for explicit acceptance by someone with the authority to accept it. Most of the time this step alone changes the outcome — accepting a named risk in writing is very different from approving a schedule. Four: escalate only on catastrophic severity with no independent detection path.

**Grounding.** This comes out of applying uFMEA to Lunar Gateway clinical workstations at NASA against NASA-STD-3001 and MIL-STD-1472 — where "how would anyone catch this before it matters" was the question that actually drove design changes.

**Earned secret and mechanism.** The escalation you win is the one you negotiated before the incident. So the mechanism is a stop-ship criterion agreed in advance, in calm conditions — because a threshold argued for the first time under schedule pressure reads as obstruction no matter how right it is.

### Follow-ups

**F1 — "Give me the actual sequence: who did you go to first, what did you put in writing, and where did you stop?"** *(~80 words)*

> [Your specific instance.] The sequence I hold to: the decision owner first, always, and never around them — going over someone's head before going to them is how a researcher becomes untrustworthy in one move. In writing goes the failure mode, the severity, whether anything catches it before consequence, and what evidence would change my view. I stop when a person with the authority to accept the risk has accepted it explicitly and it's documented. That's the system working, even when I disagree.

**F2 — "What severity of consequence moves you from documenting the risk to formally escalating it?"** *(~65 words)*

> Catastrophic or irreversible harm combined with no independent detection path before the consequence. Either alone doesn't do it — high severity with a reliable catch is a managed risk, and an undetectable error with recoverable consequences is a defect. It's the conjunction that removes the organization's ability to learn from the mistake before it costs something, and that's the line where documenting stops being enough.

**F3 — "Have you ever escalated and been wrong? What did that cost you with the team?"** *(~70 words)*

> [Your specific instance — and answer it honestly; a candidate who has never been wrong on this either hasn't escalated or isn't telling you.] What being wrong costs is precision: the next time you raise something, people quietly discount it. The repair isn't apologizing, it's raising the bar on yourself publicly — being the one who says "this one is sub-optimal, not unsafe" when it would be easier to leave it ambiguous.

### Senior → Lead/Staff

- **Senior:** voices the concern clearly and persistently.
- **Lead/Staff:** has a pre-agreed escalation and stop-ship threshold that leadership accepted before the incident.
- **Say this:** *"I'd want to negotiate the stop-ship line in a quiet month. Arguing about where the line is, during the week you need it, is already a failure."*

---

## BQ08 — Failure & Course Correction

**Structure:** STARE+M · **Target:** ~100s

> **Base:** Tell me about a research study or interface design of yours that completely failed during testing. What went wrong, and how did you recover?

> ⚠️ **This is the one pillar you must supply yourself.** There is no canonical failure in your evidence set, and a manufactured one will collapse under the follow-ups — which are specifically designed to find the seam. Pick a real one before you drill this. Strongest candidate anchors, in order: a study design at Amazon that had to be re-run; a simulator protocol at Mercedes that didn't produce the effect; a NASA validation assumption that testing overturned; a Sling framework draft that didn't survive contact. Choose the one where **the error was yours**, not the constraint's.

### Model answer — skeleton to fill (~245 words / 98s)

**Situation.** [Program and stakes — one sentence. What was riding on the study.]

**Task.** [What you specifically owned.]

**Action.** [What you did — and critically, the assumption you built in without testing it. Name the moment you realized it had failed, and what you did in the next 48 hours.] The recovery beat is where the points are: what you told stakeholders, how fast, and what you salvaged.

**Result.** [What the corrected work produced. If the honest answer is that the study was written off, say so — the recovery is the result.]

**Earned secret.** The pattern worth generalizing, and the version I'd defend: study failures almost never come from the analysis. They come from an assumption made during design that nobody wrote down as an assumption — usually about what the task actually is, or about what participants will do when the instructions are ambiguous. The analysis is where you *discover* it, which is far too late and far too expensive.

**Mechanism.** [The practice you now run every time.] Mine is a pre-mortem on the design: before fielding, I write down what result would make the study uninterpretable, and what assumption has to hold for it to mean anything. If I can't state that, the design isn't finished. And I pilot with two people who aren't researchers, because researchers unconsciously repair ambiguous instructions.

### Follow-ups

**F1 — "What was your specific error, as opposed to the team's or the constraint's?"** *(~65 words)*

> [Name it in one sentence, in the first person, with no surrounding context.] This follow-up is a trap for anyone who narrated a failure that was really someone else's. Answer it in under twenty seconds and do not add mitigating context — the mitigation is what makes it sound like a dodge. "I assumed X and never tested that assumption" is a complete answer and it scores better than a paragraph.

**F2 — "How much time and money did the failure cost, and who else absorbed it?"** *(~65 words)*

> [Time and cost, stated plainly, no softening.] The part that earns credit is the second half: naming who else paid for it. Failures in research are rarely absorbed by the researcher — an engineering team waited, a decision slipped, participants were spent. Saying that out loud is the difference between accountability and a story about learning.

**F3 — "What practice do you now run every time because of that failure?"** *(~65 words)*

> [Your practice.] The design pre-mortem — before fielding anything, I write down the result that would make the study uninterpretable and the assumption that has to hold for it to mean anything. It costs twenty minutes. It's caught more problems for me than any analysis technique I know, because it moves the discovery from after data collection to before it.

### Senior → Lead/Staff

- **Senior:** recovers the study and learns from it.
- **Lead/Staff:** turns the failure into a checklist, review step, or method standard that prevents the class of error team-wide.
- **Say this:** *"The individual mistake isn't very interesting. What matters is whether the next person on this team can make it, and after that one they couldn't."*

---

## BQ09 — Scaling Culture & Mentorship

**Structure:** STARE+M · **Target:** ~100s

> **Base:** How do you scale research operations, build shared insight repositories, and mentor junior team members as a Lead/Staff engineer?

**Persona variants**

- **Kim:** "What operating system would you build for Air Defense research so repositories, standards, mentorship, and research quality scale beyond your own studies?"
- **Systems/ML:** "How would you make Human Factors insights reusable by systems and ML teams through traceable requirements, failure modes, and verification artifacts while developing junior researchers?"
- **Product:** "How would you build research operations that help multiple product teams find prior evidence, understand decision impact, and avoid repeating low-value studies?"
- **Design:** "How would you connect shared insights, service blueprints, design patterns, and mentorship so operator-workflow knowledge compounds across Air Defense products?"

### Model answer (~240 words / 96s)

**Situation.** At Sling I lead organizational Human Factors strategy across core software, hardware, and AI platforms. The scaling problem there is the one I'd expect here: one practitioner, many teams, and demand that will always exceed capacity.

**Task.** Raise what the organization can do without me in the room — not increase my own throughput, which is a losing race.

**Action.** I invested in three things instead of in more studies. Criteria, so decisions have a bar to clear: usability criteria for latency, auditory and visual feedback, and spatial layout grounded in perceptual thresholds, and physical specifications for reach envelope, anatomical safety, and mechanical fit. A shared framework, so people have language for the hard cases — *Principles for Agentic Trust*, with Alignment, Execution, Control, and Calibration as auditable dimensions rather than opinions. And on mentorship, my approach is to hand over the *decision* rather than the task: a junior researcher who only executes protocols learns method, but never learns judgment, which is the actual scarce skill.

**Result.** Those criteria became how the organization evaluates its systems, and the Agentic Trust framework was accepted to ACM CSCW 2026 Industry Perspectives.

**Earned secret.** Scaling research isn't about doing more studies faster. It's about reducing the number of decisions that require a study at all — a good criterion answers a hundred questions that would otherwise each arrive as a request.

**Mechanism.** Criteria, a shared audit framework, and a decision-indexed record of what we've already answered. Those raise the floor. My own studies only ever raised the ceiling.

### Follow-ups

**F1 — "Name a person you developed and the specific capability they had after working with you that they did not have before."** *(~70 words)*

> [Name a real person and a specific capability — "they could scope a study to a decision instead of to a question," "they could defend a sample size to an engineering lead."] Do not answer this one generically. A vague answer here reads as never having actually mentored anyone, and it's the single most common place strong candidates lose the Lead/Staff argument. One person, one capability, one sentence about how the handover happened.

**F2 — "What standard or artifact of yours is still being used by a team you have left?"** *(~65 words)*

> The perceptual-threshold approach to latency specification at Amazon — the practice of stating a percentile and a modality rather than a round number. That outlived my involvement because it was embedded in how targets got proposed, not in a document someone had to remember. That's my test for whether something scaled: does it still operate when the author is gone and nobody is advocating for it?

**F3 — "How do you shape team culture when you have no direct reports and no formal authority?"** *(~75 words)*

> Through artifacts and through what you visibly reward. A written criterion changes behavior in a way that advocacy doesn't, because it's there when you're not. And culture is mostly set by what a senior person praises publicly — I make a point of crediting the person who kills their own study or reports the null, because that's the behavior that decides whether a research function is honest. Authority helps, but it isn't the mechanism.

### Senior → Lead/Staff

- **Senior:** mentors informally and documents well.
- **Lead/Staff:** builds the repository, review ritual, and growth path that raises the whole function's floor.
- **Say this:** *"My studies raise the ceiling. The criteria raise the floor. At this level the floor matters more, because it's what operates when I'm on a plane."*

---

## BQ10 — Competing Priorities

**Structure:** STARE+M · **Target:** ~95s

> **Base:** When three different product managers are demanding urgent user research for different Air Defense platforms simultaneously, how do you triage and allocate your time?

**Persona variants**

- **Kim:** "How would you allocate scarce research capacity across three urgent Air Defense programs while protecting the long-term research agenda and team health?"
- **Systems/ML:** "How do you rank simultaneous research requests when one affects a safety-critical autonomy threshold, one blocks integration, and one improves operator efficiency?"
- **Product:** "Three PMs each claim their Air Defense study is urgent. Walk me through the decision framework, ROI evidence, and stakeholder conversation you use to allocate research capacity."
- **Design:** "How would you triage competing workflow studies across platforms while preserving shared service-blueprint knowledge and avoiding fragmented operator experiences?"

### Model answer (~235 words / 95s)

**Situation.** At Sling I cover software, hardware, and AI platforms as the Human Factors function, so simultaneous competing requests are the normal operating condition rather than an occasional crunch. At Amazon the same problem existed at portfolio scale.

**Task.** Allocate scarce capacity in a way that's defensible to the people who don't get what they asked for — because that's the actual constraint, not the scheduling.

**Action.** I triage on three questions, in order. First: what decision does this change, and when is it made? A request with no decision behind it doesn't get research, it gets a conversation — and that conversation is often the whole deliverable. Second: what's the cost of being wrong, and is it reversible? A safety-critical threshold outranks an efficiency improvement even when the efficiency work is louder and better socialized. Third: is this already answered? A meaningful share of urgent requests are re-runs of something the organization already knows, and the fastest study is the one you don't run.

**Result.** [Your specific instance — the quarter where this framework produced a defensible allocation.]

**Earned secret.** Prioritization arguments are almost never about priority. They're about *visibility* — a PM who understands why they lost, and sees the queue, will accept losing. A PM who just gets a no starts hiring their own research or making the call without evidence, which is much worse for me than the study I didn't run.

**Mechanism.** So the answer isn't my triage judgment, it's a published intake and prioritization model — decision, date, consequence class, reversibility — that makes the trade-offs legible to everyone, including the person who lost.

### Follow-ups

**F1 — "Which request do you say no to first, and how do you say it so that PM still brings you the next problem?"** *(~75 words)*

> First no goes to the request with no decision attached — usually a request for reassurance about something already built. And the way you say it matters more than the criterion: never a flat no. It's "here's what I think you already know, here's the question I'd actually be worried about, and here's when I have capacity." You're trading a study for judgment, delivered immediately. People come back for that.

**F2 — "What did you stop doing last time to make room for the highest-value work?"** *(~65 words)*

> [Your specific instance.] The category I stop first is validation work on decisions that are already effectively made — the study whose result would not change the outcome. It's comfortable work, it makes a team feel supported, and it's the least valuable thing a research function does. Killing it is unpopular for about two weeks and then nobody mentions it again.

**F3 — "How do you tell a PM their question does not need research at all?"** *(~70 words)*

> Directly, and with the answer attached. "You don't need a study, you need a decision — here's what the evidence we already have implies, and here's the risk you're taking if it's wrong." The thing that makes it land is that it's not a refusal, it's a faster service. And it buys enormous credibility for the times I come back and say this one genuinely does need three weeks.

### Senior → Lead/Staff

- **Senior:** triages their own queue well.
- **Lead/Staff:** publishes the intake and prioritization framework that makes the trade-offs legible to every stakeholder.
- **Say this:** *"I want the queue visible. If people can see why they lost, they stop escalating and start negotiating — and I stop being the bottleneck they route around."*

---

## Track drill sheet

| ID | Pillar | Anchor evidence | Hardest follow-up | Needs your input |
|---|---|---|---|---|
| BQ01 | Warfare & ethics | Agentic Trust, CCF thesis | F1 — a real ethical decline | ✔ |
| BQ02 | Military operators | Uber field, NASA | F1 — expert who was wrong | ✔ |
| BQ03 | Scrappiness vs rigor | Amazon $50M, patent | F2 — smallest study that mattered | ✔ |
| BQ04 | Cross-functional standoff | Amazon latency spec | F1 — what you conceded | |
| BQ05 | Intensity & tempo | Uber / Mercedes / NASA field | F2 — the week it degraded | ✔ |
| BQ06 | Extreme ambiguity | Sling standing start | F3 — obsolete research | ✔ |
| BQ07 | Ignored insights | NASA uFMEA | F3 — escalated and wrong | ✔ |
| BQ08 | Failure | **none — you must supply** | F1 — your specific error | ✔✔ |
| BQ09 | Scaling & mentorship | Sling criteria, CSCW | F1 — name a mentee | ✔✔ |
| BQ10 | Competing priorities | Sling portfolio | F2 — what you stopped | ✔ |

**Fill the ✔ rows before you drill.** Eight of ten pillars have at least one follow-up that requires a specific fact only you have. BQ08 and BQ09 F1 are the two that will decide the Lead/Staff argument — a generic answer to "name someone you developed" costs more than a weak technical answer anywhere else in the loop.

**Three sentences that carry this entire track:**

1. *"What I left behind was [the standard], and [who] still has to clear it."* — the M beat, every time.
2. *"Sub-optimal and unsafe are different, and I only fight one of them."* — credibility economics.
3. *"I want to be precise rather than impressive here."* — deploy before any boundary admission. It converts a gap into evidence of judgment.


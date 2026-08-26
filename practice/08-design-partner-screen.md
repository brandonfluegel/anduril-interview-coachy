# 08 — Design Partner Screen: 30 Minutes with the Principal Designer (DS01–DS14)

The **Monday, August 31** embedded stakeholder screen — 30 minutes with **Tiffany Chen**, Principal Product Designer and Design Manager on Air Defense / Lattice. Rigor has already been ruled on. The only question here is whether a Ph.D. researcher is a fast, concrete design partner or a reviewer who shows up after the work and grades it. Her background — computer science, then Windows accessibility and assistive technology — means she thinks in mechanisms, states, and failure modes. Speak in the same units.

**Targets:** anchor **~90s** · main answers **60–75s** · follow-ups **45–80 words**. You get roughly twenty minutes of talking, so a 110-second answer costs you a whole topic.

> ⚠️ **Four boundaries.**
> **One — the 1:1 stays private.** Never quote Dr. Kim or reference coaching you were given. It shapes *how* you answer; it is never content.
> **Two — her public writing is a lens, not an icebreaker.** Don't name-check her essay or her plugin. Demonstrate the argument instead. One attributed reference is allowed, late, and only if she raises design philosophy first (DS03).
> **Three — assert nothing internal.** You don't know how their design system is structured, what the sprint cadence is, or what operators do in Lattice today. Each of those is a question, never a statement.
> **Four — no apology framing.** Never "I haven't worked with military operators, but…" Say instead: *"I've worked in high-consequence environments where a use error is irreversible — spaceflight medical operations, autonomous vehicle handovers. I'd rather be exact about what transfers and what doesn't."*

---

## The 30 minutes, blocked

| Minutes | What is happening | What you do |
|---|---|---|
| 0–2 | Her framing of the role | Listen for the words she uses for the operator. Reuse them all call. |
| 2–5 | "Tell me about yourself" | **DS02** verbatim. Stop at 90 seconds. |
| 5–20 | Her three or four real questions | **DS06–DS11**, or **DS12–DS14** if she goes at your current role. One example each. |
| 20–27 | Your questions | Ask three from the reverse set; hold one for the gap she opens. |
| 27–30 | Close | The close line at the end of this track. Do not re-pitch. |

**What she is scoring:** interaction-architecture reasoning · physical-digital ergonomics · information-density judgment · multimodal and handover reasoning · design partnership.

---

## DS01 — The Frame

**1. Constraints beat archetypes.** A persona summarizes a person; a constraint is a boundary the system has to satisfy. Work in the second currency — reach envelopes, time budgets, perceptual thresholds, error classes.

**2. Assistive-technology mechanics are high-stress interaction mechanics.** Unreliable input channel, feedback that has to confirm what the system *believes* it received, recovery cheaper than the error. An operator in gloves, at night, three targets deep is a temporarily impaired user by every definition that matters.

**3. Speed is a competency, not a compromise.** Every answer needs a "here's the version that fits in four days" branch. A researcher with only a good six-week answer is a scheduling risk.

| Do | Don't |
|---|---|
| Name what you'd hand her, and when | Describe a study design she didn't ask about |
| Give the four-day version | Present method as the point |
| Talk in states, edge cases, error classes | Talk in themes and generalities |
| Say "spaceflight medical operations," "four-second handover budget" | Say "I don't have combat experience, but" |
| Ask how something works at Anduril | Assert how something works at Anduril |
| Cede the solution space out loud, once | Sketch her a screen |

> **The sentence she should repeat in the debrief:** *"He gives designers something they can actually design from, and he's fast."*

---

## DS02 — The 90-Second Anchor

**Arc:** opening · **Target:** 90s · `PQ01` retuned for a designer.

> **Base:** Give me the quick version of your background.

### Model answer — memorize verbatim (~195 words / 80s)

> I'm a human factors engineer, and the through-line is that I work where a use error can't be taken back.
>
> My Ph.D. is in human factors psychology, on working memory and reaction time under high-stress interruption. Six years applied since then.
>
> Three things that are relevant to what you build. At NASA Langley I did human-systems integration on Lunar Gateway clinical workstations, running a use-error analysis against NASA-STD-3001 and MIL-STD-1472. Task time came down 30% and the critical input errors were eliminated by physical layout rather than by training.
>
> At Mercedes-Benz I studied Level 2 and Level 3 handovers, where a driver who is genuinely out of the loop has four to seven seconds to take back control.
>
> At Sling I'm Staff, and I own human factors across software, hardware, and AI. That's reach envelopes and physical fit on one side, and *Principles for Agentic Trust* on the other, for systems whose behavior isn't deterministic.
>
> What that adds up to for you is that I don't hand designers a report and walk away. I hand you insight you can iterate against, and what you do with it stays yours.
>
> Air Defense is where being wrong about attention actually costs something. That's why I'm here.

**F1 — "What would you be doing in your first month?"** *(~65 words)*

> Watching the flow before touching it, end to end, looking for where the interface competes with the mission instead of serving it. Then one thing fast: an edge-case and error inventory for whichever surface is closest to shipping, in your format rather than mine. I'd want that month judged on whether the document changed a screen, not on whether it was thorough.

**F2 — "Ph.D., patent, NASA. Which of those do I actually care about?"** *(~55 words)*

> None of them directly. What matters is the method underneath — establishing a human limit defensibly with a small sample, quickly. That's the constraint here too, because you're never going to have two hundred operators. The credentials are evidence I can do that. They aren't the thing itself.

### Senior → Lead/Staff

- **Senior:** gives a competent history and waits to be asked what it means for design.
- **Lead/Staff:** ends on the working relationship — *what I hand you, and what stays yours* — before she has to ask.

---

## DS03 — Pillar 1: Constraints Over Archetypes

**Arc:** her most likely philosophical probe · **Target:** 65s

> **Base:** How do you represent the operator to a design team? We're not really a personas shop.

### Model answer (~165 words / 66s)

> Good, because a persona is a compression artifact. It takes a distribution of real people and hands you a fiction with a name and a coffee preference, and the parts that got compressed out are exactly the parts that break the design — the tails, the degraded conditions, the moment somebody is doing three things at once.
>
> What I build instead is a task model and a constraint set. A cognitive task analysis gives you the decision sequence: what the operator has to know at each step, what they're holding in working memory, and what the interface is competing with for attention. Then the constraints get numbers, like the time budget for a decision or the point where added items stop being scanned and start being sampled.
>
> That's testable, and a persona isn't. If I tell you the assessment step has a four-second budget, you can hold me to it, and you can design against it without me in the room.

### The permitted attributed reference

Only if **she** raises the persona argument first. Say it once, then move on.

> You've written about that publicly, and the objection I'd add is that personas don't just lose accuracy — they quietly assume a nominal operator. In this domain the nominal operator is not the design case.

**Do not** say you read it if she hasn't opened the door, and do not say you enjoyed it. It is a claim about the argument, not a compliment.

### STAR — NASA Langley

- **S:** Lunar Gateway clinical workstations. Crew performing medical procedures in microgravity, with no evacuation option.
- **T:** As the human-systems integration contributor, establish what the workstation had to satisfy before anyone argued about layout.
- **A:** I ran a use-error analysis against NASA-STD-3001 and MIL-STD-1472 — every foreseeable use failure, its consequence, and how you would verify it was closed. I drove it down to physical reach and control placement rather than to a training recommendation, because training is what you reach for when the design can't be fixed.
- **R:** Task time down 30% and critical input errors eliminated — by geometry, not by vigilance.
- **Earned secret:** Compliance is the floor, not the argument. A standard only becomes useful when it's tied to a specific use failure.

### Senior → Lead/Staff

- **Senior:** critiques personas.
- **Lead/Staff:** replaces them with a task model the team keeps using without the researcher present.

---

## DS04 — Pillar 2: Rigor Into Things You Can Iterate On

**Arc:** the question behind every other question in this screen · **Target:** 70s

> **Base:** Walk me through what you'd actually hand me at the end of a study.

### Model answer (~180 words / 72s)

> Three things, and none of them is a deck that ends a project.
>
> First, a short insight report — what I saw, what I think it means, and how confident I am in each line. I want you reading my uncertainty, not just my conclusions.
>
> Second, a flow map of the operator's sequence with the failure points marked, showing where what the person expects and what the system is doing come apart. That becomes the shared object. When design and research disagree afterward, we find out we're disagreeing about the model rather than about taste.
>
> Third, an annotated list of interaction edge cases — the states nobody thinks about. A degraded feed, contradictory tracks, an alert landing mid-input, the operator coming back after ninety seconds away.
>
> I'd be clear about what those are, though. They're insight to iterate against, not requirements I'm handing down. You're the one who decides what the interface does about them, and I'd rather be in the room while you do that than get a link to the file afterward.

### STAR — Uber

- **S:** Drivers were navigating dense urban environments where the app was competing for attention against the road.
- **T:** Find out where the mobile interface was failing them in the field, not in a lab.
- **A:** I ran field studies in the actual environment, riding along and watching spatial-navigation behavior at the moments it broke down, then turned that into interface insight the design team iterated on over several releases.
- **R:** A 5% increase in driver retention.
- **Earned secret:** Nothing about that was findable in a usability lab. The failures were environmental, and you only see them where the work happens.

### The four-day version — volunteer this

> The heavier version of that is a controlled study, and I've run those — at Amazon I spent multiple years replacing arbitrary latency targets with measured perceptual thresholds. But the sprint version of the same logic is two days: one variable, the single interaction that's actually in dispute, six to eight people. You get a defensible answer by Thursday, it won't generalize past that interaction, and I'd say so.

### Senior → Lead/Staff

- **Senior:** produces excellent artifacts on request.
- **Lead/Staff:** produces the one artifact the team keeps opening after the project ends.

---

## DS05 — Pillar 3: High-Stress Accessibility and Error Prevention

**Arc:** the strongest bridge to her own background · **Target:** 70s

> **Base:** You've seen the environments this runs in. What actually breaks an interface out there?

### Model answer (~175 words / 70s)

> The framing I'd use is that a stressed operator is a temporarily impaired user, and that isn't a metaphor — it's the same mechanics. Under acute stress, working memory shrinks, attention narrows, and fine motor control degrades. That's what my dissertation was on. So the interface has to survive a user whose channels are worse than the ones it was designed for.
>
> Which makes the accessibility toolkit the right toolkit rather than an adjacent one. Redundant coding, because color alone fails at night and under adrenaline. Confirmation of what the system believes it received, because an unacknowledged input under load gets repeated. Target sizes set by gloved reach rather than by a mouse. And recovery that costs less than the error, so nobody is choosing between an undo and the mission.
>
> The failure I'd watch hardest is silent mode error — the operator acting correctly for a state the system is no longer in. That one doesn't show up in usability testing. It shows up in an incident.

### The hardware boundary — say this next

It is the part most researchers don't have, and it is half of what she works on.

> The other thing I'd say is that the screen isn't the system. Whatever this runs on — a tablet in gloved hands, something vehicle-mounted, a display at a fixed site — the hardware sets the constraint before the layout gets a vote. Mount angle, glare, one-handed reach, and the fact that a person under load presses harder and faster than anyone in a usability lab ever does.
>
> What I've watched happen in every hardware program I've worked on is that an illegible interface state gets escalated physically. Nothing acknowledges the input, so the operator taps again. Still nothing, so they press harder. Then they start hunting for a power button. Each of those is a rational response to an unreadable state, and each one leaves the system worse off than the original delay did — a power cycle to clear an ambiguous state costs you the whole session at the moment you can least afford it.
>
> So the insight I'd want in front of you is a single line: acknowledgment and completion are two different signals, and collapsing them is what manufactures double-actuation.

> ⚠️ You do not know the hardware envelope here. Say *"whatever this runs on"* and then ask — that is what **RQ4** is for.

### STAR — Mercedes-Benz

- **S:** Level 2 and Level 3 handovers in a high-fidelity simulator, with the driver genuinely out of the loop and four to seven seconds to take back control.
- **T:** Determine which alert modality actually restores control, not just attention.
- **A:** I decomposed takeover latency into hands-on-wheel, eyes-on-road, and first control input, because a single reaction time hides which stage failed. Multimodal alerts against auditory-only, haptic-only, and a visual baseline.
- **R:** A 24% improvement in safety and trust ratings for the multimodal condition.
- **Earned secret:** A handover transfers situation awareness, confidence, and control — not a notification. Alerting faster doesn't help if the operator hasn't rebuilt the picture.

### The Anduril bridge — say it unprompted

> That transfers because an operator handing control back and forth with an autonomous system is running the same sequence, at higher consequence and with more agents demanding attention at once. What doesn't transfer is the timeline and the adversary. A car doesn't have one.

---

## DS06 — The Sprint-Speed Question

**Arc:** her most probable opener after the pitch · **Target:** 65s

> **Base:** Design locks Friday. It's Monday and I have one operator for thirty minutes. What do you do with it?

### Model answer (~150 words / 60s)

> I don't run a study, I resolve the one disagreement blocking the lock. So the first thing I'd need from you is which decision is actually open, because thirty minutes of operator time buys one answer and a pile of context.
>
> Then it's a structured walkthrough on the real build, not an interview. I'd have them narrate a task they've done a thousand times while I time the decision points and mark every place they hesitate, back up, or ask the screen a question it can't answer. Hesitation is the signal. Stated preference isn't, not in thirty minutes.
>
> You'd get notes the same day rather than a readout: the edge cases that surfaced, the one thing I'd change before Friday, and what I still don't know. Everything left over goes in a backlog tagged with the decision it would unblock.

**F1 — "What if there's no operator available at all?"** *(~65 words)*

> Then I say that out loud and we decide on the best available basis instead of pretending otherwise. I'd run a cognitive walkthrough against the task model with two internal proxies, label the conclusion as inference rather than evidence, and make sure the thing reports on itself once it's in front of real users. What I won't do is launder a walkthrough into "research shows."

**F2 — "You'd really ship on that?"** *(~50 words)*

> Yes, with the risk named. Most design decisions are low-consequence and reversible, and blocking those on evidence costs more than being wrong. The irreversible ones are where I'd hold the line, and in any given flow there are usually two or three of them, not thirty.

---

## DS07 — The Research–Design Friction Question

**Arc:** partnership test · **Target:** 60s

> **Base:** Tell me about a time your research contradicted a design direction someone was already committed to.

### Model answer (~165 words / 66s)

> The one I'd pick is the frictionless-experience argument, because I lost the first round of it.
>
> The prevailing position was that every confirmation step is a defect — count the taps, remove the taps. My evidence said the opposite for one class of action. Where the action is irreversible and the system's confidence is low, removing the checkpoint doesn't buy speed, it buys automation bias. The operator stops evaluating and starts executing.
>
> Arguing it as a principle got me nowhere. What worked was making it risk-proportional and explicit: irreversible actions behave one way, reversible ones behave another, and the classification is written down so it's predictable rather than arbitrary. That gave design a consistent rule instead of a consistent pattern, which is what consistency was protecting anyway.
>
> I'd flag honestly that this is a thesis I've argued, not a result I've deployed at scale. I call it Calibrated Cognitive Friction, and this is the kind of place where it would actually get tested.

**F1 — "How do you tell me a design I've spent three weeks on doesn't work?"** *(~65 words)*

> Early, directly, and about the constraint rather than the artifact. Early is the part that matters, because the cost isn't being told — it's the three weeks spent after I already knew and was working out how to say it. And framed as "here's the constraint this runs into," which is a shared problem, rather than "this doesn't work," which buys you a defense instead of a revision.

**F2 — "When has a designer been right and your data wrong?"** *(~105 words / 42s)*

Conceding this well is what makes everything else you've said about partnership credible.

> At Amazon I had eye-tracking data showing a region of an interface that people simply weren't looking at. My read was salience — make it louder, move it up. The designer's read was that the region was fine and the problem was where it sat in the task sequence, so it was never in the scan path at the moment it mattered. She was right, and the fix was sequence rather than styling.
>
> What I took from it is that my measurement was authoritative about where the failure was and had nothing to say about why. She was reading the state model. I was reading a distribution.

> ⚠️ The gaze evidence is canonical. Attributing the diagnosis to a specific designer is *your recollection* — if you can't place the conversation, say "a designer on the team," and never quote words you aren't sure of.

---

## DS08 — The Non-Deterministic UI Question

**Arc:** the question her Anduril context makes unavoidable · **Target:** 70s

> **Base:** How do you evaluate an interface when the system underneath it doesn't behave the same way twice?

### Model answer (~170 words / 68s)

> You stop evaluating outputs and start evaluating whether the operator's trust is calibrated to how reliable the system actually is. That's the measurable thing.
>
> Concretely, that means two error rates rather than one. The times an operator accepted a recommendation that was wrong, and the times they overrode one that was right. Those are different failures with different fixes, and a single accuracy number hides both. Then I'd look at whether the interface's expression of uncertainty actually moves behavior, because if confidence is displayed and reliance doesn't change with it, the display is decoration.
>
> The framework I wrote at Sling splits trust into four things people usually collapse into one: does the system intend the right goal, does it execute reliably, can I still take control, and does it tell me how sure it is in time for me to intervene. Alignment, execution, control, calibration.
>
> What that gives you as a designer is that "make it trustworthy" becomes four separate things to design for instead of a vibe.

**F1 — "What would you look at first on an autonomy display?"** *(~60 words)*

> Whether operators can tell at a glance what mode the system is in and what it currently believes. Mode error is the highest-consequence failure in every automation domain I've worked in, and it precedes every other problem you'd want to study. If the state isn't legible before the operator commits, nothing downstream of that is worth measuring yet.

**F2 — "Does that change on a device in the field instead of a desk?"** *(~70 words)*

> Substantially, and it's the part I'd look at first. On fielded hardware, three different conditions produce the same visual signature — the system is thinking, it's waiting on data it isn't getting, or the device is wedged. The right response differs in each case, and if the display can't separate them, people default to the physical remedy: press again, then power-cycle.

---

## DS09 — The Domain Transfer Question

**Arc:** the challenge · **Target:** 60s · **No apology form. Ever.**

> **Base:** Everything you've described is a lab, a car, or a consumer device. Why should I believe any of it holds for an operator under fire?

### Model answer (~145 words / 58s)

> I'd separate what transfers from what doesn't, because both answers matter.
>
> What transfers is the human under load. Working memory doesn't get bigger because the stakes went up, it gets smaller. Attention narrows, motor control degrades, and mode error becomes more likely rather than less. The spaceflight medical work was irreversible-consequence, and the handover work ran on a four-second budget with a genuinely out-of-the-loop human. Those are the two mechanics that matter here, and I've measured both.
>
> What doesn't transfer is the domain content, and I won't pretend otherwise. I don't know the doctrine, the timeline, or what an operator's day actually looks like, and that's a curve I'd close by watching rather than by reading.
>
> So I'm not claiming the operator's world. I'm claiming the limits of the human sitting in it.

**F1 — "How fast do you close that curve?"** *(~50 words)*

> Weeks to be useful, months to be right. The accelerant is task observation, because an hour watching someone work beats a week of documents. I'd also expect to be corrected early and often, and I'd rather be corrected than be careful — careful is slow, and slow is the real risk.

---

## DS10 — The Scoping Question

**Arc:** speed and judgment · **Target:** 60s

> **Base:** What do you cut when a study won't fit in the time you have?

### Model answer (~145 words / 58s)

> The rule I use is cut scope, never cut controls. One interaction with the confounds handled is useful. Six interactions with the confounds loose isn't a smaller finding, it's a wrong one, and a wrong number travels faster than no number because it's quotable.
>
> So the order is conditions first, then participants, then how far I'll generalize — and I say what got cut, out loud, in one line. Sample size is more negotiable than people think when the design is within-subjects and the effect is perceptual. Six to eight people will find a threshold. Six to eight people will not find a preference.
>
> What I never cut is the falsifier. Before I run anything I write down the result that would tell me I'm wrong. Without that, a study isn't shorter, it's theater.

**F1 — "What's the smallest thing you'd call real research?"** *(~45 words)*

> Five structured task observations against a build, timed, with the errors classified. That's a day of work and it will change a design. What it won't do is establish a rate — and knowing which of those two I'm being asked for is most of the job.

---

## DS11 — The Level Question, If She Raises It

**Arc:** only if she opens it · **Target:** 45s · Argue from scope, never from title. Do not raise this yourself.

> **Base:** You're currently Staff. This is posted at Senior. Is that going to be a problem?

### Model answer (~110 words / 44s)

> Not for me, and I'd rather be direct about why.
>
> I'm optimizing for the consequence class of the problem, not the label on it. The scope I'd want is the same either way — I want to own the questions the team keeps running into, not just the studies, and what outlasts me should be a shared way of thinking about the operator.
>
> If that scope is available here, the title is bookkeeping. If it isn't, I'd rather have that conversation now than in a year. Either way it doesn't change what I'd do on Monday.

> ⚠️ Never raise compensation, location, travel, or clearance. All four are settled. If she raises one, answer in a sentence and go back to the work.

---

## DS12 — Sling: Agentic AI Without Slowing the Sprint

**Arc:** current-role probe · **Target:** 70s · She is checking whether your framework work is a tax on velocity.

> **Base:** You're doing AI trust work at Sling. How does that survive a two-week sprint?

### Model answer (~155 words / 62s)

> By making it something you check at design time rather than something you study afterward. That was deliberate. If the only way to know whether an agentic feature is trustworthy is to run research once it's built, the framework doesn't survive contact with a sprint, and it shouldn't.
>
> So *Principles for Agentic Trust* is four questions you can ask of a design in a review. Does the system intend the right goal, does it execute reliably, can the user still take control, and does it say how sure it is in time for someone to intervene. Alignment, execution, control, calibration.
>
> Each one fails differently and each one shows up somewhere specific in the interface, which is what makes it fast — an hour in a critique rather than a sprint of work. It's peer-reviewed at CSCW 2026, but I'd be clear that I've used it as a review instrument. I haven't validated it as a measure of deployed trust.

**F1 — "Where has it actually changed something?"** *(~50 words)*

> Mostly at the control and calibration ends — moving behaviors out of silent action into acknowledge-or-undo, and pushing a system that had one confidence display to say what the confidence was about. It changed design decisions. It didn't produce a measured trust outcome, because I haven't measured one.

---

## DS13 — Sling: Framework Work vs. Hands in the Work

**Arc:** the down-level probe in disguise · **Target:** 65s

> **Base:** At Staff level, how much of your time is actually hands-on versus setting direction?

### Model answer (~150 words / 60s)

> More hands-on than the title implies, and I want it that way.
>
> A normal week at Sling has reach-envelope modeling and physical fit work in it — anatomical limits, what a person can operate without looking — plus usability criteria for latency, feedback, and spatial layout. That's tactical work. It has millimeters and milliseconds in it.
>
> The framework work only exists because of that. *Principles for Agentic Trust* came out of hitting the same wall in ordinary design reviews, where the usability methods I had were built for deterministic systems and I was being asked to weigh in on ones that weren't. Written without the hands-on work, it would have been a literature review.
>
> So I'm doing the tactical work either way. The Staff part is just that I try not to solve the same problem twice.

**F1 — "So what would you not want to be doing here?"** *(~45 words)*

> Nothing on the list, honestly. What I'd push back on isn't a task, it's a pattern — being brought in after the decision to validate it. Give me the ugly part of the flow early and I'll take whatever method it needs, including a stopwatch.

---

## DS14 — Sling: Why Leave, in Design Terms

**Arc:** motivation probe · **Target:** 55s · Say it without a word against Sling.

### Model answer (~135 words / 54s)

> The honest answer is the consequence class of a user error.
>
> The methods I use at Sling are the same ones I'd use here — same task analysis, same thresholds, same criteria. What's different is what happens when I get it wrong. There, a bad interaction costs someone a few seconds and some goodwill. I take that seriously, but nothing in that environment forces the answer to be right.
>
> I've spent the rest of my career in places where it was forced, like spaceflight medical operations and automated driving handovers, and that's the constraint I do my best work under.
>
> The argument I care about — that friction should be proportional to consequence — stays a thesis anywhere the consequences are small. It only gets tested somewhere it matters.

**F1 — "Everyone says they want fast-paced. What makes you think you'd like it here?"** *(~50 words)*

> Because the pace I dislike is the one with no decision at the end of it. I've worked in slow places where the slowness was deliberation and slow places where it was diffusion, and only the second one is intolerable. A short deadline with a clear decision owner suits me.

---

## Reverse interview — 5 to 7 minutes

Ask **three**, and hold one back for whatever she opens up. Each is a question about her world, never a statement about it. Write the answers down — they are your follow-up email.

**RQ1 — Where the design system strains.**
> Where does the design system currently force a compromise you're not happy with in the densest views? I'd rather bring evidence where it's already contested than where it isn't.

**RQ2 — The friction point she'd name herself.**
> If you mapped an operator's attention across detection, assessment, authorization, and intervention, where do you think the interface competes with the mission instead of serving it? I want to hear your read before I form my own.

**RQ3 — The working cadence.**
> Where would research actually plug into your week, and what would you want in your hands? Some designers want a raw edge-case list mid-sprint; some want a synthesized model at the start of the cycle. Those are different jobs and I'd rather do the one you need.

**RQ4 — Degraded conditions, codified or re-litigated.**
> How much of the degraded-conditions envelope is codified as a design constraint versus re-argued screen by screen? I mean gloved input, low light and glare, noise, sustained wear — the things that set target sizes and contrast before anyone opens a layout.

**RQ5 — The gap between intent and use.**
> What's something design shipped that operators ended up using differently than intended? That tells me more about where research is worth spending than a roadmap does.

---

## The close

Do not re-pitch. One sentence, then let her end it.

> The thing I'd want you to take from this is that I'm not going to hand you research and ask you to interpret it. I'll give you insight you can iterate against, fast enough to be useful, and the design stays yours.

---

## Drill sheet

**Priority order if you only rehearse three:** DS02, DS04, DS06. Those are the three she is most likely to ask and the three that decide the debrief line.

**Confirm before Monday:** the designer attribution in DS07 F2. Everything else in the track is resume-canonical.

**Cut first if you're running long:** the second half of any STAR block. She needs the situation and the result; the method detail is follow-up material.

**Six sentences that carry this entire screen:**

1. *"I give designers something they can iterate against, not a verdict."*
2. *"A persona is a compression artifact, and the parts that get compressed out are the parts that break the design."*
3. *"A stressed operator is a temporarily impaired user, and that's mechanics, not metaphor."*
4. *"An illegible state gets escalated physically — tap again, press harder, power cycle."*
5. *"Cut scope, never cut controls. A wrong number travels faster than no number."*
6. *"I'm not claiming the operator's world. I'm claiming the limits of the human sitting in it."*

**Monday morning, three minutes.** Say DS02 once against a timer, read the Do/Don't rows you're most likely to violate, then stop preparing.

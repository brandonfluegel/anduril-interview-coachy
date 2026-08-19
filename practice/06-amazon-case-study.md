# 06 — Amazon Latency Case Study (AC01–AC11)

**This is the primary case for the 45-minute hiring manager conversation with Dr. Daniella Kim.** NASA moves to second position — a 55-second module you deploy yourself, covered in AC09.

**Why this case, and not NASA.** Kim is judging rigor, speed, whether you set direction, whether your work outlasts you, and whether you can move people who outrank you. The latency program hits all five, and you ran it. The posting's Lead/Staff language — *"bridges engineering latency with human perception," "translates findings into hard specifications"* — describes this program.

**Timings** are counted from the text at 150 words a minute, not estimated. **How to say it:** short sentences, one idea each; define any technical term in the next breath, in words a product manager would understand.

> **Confidentiality — a scoring dimension, not just ethics.** The source reports in `references/` are former-employer confidential. Never speak an internal codename, dashboard, percentile table, competitor benchmark, or any figure other than the ~$50M on your resume. Kim is judging whether you'd be careful with *her* data, and this failure is silent. Say the discretion out loud once, early: *"I'll go into detail on method and thresholds, and keep the internal figures and the competitive benchmarking out of it."*

---

## Two-Day Plan

**Memorise one thing: the eight triggers in the AC01 table.** Say them in order until you can do it in fifteen seconds — the words then fill themselves in, because you already know this work and are only learning the running order. **Never memorise the script sentence by sentence;** a memorised paragraph sounds memorised.

**Day 1** — read AC01–AC02 once, no notes (30 min) · learn the eight triggers (20) · record the presentation three times, check the clock (40) · read the AC10 boundaries (20) · say the NASA module twice (15).

**Day 2** — the five core layers cold, 90s each (30 min) · AC03 F1 and F2 (20) · the off-case four in AC07 (20) · the tier ladder and level guidance (15) · pick two questions from AC11 (10) · one full mock, then stop (20).

**Drill Layers 1–5 only.** The reserve list is read-once. AC04–AC06, AC08 and AC10 are judgment rather than lines. **Two hours total?** The eight triggers, Layer 4, the "never assert" list, and the level guidance in AC06.

---

## AC01 — The 3-Minute Presentation

**Arc:** opening of the conversation · **478 words = 3:11. Cut beat [2] and it's 446 = 2:58 — do that by default.** Never cut [4], [6], [7] or [8].

> **Base:** Walk me through a piece of research you led, end to end. Take about three minutes.

### The eight triggers — memorise this column, not the script

| # | Trigger | The job it does | ≈ |
|---|---|---|---|
| 1 | **Wrong goal** | The company chased the wrong target. Say it flat. | 20s |
| 2 | **Nobody could define it** | "Fast enough" was undefined. *Cut this one first.* | 13s |
| 3 | **Numbers, not opinions** | Your charge, in first person. | 9s |
| 4 | **Simplest method** | Constant stimuli, and the staircase you turned down. | 44s |
| 5 | **Depends — both ways** | Task-dependent, and a floor as well as a ceiling. | 25s |
| 6 | **Four things** | Never one number. **This beat shows the level.** | 25s |
| 7 | **Renamed it** | The spec, the ~$50M, the metric that outlived you. | 23s |
| 8 | **Workload** | Air Defense, and the limit of your own evidence. | 25s |

### Model script (478 words / 3:11 · 446 / 2:58 without beat [2])

> **[1]** Short version: a very large engineering organization was chasing the wrong goal, and my job turned into proving it. Everyone treated response delay as a number to push toward zero. There's no single right answer. It depends on what the person just asked for — and past a point, faster does harm.
>
> **[2]** The hard part was that nobody could define "fast enough." So targets got set by whatever engineering could build, and the same argument came back every review with nothing to settle it.
>
> **[3]** My job was to produce numbers strong enough that engineering would treat them as requirements rather than a researcher's opinion.
>
> **[4]** I used the simplest method in psychophysics — constant stimuli. Pick a fixed set of delays, play them in random order, ask the person to judge each one. Enough repetitions and you can draw the curve connecting delay to reaction.
>
> Twelve kinds of interaction, six delays, half a second to three. That's seventy-two combinations, three passes each — about two hundred trials a person.
>
> Three answers after every trial: not slow, somewhat slow, too slow. Not a seven-point scale. People don't notice speed, only slowness — so I measured the thing that exists.
>
> There's a faster method called a staircase. I turned it down. It finds one point on the curve. I needed the whole curve.
>
> **[5]** Two findings. The right delay depends on the task. Anything with a real-world equivalent — a light switch, a notepad — has to land near half a second or it feels broken. Looking something up gets twice as long. And I set a limit the other way: when a spoken answer beats a human's, it stops feeling responsive and starts feeling wrong.
>
> **[6]** The part I'd want you to push on is what I handed over. Never a single number. Every spec carried four things: the delay, my confidence in it, how steep the curve was there, and which mode and workload it applied to. On a steep stretch, a hundred milliseconds decides fine versus not fine. On a flat stretch it's noise. That tells you where the money goes.
>
> **[7]** What I left behind is the part I'd point at. Two numbers per interaction became the criteria the organization designed against, and about fifty million dollars in operational value was attributed to the program. I also got a company metric renamed, because its name assumed the real delay and the felt delay were the same thing. Both outlived me.
>
> **[8]** It carries over directly — a threshold is a threshold. Where it stops: my people were customers, not trained operators, and I held workload steady instead of varying it. The version that matters here turns workload up and down. That's the study I'd want, and it's why counter-drone is the problem I want. The timeline squeezes until you have to decide in advance what the human is for.

### What Kim repeats afterwards — the actual test

She won't replay your case to the panel. She'll compress 45 minutes into two or three sentences, from memory, days later. Those sentences *are* the output, so engineer them:

1. *"He turns human limits into numbers engineers can build to — and ships them with error bars instead of opinions."* → beat **[6]**
2. *"He killed a company-wide assumption and got the metric definition changed. That's still there and he isn't."* → beat **[7]**
3. *"He told me where his own evidence runs out before I had to ask."* → beat **[8]**

**The sentence that means you failed:** *"Strong researcher, ran a big study, got a good result."* Entirely positive — and a Senior review. Excellent execution is the baseline expectation, not the bar.

| | Senior sounds like | Lead/Staff sounds like |
|---|---|---|
| **Finding** | "The acceptable delay is X." | "The question was wrong. There isn't one delay." |
| **Delivery** | "I recommended a target." | "I shipped a criterion with error bars." |
| **Legacy** | "They adopted my recommendation." | "The definition changed and stayed changed after I left." |
| **Limits** | Answers honestly when asked. | Says it first, and turns it into the next study. |

**Structural test:** delete beat [7]. If the story still feels finished, you told it as a Senior.

---

## AC02 — The Deep-Dive Layers

Three minutes is the presentation. The other forty are these. **Drill the five below; the reserve list at the end is read-once.** One layer per question — never chain two.

### Layer 1 — Why the simplest method, and why not the fancier one

**This is the confidence answer. Say it without a hint of apology.**

> I used the oldest, plainest tool in the box, and that was a choice, not a default.
>
> The efficient alternative is a staircase — it moves the delay based on your last answer, so it homes in on a threshold in far fewer trials. I turned it down for three reasons. It finds one point on the curve, and I needed two: a "good enough" line and a "genuinely good" line. It's accurate about where the line is but poor at how steep the curve is there, and the steepness was half of what I owed people. And it's harder to explain to the engineers who have to accept the number, which matters more than it should.
>
> So I spent more trials and got the whole curve back — which let me read off whatever line the spec needed, including ones nobody had asked for yet.

**The line to land it:** *"I'd rather use the simplest method that answers the question and put the effort into what I do with the results. The clever part shouldn't be the procedure."*

### Layer 2 — Why thirty people is enough

**The other question she's most likely to ask. Have it word-perfect.**

> The precision comes from the trials, not the headcount. Everybody saw every delay, so each person acts as their own comparison. Seventy-two combinations, three passes each, about two hundred trials — and three passes is the number that matters, because it's what let me fit a curve for each individual person rather than only for the group. The thirty people set how much the threshold varies from person to person, and that variation is exactly what I reported rather than hiding it.
>
> I also priced the alternative and argued against it in writing. Tightening that range meant roughly ten times the people, six to twelve months, and several hundred thousand dollars. The decision I had to serve was which interactions to fix first and how far. The differences driving that were big. A tighter range would have moved the error bars and changed nothing about what we did.
>
> I bought a decision, not a publication. And I said out loud which one I was buying.

### Layer 3 — Mode and workload

> Two things I controlled instead of letting them drift.
>
> First, the mode. A spoken response and a response you see on screen have different thresholds. Average them together and you get a number that's wrong for both. So every threshold I published named the mode it applied to.
>
> Second, workload. I ran the judgments while people were doing something else, not sitting there with nothing to do. It was a light visual monitoring task on a second screen — watch for a shape to change, press when it does. Deliberately dull, because I wanted the low-grade busy of someone half-occupied in a kitchen, not a hard cognitive test. The difficulty was fixed, the same for everyone, set from a short practice block.
>
> I used the NASA Task Load Index after each block to check the load actually landed where I'd aimed it and didn't drift between conditions. That's what it's for — confirming the setup worked, not serving as the result.
>
> The honest limit is that I held workload steady rather than turning it up and down. So I have the threshold at one setting, not across the range. That's the next study, and it's the one that matters when the person is an operator.

**Why this layer is load-bearing:** it is your cleanest bridge to Air Defense, because operators under load *is* the domain. Naming that you controlled workload, and that the obvious next step is to vary it, turns a limitation into a proposal.

### Layer 4 — Why you never ship one number

**Deploy when she asks what you actually delivered, or how research turns into a requirement.**

> I stopped handing over single numbers, because a single number just starts an argument about the number.
>
> Every spec went out with four things: the line itself, how confident I was in it, how steep the curve was at that point, and which mode and workload it applied to.
>
> Two things changed because of that. Because there was a confidence range, I could tell engineering to build against the cautious end rather than the middle — which is what you do when being wrong in one direction costs more than the other. And because there was a steepness number, they could see where the cliffs were. Steep stretch: a hundred milliseconds is the difference between fine and not fine, and that's worth real engineering money. Flat stretch: it's noise, spend it somewhere else.
>
> That's the habit I'd bring here. One number tells you where the line is. A line plus a range plus a slope tells you what it costs to miss it — which is the question anyone working to a schedule is actually asking.

### Layer 5 — The speed limit in the other direction

**Your most valuable thirty seconds. See AC08 for how to spend it.**

> For spoken answers I had to set a lower limit as well as an upper one. A response that comes back faster than a person would answer stops feeling responsive and starts feeling wrong. That's the finding that made me stop believing faster is always better.
>
> The curve has two edges, not one. Both are real. If you only ever optimize in one direction, you'll walk off the far edge and have nothing measuring to tell you that you did.

### Reserve — read once, don't drill

- **Why psychophysics, not analytics.** Telemetry tells you what happened after a slow response; it can't tell you where the line is, because the line is in the person, not the logs. Psychophysics gives a number you can put in a requirement.
- **Why the answer depends on the task.** People benchmark a light switch against the switch, not the software. That killed the single company-wide target and replaced it with a number per interaction — a very different roadmap.
- **The metric rename.** Its name described a measured interval but was worded as what the customer *felt*, silently assuming the two were the same thing — the exact assumption my data disproved. A definition shapes every argument afterwards.
- **Two methods that fail differently.** A partner team's economic model and my controlled study shared no assumptions and agreed anyway. Better two imperfect methods that break in different directions than one strong method with a blind spot.
- **Measuring mental effort directly.** fNIRS plus eye tracking: effort differences tracked how cluttered people said each interface was, and gaze showed regions nobody looked at. The value isn't beating self-report, it's not interrupting. **Never imply it outperformed NASA-TLX — no head-to-head exists. The claim is convergence and non-reactivity.**
- **The patent.** Context-based control inputs — the same button does different things depending on what's on screen. Same move as the latency work: what a signal means is a property of the situation, not the signal.

---

## AC03 — Kim Follow-Ups: Rigor and Velocity

**F1 — "Constant stimuli and a three-point scale. That's a fairly basic design for a multi-year program."**

> It is, and that's on purpose. The design is simple; what I did with the results isn't. I drew the full curve for every condition, published lines with confidence ranges and steepness rather than bare numbers, and named the mode and workload each applied to.
>
> The fancier designs would have been faster and given me less. A staircase finds one point well and tells you little about the shape around it — I needed two points and the shape. I'd rather be plain in the procedure and demanding in the analysis than the other way round.

**F2 — "Thirty people. Convince me that's not just a number you could afford."**

> The estimate doesn't rest on thirty. It rests on about two hundred trials each — seventy-two combinations, three passes — with everyone seeing every delay, so each person is their own comparison. Three passes is what let me fit a curve per person rather than only across the group.
>
> What the thirty buys is how much the line moves between people, and I published that spread rather than burying it. I also priced the alternative: ten times the people, six to twelve months, several hundred thousand dollars, for a tighter range on a decision that was already clear. I argue against studies that can't change a decision.

**F3 — "What's the weakest part of that study? Not the limitation section — the part that actually worries you."**

> The controlled setting. I stripped out everything that happens alongside delay in real life — the light ring, the sounds, background noise, the fact that people are usually busy. Those aren't nuisances, they probably change the answer, so my numbers are off in one direction and I can't tell you which.
>
> The second thing is that I measured a judgment, not a behavior. Someone can tell me a response was fine and still quietly use the product less. My design can't see that gap.

**F4 — "If you re-ran it today with no constraints?"**

> Workload as a factor instead of a control, so I get the threshold across the range rather than at one point — that's the version that applies to an operator. The visual and auditory feedback back in as factors, because that's where I think the remaining budget sits. And a behavioral measure alongside the judgment, so the spec doesn't rest on one response type.

**F5 — "What did you get wrong?"**

> I framed the first deliverable as a single global threshold, because that's what I'd been asked for and it was easiest to adopt. The data didn't support it and I had to restructure the whole recommendation around interaction type. The lesson is that the shape of the deliverable is itself a research decision — I'd pre-committed to an answer format before I knew the answer's shape.

---

## AC04 — Evidence Tiers, Cadence, and Ambiguity

### The evidence ladder

**Your answer to "how would you actually work here."** It solves the problem every fast company has: research is either quick and untrustworthy, or trustworthy and too late. Tiering fixes that by putting the strength of the claim on the artifact itself.

| Tier | Time | What it is | What it's allowed to decide | What it's never allowed to decide |
|---|---|---|---|---|
| **Directional** | Days | A rough read — a few people, existing research, a quick check. A best guess, no precision claimed | Which way to lean, what to prototype, what to stop building | A spec, a freeze, or a number anyone quotes in a review |
| **Threshold-grade** | Weeks | The real curve for a condition, with a confidence range and a steepness, named to a mode and a workload | A design target, a budget, a roadmap priority | A release gate by itself |
| **Decision-grade** | Longer, and rare | Threshold-grade, repeated in the real operating setup, with a stated way it could be proven wrong and a plan to watch it in the field | Acceptance criteria and sign-off | Anything outside what it was measured on — the scope is part of the claim |

**Two rules that make this real rather than decorative.** The tier is *written on the artifact*, not remembered — a rough number that loses its label becomes a hard number within about two weeks, and nobody lied. And rough findings *expire*: each carries a date and the tier it's waiting for, so it never quietly becomes fact.

> The discipline isn't the three tiers. It's that the label travels with the number. What actually rots an evidence base is a rough finding quietly getting promoted while nobody's watching.

### Cadence, and the three gates

**"How do you deliver something useful before the rigorous answer exists?"**

> By shipping the rough version on a schedule and being loud that it's rough. Engineering needed a target long before I had a defensible curve, so I gave them a provisional band with the tier written on it and a plain statement that it would move. It did move — and because the label was on it, that was an update rather than a retraction. That's the whole difference.
>
> Something lands every couple of weeks. If research goes quiet for a quarter and reappears with the truth, the roadmap has already worked around you and your truth arrives as an obstacle.

> *A wrong number labeled provisional is a working agreement. A wrong number labeled final is a credibility event. The label does more work than the number.*

**"How do you decide what research not to do?"** — three gates.

> One: name the decision. If I can't write "this determines whether we do X or Y," it's curiosity, and curiosity gets a memo. Two: name in advance what result would change the decision and in which direction — if every outcome leads to the same action, I've found an expensive way to feel confident. Three: cost the precision. Most requests for a bigger sample are requests for reassurance, and reassurance is cheaper to buy other ways.

**"Nobody can tell you what the research question is. Week one?"**

> I start with the arguments, not the users. I look for decisions being settled by seniority, by intuition, or by whoever is loudest in the review — that's where evidence has leverage, and it's visible within days. The latency work came from exactly that: the same argument kept recurring and never resolved, because there was nothing solid it *could* resolve against. A recurring unresolved argument is a research question with the label torn off.

**"A stakeholder wants a study to confirm a decision they've already made."**

> I ask what they'll do if it comes back the other way. If the honest answer is "ship anyway," I say so and offer to spend the money on something genuinely undecided — which goes better than it sounds, because most people know they're doing it. The gate is falsifiability of the decision, not of the hypothesis.

---

## AC05 — Stakeholder Management and the Multi-Year Arc

**"Walk me through how a multi-year program actually stayed alive."**

> About three years, in three phases, and sequencing was most of it.
>
> Phase one was a few months and deliberately the smallest thing that could settle a live argument — a rough band on the highest-traffic interactions, labeled as rough. The fastest way to lose a multi-year program is to ask for multi-year funding on day one.
>
> Phase two was the real curves, per interaction and per mode, and that's where the two-number spec came from. By then engineering wanted it rather than tolerated it, because phase one had already been useful to them.
>
> Phase three added workload and the mental-effort instrument, and moved from measuring what shipped to setting targets for things that hadn't launched. Each phase came out of the questions the previous one couldn't answer, and I kept that list written down — the open-questions list is what made it read as a roadmap rather than a series of requests.
>
> I ran it with the performance-engineering group and an economics team, and made sure their modeling and my perceptual data were argued together rather than competing. Two teams with one recommendation is a different object in a review than two teams with adjacent findings.

**"Who disagreed with you, and how did it resolve?"**

> The sharpest one was in a design review, over the half-second target for the smart-home commands. A principal engineer's position was that this is a hardware feasibility question, that research should report how satisfied people are and let engineering decide the target — describe, don't constrain. It wasn't an unreasonable position.
>
> I didn't win it by arguing. I won it by rewriting the recommendation as a pass/fail test: measure the fleet against the stated band, and either it clears or it doesn't. The moment a criterion has a test attached it stops sounding like an opinion. I also gave ground where he was right — that's where the second, looser band came from, so engineering had something to prioritize against instead of one number to miss.

---

## AC06 — The Level Move: The Mechanisms

Kim's own stated bar is *"how would you build a research function whose standards survive after you leave?"* You have four real answers. **Pick the two that fit the question. Never recite all four as a list.**

> **The spec.** "Two numbers per interaction, each with a pass test attached — not a suggested target, a line the hardware has to clear. That's what engineering builds against, and it works with me out of the room."

> **The definition.** "I got a company metric renamed, because its name assumed something my data had disproved. It's the least impressive-sounding thing I've done and the one I'm proudest of. A definition shapes every argument that comes after it."

> **The instrument.** "The mental-effort setup was built as a capability, not a study — something other researchers could point at their own questions. The point was to leave behind a tool, not a result."

> **The evidence ladder.** "Every artifact says what it's allowed to decide and what it was measured on, so a rough read can't quietly turn into a spec. That's the one I'd set up here first. It costs a week, and it's what lets research move fast without getting caught out later."

**One more, and don't forget it's available.** Amazon is where you did the work. **Sling is where you have the scope right now**, and it's the strongest level evidence you own — you are Staff there today, you built the human factors function from nothing, and you own specs across software, hardware, and AI. Use it whenever the question is about scope rather than craft:

> "At Amazon I owned a program. At Sling I own the function — I built it from a standing start, and I write the specs across software, hardware, and AI. That's the scope I'm arguing for here, and it's the one I'm doing now rather than the one I did four years ago."

### The first-ninety-days answer — where level actually gets decided

**She will ask some version of this.** Answer with what you'd *own*, not what you'd learn. A list of things you'd read is a Senior answer.

> The first few weeks I'd spend on the arguments rather than the users — finding the decisions currently being settled by whoever is most senior in the room, because that's where evidence has leverage and it shows up fast.
>
> Then one thing installed, not five. The tier language: every research artifact says what it's allowed to decide and what it was measured on — which mode, which workload, which kind of operator. That's about a week of work and it changes behavior immediately, because a rough number can no longer quietly harden into a spec.
>
> And one study started that could actually come out against me. I'd rather be six weeks into a question that might overturn something than three months into a survey nobody disputes.

**Why this lands the level:** it names a mechanism other people run, it sets a standard rather than delivering a study, and the last line is evidence hygiene as a habit rather than a talking point.

### The level question — say nothing, and let the scope do it

**Default: do not ask for an uplevel.** The recruiter already knows you're targeting up, so an ask adds risk without adding information. Worse, it changes the bar mid-conversation — she's currently asking "is this a strong Senior," which you clear comfortably. Say "I'm Staff scope" and she starts testing you against a Staff bar in 45 minutes on one case, where your real gaps weigh more. And she can't act on it anyway; level is decided after the loop.

**Managers uplevel when they hear themselves think *"we'd be underusing this person."*** Three habits produce that, and a request doesn't:

1. **Criteria, not findings.** "The spec engineering builds against," never "the study I ran."
2. **Present tense about Sling.** *"I own the function."* Your loudest level signal, and it costs nothing.
3. **What you'd own, not what you did.** On first-ninety-days, describe the standard you'd install and who else runs it.

**If she opens the door** — she mentions the posted level, asks about title, or asks what you're looking for — answer once and move on:

> Honestly, I'm optimizing for the problem rather than the label. The work I do now is function-level — I own the standards, not a project — and I'd rather the loop test whether that scope is real than have either of us guess. If the panel says it isn't there, I'd want to hear that.

It declines to make a demand, hands the decision to the process, and removes her risk by saying out loud that you'll accept a no.

**If she never opens it,** say nothing. Use the third question in AC11 instead — it raises the subject without you using the word, and invites her to describe the higher bar herself.

**What she needs to defend an uplevel without you:** a criterion others use without you (the spec, or the ladder) · something that changed and stayed changed (the rename) · a function you built from nothing (Sling — the one you're most likely to forget). **What kills it:** arguing from title, years, or the patent. Those are inputs. Level is decided on scope.

---

## AC07 — When She Leaves the Case Study

**She will not spend forty-five minutes on Amazon.** Around minute 25 she'll test whether you're a one-case candidate. The Amazon work cannot answer any of these. **Bridge honestly, answer from the right job, name the boundary** — reaching for Amazon here is the tell of someone with one story. 45–90 seconds each, then stop.

**1. Misplaced trust** — *"How would you tell an operator is trusting the system more than they should, before something goes wrong?"*

> I'd watch how often they approve, sorted by how confident the system said it was. If people accept the low-confidence recommendations at the same rate as the high-confidence ones, they've stopped reading the confidence and they're clearing a queue. That's measurable continuously, and it doesn't need an incident to show up.
>
> I'd also recheck it after every model update. Trust gets calibrated to how the system used to behave and carries over when the behavior changes underneath it. That's where I'd expect the gap to open.

**Boundary, say it:** *"That's a prediction. I've written the framework — it's a thesis, not something I've deployed."*

**2. Hardware** — *"What would you want measured on an operator station before anyone designs a screen?"* Answer from Sling, not Amazon.

> Reach and posture, with the operator wearing what they'll actually be wearing — gloves, vest, seated, possibly moving. That gives you the box the controls have to live in, and it's a physical answer, not a preference. Do it before anyone touches the display, or you design the screen and then discover the person can't hold that position for four hours. That's the work I do now at Sling: reach envelopes, anatomical safety, mechanical fit specs, written so hardware has to clear them.

**3. Field work** — *"How would you spend two weeks with operators?"* Lead with the gap.

> Straight answer first: most of my work has been lab and simulator, not field. That's a real gap and I'd rather say it than dress it up.
>
> Week one is watching, with nothing but a question list agreed with engineering and product in advance — operator access is scarce, and one visit should answer three teams' questions rather than mine. Week two is structured tasks against what I actually saw. What I'd bring back isn't a report; it's a workflow model with the failure points marked, so the next person doesn't have to go back for the same picture.

**4. Growing people** — *"How do you raise the level of the people around you?"*

> Mostly by making the standard visible. At Sling I built the function from nothing, so the useful thing wasn't advice, it was a review ritual — every spec checked against a stated criterion instead of against taste. That raises the floor for everyone including me, and it works whether or not I'm in the room.
>
> The honest boundary: I've mentored inside teams. I haven't managed a research bench. If part of this role is growing one, I'd want to be clear that's a step I'm ready for rather than one I've already taken.

**Never skip that last sentence.** Claiming management you don't have is the fastest way to lose a Head of Research.

**Bridge back to the case:** *"That's the part I'd have to learn here. What I'd bring on day one is the habit of turning a human limit into a number somebody can build against."*

---

## AC08 — The Bridge: Kim's Three Questions

> **From `references/Human Factors Response to Autonomous System Design`.** You wrote a four-page research response to three questions Dr. Kim posed publicly at the Learners Conference, San Francisco, May 2026. It is your strongest asset for this specific conversation.

**Use it as a research agenda, not as flattery.** Never open with "I saw your talk." Deploy it when she asks what you'd work on, or why this role.

### The pivot into the agenda

> The reason I keep coming back to that floor finding is that it's the same shape as your Learners Conference question — whether better UX on autonomous systems reduces harm or just makes harm easier to authorize. In the consumer case the answer was empirical and slightly absurd: past a point, faster made the system worse, and we could measure where. I think the defense version is measurable too. I wrote up a response to those three questions because I couldn't stop thinking about the third one.

### The three, compressed — one sentence of position, one of method

| Her question | Your position | Your proposed method |
|---|---|---|
| **Responsibility gap** — who keeps humans in the loop when deployment outruns governance? | Responsibility defaults to the builder; if the interface permits it, operators infer it's authorized. | Vignette walkthrough, enforced-checklist vs. discretionary interface, measuring where operators locate accountability. |
| **Friction paradox** — does better UX reduce harm or make harm easier to authorize? | Micro-frictions should cost completion time and buy a disproportionate drop in false-positive authorizations. | A/B simulator under time pressure; a friction gate requiring the operator to identify the justifying evidence before approval unlocks; eye tracking on data versus the approve button. |
| **Moral crumple zone at scale** — is a human evaluating 50 recommendations a minute really in the loop? | There's a rate past which operators abandon verification and default to compliance. Past it, human control is nominal regardless of interface. | Ramp the rate with seeded false positives; measure error-catch rate, NASA-TLX, and arousal to find the inflection point. |

### The single best thing you can say in this conversation

> The third question is the one I'd answer first, because it's the only one falsifiable with a number. If there's a recommendation rate past which operators stop catching seeded errors, that's an inflection point you can measure — and once you have it, it becomes a design constraint on how fast the system is allowed to present decisions to a human. Same move as the latency thresholds, in a domain where it matters.

**Guardrails.** Those hypotheses are proposed, not run — say "I'd predict," never "we found." The numbers in them are predictions you wrote down, not results. Claim only that she posed three questions publicly and that you wrote a response: no acquaintance, no private exchange, and nothing characterized beyond those three questions.

---

## AC09 — The NASA Module (55 seconds)

**Deploy this yourself, around minute 25, before she raises it** — it pre-empts the objection that everything above is consumer technology with recoverable consequences. Volunteering the intern caveat unprompted buys more credibility than the story costs.

> The obvious hole in what I've described is that nothing in it was irreversible. Let me give you the version where it was. At NASA Langley I did human-systems integration for Lunar Gateway clinical workstations in simulated microgravity — a use-error analysis against NASA-STD-3001 and MIL-STD-1472 rather than a usability study, because the failures that matter there are rare and high-consequence and won't appear in any sample you can get. Enumerate the error modes, rank by consequence rather than frequency, redesign the physical layout so the irreversible action isn't adjacent to the routine one. Task time dropped thirty percent and the critical input errors were eliminated — and the layout is what eliminated them, not the speed. I was a Ph.D. intern on that, so the analysis and the redesign recommendation are the honest claim, not the program.

**~140 words ≈ 55 seconds.** Say it and stop. Full material in [05-nasa-case-study.md](practice/05-nasa-case-study.md).

---

## AC10 — Evidence Boundaries for This Case

### Assert freely

Multi-year psychophysics program replacing arbitrary latency targets with perception-derived thresholds; **~$50M** projected operational value · method of constant stimuli, within-subjects, 12 interaction types × 6 delays (500–3000ms), randomized, three repetitions per cell for ~216 trials each, 30 participants, Wizard-of-Oz rig with per-trial millisecond control, three-point slowness scale · the deliberate rejection of an adaptive staircase · workload held constant by a low-demand visual monitoring task, NASA-TLX per block **as a manipulation check only** · reporting as criterion + estimate + confidence interval + slope, scoped to one mode at a stated workload · two-band threshold spec with pass criteria · findings: task-dependent thresholds, ~500ms for real-world analogues, non-monotonic curve needing a floor · the sample-size counterfactual you costed and argued against · the metric rename · independent corroboration with a partner team's economic model · fNIRS + eye-tracking cognitive-load capability · **US Patent US-12532040-B1**, 2023 Amazon Inventor Award · portfolio strategy influence across 75M+ customers.

### Never assert

- Any internal codename, dashboard, percentile table, or competitor benchmark
- **Any figure other than ~$50M.** Don't quote the larger internal modeling and **don't allude to it** — no "the internal number was higher," no "I'm being conservative." Gesturing at a bigger figure you won't name reads as a brag you're pretending not to make
- Any head-to-head showing fNIRS beat the NASA Task Load Index — the claim is convergence and non-reactivity
- fNIRS at Brigham or Harvard — that instrument belongs to Amazon
- Any Echo-specific metric beyond portfolio reach · any result from the three proposed autonomous-systems studies · any deployment of Calibrated Cognitive Friction · any clearance status, classified detail, or Anduril-internal process, team or headcount

### The magnitude question

**$50M is the only number, and it's also the better one.** A nine-figure claim from a single researcher triggers disbelief and spends her next question auditing you. When she asks where it comes from, answer with derivation, not size:

> That's the operational value attributed to the program, and the modeling behind it was an economics team's work, not mine — so I'd hold it loosely and rather tell you the mechanism. Thresholds were missing on high-traffic interactions, slow responses measurably suppressed engagement, and the thresholds gave the org a place to target. The part I'd defend is the threshold structure. The dollar figure is a consequence of it, and it isn't mine.

Volunteering that the attribution belongs to someone else is the most credible thing you can say about your own biggest number. **If she seems unimpressed, go smaller and more specific — never larger.**

### The four facts, filled in

> **Drafted to be plausible and consistent — but they have to be true for you.** Adopt or correct each one before you drill, then stop thinking about it.

- **Trials** — "Seventy-two combinations, three passes each, about two hundred trials a person." 12 × 6 = 72 is arithmetic she can do while listening; three passes is what lets you fit a curve per person. ~12s a trial ≈ a 90-minute session.
- **Secondary task** — "A light visual monitoring task on a second screen, fixed difficulty, set from a practice block. NASA-TLX after each block to confirm the load landed where I aimed it." Visual so it doesn't mask the audio.
- **Duration** — "About three years, three phases: rough band on the top interactions, then the real curves per interaction and mode, then workload and the mental-effort instrument."
- **The disagreement** — "A principal engineer in a design review, on the half-second smart-home target: his position was it's a feasibility question, and research should describe rather than constrain."

**Team, if asked:** by function only — the performance-engineering group and an economics team. Never an internal org name.

### The narrowed panelist rule

You may state that Dr. Kim posed three questions publicly at the Learners Conference, San Francisco, May 2026, and that you wrote a research response. No acquaintance, no private correspondence, and nothing characterized beyond those three questions.

---

## AC11 — The 45-Minute Run Sheet

You do not control the agenda. You do control what you have ready and what you volunteer. This is a plan for *your* half of it.

| Minutes | What's happening | What you're doing |
|---|---|---|
| 0–4 | Warm-up, then the case | Discretion line early. Then AC01 without beat [2], ~2:58, and stop talking |
| 4–22 | Her probing on the case | AC02 layers on demand. One layer per question. Never chain two |
| ~22 | The likely rigor attack | AC03 F1 and F2. Volunteer the weakness before she isolates it |
| ~25 | **Your move** | AC09 NASA module, unprompted, as the answer to the consumer-tech objection |
| 25–33 | **She leaves the case** | **AC07.** Autonomy, hardware, field work, people. Answer from Sling and the thesis, not from Amazon |
| 33–40 | Scope, mechanisms, what you'd work on | AC05, AC06, then AC08. This is where level is decided |
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
| 1 | AC01 cold, recorded, no notes | Under 3:10, all eight beats, no codename spoken |
| 2 | Each of Layers 1–5, cold | Under 90s each, no re-narration of the case |
| 3 | AC03 F1 and F2 word-perfect | Method-choice and trials-not-headcount, each under 40s |
| 4 | The tier ladder cold | Three tiers, what each may and may not decide, under 40s |
| 5 | **The off-case four** | AC07 cold, in any order. Each names its own boundary. Zero reaches back to Amazon |
| 6 | Confidentiality audit | Replay every recording. Only ~$50M survives, never hedged |
| 7 | **Sling check** | Across a full mock, Sling comes up twice unprompted. If the only job you discuss is one you left in 2024, the level argument is coming from the wrong place |

**Three failure modes on playback:** stacking layers (three answers to one question, which burns material you'd need at minute 30) · slipping a confidential figure in under pressure, which you won't notice · reaching back to Amazon during the AC07 stretch, the tell of a one-case candidate.

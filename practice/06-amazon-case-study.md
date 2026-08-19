# 06 — Amazon Latency Case Study (AC01–AC11)

**This is the primary case for the 45-minute hiring manager conversation with Dr. Daniella Kim.** NASA moves to second position — a 45-second module you deploy yourself, covered in AC09.

**Why this case, and not NASA.** Kim is judging five things: is your work rigorous, do you move fast enough, do you set the direction or follow it, does what you build outlast you, and can you move people who outrank you. The latency program hits all five. You ran it. And it has enough depth to survive forty minutes of questions without running dry. The job posting describes Lead/Staff as someone who *"bridges engineering latency with human perception"* and *"translates findings into hard specifications."* That is a description of this program.

**Targets:** presentation 420–450 words ≈ 2:50–2:58 · deep-dive answers 160–230 words ≈ 90s · follow-ups 45–90 words. **Speaking pace is 150 words a minute** — every timing in this file is derived from that, so count words rather than trusting your sense of how long something felt.

**How to say all of it.** Short sentences. One idea each. When you use a technical term, define it in the next breath in words a product manager would understand — that habit is itself a seniority signal, because it shows you've had to sell this work to people who don't share your training. Never use two clauses where one will do. If a sentence needs a comma and a dash, cut it in half.

---

## START HERE — The Two-Day Plan

**This file is long because it's a reference. You are not meant to learn all of it.** Most of it exists so that when she asks something specific, you've already thought about it once. Thinking about it once is enough for most of this.

**There is exactly one thing to memorize: eight trigger words.** Everything else you either know already or only need to have read.

### The eight-word spine — this is the whole presentation

| # | Trigger | What comes out |
|---|---|---|
| 1 | **Wrong goal** | Everyone pushed delay toward zero. There's no single right answer. |
| 2 | **Nobody could define it** | "Fast enough" was undefined, so the same argument recurred. |
| 3 | **Numbers, not opinions** | My job: thresholds engineering treats as requirements. |
| 4 | **Simplest method** | Constant stimuli. Twelve interactions, six delays, three-point scale. Turned the staircase down. |
| 5 | **Depends — both ways** | Real-world equivalent needs half a second. And a floor: too fast feels wrong. |
| 6 | **Four things** | Never one number: delay, confidence, steepness, mode + workload. |
| 7 | **Renamed it** | The spec, the ~$50M, the metric definition that outlived me. |
| 8 | **Workload** | Consumers not operators, load held steady. That's the study I'd want here. |

Say those eight aloud in order until you can do it in fifteen seconds. Once the order is automatic, the words fill themselves in — you already know this work, you're only learning the running order. **Do not memorize the script sentence by sentence.** A memorized paragraph sounds memorized, and she'll hear it.

### Day 1

| Time | Do this |
|---|---|
| 30 min | Read AC01 and AC02 straight through, once. Don't take notes. |
| 20 min | Learn the eight triggers. Say them until fifteen seconds. |
| 40 min | Record the full presentation three times. Third take only, check the clock — under 3:00. |
| 20 min | Read AC10 boundaries. This is the only part you must not get wrong. |
| 15 min | Say the AC09 NASA module twice. It's 140 words. |

### Day 2

| Time | Do this |
|---|---|
| 30 min | The five core layers below, cold, one at a time. Stop each at 90 seconds. |
| 20 min | AC03 F1 and F2 — the two rigor attacks. These are the likeliest hard questions. |
| 20 min | AC07, the off-case four. Short answers, each naming its own limit. |
| 15 min | The tier ladder in AC04, and the level guidance in AC06. |
| 10 min | Pick your two questions from AC11. Write them on a card. |
| 20 min | One full mock end to end. Then stop preparing. |

### Learn these five layers. Skip the rest until after the screen.

**Core — drill these:**
- **Layer 2** — why the simple method, and the staircase you turned down
- **Layer 3** — why thirty people is enough
- **Layer 4** — mode and workload *(your bridge to Air Defense)*
- **Layer 5** — why you never ship one number *(your strongest single answer)*
- **Layer 7** — the speed limit in the other direction *(your thesis, with data)*

**Reserve — read once, don't drill.** Layers 1, 6, 8, 9, 10, 11. You know this material; you just need to have decided how you'd say it. If one comes up, you'll find the words.

### Read once, never memorize

The confidentiality box · AC04 cadence and gates · AC05 stakeholder answers · AC08 Kim's three questions · AC10 boundaries. These are judgment, not lines. Reading them once changes what you say without you having to recall anything.

### If you only have two hours total

The eight triggers. Layer 5. The AC10 "never assert" list. the level guidance in AC06. That combination still gets you a strong Senior signal and keeps the uplevel argument alive.

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

**Arc:** opening of the hiring manager conversation · **Target:** 2:50–2:58 · **hard ceiling 3:00**

> **Base:** Walk me through a piece of research you led, end to end. Take about three minutes.

### The beat spine

| # | Beat | Words | Time | The one job it does |
|---|---|---|---|---|
| 1 | **The claim** | 45–55 | ~20s | The company was chasing the wrong goal. Say it flat. |
| 2 | **Why it was hard** | 30–35 | ~13s | Nobody could define "fast enough." Cut this one first. |
| 3 | **Your job** | 20–25 | ~9s | First person. Numbers engineering would treat as requirements. |
| 4 | **What you did** | 105–115 | ~44s | The plain method, and the fancier one you turned down. |
| 5 | **What you found** | 60–65 | ~25s | It depends on the task — and there's a speed limit in both directions. |
| 6 | **What you handed over** | 60–65 | ~25s | Never one number. This is the beat that shows the level. |
| 7 | **What you left behind** | 55–60 | ~23s | The spec, the ~$50M, the renamed metric. |
| 8 | **What it means here** | 60–65 | ~25s | Air Defense, and the one thing your evidence can't cover. |

**Counted, not estimated: 463 words = 3:05 at 150 words a minute. Drop beat [2] and it's 431 words = 2:52.**

**So beat [2] is optional by default.** Keep it only if she seems to want context; cut it the moment you feel yourself running. Never cut [4], [6], [7], or [8] — those three are what the whole conversation is for.

### Model script (463 words / 3:05 · 431 / 2:52 without beat [2])

> **[1]** Short version: a very large engineering organization was chasing the wrong goal, and my job turned into proving it. Everyone treated response delay as a number to push toward zero. There's no single right answer. It depends on what the person just asked for — and past a point, faster does harm.
>
> **[2]** The hard part was that nobody could define "fast enough." So targets got set by whatever engineering could build, and the same argument came back every review with nothing to settle it.
>
> **[3]** My job was to produce numbers strong enough that engineering would treat them as requirements rather than a researcher's opinion.
>
> **[4]** I used the simplest method in psychophysics — constant stimuli. Pick a fixed set of delays, play them in random order, ask the person to judge each one. Enough repetitions and you can draw the curve connecting delay to reaction.
>
> Twelve kinds of interaction, six delays, half a second to three. A couple hundred trials per person.
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

### What each beat is buying you

- **[1]** *Decision first* + it opens on a claim Kim can disagree with, which is what makes her lean in.
- **[2]** **Ambiguity.** This beat exists because the JD asks for someone who can "work through ambiguity." Show the problem was undefined before you defined it.
- **[4]** The rigor beat, and the register beat. Using the plainest method available and *saying you chose it over the fancier one* is a confidence signal. Junior researchers reach for exotic procedures; senior ones reach for the simplest design that answers the question.
- **[5]** The floor is your best single moment. It is *Calibrated Cognitive Friction with data behind it* — see AC08.
- **[6]** **Say this even if it costs you time.** Almost nobody ships a spec as a distribution with a slope. Inviting her to push on it is a confidence signal, and it sets up AC02 Layer 5.
- **[7]** *Reusable mechanism.* Renaming an organizational metric is a Staff-level act. Do not leave it out.
- **[8]** *Evidence hygiene.* Name the workload boundary before she does — and it doubles as your proposal.

### What Kim has to be able to say about you afterwards

**This is the real test, and it is not the one you think you're taking.** She will not replay your case study to the panel. She will compress the whole 45 minutes into two or three sentences, from memory, days later. Those sentences *are* the output of this conversation. So decide what they should be and make every answer produce them.

**The three you want:**

1. *"He turns human limits into numbers engineers can actually build to — and he ships them with error bars instead of opinions."*
2. *"He killed a company-wide assumption and got the metric definition changed. That's still there and he isn't."*
3. *"He told me where his own evidence runs out before I had to ask."*

Each one maps to a beat. The first is [6]. The second is [7]. The third is [8]. That's why those three beats never get cut.

**The sentence that means you failed:** *"Strong researcher. Ran a big study, got a good result."* That is a completely positive review and it is a Senior review. It means you described excellent execution, which is the baseline expectation, and never showed her anything that outlived you.

### Senior vs. Lead/Staff, in plain terms

| | What Senior sounds like | What Lead/Staff sounds like |
|---|---|---|
| **The finding** | "We found the acceptable delay is X." | "We found the question was wrong. There isn't one delay." |
| **The delivery** | "I recommended a target." | "I shipped a criterion with error bars, and engineering budgets against the conservative edge." |
| **The method** | "Here's the design I ran." | "Here's the design I ran and the better-sounding one I turned down, and why." |
| **The legacy** | "The team adopted my recommendation." | "The definition changed and stayed changed after I left." |
| **The limits** | Answers honestly when asked. | Says it first, unprompted, and turns it into the next study. |

**Structural test:** delete beat [7]. If the story still feels finished, you told it as a Senior.

---

## AC02 — The Deep-Dive Layers

Three minutes is the presentation. The other forty are these. **Each layer is a separate answer you should be able to give cold.** Do not volunteer them all — hold them and deploy the one that answers the question asked.

### Layer 1 — Why psychophysics rather than analytics

> The company already had behavior data at enormous scale. That data tells you what happened after a slow response. It can't tell you where the line is, because the line isn't in the logs. It's in the person. Psychophysics is the method built for exactly that: change one thing on purpose, ask people to judge it, and find the point where the judgment flips. Analytics gives you a pattern across millions of people. Psychophysics gives you a number you can put in a requirement. I needed the second one.

### Layer 2 — Why the simplest method, and why not the fancier one

**This is the confidence answer. Say it without a hint of apology.**

> I used the oldest, plainest tool in the box, and that was a choice, not a default.
>
> The efficient alternative is called a staircase. It moves the delay based on what you said last time, so it homes in on your threshold in far fewer trials. I looked at it and turned it down for three reasons.
>
> It finds one point on the curve, and I needed two — a "good enough" line and a "genuinely good" line. It's accurate about where the line is but poor at telling you how steep the curve is there, and the steepness was half of what I owed people. And it's harder to explain to the engineers who have to accept the number, which matters more than it should.
>
> So I spent more trials and got the whole curve back. That let me read off whatever line the spec needed — including ones nobody had asked for yet.

**The line to land it:**

> I'd rather use the simplest method that answers the question and put the effort into what I do with the results. The clever part shouldn't be the procedure.

### Layer 3 — Why thirty people is enough

**The other question she's most likely to ask. Have it word-perfect.**

> The precision comes from the trials, not the headcount. Everybody saw every delay, so each person acts as their own comparison, and a couple hundred trials each is what makes the curve steady. The thirty people set how much the threshold varies from person to person — and that variation is exactly what I reported, rather than hiding it.
>
> I also priced the alternative and argued against it in writing. Tightening that range meant roughly ten times the people, six to twelve months, and several hundred thousand dollars. The decision I had to serve was which interactions to fix first and how far. The differences driving that were big. A tighter range would have moved the error bars and changed nothing about what we did.
>
> I bought a decision, not a publication. And I said out loud which one I was buying.

### Layer 4 — Mode and workload

> Two things I controlled instead of letting them drift.
>
> First, the mode. A spoken response and a response you see on screen have different thresholds. Average them together and you get a number that's wrong for both. So every threshold I published named the mode it applied to.
>
> Second, workload. I ran the judgments while people were doing something else at a fixed level of difficulty, not sitting there with nothing to do. A threshold measured by someone at rest isn't the threshold that applies in real use. I used a standard workload questionnaire to confirm the load actually landed where I'd aimed it — that's what it's for, checking that the setup worked, not as the result itself.
>
> The honest limit is that I held workload steady rather than turning it up and down. So I have the threshold at one setting, not across the range. That's the next study, and it's the one that matters when the person is an operator.

**Why this layer is load-bearing:** it is your cleanest bridge to Air Defense, because operators under load *is* the domain. Naming that you controlled workload, and that the obvious next step is to vary it, turns a limitation into a proposal.

### Layer 5 — Why you never ship one number

**Deploy when she asks what you actually delivered, or how research turns into a requirement.**

> I stopped handing over single numbers, because a single number just starts an argument about the number.
>
> Every spec went out with four things: the line itself, how confident I was in it, how steep the curve was at that point, and which mode and workload it applied to.
>
> Two things changed because of that. Because there was a confidence range, I could tell engineering to build against the cautious end rather than the middle — which is what you do when being wrong in one direction costs more than the other. And because there was a steepness number, they could see where the cliffs were. Steep stretch: a hundred milliseconds is the difference between fine and not fine, and that's worth real engineering money. Flat stretch: it's noise, spend it somewhere else.
>
> That's the habit I'd bring here. One number tells you where the line is. A line plus a range plus a slope tells you what it costs to miss it — which is the question anyone working to a schedule is actually asking.

### Layer 6 — Why the answer depends on the task

> The result that reorganized the whole program was that the right delay isn't a property of the system. It's a property of what the person just asked for. Anything with a real-world equivalent — flipping a switch, writing on a notepad — has to finish near half a second, because people are comparing it to the object, not to the software. Several people said it outright: if it isn't faster than the physical thing, why own the device. Anything that looks like looking something up got about twice as long. That killed the idea of one company-wide speed target and replaced it with a separate number per interaction, which is a completely different engineering roadmap.

### Layer 7 — The speed limit in the other direction

**Your most valuable thirty seconds. See AC08 for how to spend it.**

> For spoken answers I had to set a lower limit as well as an upper one. A response that comes back faster than a person would answer stops feeling responsive and starts feeling wrong. That's the finding that made me stop believing faster is always better.
>
> The curve has two edges, not one. Both are real. If you only ever optimize in one direction, you'll walk off the far edge and have nothing measuring to tell you that you did.

### Layer 8 — Getting the metric renamed

> The company had a metric whose name described a real measured interval but was worded as if it described what the customer felt. That sounds like a quibble. It wasn't. It meant every conversation about that metric silently assumed the measured delay and the felt delay were the same thing — which is precisely the assumption my data disproved.
>
> So I pushed to rename it to describe what it actually measured, and to make perception a separate thing with its own numbers. Changing a metric definition is slower and less fun than getting a study funded, and it's worth more, because the definition shapes every argument that happens afterwards.

### Layer 9 — Two methods that fail differently

> A partner team had built an economic model estimating what slow responses cost downstream. Its numbers were big enough that people quietly doubted it. My work was completely independent — different method, different data, no shared assumptions — and it backed up the core claim that people really are sensitive to these differences.
>
> That's the structure I want in an evidence base. One model built on observed behavior, one controlled study built on judgments. They fail in different directions. So when they agree, the agreement actually means something. I'd rather have two imperfect methods that break differently than one strong method with a blind spot.

### Layer 10 — Measuring mental effort directly

> Separately I helped build a way to measure mental effort without asking. We used a brain-imaging technique that reads blood flow in the front of the head, plus eye tracking, while people looked at a set of comparable interfaces. We saw differences in effort between interfaces that lined up with how cluttered people said those interfaces were, and gaze patterns showing whole regions of a layout that nobody ever looked at.
>
> The value isn't that the brain measure beats asking people. It's that it doesn't interrupt. You don't have to make someone stop and rate their own effort while they're spending it, and the measure doesn't shift when you reword your question.

**Boundary — say it before she asks:** you have no head-to-head result showing the neural measure outperformed the NASA Task Load Index. Never imply one. The defensible claim is convergence and non-reactivity, not superiority.

### Layer 11 — The patent

> The patent came from a different thread — context-based control inputs. The idea is that pressing the same button does different things depending on what's on screen and where you are in it. The meaning is worked out by the system in the moment rather than fixed in the hardware.
>
> It's the same move as the latency work, which is why I mention it. In both cases, what a signal means isn't a property of the signal. It's a property of the situation the system and the person are in.

---

## AC03 — Kim Follow-Ups: Rigor and Velocity

**F1 — "Constant stimuli and a three-point scale. That's a fairly basic design for a multi-year program."** *(~85 words)*

> It is, and that's on purpose. The design is simple. What I did with the results isn't. I drew the full curve for every condition, published lines with confidence ranges and steepness rather than bare numbers, and named the mode and workload each one applied to.
>
> The fancier designs I looked at would have been faster and given me less. A staircase finds one point well and tells you little about the shape around it, and I needed two points and the shape. I'd rather be plain in the procedure and demanding in the analysis than the other way round.

**F2 — "Thirty people. Convince me that's not just a number you could afford."** *(~80 words)*

> The estimate doesn't rest on thirty. It rests on a couple hundred trials each, with everyone seeing every delay, so each person is their own comparison. That's what makes the curve steady, and it's why this method works at these numbers.
>
> What the thirty buys me is how much the line moves from person to person — and I published that spread rather than burying it. I also priced the alternative: about ten times the people, six to twelve months, several hundred thousand dollars, for a tighter range on a decision that was already clear. I argue against studies that can't change a decision.

**F3 — "What's the weakest part of that study? Not the limitation section — the part that actually worries you."** *(~90 words)*

> The controlled setting. I stripped out everything that happens alongside delay in real life — the light ring, the sounds, background noise, the fact that people are usually busy doing something else. Those aren't nuisances, they probably change the answer. So my numbers are almost certainly off in one direction and I can't tell you which one.
>
> The second thing that bothers me is that I measured a judgment, not a behavior. Someone can tell me a response was fine and still quietly use the product less. My design can't see that gap.

**F4 — "If you re-ran it today with no constraints, what changes?"** *(~75 words)*

> I'd make workload a factor instead of a control, so I get the threshold as a function of load rather than at one point on it — that's the version that applies to an operator. I'd add the visual and auditory affordances back in as manipulated factors, because I now think the interaction between feedback and perceived latency is where the remaining budget sits. And I'd pair the subjective threshold with a behavioral one, so the spec doesn't rest on a single response class.

**F5 — "What did you get wrong?"** *(~70 words)*

> I framed the first version of the deliverable as a single global threshold, because that's what I'd been asked for and it's what would have been easiest to adopt. The data didn't support it and I had to go back and restructure the whole recommendation around interaction type. The lesson I took is that the shape of the deliverable is a research decision — I'd pre-committed to an answer format before I knew the answer's shape.

---

## AC04 — Evidence Tiers, Cadence, and Ambiguity

### The evidence ladder

**This is the most portable thing you own, and it's your answer to "how would you actually work here."** It solves the problem every fast company has: research is either quick and not trustworthy, or trustworthy and too late. Tiering fixes that by putting the strength of the claim on the artifact itself, so moving fast never costs you credibility later.

| Tier | Time | What it is | What it's allowed to decide | What it's never allowed to decide |
|---|---|---|---|---|
| **Directional** | Days | A rough read — a few people, existing research, a quick check. A best guess, no precision claimed | Which way to lean, what to prototype, what to stop building | A spec, a freeze, or a number anyone quotes in a review |
| **Threshold-grade** | Weeks | The real curve for a condition, with a confidence range and a steepness, named to a mode and a workload | A design target, a budget, a roadmap priority | A release gate by itself |
| **Decision-grade** | Longer, and rare | Threshold-grade, repeated in the real operating setup, with a stated way it could be proven wrong and a plan to watch it in the field | Acceptance criteria and sign-off | Anything outside what it was measured on — the scope is part of the claim |

**Two rules that make this real instead of decorative:**

1. **The tier is written on the artifact, not remembered.** A rough number that loses its label turns into a hard number in about two weeks. Nobody lies. It just happens.
2. **Rough findings expire.** Each one carries a date and the tier it's waiting for. If nothing replaces it, it gets reopened or thrown out. It never quietly becomes fact.

### Saying it out loud (~120 words)

> The way I keep research fast without it becoming unreliable is that I sort it into three tiers and write the tier on the thing itself.
>
> Rough is days. A few people, a quick read, enough to tell you which way to lean or what not to build — and explicitly not allowed to set a spec.
>
> Threshold-grade is weeks. A real curve with a confidence range and a steepness, named to a mode and a workload. That can carry a design target.
>
> Decision-grade is what gates a freeze. It has to hold up in the real operating setup, and I have to say in advance what result would prove me wrong.
>
> The discipline isn't the three tiers. It's that the label travels with the number. What actually rots an evidence base is a rough finding quietly getting promoted while nobody's watching.

### Cadence — how directional specs got made along the way

**"How do you deliver something useful before the rigorous answer exists?"** *(~105 words)*

> By shipping the rough version on a schedule and being loud about the fact that it's rough. On the latency program, engineering needed a target long before I had a defensible curve. So I gave them a provisional band, with the tier written on it and a plain statement that it would move.
>
> It did move. And because the label was on it, that was an update rather than a retraction. That's the whole difference.
>
> The schedule matters as much as the label. Something lands every couple of weeks. If research goes quiet for a quarter and then reappears with the truth, the roadmap has already worked around you, and your truth shows up as an obstacle.

**The sentence to land it:**

> A wrong number that's labeled provisional is a working agreement. A wrong number that's labeled final is a credibility event. The label is doing more work than the number.

### What you'd install here (~90 words)

**Deploy when she asks about your first ninety days or how you'd operate.**

> The first thing I'd set up is the tier language, because it's cheap and it changes behavior straight away. Every research artifact says what it's allowed to decide and what it isn't, and every one names what it was measured on — which mode, which workload, which kind of operator. Then I'd organize the repository by tier instead of by project, so anyone hunting for a number sees how much weight it can carry in the same glance. That's about a week of work, and it's what lets research move at engineering speed without getting caught out a year later.

---

### Ambiguity and the gates

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

Kim's own stated bar is *"how would you build a research function whose standards survive after you leave?"* You have four real answers. **Pick the two that fit the question. Never recite all four as a list.**

> **The spec.** "Two numbers per interaction, each with a pass test attached — not a suggested target, a line the hardware has to clear. That's what engineering builds against, and it works with me out of the room."

> **The definition.** "I got a company metric renamed, because its name assumed something my data had disproved. It's the least impressive-sounding thing I've done and the one I'm proudest of. A definition shapes every argument that comes after it."

> **The instrument.** "The mental-effort setup was built as a capability, not a study — something other researchers could point at their own questions. The point was to leave behind a tool, not a result."

> **The evidence ladder.** "Every artifact says what it's allowed to decide and what it was measured on, so a rough read can't quietly turn into a spec. That's the one I'd set up here first. It costs a week, and it's what lets research move fast without getting caught out later."

**One more, and don't forget it's available.** Amazon is where you did the work. **Sling is where you have the scope right now**, and it's the strongest level evidence you own — you are Staff there today, you built the human factors function from nothing, and you own specs across software, hardware, and AI. Use it whenever the question is about scope rather than craft:

> "At Amazon I owned a program. At Sling I own the function — I built it from a standing start, and I write the specs across software, hardware, and AI. That's the scope I'm arguing for here, and it's the one I'm doing now rather than the one I did four years ago."

### The sentence that must be said out loud

> "The thing I'd want to be judged on isn't the thresholds. It's that the org's definition of the metric changed, and it stayed changed after I left."

### And the level claim, in one sentence

> "The scope I'm arguing for is the one where I own the criteria the organization designs against — which is what I did at Amazon, and it's the difference between running excellent studies and setting the bar those studies get measured against."

### The level question — say nothing, and let the scope do it

**Default: do not ask for an uplevel in this conversation.** The recruiter already knows you're targeting up, so an explicit ask adds risk without adding information. Worse, it changes the bar mid-conversation — right now she's asking "is this a strong Senior," which you clear comfortably. Say "I'm Staff scope" and she starts measuring you against a Staff bar using 45 minutes and one case, where your real gaps carry more weight than they should. And she can't act on it anyway; level gets decided after the loop, on panel evidence.

**Hiring managers uplevel when they hear themselves think *"we'd be underusing this person."*** That thought is produced by three habits, not by a request.

1. **Talk in criteria, not findings.** "The spec engineering builds against," never "the study I ran."
2. **Present tense about Sling.** *"I own the function."* Not "I owned a program four years ago." Present-tense scope is your loudest level signal and it costs nothing to use.
3. **Answer what you'd own, not what you did.** On the first-ninety-days question, describe the standard you'd install and who else runs it.

Do those three and she raises level herself \u2014 which is far stronger than you raising it, because then it's her conclusion and she'll defend it in calibration.

### If she opens the door

Only these count as an opening: she mentions the posted level, asks what you're looking for, asks about title, or asks whether Senior is a fit. Then answer once, briefly, and move on.

> Honestly, I'm optimizing for the problem rather than the label. What I'd say is that the work I do now is function-level \u2014 I own the standards, not a project \u2014 and I'd rather the loop test whether that scope is real than have either of us guess at it. If the panel says it isn't there, that's useful information and I'd want to hear it.

*(~60 words. Say it, stop, let her steer.)*

**Why this version is safe:** it declines to make a demand, hands the decision to the process rather than to her, and removes her risk by saying out loud that you'll accept a no. It reads as confidence rather than negotiation.

### If she never opens the door

Say nothing about level at all. Use the third question in AC11 instead \u2014 *"what would have to be true in a year for you to say this hire cleared the bar you were hoping for rather than the one you posted?"* That raises the whole subject without you ever using the word, and it invites her to describe the higher bar in her own words. If she does, you've won the argument without making it.

### The three things she needs to defend an uplevel without you

She has to argue it to people who never met you. Make sure at least two of these have landed:

1. **A criterion other people use without you.** The spec, or the evidence ladder.
2. **Something that changed and stayed changed.** The metric rename.
3. **A function you built from nothing.** Sling. This one most directly says "Staff," and it's the one you're most likely to forget.

**What kills it.** Arguing from title, from years, or from the patent. All three are inputs. Level is decided on scope \u2014 what someone else has to clear because you defined it.

---

## AC07 — When She Leaves the Case Study

**She will not spend forty-five minutes on Amazon.** Somewhere around minute 25 she'll test whether you're a one-case candidate. These are the four questions most likely to come, and the Amazon work cannot answer any of them. Each answer here is short on purpose — 45 to 90 seconds, then stop.

**The rule for all four: bridge honestly, answer from the right job, and name the boundary.** Reaching for Amazon when Amazon doesn't apply is the single worst thing you can do in this stretch, because it's the tell of someone with one story.

### 1. Autonomy and misplaced trust — her home ground

> **Likely:** "How would you tell that an operator is trusting the system more than they should — before something goes wrong?"

> I'd watch how often they approve, sorted by how confident the system said it was. If people accept the low-confidence recommendations at the same rate as the high-confidence ones, they've stopped reading the confidence and they're just clearing the queue. That's measurable continuously, and it doesn't need an incident to show up.
>
> The second thing I'd insist on is rechecking it after every model update. Trust gets calibrated to how the system used to behave, and it carries over even when the behavior changes underneath it. That's the moment I'd expect the gap to open.

**Boundary, say it:** *"That's a prediction. I've written the framework — it's a thesis, not something I've deployed."*

### 2. Hardware and the physical operator — answer from Sling, not Amazon

> **Likely:** "What would you want measured on an operator station before anyone designs a screen?"

> Reach and posture, with the operator wearing what they'll actually be wearing. Gloves, vest, seated, possibly moving. That gives you the box the controls have to live in, and it's a physical answer, not a preference.
>
> I'd do that before anyone touches the display, because otherwise you design the screen and then discover the person can't hold that position for four hours. That's the work I do now at Sling — reach envelopes, anatomical safety, mechanical fit specs, written so hardware has to clear them.

### 3. Field work with operators — lead with the gap

> **Likely:** "How would you spend two weeks with operators?"

> Straight answer first: most of my work has been lab and simulator, not in the field. That's a real gap and I'd rather say it than dress it up.
>
> What I'd run: week one is watching, with nothing but a question list I've agreed with engineering and product in advance — because operator access is scarce, and one visit should answer three teams' questions rather than mine. Week two is structured tasks against what I actually saw, not what I assumed.
>
> The thing I'd bring back isn't a report. It's a workflow model with the failure points marked, so the next person doesn't have to go back to get the same picture.

**Why this works:** naming the gap first is worth more than the protocol. It's the third debrief sentence in action.

### 4. Growing other people — the honest version

> **Likely:** "How do you raise the level of the people around you?"

> Mostly by making the standard visible. At Sling I built the function from nothing, so the useful thing wasn't advice, it was a review ritual — every spec gets checked against a stated criterion instead of against taste. That raises the floor for everyone including me, and it works whether or not I'm in the room.
>
> The honest boundary: I've mentored inside teams. I haven't managed a research bench. If part of this role is growing one, I'd want to be clear that's a step I'm ready for rather than one I've already taken.

**Do not skip the last sentence.** Claiming management experience you don't have is the fastest way to lose a Head of Research, and volunteering the limit is exactly the move that has been earning you credit all conversation.

### The bridge sentence back to the case

When you've answered one of these and want the ground back:

> "That's the part I'd have to learn here. The part I'd bring on day one is the habit of turning a human limit into a number somebody can build against."

---

## AC08 — The Bridge: Kim's Three Questions

> **This section changed based on `references/Human Factors Response to Autonomous System Design`.** You wrote a four-page research response to three questions Dr. Kim posed publicly at the Learners Conference in San Francisco in May 2026. That document is the strongest asset you have for this specific conversation, and the previous guidance in this repo — which told you never to reference a panelist's talk — was written before it existed. See AC10 for the narrowed rule.

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

## AC09 — The NASA Module (45 seconds)

**Deploy this yourself, around minute 25, before she raises it.** The objection you are pre-empting is that everything above is consumer technology with recoverable consequences.

> The obvious hole in what I've described is that nothing in it was irreversible. Let me give you the version where it was. At NASA Langley I did human-systems integration for Lunar Gateway clinical workstations in simulated microgravity — a use-error analysis against NASA-STD-3001 and MIL-STD-1472 rather than a usability study, because the failures that matter there are rare and high-consequence and won't appear in any sample you can get. Enumerate the error modes, rank by consequence rather than frequency, redesign the physical layout so the irreversible action isn't adjacent to the routine one. Task time dropped thirty percent and the critical input errors were eliminated — and the layout is what eliminated them, not the speed. I was a Ph.D. intern on that, so the analysis and the redesign recommendation are the honest claim, not the program.

**~140 words ≈ 55 seconds.** Say it and stop. If she wants more, the full material is in [05-nasa-case-study.md](practice/05-nasa-case-study.md).

**Why it works here:** it supplies safety-criticality and military-standard fluency, it pre-empts the consumer-tech objection, and volunteering the intern caveat unprompted buys more credibility than the story costs.

---

## AC10 — Evidence Boundaries for This Case

### Assert freely

- Multi-year psychophysics program at Amazon Devices replacing arbitrary engineering latency targets with human perception-derived thresholds; ~$50M in projected operational value
- Method: within-subjects psychophysics using method of constant stimuli — twelve interaction types crossed with six latency levels from 500ms to 3000ms, randomized presentation, repeated cells sufficient to fit a psychometric function, a couple hundred trials per participant, thirty participants, Wizard-of-Oz instrumentation with per-trial millisecond control, three-point slowness rating scale
- The deliberate rejection of an adaptive staircase, for the three stated reasons: two criteria needed, slope needed, and explicability to the engineers who had to accept the number
- Reporting structure: criterion, threshold estimate, confidence interval, and slope, scoped to a stated modality at a held-constant workload verified by a manipulation check
- Two-tier threshold structure (acceptable band and high-satisfaction band) defined per condition, with stated pass criteria
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
| Repetitions per cell | AC01 beat [4] | Twelve types × six levels is 72 cells; the trial count follows from how many times each cell repeated. Confirm the number you'll say, and check the session-length math holds — 200 trials is roughly a 45–50 minute session |
| The secondary task | AC02 Layer 4 | What you actually used to hold workload constant, and what instrument verified it landed |
| Program duration | AC05 | The honest span of the latency program in years, and how many distinct phases |
| Team composition | AC05 | Who you partnered with, described by function only — never by internal org name |
| The disagreement | AC05 | The concrete instance behind "research should describe, not constrain." Have one real example |

---

## AC11 — The 45-Minute Run Sheet

You do not control the agenda. You do control what you have ready and what you volunteer. This is a plan for *your* half of it.

| Minutes | What's happening | What you're doing |
|---|---|---|
| 0–4 | Warm-up, then the case | Discretion line early. Then AC01, 2:50, and stop talking |
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
| 1 | AC01 cold, recorded, no notes | Under 3:00, all eight beats, no internal codename spoken |
| 2 | Each AC02 layer, cold, isolated | Under 90s each, no re-narration of the case |
| 3 | AC03 F1 and F2 word-perfect | The method-choice defense and the trials-not-headcount defense, each under 40s |
| 4 | The tier ladder cold | AC04 in under 40s, all three tiers with what each may and may not authorize |
| 5 | **The off-case four** | AC07, all four cold, in any order. Each must name its own boundary. Zero reaches back to Amazon |
| 6 | Confidentiality audit | Replay every recording; every dollar figure, codename, and competitor mention gets marked. Only ~$50M survives, and it is never hedged with "at least" or "publicly" |
| 7 | The NASA pivot | AC09 delivered unprompted, 45s, with the intern caveat intact |
| 8 | AC08 without flattery | Say the bridge without the words "your talk was interesting." Agenda, not admiration |
| 9 | Mechanism check | Answer any three questions in a row; at least two must land a mechanism, not a finding |
| 10 | Sling check | Across a full mock, Sling comes up at least twice unprompted. If the only job you talk about is one you left in 2024, the level argument is being made from the wrong place |

**The three failure modes on playback:** stacking layers — answering one question with three of AC02 at once, which reads as rehearsed and burns the material you'd need at minute 30; slipping a confidential figure in under pressure, which you will not notice yourself; and reaching back to Amazon during the AC07 stretch, which is the tell of a one-case candidate. Drills 5 and 6 exist for the last two.

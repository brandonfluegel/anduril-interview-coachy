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

# 03 — Culture, Mission-Fit & Stakeholder Track (CQ01–CQ10)

Ten pillars covering mission fit and every stakeholder group you'll face: research leadership, systems/ML, hardware and field test, product, design, operators and customers, security partners, and peers.

**Target: 170–220 words ≈ 75–90 seconds.** Shorter than behavioral. These questions reward a clear position plus one grounded proof point — not a full narrative.

**Structure:** most are **Position → proof point → mechanism**. Where the question says "tell me about a time," switch to STARE+M.

**Hard boundaries in this track.** Location, compensation, travel percentage, and clearance are closed — settled in the recruiter screen. Never raise them, never treat them as a gap, never state or imply a clearance status. Never assert Anduril's internal process, team structure, headcount, or program details; when a question edges there, say what you'd *want* and note you'd take direction. Level is the only open item, and it's argued from scope.

---

## CQ01 — Mission Fit & Motivation

**Stakeholders:** Hiring manager, research leadership, panel at large · **Target:** ~85s

> **Base:** You have spent your career on consumer devices, spaceflight, and automotive systems. Why defense, why Air Defense, and why now?

**Persona variants**

- **Kim:** "What drew you from consumer and aerospace Human Factors to autonomous Air Defense, and what would make you walk away from this kind of work?"
- **Systems/ML:** "Defense work means your recommendations can affect whether a system engages a threat. What changes about how you do research when that is the consequence?"
- **Product:** "Why defense, and why now? I want to know what keeps you here when the schedule gets ugly and the mission gets uncomfortable."
- **Design:** "What about protecting service members changes the way you would approach an operator experience compared with a consumer device?"

### Model answer (~210 words / 85s)

**Position.** The through-line in my work isn't the industry, it's the consequence class. The work I've cared about has been the work where a use error costs something irreversible — Lunar Gateway clinical workstations at NASA, autonomous handovers at Mercedes where the failure mode is a crash. Consumer devices taught me scale and method; those two taught me what I actually want the method for.

**Why Air Defense specifically.** Counter-drone is the clearest case I know of where the machine has to act faster than a person can deliberate, and the human authority question stops being philosophical. That's exactly the problem I've been writing about — *Principles for Agentic Trust* and Calibrated Cognitive Friction are both attempts to answer it. Most domains let you defer that question. This one doesn't.

**Why now.** Agentic systems are being fielded right now, and the human-control patterns are getting set by default rather than by design. Defaults are extremely hard to reverse once operators have trained on them. I'd rather be arguing about this while it's still being decided.

**Honesty beat.** I'll be direct that I haven't worked in defense, and I don't think enthusiasm substitutes for that. What I bring is a method for consequential systems and a specific position on the hardest question in this one.

### Follow-ups

**F1 — "What specifically about counter-drone and air defense pulled you, as opposed to any other defense program?"** *(~70 words)*

> The time constant. In most systems you can design a human-authorization step that's genuinely deliberative, because the timeline permits it. Counter-drone compresses that until the authorization question becomes structural rather than procedural — you have to decide in advance what the human is actually for. That's the exact question my thesis is about, and there aren't many places where it's a live engineering problem rather than a paper.

**F2 — "Where is your personal line on this work, and what would you refuse to design?"** *(~75 words)*

> My line isn't about lethality — it's about comprehension. I'd refuse to design an interface whose purpose is to make authorization easier without making the basis for it clearer, because that produces a human who is accountable for something they can't evaluate. That's not a safeguard, it's a liability shield. I'd say that in a design review, and I'd want it to be a rule we agreed on rather than a stand I take.

**F3 — "What have you actually done to prepare for this domain beyond reading about it?"** *(~75 words)*

> The honest answer is that the preparation is in the work, not in a course. I applied MIL-STD-1472 and NASA-STD-3001 to a safety-critical workstation and ran a uFMEA against it. I wrote an audit framework for non-deterministic agentic systems and put it through peer review at CSCW. And I've built a specific position on operator authority I can defend and falsify. What I haven't done is spend time with military operators, and that's the first thing I'd fix.

### Senior → Lead/Staff

- **Senior:** gives a sincere personal motivation.
- **Lead/Staff:** ties the motivation to a specific research position they intend to advance, and names the trade-offs they accept to hold it.
- **Say this:** *"I'm not here because defense is interesting. I'm here because the authorization question is being answered by default right now, and I have a position on it I'm willing to be wrong about in public."*

---

## CQ02 — Ownership With Little Oversight

**Stakeholders:** Research leadership, product, program · **Structure:** STARE+M · **Target:** ~90s

> **Base:** This role expects you to work through ambiguity with little oversight. Tell me about a time nobody told you what to research and you had to decide.

**Persona variants**

- **Kim:** "With no assigned roadmap and no research precedent on this team, how would you choose your first study, and who would you tell before you started?"
- **Systems/ML:** "If nobody asks you for Human Factors input, how do you insert yourself into a technical decision before the architecture is locked?"
- **Product:** "Nobody is going to hand you a research brief here. Tell me about a time you defined the question yourself and were held to the outcome."
- **Design:** "How do you decide what to investigate when design, product, and engineering are all moving without waiting for you?"

### Model answer (~215 words / 86s)

**Situation.** At Sling nobody asked me to write *Principles for Agentic Trust*. There was no mandate for it and it wasn't on anyone's roadmap. What existed was a gap I could see from inside the work: we were evaluating non-deterministic AI behavior with usability methods built for deterministic systems, and the methods were quietly failing.

**Task.** I decided that was the highest-value thing I could do, and I owned that call.

**Action.** I scoped it to be checkable rather than philosophical — four audit dimensions, Alignment, Execution, Control, and Calibration, each with something you could actually assess. I told my stakeholders what I was doing and why before I was sure it would work, which I think is the part that matters: self-direction without disclosure is just working on what you like. And I put it through external peer review, because a framework nobody outside the building has stress-tested is an opinion with formatting.

**Result.** It was accepted to ACM CSCW 2026 Industry Perspectives, and it's the shared language the organization now uses for agentic systems.

**Earned secret.** The risk in autonomous ownership isn't picking the wrong problem — it's picking a right problem privately. Announcing the bet early costs nothing and it's what converts a personal project into something the team can use.

**Mechanism.** The framework itself is the mechanism: it's how the next agentic feature gets evaluated whether or not I'm involved.

### Follow-ups

**F1 — "How did you know it was the right thing to work on, and what did you deliberately ignore?"** *(~70 words)*

> I knew because the failure was recurring — the same category of question kept arriving and our methods kept giving unsatisfying answers. Recurrence is the signal I trust most; a one-off gap is usually noise. What I deliberately ignored was the queue of individual feature evaluations. Some of those went unserved, and a few people noticed. That was the actual cost, and I'd make the trade again, but I wouldn't pretend it was free.

**F2 — "Who did you keep informed, and how did you avoid surprising them with your conclusion?"** *(~65 words)*

> I told stakeholders at the start, when it could still have been stopped, rather than presenting a finished thing. And I shared the framework in draft while it was still ugly. Surprise is the enemy of adoption — if the first time someone sees your conclusion is the day you want them to act on it, you've made adoption a referendum on you instead of on the work.

**F3 — "Tell me about a time you self-directed onto the wrong problem. How long did it take you to notice?"** *(~70 words)*

> [Your specific instance.] The signal I now watch for: nobody asks about it. Not disagreement — disagreement means it's live. Silence for several weeks means it isn't connected to a decision anyone is making, and that's usually correct feedback. My rule is a checkpoint at four weeks where I ask what decision this now touches, and if I can't name one, I stop rather than finish it out of momentum.

### Senior → Lead/Staff

- **Senior:** self-manages assigned scope well.
- **Lead/Staff:** sets the agenda for the function, publishes the rationale, and is accountable for the bets they chose.
- **Say this:** *"I'd want to be judged on the bets I picked, not just on how well I executed the ones I was handed."*

---

## CQ03 — Months, Not Years

**Stakeholders:** Product, engineering, program leadership · **Target:** ~85s

> **Base:** Anduril's stated bar is delivering capability to the military in months, not years. What does research look like at that cadence, and where does it break?

**Persona variants**

- **Kim:** "At a months-not-years cadence, which parts of your research process are non-negotiable and which are the first to be cut?"
- **Systems/ML:** "We will not stop the build for a study. How do you get evidence into a decision that is already in flight?"
- **Product:** "What does your research calendar look like in a quarter where we ship twice and field-test once?"
- **Design:** "How do you keep research feeding design at sprint speed without turning into a rubber stamp on decisions already made?"

### Model answer (~205 words / 82s)

**Position.** At that cadence research stops being a project format and becomes two different things: a standing constraint layer that's already in place before anyone asks, and very short studies aimed at single decisions.

**What's non-negotiable.** Two things only. The claim has to match the design that produced it — a four-day study reported as a four-day study is honest at any speed. And anything irreversible gets the higher bar regardless of schedule, because that's precisely the decision you can't correct later at speed.

**What gets cut first.** Sample size, generality, and the write-up. I'd cut all three before I'd cut piloting, which people cut first and which is the one that actually destroys a fast study.

**Where it breaks.** It breaks on questions that are irreducibly slow — anything about learning, skill retention, or vigilance over long durations. You cannot compress a fatigue effect. Pretending otherwise is where fast research becomes dishonest research, and I'd rather say "this one can't be answered in the window, here's what we can know instead" than deliver a compressed version of an uncompressible question.

**Proof point and mechanism.** At Amazon the multi-year work was rigorous precisely so the fast work could be fast — once perceptual thresholds existed, dozens of downstream decisions needed no study at all. That's the model: invest in the constraint layer, and the cadence takes care of itself.

### Follow-ups

**F1 — "Give me the fastest study you have run that still changed a hardware or software decision. How many days?"** *(~65 words)*

> [Your specific instance — days, n, decision.] The general pattern: the fastest studies that change decisions are binary ones. Can operators do this at all; do these two controls get confused. Those resolve in days with very few participants, because a failure seen twice is real. Magnitude questions are what need time, and teams ask for them more often than they need them.

**F2 — "What did you get wrong by moving that fast, and how did you catch it?"** *(~70 words)*

> [Your specific instance.] The error mode fast work produces for me is over-generalization — a result that was true for the condition I tested getting quoted as if it were true in general, usually by someone else, three weeks later. I catch it by writing the scope limit into the finding itself rather than into a caveats section, because caveats sections don't travel with the sentence.

**F3 — "When would you tell a team to ship without research rather than wait for you?"** *(~70 words)*

> When the decision is reversible, cheap to correct, and my study wouldn't land before the call has to be made. That's most decisions. Saying it out loud is one of the more valuable things I do — it's what makes the rare "this one, wait" credible. A research function that never says ship without me gets ignored uniformly, which is worse than being ignored selectively.

### Senior → Lead/Staff

- **Senior:** compresses timelines when asked.
- **Lead/Staff:** designs the tiered evidence model that lets the organization move fast on purpose rather than by accident.
- **Say this:** *"Speed isn't the problem. Unowned speed is. I'd rather the team decide out loud that this question is worth four days than have me quietly decide it's worth four weeks."*

---

## CQ04 — Engineering Partnership

**Stakeholders:** Systems, ML, software, and test engineers · **Target:** ~85s

> **Base:** How do you embed with systems, ML, and software engineers so Human Factors evidence lands inside their workflow instead of arriving as a report?

**Persona variants**

- **Kim:** "How do you build the kind of engineering relationships that let research change an architecture rather than annotate it?"
- **Systems/ML:** "What would you put in my backlog, my test plan, or my requirements doc so your findings are something I can actually action?"
- **Product:** "How do you keep engineering from treating research as a review gate they have to survive?"
- **Design:** "When engineering, design, and research disagree about an operator interaction, how do you keep that a technical debate instead of a turf fight?"

### Model answer (~205 words / 82s)

**Position.** Findings don't land; requirements do. So my output into engineering is written in their artifact, not mine — a requirement with an acceptance test, a failure mode in the risk register, a test case. If the only place my evidence exists is a document I own, it will be read by my team and nobody else.

**Mechanism, concretely.** Three things. A finding becomes a named constraint with a verification method — not "operators struggled with X" but "X must satisfy this criterion, measured this way." Failure modes go into the risk analysis in severity/detectability language, because that's the vocabulary that already has a process attached to it. And I show up before the architecture is set, with the constraint that's about to bite, rather than after with an evaluation.

**Proof point.** At Amazon, my perceptual work only changed engineering behavior when it stopped being a finding and became a spec format — threshold, percentile, modality, and a defined fallback if the hardware couldn't hit it. The fallback is the part that did the work: it converted my evidence from a risk transfer into a risk absorption.

**Limit.** I don't know what artifacts are load-bearing here. The first thing I'd ask an engineering lead is which document actually gets read, and then I'd write into that one.

### Follow-ups

**F1 — "Name the artifact engineers actually read from you. Was it a deck, a ticket, a requirement, or a test case?"** *(~65 words)*

> The requirement, every time — and I'd say decks are the least effective thing I've produced, despite being the most requested. A deck gets attention once, in a room, and then stops existing. A requirement with an acceptance test gets read by whoever implements it and whoever verifies it, months later, without me. If I could only produce one artifact type, it would be that one.

**F2 — "When did an engineer change their mind because of your evidence, and what specifically moved them?"** *(~70 words)*

> At Amazon it wasn't the data — I led with data first and it failed. What moved them was bounding the risk: a specification with a defined fallback if the hardware couldn't hit the threshold. Their resistance was never to the finding, it was to owning an unbounded consequence. Once the fallback existed, the same evidence became easy to accept. I've assumed that's the general case ever since.

**F3 — "How do you handle an engineer who says your sample size is too small to matter?"** *(~75 words)*

> I usually agree with the part that's right and separate the claims. Small n genuinely can't support a population estimate, and I won't pretend otherwise. But it can support an existence claim — this failure occurs, here's the mechanism — and that's frequently what the decision needs. If the decision truly needs a magnitude estimate, then he's correct and I need a different study, and I'd rather say that than defend a number I can't support.

### Senior → Lead/Staff

- **Senior:** communicates findings clearly to engineers.
- **Lead/Staff:** makes Human Factors traceable inside engineering's own requirement and verification artifacts.
- **Say this:** *"I'd rather write one line in your requirements doc than give the best research presentation of my career."*

---

## CQ05 — Hardware & Field Test Collaboration

**Stakeholders:** Mechanical and industrial design, hardware engineers, field test, manufacturing · **Target:** ~85s

> **Base:** Hardware decisions get expensive fast. How do you work with mechanical, industrial design, and field test partners so ergonomic evidence arrives before a design freeze?

**Persona variants**

- **Kim:** "How do you time physical Human Factors evidence to hardware milestones so it is still cheap to act on?"
- **Systems/ML:** "What do you need from hardware and test partners to validate a physical interface before we build tooling?"
- **Product:** "Hardware changes late are the most expensive thing we can do. How do you make sure your ergonomic finding shows up early enough to matter?"
- **Design:** "How do you and industrial design divide the physical interaction problem so you are not duplicating or contradicting each other?"

### Model answer (~200 words / 80s)

**Position.** Ergonomic evidence has a value curve that collapses, and it collapses at tooling. So I don't schedule physical research by study convenience — I schedule it against hardware milestones, working backwards from the last point where a change is still cheap.

**Mechanism.** Practically that means the constraint work happens before there's anything to evaluate. Encumbered anthropometry and reach envelopes can be established from digital human modeling and dimensionally accurate mock-ups — foam and printed parts, no electronics — which means I can produce a bounding specification while industrial design is still exploring form. Then the physical checkpoint sits before tooling commitment, not before launch. And I want field test in that loop early, because they see the system in real conditions before I do and they know the failure modes I'd otherwise spend a trip discovering.

**Proof point.** At Sling I define physical ergonomics, reach-envelope modeling, anatomical safety, and mechanical fit specifications. At NASA the layout and control-display redesign against NASA-STD-3001 and MIL-STD-1472 is what eliminated critical input errors — geometry, not software.

**The division with industrial design.** They own form, manufacturability, and aesthetic coherence. I own the bounding constraints and the use-error consequences of geometry. When we contradict each other, it's almost always because the constraint wasn't written down early enough for them to design against.

### Follow-ups

**F1 — "Tell me about a time your evidence arrived too late to change the hardware. What did you do?"** *(~75 words)*

> [Your specific instance.] When it happens, the move is to shift from the physical fix to the mitigation stack — procedure, training, software compensation — and to document explicitly that it's a mitigation, not a fix, so it appears as accepted risk on the next revision rather than disappearing. The larger correction is always calendar, not method: late evidence is almost never a study problem, it's a milestone-visibility problem.

**F2 — "How do you get useful ergonomic data from a mock-up rather than a production unit?"** *(~70 words)*

> Dimensional accuracy is what matters, not function. A non-functional mock-up at correct dimensions gives you real reach, clearance, pinch points, sightlines, and sustained-posture load — with participants in actual encumbrance, which is the variable people leave out. What a mock-up cannot give you is anything thermal, vibrational, or duration-dependent. I scope those explicitly to the first functional article rather than over-claiming what the foam told me.

**F3 — "How do you work with field test teams who see the system in real conditions before you do?"** *(~70 words)*

> I treat them as instrumentation rather than as competition. They're seeing conditions I'll never schedule, so the highest-leverage thing I can do is give them a small, specific observation protocol — three or four things to capture — so their trips return usable human-factors data. In exchange they tell me where to spend my scarce operator access. That trade has been worth more to me than any single study I could have run instead.

### Senior → Lead/Staff

- **Senior:** evaluates hardware when asked.
- **Lead/Staff:** embeds Human Factors checkpoints into the hardware milestone cadence so the evidence is never late.
- **Say this:** *"I want a standing checkpoint before tooling, not an invitation to review. If I'm being invited, we're already past the point where I'm cheap."*

---

## CQ06 — Product & Roadmap Partnership

**Stakeholders:** Product managers, program leadership, business stakeholders · **Target:** ~85s

> **Base:** How do you integrate research into an existing roadmap without becoming either a bottleneck or a rubber stamp?

**Persona variants**

- **Kim:** "How do you keep a research agenda intact while serving a roadmap that changes underneath you?"
- **Systems/ML:** "When product priorities and safety evidence point different directions, what do you bring to that conversation besides an opinion?"
- **Product:** "Walk me through how you would plug into my planning cycle. What do you need from me, and what do I get from you every sprint?"
- **Design:** "How do you keep research shaping the roadmap upstream instead of validating decisions that are already designed?"

### Model answer (~200 words / 80s)

**Position.** Bottleneck and rubber stamp are the same failure with different symptoms — both come from research being positioned as a checkpoint. The fix is placement, not effort: most of my output should be constraints that exist *before* the question is asked, so the roadmap moves through a floor rather than around a gate.

**Mechanism.** Three parts. Standing criteria available in advance, so the majority of decisions clear themselves without my involvement. A visible intake — decision, owner, date, consequence class — so people can see what they're competing with and why they won or lost. And a protected allocation for foundational work, because roadmap-driven research eats the agenda entirely within two quarters if you let it.

**What the PM gets.** Every cycle: an answer to the decision that's actually blocking, and an honest "you don't need a study for this" when that's true. The second one is a service, not a refusal, and it's what makes the rare "wait for me" credible.

**Proof point.** At Amazon my work shaped strategy across a portfolio reaching 75M+ customers, and the leverage was never study volume — it was that perceptual thresholds existed, so a whole class of roadmap decisions stopped needing research at all.

### Follow-ups

**F1 — "What is the intake process you would want, and what happens to requests that do not fit it?"** *(~70 words)*

> One page: what decision, whose decision, by when, and what happens if we're wrong. Requests that can't fill that in usually aren't research requests — they're either a decision someone doesn't want to own, or a question that's already been answered. Both get a conversation the same week instead of a study. Nothing gets silently queued; a request sitting in a backlog for six weeks is a no that nobody had the nerve to say.

**F2 — "Tell me about a time your evidence killed or materially changed a feature people wanted."** *(~75 words)*

> [Your specific instance.] The closest canonical case is the latency work at Amazon, which changed targets in both directions — some specs were tighter than anyone could perceive, so we were paying for performance that couldn't be detected. Killing over-engineering is the version of this that builds the most credibility, because it establishes that your evidence isn't systematically biased toward more caution and more cost.

**F3 — "How do you represent business needs, not just user needs, in that recommendation?"** *(~70 words)*

> By putting the cost of the recommendation in the recommendation. If a control costs seconds in a time-critical flow, I state that cost, not just the risk it mitigates — the PM shouldn't have to discover the downside himself. And I'll say when the business case wins. A researcher who only ever advocates for the user is easy to discount, because everyone knows the answer before you speak.

### Senior → Lead/Staff

- **Senior:** services roadmap questions well.
- **Lead/Staff:** shapes which questions the roadmap asks, and makes the research intake and prioritization model explicit.
- **Say this:** *"I'd measure myself on how many decisions got made well without me, not on how many studies I ran."*

---

## CQ07 — Design Partnership & Critique

**Stakeholders:** Design lead, product designers, content and visualization partners · **Target:** ~85s

> **Base:** How do you partner with design so research is co-ownership of the operator experience rather than a verdict delivered after the fact?

**Persona variants**

- **Kim:** "How do you keep a productive boundary with design so research neither dictates solutions nor gets reduced to usability testing?"
- **Systems/ML:** "When design and research reach different conclusions about an operator workflow, how does that get resolved before it hits my team?"
- **Product:** "How do you and design present one recommendation to me instead of two competing ones?"
- **Design:** "Be honest: where does a researcher's input stop being helpful and start being design by committee?"

### Model answer (~200 words / 80s)

**Position.** The boundary I hold is that I own the constraints and the evidence about what happens to people; design owns the solution space inside them. When I cross into specifying the solution, I'm doing a worse version of someone else's job, and I've watched that dynamic wreck research-design relationships more often than any disagreement about findings.

**Answering the honest version of the question.** A researcher stops being helpful the moment they start giving feedback on execution — spacing, hierarchy, wording — rather than on consequence. If I can't connect a comment to a use error, a workload cost, or a physical constraint, I shouldn't be making it in a critique. I try to hold myself to that literally.

**Mechanism.** What makes co-ownership real is shared artifacts rather than shared meetings. A blueprint and an authority-state map that we both maintain means design and research are working from one model of the operator, so disagreements surface as disagreements about the model — which is resolvable — instead of about taste, which isn't.

**Proof point.** At Amazon the multimodal interaction architecture work was genuinely joint; my contribution was the perceptual and cognitive constraint layer, and the interaction design was better than anything I would have specified alone. That's the arrangement I want.

### Follow-ups

**F1 — "Tell me about a time you were wrong in a design critique and a designer's instinct beat your data."** *(~75 words)*

> [Your specific instance.] The general shape, and I've seen it more than once: my evidence was right about the failure and wrong about the cause, so my implied fix would have addressed a symptom. A designer who'd spent longer in the problem space saw the actual structure. What I took from it is that a finding is authoritative about *what happened* and much weaker about *why* — and researchers routinely over-extend into the second one.

**F2 — "How do you deliver a finding that invalidates a design someone spent weeks on?"** *(~70 words)*

> Early, privately, and framed around the constraint rather than the artifact. Early matters most — the cost isn't the invalidation, it's the three extra weeks spent after I already knew. Privately first so the designer isn't finding out in a room. And framed as "here's the constraint this runs into," which is a shared problem, rather than "this doesn't work," which is a verdict and invites defense instead of iteration.

**F3 — "What do you do when design wants one consistent pattern and your evidence supports risk-proportional variation?"** *(~75 words)*

> I try to give them a consistent *rule* rather than a consistent pattern, because that's what consistency is actually protecting — predictability for the operator. If the rule is "irreversible actions always behave this way, reversible ones always behave that way," the system is learnable and the variation is meaningful. What genuinely breaks operators is unprincipled variation. Uniformity across consequence classes is a different failure: it trains people to treat everything identically, which is exactly what we can't afford.

### Senior → Lead/Staff

- **Senior:** collaborates well with designers.
- **Lead/Staff:** establishes the shared artifacts and critique norms that keep research and design converging by default.
- **Say this:** *"If design and I are arriving at different conclusions, that means we're working from different models of the operator — and the fix is one shared model, not a better argument."*

---

## CQ08 — Operator & Customer Access

**Stakeholders:** Military operators, government and program customers, field liaisons, training staff · **Target:** ~85s

> **Base:** Operator access is scarce and expensive. How do you build and protect a working relationship with military end users across a program?

**Persona variants**

- **Kim:** "How would you build a sustainable operator research panel and cadence when access is limited and every visit is expensive?"
- **Systems/ML:** "How do you make one field visit produce enough evidence to change a requirement, given we may not get back for months?"
- **Product:** "How do you maximize the return on a trip when three teams all want their questions answered by the same operators?"
- **Design:** "How do you keep operators engaged as partners across a program rather than treating each visit as a one-off test session?"

### Model answer (~205 words / 82s)

**Position.** I'd treat operator access as shared infrastructure with a protocol attached, not as a research budget I spend. That reframe drives everything else — if it's infrastructure, then the questions of who gets access, in what sequence, and what comes back to the operator are organizational decisions with owners, not favors negotiated trip by trip.

**Mechanism.** Three things. A consolidated question set before any trip, so three teams' questions get answered in one visit rather than three — which is usually feasible, because most of them are answered by the same observation. A standing observation protocol, so field test partners and engineers who get there before I do return usable data. And a closing of the loop: operators find out what changed because of what they told us. That single practice is what converts a participant into a partner, and it's the one organizations skip.

**Proof point.** At Uber I worked with drivers in live conditions where their time was literally their income; at NASA I worked with domain experts whose expertise exceeded mine in the task. The lesson from both is that credibility comes from showing what changed, not from how well you ran the session.

**Boundary.** I haven't worked with military operators, and I'd expect the access model here to have constraints I don't yet know. I'd take direction on that rather than assume my model transfers.

### Follow-ups

**F1 — "How do you earn credibility with an operator in the first ten minutes?"** *(~70 words)*

> By being visibly there to learn rather than to test. Concretely: I say what I don't understand, and I show my model of their work and invite correction. People who suspect a researcher can't understand their job are highly motivated to fix your description of it, and that's the fastest rapport I know. What kills it in the first ten minutes is defending your model, or opening with a script.

**F2 — "How do you share operator time with other teams without burning the relationship?"** *(~70 words)*

> Consolidate before you arrive, and have one person accountable for the total ask. The failure mode isn't sharing — it's three uncoordinated requests that each seem reasonable and together are an imposition. I'd rather run a session with another team's questions in it than have that team schedule separately. And I'd want a visible ledger of what's been asked of whom, so the load is a fact rather than a guess.

**F3 — "What do you send back to those operators afterward so they see their input mattered?"** *(~65 words)*

> Short, specific, and about the change, not the research: here's what you told us, here's what's different now. Not a report — nobody reads a report they didn't commission. And where nothing changed, say that too, with the reason. Operators are used to being consulted and ignored; being told honestly that a constraint prevented the change buys more trust than a selective success story.

### Senior → Lead/Staff

- **Senior:** runs strong field visits.
- **Lead/Staff:** builds the participant pipeline, cadence, and shared access model the whole organization draws on.
- **Say this:** *"The scarcest resource in this domain isn't research capacity, it's operator hours. I'd want to be accountable for how the organization spends them, not just for how I spend mine."*

---

## CQ09 — Security-Conscious Collaboration

**Stakeholders:** Security and compliance partners, program leadership, government stakeholders · **Target:** ~80s

> **Base:** Some of this work sits behind access restrictions. How do you run research operations and share insights when findings cannot travel freely?

> ⚠️ **Boundary:** never state or imply a clearance status, never assert Anduril's internal handling process, and never speculate about classified content. Speak to your handling track record, your proposed practice, and your willingness to take direction.

**Persona variants**

- **Kim:** "How would you design a research repository and synthesis practice that works when some findings cannot be written into it?"
- **Systems/ML:** "How do you keep requirements traceable to evidence when the evidence lives at a different access level than the requirement?"
- **Product:** "How do you brief stakeholders who cannot see the underlying data but still have to make the call?"
- **Design:** "How do you keep design partners aligned to operator reality when you cannot show them everything you saw?"

### Model answer (~195 words / 78s)

**Position.** The practice I'd want is two-tier synthesis. Most human-factors findings have a generalizable layer — the failure mode class, the perceptual or workload principle, the constraint — that is expressible without the specifics that make it restricted. That layer goes where the team can use it. The instance stays where it belongs, with a pointer recording that substantiating evidence exists and who can speak to it.

**Why the pointer matters.** Without it, teams conclude no evidence exists and re-derive the wrong answer confidently. A record that says "this is grounded, ask this person" is often enough to prevent a bad decision even when the content can't travel — and it's the part people omit.

**On traceability.** A requirement can cite a constraint and its owner without citing the underlying data. That's normal in regulated research: the chain of custody for evidence and the statement of the requirement live at different levels, and the link between them is maintained by a person, not a document.

**Track record.** I've worked under IRB and federal research compliance handling clinical and physiological data, and on safety-critical government-adjacent work at NASA. I'd take direction on the specific rules here rather than import assumptions.

### Follow-ups

**F1 — "What is your track record handling sensitive or regulated research data, and what protocol did you follow?"** *(~70 words)*

> At Brigham and Women's I processed neuroimaging, ECG, and telemetry data for acute-stress research under IRB and federal research compliance — de-identification, controlled access, documented chain of custody. At NASA the work was safety-critical and government-adjacent. The habit that carries over is treating handling rules as design constraints on the research itself rather than as paperwork after the fact — it changes what you collect, not just where you store it.

**F2 — "How do you separate what is genuinely restricted from what is just being hoarded?"** *(~70 words)*

> By asking what specifically makes it restricted, and expecting a rule-based answer rather than a judgment call. Genuine restriction cites a category. Hoarding cites discomfort. That said, I'd be careful about my own confidence here — in a new organization I wouldn't assume I can tell the difference in month two, so I'd ask rather than decide, and I'd raise a pattern rather than challenge an instance.

**F3 — "What do you do when a compartmented finding contradicts a widely held team assumption?"** *(~75 words)*

> I go to whoever can act on it at the right level, rather than trying to signal it sideways to the team — hinting is the worst option and it's the tempting one. Then I look for whether the *generalizable* layer of the finding can be stated without the specifics, because usually it can, and that's often enough to change the assumption. If it isn't, the correction has to be made by someone with the access to make it.

### Senior → Lead/Staff

- **Senior:** follows handling rules correctly.
- **Lead/Staff:** designs the two-tier synthesis and briefing practice that keeps decisions evidence-driven inside those constraints.
- **Say this:** *"The failure I'd design against is a team concluding there's no evidence when there is. A pointer costs nothing and prevents that."*

---

## CQ10 — Teammate Behavior, Culture & Mentorship

**Stakeholders:** Research peers, junior researchers, cross-functional partners, recruiting · **Target:** ~85s

> **Base:** The posting asks for a good teammate who shapes team culture and mentors. What is the specific culture you would build here, and what would you refuse to tolerate?

**Persona variants**

- **Kim:** "As a senior researcher joining a small function, what culture and quality bar would you set, and how would you set it without being appointed to?"
- **Systems/ML:** "How do you raise the Human Factors literacy of engineers who have never worked with a researcher before?"
- **Product:** "What makes you a teammate people want on a hard program at two in the morning, rather than just a strong individual researcher?"
- **Design:** "How do you give and take hard critique in a small team without it becoming personal or political?"

### Model answer (~205 words / 82s)

**The culture, specifically.** One where it's normal to report the null, kill your own study, and say "I don't know" in front of engineers. That sounds soft; it's the opposite. A research function whose findings always conveniently support more research is worthless, and everyone outside it can tell within a quarter.

**What I'd refuse to tolerate.** Two things. Certainty that outruns the evidence — stating a finding without its boundary, because in this domain someone will build on it. And quiet non-cooperation after losing a decision: the slow-walk, the relitigation in the next meeting. If we lost, we lost, and we go get better evidence.

**How you set it without authority.** Not by advocating — by what you visibly reward and what you visibly do. I make a point of publicly crediting the person who reports the inconvenient result, and I say "I don't know, here's how I'd find out" in rooms where it costs me something. Culture is set by what senior people do when it's expensive, and everyone is watching for exactly that.

**Proof point and mechanism.** At Sling, *Principles for Agentic Trust* became shared language across teams — that's the mechanism I trust. A framework people argue *inside of* does more for a team's quality bar than any statement of values.

### Follow-ups

**F1 — "Name someone you mentored and the capability they had afterward that they did not have before."** *(~70 words)*

> [A real person, one specific capability, one sentence on how.] **Do not answer this generically.** This is the single highest-leverage follow-up in the entire culture track for a Lead/Staff argument, and a vague answer reads as never having mentored anyone. Good shape: "They could scope a study to a decision rather than to a question — I stopped giving them research questions and started giving them decisions, and made them write the question themselves."

**F2 — "What behavior have you actually confronted on a team, and how did that conversation go?"** *(~70 words)*

> [Your specific instance.] The category I do confront reliably is overstated certainty — a finding presented without its boundary to an audience that will build on it. I raise it privately and immediately, framed as risk to them rather than as correction: if this gets built on and the boundary surfaces later, it lands on you. That framing has never gone badly for me, and it's true, which is why.

**F3 — "How do you shape culture when you have no direct reports and no formal authority?"** *(~70 words)*

> Artifacts and visible behavior. A written criterion changes what people do when I'm not there, which advocacy never does. And people calibrate on what a senior person does when it's costly — saying "I don't know" in a room where confidence would be easier, or crediting the person whose result was inconvenient. Authority makes that faster. It isn't the mechanism, and waiting for it is how researchers stay junior.

### Senior → Lead/Staff

- **Senior:** is a strong individual contributor and informal mentor.
- **Lead/Staff:** installs the rituals, quality bar, and growth path that raise the whole function's floor.
- **Say this:** *"The culture question I'd want to be judged on is whether it's safe here to report a null. Everything else about research quality follows from that one."*

---

## Track drill sheet

| ID | Pillar | Primary stakeholder | Hardest follow-up | Needs your input |
|---|---|---|---|---|
| CQ01 | Mission fit | Hiring manager | F2 — your personal line | |
| CQ02 | Ownership, no oversight | Research leadership | F3 — wrong problem | ✔ |
| CQ03 | Months not years | Product / engineering | F1 — fastest study | ✔ |
| CQ04 | Engineering partnership | Systems / ML | F3 — sample size challenge | |
| CQ05 | Hardware & field test | Mechanical / ID / test | F1 — evidence arrived late | ✔ |
| CQ06 | Product & roadmap | Product | F2 — evidence killed a feature | ✔ |
| CQ07 | Design partnership | Design | F1 — designer beat your data | ✔ |
| CQ08 | Operator access | Operators / customers | F1 — first ten minutes | |
| CQ09 | Security-conscious | Security / program | F2 — restricted vs hoarded | |
| CQ10 | Culture & mentorship | Peers / juniors | F1 — name a mentee | ✔✔ |

**Boundary rehearsal.** Three sentences you should be able to say without hesitation, because each converts a gap into evidence of judgment:

1. *"I haven't worked with military operators — I've worked with high-stress domain experts, and I'd rather be exact about the difference."*
2. *"I don't know how that's structured here, and I'd take direction rather than assume my model transfers."*
3. *"That's my thesis, not a deployed result."*

**Three sentences that carry this entire track:**

1. *"Bottleneck and rubber stamp are the same failure — both come from research being a checkpoint instead of a floor."*
2. *"I'd rather write one line in your requirements doc than give the best research presentation of my career."*
3. *"I'd measure myself on how many decisions got made well without me."*


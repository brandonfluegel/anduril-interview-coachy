# Anduril Industries — Senior Human Factors Engineer, HSI/HFE

**I measure how people actually perform with a system, and I turn that into requirements that engineers can build to and test against. Along the way, I run quick rounds of design testing. I pick the method based on what the decision needs to know.**

## Ground rules

- Three beats, sixty to seventy-five seconds: the claim, the proof, the boundary. Then I stop. Citations, standard numbers, and dates come out only when someone asks.
- I don't define terms to Jake. He's the HSI lead, so explaining HSI, its domains, or fNIRS reads as explaining his job to him.
- Before a design or planning answer, I ask one scoping question, and then I answer. Two or three questions per interview at most; the rest wait for my question time.
- Say "operator" and "assets," not "pilot" or "aircraft," unless the interviewer does. The operator may be a soldier. Never say "customer," "delight," "pain point," or "engagement."
- EchoStar is "since June 2025," and I have "six-plus years" in industry. The only dollar figure is fifty million, always "projected" by an economics team's model.
- NASA was formative, never "validation," and the thirty percent was a side effect. fNIRS was Amazon, and fMRI was Brigham. No Mercedes percentage.
- Program facts come only from public postings and anduril.com. I never name a platform first, and nothing Daniella shared goes into an answer.
- I don't claim HSI work under contract or operator experience I don't have. If asked, one honest sentence, then how I'd learn the user: time with operators at test events.
- Never say "downlevel," "co-invented," or "I haven't worked in defense," never name the other company or Calibrated Cognitive Friction, and never reopen level.
- "I don't know, and here's how I'd find out" beats any guess. I say "I use" only for methods I've actually run.

**Rehearse first, out loud, sixty to seventy-five seconds each:** The bridge from Monday; Tell me about yourself; Researcher or engineer?; Latency; HSI program fluency; Writing verifiable requirements; MPT; Span of control; the thirty-sixty-ninety.

## The bridge from Monday — Tier 1

> **Why it's here:** Jake watched me pitch a seat built on rapid qualitative work. I name the shift once, early, so it reads as range, not reinvention. **Jake only.** The TPM wasn't there Monday, and the team meeting shouldn't open on a correction.

### Answer

**Say it once, to Jake.** "Monday I led with the research half, because that was the seat. This seat is the other half: requirements, verification, and HSI documentation."

**If asked, "What happened with Air Defense?"** "They chose someone else, the feedback was fair, and this seat is closer to my training."

**If they raise the other resume.** "That earlier version used functional titles. My titles of record are Staff Product Researcher and UX Researcher II. The engineering work behind both versions is the same." I answer only what's asked about its wording, and I don't volunteer anything else.

---

## Facts I say out loud

- I've been at EchoStar since June 2025 as a Staff Product Researcher, working on Sling, which is part of EchoStar. I built a net-new human factors function there, and I report to the VP of Product.
- From November 2024 to June 2025, I was a Managing Scientist in Human Factors at J.S. Held.
- From June 2020 to November 2024, I was a UX Researcher II in human factors in Amazon's Devices Design Group, and the sole human factors researcher in the group. I hold patent US-12532040-B1 and a 2023 Amazon Inventor Award.
- From 2018 to 2019, I was a PhD intern at NASA Langley on the Lunar Gateway medical workstation, and I led its human-systems integration evaluation.
- In 2017, at Mercedes-Benz, I ran simulator studies of sound, vibration, and biometric takeover alerts during Level 2 automated-driving handovers.
- I have an MS in Human Factors Psychology from Old Dominion, from 2017, and a PhD from 2020. My "Principles for Agentic Trust" paper was accepted at ACM CSCW 2026, in Industry Perspectives.
- I don't hold a clearance today. I'm fully eligible, with a clean background.

## Crash course: the ideas behind the answers

#### How a defense program works

- **Human systems integration (HSI).** Treating the people who operate and maintain a system as part of the system, planned with the same weight as hardware and software. DoD Instruction 5000.95 splits it into seven domains: human factors engineering, manpower, personnel, training, safety and occupational health, force protection and survivability, and habitability.
- **Manpower, personnel, and training (MPT).** Three of those domains, as three questions: how many people does the system need, what kind of people with what skills, and what training gets them there.
- **MIL-STD-1472.** The military's design rulebook for the human side of equipment: control sizes, display legibility, reach distances, labels, and alarms. The current version is H, from 2020; my NASA work in 2018 used G.
- **MIL-STD-46855A.** The process rulebook. It says what human engineering work a contractor has to do, and when, across analysis, design, and test. 1472 is the "what"; 46855A is the "how and when."
- **MIL-STD-882E.** The system safety standard. Each hazard is rated on how bad it would be and how likely it is, which gives its risk level. Fixes go in a fixed order: design the hazard out, add engineered safeguards, add warnings, and only then rely on procedures and training.
- **SAE6906A.** The industry standard for running an HSI program. Each requirement is numbered so a program can pick which ones apply, which is called tailoring.
- **Data item description (DI-HFAC-…).** The government's template for a document the contractor delivers, such as the HSI Program Plan.
- **Design reviews.** The formal gates in a classic program: system requirements review (SRR), preliminary design review (PDR), critical design review (CDR), and test readiness review (TRR). Each one has human factors work due.
- **Interface control document (ICD).** The agreement between two systems about exactly what data passes between them. If an operator sees that data, it needs human factors requirements, like how often it updates.
- **Human Readiness Level (HRL).** A one-to-nine scale for whether a technology is ready for people to use safely, built to sit next to the Technology Readiness Level. DoD formally adopted a human readiness standard in August 2025.

#### How a requirement is built

- **Requirement.** A "shall" statement, plus a minimum acceptable value (the threshold), a goal value (the objective), the conditions it applies under, and how it will be checked.
- **Verification method.** The four ways to prove a requirement is met: inspection (look at it), analysis (calculate it), demonstration (show it working), or test (measure it under controlled conditions).
- **Success-run sample size.** With zero failures allowed, the trials needed are the natural log of one minus the confidence, divided by the natural log of the reliability. Ninety-five percent reliability at ninety-five percent confidence takes 59 trials; ninety-nine percent takes 299.
- **Traceability.** Each requirement links back to the analysis that produced it and forward to the test that proves it. Tools like Jama hold those links.

#### How I analyze the work

- **Task analysis.** Breaking a job into its steps, decisions, and information needs. Almost everything else starts here.
- **Function allocation.** Deciding who does each step, the human or the automation, and who has the authority to change that. Fitts lists, the old "humans are better at, machines are better at" tables, are only a starting point.
- **Usability FMEA.** A failure modes and effects analysis for use errors: list every way a person could get a step wrong, rate how bad each would be, and fix the worst first. The posting calls this kind of work human error analysis, or HEA.
- **Anthropometry.** Body measurement. The usual rule sets reach for a small person, the fifth-percentile female, and clearance for a large one, the ninety-fifth-percentile male. ANSUR II is the Army's body-measurement survey.
- **Formative versus summative testing.** Formative testing is small and repeated, and it finds problems to fix. Summative testing is larger and final, and it measures how well the design performs. Only summative results support an error rate or a safety claim.
- **Heuristic evaluation and cognitive walkthrough.** Expert reviews without users. A heuristic evaluation checks the design against a list of rules, and a walkthrough steps through a task the way a new user would.
- **IMPRINT.** Army software that simulates an operator's tasks step by step to predict workload and crew size before hardware exists.

#### How I measure the operator

- **Workload.** How much of a person's mental capacity a task uses. The NASA Task Load Index, or NASA-TLX, is a six-question rating given after a task. The Bedford scale asks how much spare capacity was left.
- **Situation awareness (SA).** Knowing what's going on, what it means, and what will happen next, which are Endsley's three levels. SAGAT pauses a simulation and quizzes the operator. SPAM asks questions while the task keeps running and times the answers.
- **Fatigue measures.** The psychomotor vigilance task is a simple reaction-time test that catches lapses. The Karolinska Sleepiness Scale and the Samn-Perelli checklist are quick self-ratings.
- **Body-based measures.** Functional near-infrared spectroscopy, or fNIRS, measures brain activity with light through the scalp. Eye tracking shows where people look, and heart-rate variability tracks sustained stress. They show that load changed, not why.
- **Psychophysics.** Measuring the point at which people start to notice something, like a delay. That's how I set the latency thresholds.
- **Within-subject designs and mixed-effects models.** In a within-subject design, each person tries every condition, which matters when operators are scarce. Mixed-effects models account for the fact that one person's many answers aren't independent.

#### How autonomy goes wrong, and how it's designed

- **Stages and levels of automation.** Parasuraman, Sheridan, and Wickens split automation into four stages: gathering information, making sense of it, choosing an action, and carrying it out. Each stage can be automated to a different degree.
- **Adaptive versus adaptable automation.** Adaptable means the operator changes the automation level. Adaptive means the system changes it on its own, so it has to announce the change.
- **Mode error and automation surprise.** The operator believes the system is in one mode when it's in another, or the system does something the operator didn't expect.
- **Agent transparency.** Chen and colleagues' model, from the Army Research Laboratory: show what the system is doing, why, and what it will do next, with how sure it is.
- **Trust calibration.** People should rely on automation exactly as much as it deserves. Over-trust means accepting bad output, and disuse means ignoring good output.
- **Span of control and fan-out.** How many assets one operator can supervise. Neglect time is how long an asset can run unattended, and interaction time is how long the operator needs to get it back on track. Fan-out is neglect time plus interaction time, divided by interaction time.
- **Signal detection.** Every alert outcome is a hit, a miss, a false alarm, or a correct rejection. Too many false alarms teach operators to ignore the alarm.
- **Multiple resources.** Wickens's idea that seeing and hearing, and words and spatial information, draw on partly separate mental capacity. That's why a critical cue goes on the channel the operator isn't already using.
- **Lost link.** The control connection to an uncrewed asset drops. The operator should know in advance what each asset will do when that happens.

## Qualifications map — Tier 1

- **Exact or strong.** MS and PhD in Human Factors Psychology (Old Dominion, 2017 and 2020). Six-plus years of industry HF, though my titles say researcher. Task analysis at NASA, Echo Hub, and EchoStar. Field research: Uber Brazil ride-alongs and Echo Hub home visits. A/B tests, think-aloud, and card sorts. Test plans and reports: the NASA evaluation plan and uFMEA report, and the Amazon latency protocol and specification. Workload measurement: fNIRS and eye tracking at Amazon, NASA-TLX as a manipulation check in the latency study, decomposed takeover latency at Mercedes, ECG at Brigham. Anthropometrics: fifth and ninety-fifth percentile at NASA, reach envelopes at EchoStar. Requirements and specs: latency for software, reach for hardware. Surveys and structured interviews. Clearance eligibility.
- **Partial.** MIL-STD-1472: one evaluation, in 2018, against 1472G. Uncrewed and autonomous systems, through automation handovers and the agentic AI framework. JIRA and Confluence daily, but not Jama yet. MIL-STD-1474, through audiology research and sound-based alerts. DoD HSI domains: knowledge, not practice. SAGAT and SPAM: I know them, but I haven't run them on a program.
- **Gaps.** MIL-STD-46855 and 882 under contract, though I've done the analyses through a usability FMEA. Defense hardware or software. An active TS clearance.

# Part 1 · Jake: the HF role and how my experience maps

> **The room.** Jake watched Monday's pitch, which led with rapid qualitative work, and he read the CSCW paper. He's testing whether I hold the engineering half: requirements, verification, and HSI documentation. He's the expert on HSI, so I use his terms without defining them.

## Tell me about yourself — Tier 1

> **Question:** "Tell me about yourself." Or: *"Walk me through how your background maps to this role."*

### Answer

**The claim.** I'm a human factors engineer. I turn human-performance data into requirements a program can build against and tests that verify them, mostly where hardware, software, and automation meet.

**The proof.** Since June 2025, I've built the human factors function at EchoStar, including the reach envelopes and fit criteria the hardware team designs against. At Amazon, I set latency thresholds with psychophysics that engineering adopted as targets, and measured workload with fNIRS and eye tracking. Before that, a usability FMEA and 1472 accommodation work at NASA, and takeover-alert studies at Mercedes.

**The boundary.** What I want next is autonomy that people supervise, where the human side of the requirement decides whether the system works.

### Say this

- *"I turn human-performance data into requirements, and into the tests that verify them."*

---

## Researcher or engineer? — Tier 1

> **Question:** "Are you a researcher or a human factors engineer?" Or: *"Your last title says researcher."*

### Answer

**The claim.** The engineering half is the job: requirements, verification, and HSI documentation. Research is how I find out what a requirement needs to say.

**The proof.** My titles say researcher, but the outputs were engineering outputs, produced inside the hardware and software teams the way an IPT works. At Amazon, latency thresholds with pass criteria that engineering adopted as targets. At EchoStar, reach envelopes and fit criteria the hardware team designs against, from the concept review on.

**The boundary.** I haven't authored HSI documentation under a DoD contract. That's the ramp-up.

### Follow-ups

**Follow-up: "Your other resume says Staff Human Factors Engineer."**

> That version used functional titles. My titles of record are Staff Product Researcher and UX Researcher II, and the work behind them is the same.

### Say this

- *"Research is how I find the number. Engineering is how I turn it into a requirement someone can verify."*

---

## Why this role — Tier 1

> **Question:** "Why this role?" Or: *"Why human factors engineering at Anduril?"*

### Answer

**The claim.** In autonomy that people supervise, human limits decide whether the system works: workload, fatigue, attention, and trust.

**The proof.** The posting describes the work I want: task analysis, function allocation, workload and SA testing, HF requirements in specifications and ICDs, and HSI documentation, across programs and business lines.

**The boundary.** Which programs would this seat support first?

---

## Why leave a Staff role for Senior — Tier 1

> **Question:** "Why leave a Staff role for a Senior one?" Or: *"Why should we believe you'll stay?"*

### Answer

**The claim.** Nothing is pushing me out. The function I built at EchoStar is running, but it doesn't have the stakes I want to work on.

**The proof.** What I want is the work itself: requirements and verification on autonomy that people supervise.

**The boundary.** Orange County is where my partner is from, so this is a long-term move. I'd be in Costa Mesa and travel to test events.

### Follow-ups

**Follow-up: "Two moves in two years. Why will this one stick?"**

> J.S. Held taught me that I want to own a product line rather than rotate across clients. EchoStar was the right move for that, and the function there is running now. This is the work I want to keep doing, where my family is settling.

---

## Mission conviction — Tier 1

> **Question:** "Are you comfortable working on weapons and autonomy?" Or: *"Where should the human sit in the loop?"*

### Answer

**The claim.** Yes. These systems protect warfighters, and I want to help build them.

**The proof.** DoD policy frames it as appropriate levels of human judgment over the use of force, and that isn't one dial. Sensing, deciding, and acting can each sit at a different level of automation, and the right level can change across a mission.

**The boundary.** I'd want operator data to set where the human sits at each stage, rather than assume it.

### Follow-ups

**Follow-up: "What's that based on?"**

> DoD Directive 3000.09, updated in January 2023, and Parasuraman, Sheridan, and Wickens's four stages of automation.

---

## Biggest gap for this role — Tier 2

> **Question:** "What's your biggest gap for this role?"

### Answer

**The claim.** DoD HSI documentation. I haven't authored an HSI Program Plan, and I haven't worked under contract on an 882 or 46855A program.

**The proof.** I've done the analyses those documents formalize. Today at EchoStar, body-safety and fit criteria the hardware team designs against; earlier, use errors ranked by severity in a usability FMEA and fixed in the standard order, design it out first. What's new is the process around the work, not the work.

**The boundary.** I'd read the source standards and the program's own plans, and pair with whoever has written one through a review cycle.

### Say this

- *"I haven't written one under contract. Here's how I'd learn it, and who I'd learn it from."*

---

## "Why hire you as an engineer?" — Tier 2

> **Question:** "You came from a UX research pipeline. Why should we hire you as an engineer?"

### Answer

**The claim.** The pipeline was the door, but the work is human factors engineering.

**The proof.** At NASA, the use-error hazard analysis and accommodation against 1472. At EchoStar, the reach and mechanical fit criteria. At Amazon, latency requirements with pass-fail criteria.

**The boundary.** Judge me on whether a test engineer could verify what I write.

---

## Biggest weakness — Tier 2

> **Question:** "What's your biggest weakness?" Or: *"How do you like to be managed?"*

### Answer

**The claim.** I state a point of view as a conclusion before I've asked enough.

**The proof.** I got that feedback recently, and it was fair. When I know a domain well, I move to the answer before I've heard how the team sees the problem.

**The boundary.** Now I open with one scoping question, label my view as a hypothesis, and ask what I'm missing before I propose anything. On management: I work best with a clear outcome, room on the method, and early feedback when something isn't landing.

---

## HSI program fluency — Tier 1

> **Question:** "What's your experience with MIL-STD-882 and 46855? How would you build an HSI Program Plan?"

### Answer

**The claim.** I've done the analyses these standards formalize, but not under contract.

**The proof.** I'd build the plan from the HSI Program Plan data item: domain owners, requirements traced to tests, the analyses, and HF objectives on existing test events. In a classic program, task analysis lands at SRR, workload and accommodation by PDR, 1472 compliance by CDR, and test plans before TRR. For faster programs, SAE6906A is built for tailoring. Which gates does this program run?

**The boundary.** By month three, I'd deliver plan inputs and a traceability map, reviewed by someone who's written one.

### Follow-ups

**Follow-up: "Walk me through 882."**

> Severity has four categories: catastrophic, critical, marginal, and negligible. Probability has six levels, from frequent down to eliminated. Together they give a risk level of high, serious, medium, or low, and the higher the risk, the more senior the person who formally accepts it. Each hazard is tracked to closure in a hazard log. Mitigation follows the design order of precedence: eliminate through design, reduce through design changes, engineered features, warning devices, and only then signs, procedures, training, and protective equipment. My usability FMEA ran the same logic on use errors.

**Follow-up: "Which human engineering standard do you work from?"**

> Two, because they do different jobs. 1472H for design criteria, and 46855A for the human engineering program across analysis, design, and test. The 1999 handbook was folded into the standard in 2011.

**Follow-up: "Walk me through 46855A."**

> It sets the human engineering work a contractor does in analysis, design and development, and test and evaluation, delivered through data items like the human engineering program plan and test plan. The HSI Program Plan sits above it across all seven domains, but it doesn't replace those plans unless the government directs it.

---

## Writing verifiable HF requirements — Tier 1

> **Question:** "Write me an HF requirement for an autonomy status display that a test engineer can verify." Or: *"How do you get HF into specs and ICDs?"*

### Answer

**The claim.** A requirement is a shall statement with threshold and objective values, its conditions, and a verification method.

**The proof.** "The control station shall display the active autonomy mode for each asset under control. Threshold: trained operators identify the mode within two seconds on ninety-five percent of probes in a representative multi-asset scenario. Objective: one second, ninety-nine percent. Verification: test, in a human-in-the-loop evaluation." The numbers are illustrative.

**The boundary.** The threshold sets the test cost. Showing ninety-five percent at ninety-five percent confidence with zero failures takes fifty-nine trials, and ninety-nine percent takes two hundred ninety-nine. I've shipped pass criteria at Amazon, not in a defense ICD, and I've used JIRA and Confluence daily, not Jama yet.

### Follow-ups

**Follow-up: "Where does fifty-nine come from?"**

> The success-run formula. With zero failures allowed, n is the natural log of one minus the confidence, divided by the natural log of the reliability. For ninety-five and ninety-five, that's 58.4, so fifty-nine.

### Say this

- *"If a test engineer can't verify it, it isn't a requirement yet."*

---

## NASA: HSI, hazard analysis, and accommodation — Tier 1

> **Question:** "Walk me through the NASA work." Or: *"Tell me about your MIL-STD-1472 experience."*

### Answer

**The claim.** A formative HSI evaluation of a Lunar Gateway medical workstation, which I led as a PhD intern.

**The proof.** I built the task list with subject-matter experts, then ran a usability FMEA as the human error analysis across three to four medical scenarios, with reach and clearance from the fifth-percentile female to the ninety-fifth-percentile male. Five astronaut candidates worked the scenarios in VR microgravity. The worst errors came from adjacent controls with different consequences; we separated them over three to four rounds, and the final round had no critical input errors.

**The boundary.** Formative, not validation, and the thirty percent faster task time was a side effect. It was 2018, so it was 1472G, not H, and the layout was joint work with the industrial designers.

### Follow-ups

**Follow-up: "That was 2018. What have you done since?"**

> At Amazon, a latency specification engineering adopted as targets, and workload measurement with fNIRS and eye tracking. Since June 2025 at EchoStar, I've built the human factors function: reach envelopes, body-safety, and fit criteria the hardware team designs against, and an experience index reviewed at the VP level.

---

## Setting a requirement from human data (latency) — Tier 1

> **Question:** "How do you set a requirement when nobody knows the right number?" Or: *"Tell me about your most impactful project."*

### Answer

**The claim.** Thresholds should come from people, measured under control, and ship with their verification method and their limits.

**The proof.** A Wizard-of-Oz rig with millisecond control and the method of constant stimuli: thirty participants, twelve interaction types, six fixed delays, about two thousand trials. Two tiers per interaction type, read off the distribution of individual ratings, not the mean. Engineering adopted them as targets, and an economics team's model projected about fifty million dollars.

**The boundary.** I held workload constant. For operators supervising assets, workload and fatigue become manipulated factors.

### Follow-ups

**Follow-up: "What were the tiers?"**

> High tier: more than seventy percent rate the delay not slow, and fewer than five percent too slow. Acceptable: more than half not slow, under fifteen percent too slow. Verification is pass-fail against the band.

**Follow-up: "Why constant stimuli, not a staircase?"**

> A staircase homes in on one point. I needed two cut-offs plus the slope between them, and engineers have to trust the method before they'll trust the number.

**Follow-up: "How was workload held constant?"**

> People made the judgments during a light visual monitoring task at a fixed difficulty, set from a practice block. I ran the NASA-TLX after each block as a manipulation check only, not as a result.

**Follow-up: "A voice assistant isn't an aircraft."**

> Agreed, and the numbers don't carry over. The method does: when a person depends on an automated response, the timing limit should come from people measured under control.

---

## Quantitative rigor — Tier 1

> **Question:** "Where does quant fit in your work?" Or: *"How do you analyze human-performance data?"*

### Answer

**The claim.** The claim sets the method. Controlled measurement when the decision needs a number; observation and usability testing when it needs to know what's actually happening.

**The proof.** Psychophysics for thresholds, and mixed-effects models, because every operator contributes repeated measures. I analyze in Python end to end. At EchoStar, I built a longitudinal experience index that pairs behavioral telemetry with attitudinal metrics, reviewed at the VP level.

**The boundary.** Small operator populations mean within-subject designs and effect sizes with intervals. An error rate needs a summative sample; a design direction doesn't.

### Say this

- *"I pick the method by the claim the decision needs."*

---

## Methods toolkit — Tier 2

> **Question:** "Which research methods do you use?" Or: *"Have you run A/B tests, think-alouds, or card sorts?"*

### Answer

**The claim.** I pick the method by what the decision needs.

**The proof.** Contextual inquiry and ride-alongs, at Uber in Brazil and in Echo Hub homes. Think-aloud in every test-fix-retest round. A/B tests on Sling flows, read from telemetry. A card sort to organize Echo Hub's controls and settings.

**The boundary.** Surveys and structured interviews when I need comparable answers at scale, with the analysis planned before the first response.

---

## Formative testing with small samples — Tier 2

> **Question:** "How many participants do you need?" Or: *"Isn't five people too few?"*

### Answer

**The claim.** Formative testing works best small and repeated: about five people a round, about three rounds, with the design changing between them.

**The proof.** The goal is to find and rank use errors, not estimate their rate, and each round tests a design that already fixed the last round's problems.

**The boundary.** A formative finding justifies a design decision, not a safety claim. A rate needs a summative study, sized by the success-run math.

---

## Heuristic analysis and cognitive walkthroughs — Tier 2

> **Question:** "How would you evaluate a prototype hardware and software interface?"

### Answer

**The claim.** Two expert passes before any operator sees it.

**The proof.** A heuristic analysis against 1472H plus task rules, like mode visibility, alert discriminability, gloved input, and night legibility, by two reviewers separately. Then a cognitive walkthrough of each critical task. Findings get rated on the hazard-analysis severity scale, and the top items become requirements.

**The boundary.** Expert reviews find violations, not performance. The serious findings get confirmed in a human-in-the-loop test.

---

## Maintainers and physical accommodation — Tier 2

> **Question:** "How do you address maintainers, not just operators?"

### Answer

**The claim.** Maintainers get their own hazard and accommodation analysis: pinch points, hot surfaces, stored energy, lifts, access, and tool clearance.

**The proof.** Encumbered dimensions from ANSUR II, with gloves and protective equipment as design inputs, and design to the range, not an average person. I wrote reach, body-safety, and fit criteria at EchoStar and set reach and clearance at NASA.

**The boundary.** I haven't studied defense maintainers in the field.

---

## Training aids and manuals — Tier 2

> **Question:** "How do you support training aids and manual development?"

### Answer

**The claim.** The task analysis defines the knowledge, skills, and abilities each role needs, and those shape the training aids and the manual.

**The proof.** Before I write a training requirement, I ask whether a design change could remove it. Training is the last fix in the order of precedence.

**The boundary.** I deliver training needs traced to tasks, plus the design changes that would cut the training burden.

---

## Building the research foundation, curiosity-first — Tier 1

> **Question:** "Our team already has research happening. How would you add rigor without slowing it down?" *Use this only if they raise existing research themselves.*

### Answer

**Ask first.** Which decisions has the current research changed, and what's measured today?

**The claim.** Research that's already running is an asset. I'd add a measurement layer under it, not a second program next to it.

**The proof.** Whoever runs it keeps the fast loops. I'd add baselines, task analysis, and requirements with verification, on one shared plan.

**The boundary.** The plan is co-owned with the people already doing the work.

---

## The CSCW paper, for Jake — Tier 1

> **Question:** "Tell me how your agentic trust paper applies here." *Jake only. He read it, so point back rather than re-pitch.*

### Answer

**The claim.** The four phases map straight to defense: Alignment previews intent, Execution shows status, Control means redirect or abort, and Calibration checks reliance against reliability.

**The proof.** My proposal is that the autonomy level for each action is set by the severity of a mistake crossed with the system's confidence, the logic of an 882 risk matrix.

**The boundary.** That's my extension, not something 882 contains, and it's a framework, not a deployed defense result. I'd want to test it here.

---

## The thirty-sixty-ninety — Tier 1

> **Question:** "What would your first ninety days look like?"

### Answer

**Ask first.** "What does the team most need from this seat in the first ninety days?" Then adjust the plan to the answer.

**The claim.** By day thirty, I'd learn the HSI practice, the program's key decisions, and where human factors enters the requirements today.

**The proof.** By day sixty, a workload, situation awareness, and fatigue baseline at the nearest simulation session or test event, and a first set of requirements with verification.

**The boundary.** By day ninety, HSI plan inputs and a measurement plan tied to milestones. I'd expect week two to correct this.

---

## Working across sites — Tier 2

> **Question:** "How would you work with a team spread across Costa Mesa and London?" *Use this only after they bring up London.*

### Answer

**The claim.** Distributed teams work when the artifact is shared, not the meeting.

**The proof.** A fixed overlap window, Pacific morning and London afternoon, one shared task model and requirement set, and decisions written down so nobody waits eight hours to learn what changed.

**The boundary.** It depends on writing things down more than on any meeting.

---

## Supporting several programs at once — Tier 2

> **Question:** "How would you prioritize HF work across several programs?"

### Answer

**The claim.** Risk first, then milestone. A hazard near a design freeze outranks a usability improvement a year from test.

**The proof.** I'd scale through shared standards: one requirement template, one test-plan template, and one heuristic checklist.

**The boundary.** The templates are what let the practice scale past me.

# Part 2 · The TPM: deliverables, milestones, and cost

> **The room.** The TPM runs schedule. Public program-manager postings for this division describe frequent test events, from full-software simulation at HQ to hardware-in-the-loop demonstrations. **Ask once, early:** "Which milestones does the program run, and what operator access do test events get?" Then attach each deliverable to their milestones, not to a classic SRR-to-TRR sequence. Cost goes in relative tiers: analyst time only, rides on an existing event, or needs its own run. No invented operator-hour numbers.

## MPT: the right person to operate this — Tier 1

> **Question:** "How would you determine the right person to operate this system?" Or: *"Selection, KSAs, training?"*

### Answer

**The claim.** The right person is an output of the task analysis, not an assumption.

**Deliverable and milestone.** Personnel cards for each role, listing knowledge, skills, and abilities, selection criteria, and training burden, plus an operator-to-asset ratio, as HSI inputs before the crew size gets locked. Before hardware exists, task-network modeling like the Army's IMPRINT sizes the crew and finds the workload peaks.

**Cost and boundary.** The model is analyst time only, and validating it rides on an existing simulation event. I haven't run IMPRINT on a program, so I'd pair with someone who has, and if testing finds a peak the model missed, we fix the model.

### Say this

- *"The right person is an output of the task analysis."*

---

## Span of control and multi-asset supervision — Tier 1

> **Question:** "How many assets can one operator supervise, and how would you find out?"

### Answer

**The claim.** The operator-to-asset ratio is a capacity you measure, not one you choose.

**Deliverable and milestone.** A span-of-control requirement with its conditions, before the crew size gets locked, because it sizes the crew. It comes from a simulation that ramps the number of assets with seeded events, tracking time to detect, error catch rate, and workload.

**Cost and boundary.** It rides on an existing full-software simulation event. The classic fan-out formula overestimates, because capacity depends on how well operators judge which assets can be left alone, so it's a trust-calibration problem. My hypothesis is that when one operator caps out, shared supervision beats a higher ratio, but I'd check that against how your operators actually work.

### Follow-ups

**Follow-up: "Neglect time versus interaction time?"**

> Neglect time is how long an asset runs unattended before performance drops, and interaction time is how long the operator needs to recover it. Fan-out is their sum divided by interaction time, from Olsen and Wood in 2004. "Fan-Out Revisited," at ICRA in 2025, showed the classic models overestimate.

### Say this

- *"Span of control is the point where operators stop checking."*

---

## Function allocation — Tier 1

> **Question:** "Walk me through function allocation for a multi-asset mission."

### Answer

**The claim.** Allocation is by stage of automation and authority, with defined triggers for every handoff.

**Deliverable and milestone.** An allocation table for each mission phase: who senses, decides, and acts, the authority state, and the transition rules. Each transition becomes a requirement before the design freezes. If the system changes the level itself, it has to annunciate the change. My working hypothesis is that modes should look the same across Anduril and third-party assets in Lattice, which I'd test, not assume.

**Cost and boundary.** Analyst time, plus a handoff check that rides on an existing simulation event. My evidence is Mercedes takeovers and the mode-error work behind my patent; neither was military.

### Say this

- *"Every change of authority is a discrete, visible state."*

---

## Third-party platforms in Lattice — Tier 2

> **Question:** "How do you keep the operator experience consistent across Anduril and third-party platforms?"

### Answer

**The claim.** My starting hypothesis: the assets can differ, but the control logic, mode logic, and alert grammar shouldn't.

**Deliverable and milestone.** A cross-platform interface standard, with each asset's lost-link behavior visible in advance, applied whenever a platform joins Lattice.

**Cost and boundary.** Verified with SA probes that ride on mixed-fleet simulation events: can operators predict each asset as well as a single platform?

---

## Human-autonomy transparency — Tier 1

> **Question:** "What does the operator need to see about what the autonomy is doing, and why?"

### Answer

**The claim.** What the autonomy is doing, why, what it will do next, and how sure it is.

**Deliverable and milestone.** Requirements for mode annunciation, intent display, and confidence shown separately from data freshness, written before the display design freezes and verified at a test event with SA probes and response time to automation surprises.

**Cost and boundary.** The probes ride on an existing test event. The evidence says more transparency improves trust calibration without much added workload, but not always SA, so I'd test display density under realistic load rather than assume it.

### Follow-ups

**Follow-up: "What's that based on?"**

> Chen and colleagues' situation-awareness-based agent transparency model, from the Army Research Laboratory, and Selkowitz and colleagues in 2015.

### Say this

- *"No mode change the operator didn't see."*

---

## Workload and situation awareness — Tier 1

> **Question:** "How do you measure workload and situation awareness?"

### Answer

**The claim.** I manipulate load deliberately, and I pair subjective, performance, and physiological measures.

**Deliverable and milestone.** A baseline for each mission phase, with limits requirements can cite, from the first simulation event. At Amazon, I used fNIRS and eye tracking, with NASA-TLX as a manipulation check. At Mercedes, I measured SA behaviorally, through decomposed takeover latency. Here I'd add Bedford, SAGAT where the sim can pause, and SPAM where it can't.

**Cost and boundary.** It rides on sessions that are already running. I haven't run SAGAT or SPAM on a program, so I'd pilot the probe set first. Physiology tells you load changed, not why.

---

## Fatigue across a long mission — Tier 1

> **Question:** "How would you measure fatigue across a long mission and turn it into a requirement?"

### Answer

**The claim.** Fatigue builds with time on task and time of day, so I measure across the full mission length.

**Deliverable and milestone.** Rules for late-mission alerting, task scheduling, and handoff limits, from one full-length simulation run before hardware testing, with the psychomotor vigilance task and quick sleepiness ratings at fixed intervals.

**Cost and boundary.** This one needs its own run, because each run lasts the whole mission, so I'd do it once, with few operators, within-subject. Lab fatigue isn't operational fatigue, so I'd confirm at test events.

---

## Automation trust with skeptical operators — Tier 1

> **Question:** "Operators are skeptical of autonomy. How do you design for, and measure, appropriate trust?"

### Answer

**The claim.** The goal is appropriate reliance. Over-trust and disuse are both failures.

**Deliverable and milestone.** A reliance log at every test event, with acceptance and override rates against the system's actual reliability, rechecked after each model update. Over-trust shows up as acceptance staying flat across confidence; disuse shows up as overrides of correct recommendations.

**Cost and boundary.** It's logged data, so it's analyst time only. My evidence is Mercedes takeover alerts with drivers, not warfighters.

### Follow-ups

**Follow-up: "What's that based on?"**

> Lee and See on trust as calibration, and Parasuraman and Manzey on complacency under multitasking, which is exactly what supervising several assets is.

### Say this

- *"Trust is earned by predictability, and it's measured against reliability."*

---

## Degraded conditions and lost link — Tier 1

> **Question:** "The link degrades or drops mid-mission. How does the operator know, and how do they recover?"

### Answer

**The claim.** The operator has to know when the system is degraded, not just when it's wrong.

**Deliverable and milestone.** Requirements for degraded-mode indication and defined lost-link behavior for each asset, plus training scenarios built from field reports, verified at a hardware-in-the-loop event. Two rules: show confidence separately from data freshness, and acknowledgment separately from completion.

**Cost and boundary.** The scenarios ride on an existing event; the cost is authoring them. I haven't tested in military field conditions, so I'd start from the field team's failure list.

### Say this

- *"Separate confidence from freshness, and acknowledgment from completion."*

---

## Human-in-the-loop evaluation and test planning — Tier 1

> **Question:** "How would you test human-machine teaming at a test event with limited operator access?"

### Answer

**The claim.** Human factors objectives ride on test events the program already runs.

**Deliverable and milestone.** A test plan before the event that ties each objective to a requirement, separates measures of performance from measures of effectiveness, and states pass criteria, then a report that traces each result back. I wrote the NASA evaluation plan and uFMEA report, and the Amazon latency protocol and specification.

**Cost and boundary.** It rides on existing events. With few operators, I use within-subject designs and many trials per person, and the success-run math tells you up front how many trials a claim costs. Formative rounds find problems; verification needs a summative sample.

### Follow-ups

**Follow-up: "How would you plan HF verification on a program that ships in months?"**

> I'd tailor rather than skip. SAE6906A numbers its requirements so a program can pick which apply. I'd keep full testing for safety-relevant requirements and let the rest ride on existing events.

### Say this

- *"Human factors rides along on the test events you already run."*

---

## Marrying HF with real-world scenarios — Tier 1

> **Question:** "How would you marry your HF experience with real-world operational scenarios?" Or: *"How would you use wargaming outputs?"*

### Answer

**The claim.** Scenarios come from operations, and one set runs through analysis, models, simulation, and test, so the results compare.

**Deliverable and milestone.** A scenario library the HSI plan references, built before the requirements are set, from operator and SME input and field reports, tagged by task, role, and workload driver.

**Cost and boundary.** Analyst and SME time only. My NASA and Mercedes scenarios had defined hazards but weren't military.

---

## Human Readiness Levels — Tier 2

> **Question:** "How would you assess whether an autonomy capability is ready for operators?"

### Answer

**The claim.** I'd rate it on a Human Readiness Level next to its TRL. The TRL says the hardware works; the HRL says people can use it safely.

**The proof.** ANSI/HFES 400-2021 defines the nine levels. The FY2025 NDAA required DoD to review the standard and report HRLs for major programs, and DoD formally adopted a human readiness standard in August 2025.

**The boundary.** I'd report the HRL with its evidence at each program milestone.

---

## Safety versus schedule — Tier 2

> **Question:** "How do you integrate HF into a program moving at Anduril speed without becoming a schedule risk?" Or: *"How do you work in a 'whatever it takes' culture without HF getting cut?"*

### Answer

**The claim.** Early human factors lowers schedule risk, because a requirement in the specification is cheaper than a finding at test.

**The proof.** At EchoStar, I brought the reach envelope into the concept review instead of the design review, and a control moved before any production tooling was built. The testing rides on existing events, and one requirement template covers every program.

**The boundary.** I don't own risk acceptance; the program's risk acceptance authority does. If I see a catastrophic hazard with no independent detection path, I escalate it to that authority with the evidence and a recommended fix, and I make sure it's in the hazard log.

---

## Cutting scope to hit a date — Tier 1

> **Question:** "What do you cut when the schedule won't move?" Or: *"Tell me about a time you had to deliver on a fixed date."* TPM.

### Answer

**The claim.** I cut scope, never controls, and I say what got cut in the first line. A smaller result with the confounds handled is useful; a bigger one with them loose is wrong.

**The proof.** At EchoStar, the hardware date doesn't wait for a full fit study. So I deliver a bounding reach envelope from modeling and mock-ups while industrial design is still exploring form, and the physical check lands before tooling. When I cut, it's conditions first, then participants, then how far the result generalizes.

**The boundary.** The one thing I don't cut is the success criterion, written down before the work starts.

> ⚠️ **Tell the EchoStar version only if it happened that way.** If not, give the rule and the cut order, and say plainly that's how I'd cut.

### Say this

- *"Cut scope, never controls, and say what got cut in the first line."*

---

## What I'd measure first — Tier 2

> **Question:** "What would you measure first on a program like this, and why?"

### Answer

**The claim.** Operator workload and SA across each mission phase on the current build, plus time on task.

**The proof.** Crew size, span of control, fatigue rules, and alert design all depend on that baseline, and it rides on the next simulation event.

**The boundary.** It's a baseline, not a verdict; the requirements come after.

---

## Getting HF requirements into a spec — Tier 2

> **Question:** "Tell me about a time you got HF requirements into an engineering spec or ICD."

### Answer

**The claim.** At Amazon, the latency targets were engineering guesses, and I replaced them with a two-tier specification with pass-fail criteria.

**The proof.** Engineering adopted it as their targets. At EchoStar, my reach and usability criteria are what the hardware team designs against.

**The boundary.** That was a specification, not a defense ICD. In an ICD, I'd attach the requirement to any data that ends up in front of an operator.

# Part 3 · The team meeting, the backup deck, and stories

> **The room.** One team meeting may replace both interviews, and Daniella may be there.

## Single team meeting — Tier 1

> **The shape:** Forty-five to sixty minutes, several people, and mixed agendas.

### Answer

**The open, thirty seconds.** "I turn human-performance data into requirements engineers can build to and test against, and I run quick design testing along the way. Where does human factors enter the program today?"

**Then I listen.** Jake frames the role and the TPM frames the program. Standards and requirements for Jake; deliverables, milestones, and cost for the TPM.

**The close.** One question per person from the cue card, one sharp reflection after each answer, and then stop.

---

## Presentation backup, ten minutes — Tier 1

> **The shape:** An HF engineering cut of the existing deck, only if I'm asked to present: latency four minutes, NASA three, the transfer three. No new slides.

### Answer

**Latency.** Thresholds by the method of constant stimuli, from thirty people and about two thousand trials, shipped as a two-tier requirement with pass-fail criteria.

**NASA.** A usability FMEA as the human error analysis across three to four scenarios, with reach and clearance against 1472G. We separated adjacent controls over three to four rounds, and the final round had no critical input errors.

**The transfer.** I held workload constant. For operators supervising assets, workload and fatigue become the manipulated factors.

---

## When you got it wrong (Echo Show benchmark) — Tier 1

> **Question:** "Tell me about a failure."

### Answer

**Situation.** My first project at Amazon was a benchmark of Echo Show against competitors that nobody had commissioned. I recruited the participants myself and spent two weeks on it.

**Result.** At the readout, the director of design asked who had asked for it, and I had no answer. The roadmap was already set, and the work changed nothing.

**Mechanism.** Now stakeholders commit in writing to what each possible result will change before a study runs. If every branch leads to the same decision, the study doesn't run.

---

## Disagreeing with engineering (latency targets) — Tier 1

> **Question:** "Tell me about a time you disagreed with engineering."

### Answer

**Situation.** At Amazon, a principal engineer pushed back in a design review on the half-second target: it was a feasibility question, and research should describe, not set limits.

**Action.** I didn't win that by arguing. I rewrote the recommendation as a pass-fail test and gave ground where he was right, which is where the looser second tier came from.

**Result.** Engineering adopted the thresholds as their targets. Once there's a test to pass, nobody is arguing from opinion.

---

## Conflict resolution — Tier 1

> **Question:** "Tell me about a conflict with a colleague."

### Answer

**Situation.** At EchoStar, a lead designer saw my usability findings on their concept for the first time in a cross-functional review.

**Action.** I asked for a one-on-one and owned my part. We named the actual decision, whether the concept moved forward and with what fixes, and I brought a possible direction for each finding.

**Result.** The concept moved forward with two fixes, and the designer presented the revision. No one should see a finding about their work for the first time in public.

---

## Disagreeing when it's infeasible — Tier 2

> **Question:** "What do you do when engineering says your requirement isn't feasible?"

### Answer

**The story.** At Amazon, a principal engineer challenged my half-second latency target as a feasibility question, and he was partly right; that's where the looser second tier came from. The same move at NASA: a vibration cue the hardware couldn't deliver went to visual and sound cues. Either way, I separate the need from the solution and document what we lost, so the gap stays on the record.

---

## When the designer was right — Tier 2

> **Question:** "When has a designer been right and your research wrong?"

### Answer

**The story.** On the workload work at Amazon, eye tracking showed a region nobody looked at. I read it as a salience problem. A designer saw it was a task-sequence problem: the region was never in the scan path at the moment it mattered. My measurement found where the failure was and said almost nothing about why.

---

## Influence through measurement (experience index) — Tier 2

> **Question:** "Tell me about influencing without authority."

### Answer

**The story.** At EchoStar, product reviews reacted to whatever had broken last. I built an experience index, pairing behavioral telemetry with attitudinal metrics, and brought it into the VP-level reviews, which shifted toward planning ahead. Leaders listen when you give them a number they actually want to track.

---

## Mentorship — Tier 2

> **Question:** "Tell me about someone you mentored."

### Answer

**The story.** At NASA, I mentored an undergraduate whose work was slipping. Coaching the work didn't help. When I asked how he was doing, he told me he was dealing with a family loss. I moved his deadlines and made our check-ins about him first, and now I ask every mentee early how they like to get feedback.

> ⚠️ **No name, and no details of the loss.**

# Part 4 · Reference — Tier 3

## Standards and data items

[[card]] **Standards and dates.** MIL-STD-1472H, design criteria, September 15, 2020; my 2018 NASA work used 1472G. MIL-STD-46855A, human engineering requirements, May 24, 2011, reaffirmed by Notice 1 in 2016; it superseded the cancelled 1999 handbook, MIL-HDBK-46855A. MIL-STD-882E, May 11, 2012, with Change 1 on September 27, 2023; 882E also rates software control of a hazard on a one-to-five software criticality index. DoD Instruction 5000.95, April 1, 2022. SAE6906A, December 13, 2023, with Appendix D for tailoring. DoD Directive 3000.09, January 25, 2023. Human readiness: ANSI/HFES 400-2021; DoD formally adopted a human readiness standard in August 2025.

[[card]] **Data items.** The HSI Program Plan template is DI-HFAC-81743A (2011). It doesn't replace the safety, training, or human engineering plans unless the government directs it. Related: the Human Engineering Program Plan, DI-HFAC-81742A, and the Human Engineering Test Plan, DI-HFAC-80743B.

## Sources, if asked

[[card]] **Who said what.** Fan-out: Olsen and Wood (2004), building on Olsen and Goodrich (2003); "Fan-Out Revisited" (ICRA 2025) found the classic formula overestimates. Transparency: Chen and colleagues, Army Research Laboratory (2014); Selkowitz and colleagues (2015). Trust: Lee and See (2004); complacency: Parasuraman and Manzey (2010). Stages of automation: Parasuraman, Sheridan, and Wickens (2000). Situation awareness: Endsley (1995). Workload: NASA-TLX, Hart and Staveland (1988).

## Maneuver Dominance, public facts

[[card]] **What the public record says.** Postings describe multi-asset autonomy, with aerial systems working in concert with ground maneuver forces, so the operator may be a soldier, not a pilot. Third-party platforms come into Lattice. Program-manager postings describe frequent test events, from full-software simulation at HQ to hardware-in-the-loop demonstrations. The HFE req itself is HSI across business lines, so I let Jake name the program first. Job postings include London roles, among them an Advanced Capabilities team that does operations analysis and wargaming.

## Also in reference

**Noise and auditory displays.** MIL-STD-1474E (2015) is the military noise standard: hearing-hazard signs above 85 decibels steady or 140 decibels peak, and Appendix C covers aural non-detectability, how quiet a system must be so it can't be heard. My hook is undergraduate audiology research, which earned the James Jerger Award in 2014, plus sound-based alerts.

**AI in my own workflow.** I use AI for first-pass qualitative coding, validated against my own coding on a held-out sample, and for drafting analysis code that I review line by line. Approved tools only, no participant or restricted data in outside models, and AI never decides whether a threshold is met.

# Part 5 · The day itself

## The loop

Two forty-five-minute video interviews are planned but not yet confirmed: Jake Wetzel, the HSI lead in Costa Mesa, on the HF role and how my experience maps to it, and a TPM on HF plus technology for human-machine teaming. Daniella may replace both with one team meeting. Maneesh Raman is involved in defining the role; if he joins, I'll ask what he wants the seat to own.

> ⚠️ **Context only. Never put it in an answer.** Daniella shared that the program is distinct from the autonomous co-pilot project, that the designers are in London, and that the research is less mature, with a designer running scrappy just-in-time research. Her feedback: show both the rigorous and the fast side, come with curiosity, and don't over-prepare a lecture.

## The last check

- Confirm with Carlie which resume sits on the HFE record, and get the internal Senior req ID. The first resume says "Staff Human Factors Engineer," "Human Factors Design Engineer," NASA "validation," and the Mercedes 24%; the title sentence is in the bridge card.
- Verify the Minaee, Mikolov, and Vinyals 2024 reference in the CSCW paper before Jake asks or I present it next month.
- Know my notice period and earliest start date cold. Hesitating on the start date reads as flight risk.
- Read 46855A and Section 4 of 882E, and privately draft a one-page HSI Program Plan outline. Only then change the gap script to past tense.
- For the Sling A/B tests, the Echo Hub card sort, and the NASA evaluation plan and uFMEA report, have one sentence each ready: the sample size, the decision it changed, and my role.
- Time each rehearse-first answer at sixty to seventy-five seconds.

## Comp scripts — recruiter only

**Posture.** Strong interest, and I'll negotiate the details. I have another process finishing soon, so timing matters to me. If comp comes up in an interview: "Comp won't be the blocker. I'll bring my asks at offer stage." I never state current comp, never accept or decline on a call, and never reopen level.

**What I know.** The base band is $146K to $194K. The comp team targets $175K to $185K, is comfortable at $190K, and can go above $194K with justification. Equity is "a hundred-something." A sign-on bonus was floated.

**Ask order.** Equity first, because it's the largest gap; then base above $194K; then the sign-on; then relocation from Denver, fully covered. The justification leads with the one data point Carlie asked for: a competing offer, if I have one in hand. Then the PhD as a preferred qualification, the patent, and hardware and autonomy experience.

**Equity diligence.** Instrument type, vesting and cliff, price basis, refresh policy, and tender history.

<h1 class="pagebreak">Cue card — safe to carry</h1>

**I measure how people actually perform with a system, and I turn that into requirements that engineers can build to and test against. Along the way, I run quick rounds of design testing. I pick the method based on what the decision needs to know.**

**The bridge, Jake only.** "Monday I led with the research half, because that was the seat. This seat is the other half." If asked about Air Defense: "They chose someone else, the feedback was fair, and this seat is closer to my training."

**Every answer.** Claim, proof, boundary, in sixty to seventy-five seconds. Two or three questions per interview at most. Citations only when asked. "Assets" and "operators." With the TPM, ask once which milestones they run.

**Standards.** 1472H is the design rulebook (2020); my NASA work used 1472G. 46855A is the process rulebook (2011), and it's current; the 1999 handbook is cancelled. SAE6906A is the industry HSI standard (December 2023).

**Human Readiness Levels.** ANSI/HFES 400-2021, nine levels next to the TRL. DoD formally adopted a human readiness standard in August 2025.

**Requirement template.** A shall statement, threshold and objective, conditions, and verification: inspection, analysis, demonstration, or test.

**Success run.** Ninety-five percent at ninety-five percent confidence, zero failures: 59 trials. Ninety-nine percent: 299.

**Fan-out.** (Neglect time + interaction time) ÷ interaction time. Real capacity is lower, because it depends on how well the operator judges which assets can be left alone.

**882.** Severity and probability go into a matrix that gives the risk level, and the risk acceptance authority signs off; each hazard is tracked to closure in a hazard log. Eliminate, reduce, engineer, warn, and only then signs, procedures, training, and protective equipment.

**Honest gap.** "I've done the analyses these standards formalize, but not under contract on an 882 or 46855A program. Here's how I'd close it."

**If I don't know.** "I don't know. My best guess is X, but that's a hypothesis. The way I'd find out is..."

#### Questions to ask

- **Jake:** "Where does HF enter the program's requirements today, and where would you want it earlier?" "What does a great first year look like for this seat?" "How does HSI split work across programs, and how is it staffed?" "What HSI documentation do you use as the baseline?" "Is the program tracking Human Readiness Levels?"
- **TPM:** "Which program decision next quarter would you most want human-performance data behind?" "Where has HF input landed too late?" "How are test events planned, and can HF objectives ride along?" "Which gates does the program run, and where would HF evidence fit?"
- **Anyone:** "Who's the operator, and how do I get time with them?" "What research is already happening, and what's missing?" "How does HSI work with the Advanced Capabilities team on wargaming?"

**To close.** "Is there anything I said today you'd want me to go deeper on?"

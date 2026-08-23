# The Finite Human and the Tireless Producer

The central problem of AI-assisted development is not how to produce good software.
What counts as good depends on the software, the stakes, the people building it, and the expertise available to them.

The more general problem is how a finite human can remain oriented while collaborating with an effectively tireless producer.

AI can generate code, explanations, plans, alternatives, questions, tests, and documentation faster than a person can absorb them.
It does not become tired, lose interest, or feel that a project has become too large.
The human does.
The human must still decide what matters, recognize when the work has drifted, and recover enough understanding to choose what should happen next.

> The machine can continue expanding the work long after the human has lost the
> ability to hold its direction.

This is not only a technical problem involving context windows.
It is an asymmetry between machine production and human comprehension.
Both participants can become poorly oriented, but they do so differently.
An agent can be trapped by an overgrown or misleading context.
A human can be saturated by the quantity of text, the branching possibilities, the unfamiliar code, and the decisions that accumulate faster than they can be consciously recognized.

## A Perspective, Not a General Method

Different software engineers work on profoundly different systems.
A method that is useful for an exploratory personal project may be inappropriate for regulated, safety-critical, security-sensitive, or mature production software.
Those systems require forms of evidence, oversight, and accountability that cannot be inferred from an informal development practice.

The perspective here is most relevant to ambitious projects in which an individual or small group is using AI to attempt work that would previously have exceeded their technical range or taken too long to pursue.
Many useful parts of society do not require every prototype or local tool to be developed as though it were safety-critical infrastructure.
A good-enough approach can make valuable systems economically possible, provided that its limits and consequences are understood.

This is therefore not a claim to have found the solution to AI-assisted development.
It is a report from an evolving practice: a collection of ways to coordinate the different strengths and weaknesses of a human and an agent without pretending that either participant fully understands the project at all times.

## A Loop Rather Than a Pipeline

A pipeline suggests that intent can be completely specified, handed to the machine, implemented, and verified in an orderly progression.
That may be possible when the problem is already understood.
It does not describe much of the work in which AI is most transformative.

Sometimes implementation is how the human discovers what the specification needs to say.
Sometimes the agent exposes a possibility the human did not know existed.
Sometimes a constraint that appeared sensible drives the work in a damaging direction.
Sometimes a plausible milestone turns out to contain an unanticipated problem and must be abandoned, re-specified, and attempted again.

The work therefore behaves more like a loop:

```text
Frame -> Explore -> Choose -> Constrain -> Build -> Observe -> Reorient
  ^                                                        |
  +--------------------------------------------------------+
```

These are not mandatory stages or boxes to tick.
Exploration may continue during implementation.
A nearly complete milestone may need stray development before it settles.
A failed attempt may generate the understanding needed to define the next one.
The value of the loop is that it creates recurring opportunities for the human to step back from production and recover direction.

## Expansion and Compression

AI naturally expands the work.
Every response can introduce additional considerations, abstractions, alternatives, compatibility concerns, tests, and nice-to-have features.
Because each addition can now be implemented quickly, the cost of saying yes appears low.

The true cost arrives later.
Every generated addition creates more code to integrate, more behavior to evaluate, more documentation to encounter, and more complexity to carry.
Construction becomes cheap before review, comprehension, and maintenance do.
The human can be tricked into spending the day reading output, answering questions, and elaborating plans while the project becomes progressively harder to complete.

Exploration requires expansion.
Orientation requires compression.
The human must periodically interrupt the expanding process, step outside it, and allow the project to settle into a form that can once again be considered as a whole.
Only then can the next meaningful direction be chosen.

This compression is imperfect.
A human cannot ingest and faithfully summarize everything the project has contained.
Nor can an AI be assumed to preserve exactly the decisions that mattered.
The practical hope is more modest: careful input at milestone boundaries, coupled with deliberate curation when the project appears aligned, can leave behind enough structure for coherent development to continue.

The challenge is not to preserve all history.
Agents can have a fanatical predisposition toward retaining history, maintaining premature backward compatibility, or constructing elaborate tests that provide little evidence of quality.
At the prototyping stage, these behaviors can protect artifacts whose value has not yet been established and impose an architecture built around the past rather than the objective.

The durable record should preserve what helps the project recover direction: the current intent, consequential decisions, important constraints, observable state, evidence, and unresolved uncertainty.
Everything else must be allowed to become less prominent, even though there is no perfect mechanism for deciding what can safely be forgotten.

## Milestones as an Interaction Pattern

Milestones are the most effective pattern I have found for creating these moments of synthesis.
They are not a project-management doctrine, a rigid spec kit, or a claim that every requirement can be written before development begins.

A useful milestone is large enough to justify the overhead of specifying, running, observing, and capturing it.
It is also bounded enough that the human has a reasonable chance of noticing the important decisions before they become deeply embedded in the system.
Finding that size is an art learned through experience rather than a formula.

The human can use AI to explore what the next milestone might contain.
They must then develop an intuition for which questions require human judgment and which can be left to the agent without important negative consequences.
This does not mean answering every question the agent asks.
Agents often ask questions that are irrelevant to the user's needs, produce passages that are difficult to interpret, or elaborate choices that do not deserve attention.

Fluency in this mode of work does not require fully understanding every passage.
It includes learning to recognize warning signs: a constraint has sent the agent in an unproductive direction, the same decision is being reopened, compatibility has become an end in itself, tests are measuring machinery rather than value, or implementation is producing activity without convergence.

A milestone can fail because its scope exceeded what the participants understood.
It can be re-specified and attempted again.
That is wasted effort, but it is not necessarily a failure of the overall project or evidence that the eventual software is poor.
The purpose of the milestone is not to guarantee success.
It is to limit how far the project can travel before human and machine have another opportunity to coordinate.

## Beyond Line-by-Line Comprehension

The abundance of generated code eventually makes comprehensive human review an implausible foundation for confidence.
Framing the choice as either direct review or indirect quality checks does not fully address the change.
The more fundamental reality is that humans may be unable to read all the code AI can produce for them.

Reduced direct exposure to code does not necessarily imply that less work or thought went into constructing the system.
The human may have spent substantial effort shaping its intent, testing constraints, rejecting directions, examining behavior, restructuring milestones, and learning from failure.
That work is real even when it does not result in familiarity with every function.

An intentional and documented process can still produce code that fails.
In a personal, academic, or exploratory context, that failure may simply become the next source of evidence.
The system is repaired and development continues.
As the project matures, extensive tests and more familiar software-engineering structures can help solidify it into an adequate result.

This does not establish a universal standard of correctness.
It suggests that AI abundance requires higher-level concepts for relating human effort to machine-produced systems.
Authorship, line coverage, and total comprehension may no longer describe the actual work.
The relevant question becomes how the human intentionally shaped the project, detected misdirection, responded to failure, and decided that its result was adequate for its particular use.

## Developing Taste for Changing Agents

Agents have idiosyncrasies that emerge from their models, instructions, context-management systems, and product harnesses.
One may become difficult to redirect because earlier context continues to dominate its behavior.
Another may redirect readily but fail to preserve decisions that should have remained stable.

Neither behavior can be reduced to a permanent rule about a product.
Models and harnesses change.
Practices learned against one version may become counterproductive against the next.
The engineer develops a provisional taste for these systems: noticing their characteristic failure modes, adapting the interaction, and remaining willing to revise the practice as the systems change.

This is one reason that learning every newly released technology is neither possible nor necessarily useful.
Industry continually offers new products, abstractions, and vocabulary as though adopting them were equivalent to making progress.
Early adopters can instead become involuntary participants in discovering product bugs and refining how a company will eventually sell its service.

Enthusiasm for AI does not require enthusiasm for every AI product.
I use AI throughout my work because I am convinced of its transformative capability.
I do not need to accept every commercial framing of trust, productivity, or collaboration.
Describing the experience in the ordinary language of the individual may produce a more honest account than adopting concepts designed primarily for enterprise purchasing and governance.

## The Emotional Cost of a Tireless Collaborator

Discussion of context management often centers on wasting model tokens or reducing model performance.
Less attention is given to what the interaction does to the person.

It is overwhelming to work with an entity that does not tire and that can outperform its operator at producing and decoding technical material.
There is no natural end to its suggestions, no shared fatigue that signals a stopping point, and no guarantee that reading one more response will resolve rather than expand the problem.
Software engineers who built careers around reducing ambiguity are being handed systems that dramatically increase both their capability and the ambiguity they must tolerate.

The technical and emotional problems are inseparable.
A person who is saturated cannot reliably decide which constraint matters.
A person anxious that the agent has lost the thread may respond by adding more context, making the thread harder to recover.
A person overwhelmed by generated possibilities may accept the next plausible direction simply to end the decision process.

Naming this experience can help experienced engineers understand what less experienced engineers are encountering, while giving younger engineers language for a discomfort they may already feel.
Managing the finite human is not a wellness concern attached to the real engineering work.
It is part of the engineering problem.

## Productivity Without Comfort

This argument begins from a bullish assumption: AI will produce extraordinary productivity gains, and those gains will make its incorporation into software work effectively unavoidable.

Where an adequate result requires roughly eighty percent of traditional human quality, much of the work becomes dramatically easier.
Where the last portion is critical, AI will still be used extensively and humans will govern that last mile for as long as necessary.
In either case, organizations and individuals that accept the productivity gain will change the baseline for everyone else.

The transition to farming offers a useful analogy.
Agriculture produced more food and supported larger, denser societies, but it did not simply improve the experience of every person who passed through the transition.
It brought disease, nutritional constraints, dependence on crops that could fail, and new social structures.
Once some populations reorganized around its productivity, however, others could not preserve the earlier way of life merely because it had meaningful advantages.

AI may create a similar distinction between increased productive capacity and improved lived experience.
A technology can become the inevitable basis of a new status quo while making daily work more ambiguous, cognitively demanding, and less satisfying.
Acknowledging those costs does not refute the productivity claim.
It makes the claim consequential.

## The Emerging Craft

The emerging craft is not a finished workflow.
It is the practice of remaining oriented across alternating periods of expansion and compression:

- giving the agent enough freedom to discover patterns the human could not specify;
- imposing bounds before the resulting work exceeds human capacity;
- noticing when constraints produce pathological behavior;
- allowing milestones to fail without confusing failure with catastrophe;
- preserving enough project state to recover direction without preserving everything;
- accepting that complete code comprehension may be unavailable; and
- deciding what adequate evidence means for the software actually being built.

The tools make this practice visible.
Chats separate working conversations.
Projects and files preserve durable context.
The terminal exposes underlying machinery.
Git records changes and makes experimentation recoverable.
Worktrees isolate parallel directions.
Tests allow reality to contradict fluent output.
Milestone documents give the next interaction a curated place from which to begin.

None of these removes the magic or resolves the ambiguity by itself.
Together, they provide places where a finite person can interrupt an unlimited stream of production and make another meaningful choice.

> AI-assisted development is becoming the craft of knowing when to let the
> work expand, when to stop it, and how to recover enough orientation to choose
> again.

The audience does not need to leave with a workflow to copy.
A more useful outcome may be a vocabulary for recognizing what is happening to both sides of the interaction: technical context can become overloaded, human attention can become saturated, and neither more output nor greater persistence necessarily restores direction.
The software engineer is being reborn into that ambiguity, not delivered from it.

# Seeing the System Around the Model

Most people who use AI products already know terms such as *model*, *prompt*, *context*, and *memory*.
The useful next step is not to accumulate more terminology, but to develop a vendor-independent way of seeing the system beneath the product.

> We do not interact with a model in isolation.
> We interact with a system built around a model, and that surrounding system
> determines much of its behavior, cost, reliability, and usefulness.

What appears to be a single intelligence may combine:

- a base model and a particular model version;
- system instructions, policies, and guardrails;
- context selected for the current request;
- persistent state retrieved from earlier interactions;
- tools, files, databases, and external services;
- an orchestration loop that decides what happens next;
- validation, retries, and feedback; and
- product behavior controlled by a vendor but hidden from the user.

Two products using the same model can therefore perform very differently.
The model matters, but the harness determines what the model can see, what it can do, when it receives feedback, and when its work is considered complete.

## Breaking Apart Context and Memory

The familiar word *memory* conceals several mechanisms.
It might refer to text still present in a context window, a summary of an old conversation, documents found through retrieval, preferences saved by a product, files available to an agent, state stored by an application, or knowledge embedded in model weights.

These mechanisms are not interchangeable.
They differ in who controls them, how reliably they are retrieved, how long they persist, what they cost, whether they can be inspected, and what privacy or security risks they introduce.
Describing all of them as memory encourages us to imagine a coherent mind where there may instead be several unrelated storage and retrieval systems.

Context is therefore not merely something a model "has."
It is something a system constructs.
Choosing what to include, exclude, summarize, retrieve, or preserve is an engineering decision with direct consequences for model behavior.

## How Generative Systems Go Wrong

Fluent output can fail for several different reasons:

- **Model failure:** the model produces an unsupported or incorrect answer.
- **Context failure:** relevant evidence is absent, stale, poorly selected, or overwhelmed by irrelevant material.
- **Instruction failure:** the objective or constraints are ambiguous, conflicting, or hidden beneath other instructions.
- **Tool failure:** an external action returns incomplete or misleading state, or the model uses the wrong tool.
- **Orchestration failure:** the harness retries, routes, summarizes, or stops in a way that prevents convergence.
- **Evaluation failure:** an output appears persuasive because the system has no independent mechanism for determining whether it is correct.

Calling every such event a hallucination obscures where intervention is possible.
The response is not simply to demand a better answer from the model.
Depending on the failure, it may be necessary to improve retrieval, narrow the task, expose source material, constrain the output, call a deterministic tool, add an executable test, compare independent attempts, require human review, or redesign the surrounding workflow.

This is one reason software has become such a productive domain for AI.
Compilers, type checkers, tests, version control, observability, deployment previews, and user behavior can contradict plausible output with evidence.
The strongest protection against generative failure is often not more generation, but a feedback loop connected to reality.

## Convenience, Control, and Lock-In

A polished product can make a capable system immediately accessible.
That convenience may also conceal context selection, compression, hidden instructions, model routing, tool behavior, retries, data retention, and silent changes in the implementation.

This does not make vendor products inherently undesirable.
Giving up control can be an excellent economic choice when the hidden behavior is not important to the task.
It becomes a problem when an organization depends on behavior it cannot inspect, reproduce, evaluate, or preserve.

> Abstraction is useful until the behavior we need to change is hidden beneath
> it.

The risk can be reduced architecturally rather than by choosing a supposedly permanent vendor:

- keep important specifications, prompts, and evaluations portable;
- maintain important context in systems the organization controls;
- separate orchestration from model access where the distinction matters;
- record model, configuration, and dependency versions;
- evaluate behavior rather than trusting a product name; and
- test more than one model when interchangeability has real value.

The objective is not to own every layer.
It is to make a deliberate decision about which layers encode durable value.
A useful rule is to own the workflow, context, judgment, and evaluation that distinguish the task, while renting components that are genuinely interchangeable.

## Bespoke Systems Become Economically Plausible

AI itself lowers the cost of building retrieval systems, orchestration, evaluations, interfaces, and task-specific tools.
A bespoke harness no longer necessarily implies a large platform project.
For a constrained and valuable workflow, a small implementation may be cheaper, more observable, and more stable than adapting the task to a broad vendor product.

Fine-tuning provides a related opportunity when the task and its evaluation are well defined.
A smaller model can sometimes be tuned or distilled to provide adequate task-specific performance at much lower inference cost.
This is not automatic: representative data and trustworthy evaluation are what make the efficiency meaningful.

The result is a wide field of engineering work.
Model laboratories need people who can improve models, training systems, inference, safety, and evaluation.
Enterprises need people who can assemble models into systems that reflect their own data, constraints, workflows, security requirements, and standards of evidence.
The latter work may be less visible, but it is where general capability becomes dependable organizational infrastructure.

## The Software Engineer's Opportunity

The complexity of these systems should not be presented merely as another body of knowledge to master.
It reveals why software engineers are well prepared to contribute.
They already work with abstractions, changing dependencies, imperfect components, hidden state, feedback, versioning, observability, and failure.

The reborn software engineer does not merely learn how to operate AI products.
They learn to see through them: to identify the model, context, control loop, feedback mechanism, hidden dependencies, and locus of ownership.

AI systems are designed systems.
They can therefore be decomposed, inspected, constrained, compared, tested, and increasingly rebuilt.
That perspective protects the user from mistaking a product boundary for a technical boundary, while opening substantial work for people who know how to turn powerful components into systems that can be trusted.

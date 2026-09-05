Assessing Quality

AI changes work in two distinct ways, creating two different problems of quality assessment.

Engineering probabilistic systems

Engineers build AI systems to perform a particular class of tasks repeatedly and at scale.
Unlike conventional software, these systems may be functionally flexible and their outputs probabilistic rather than fully specified in advance.

Quality is therefore primarily a property of the system’s behavior over a distribution of cases.
The engineering problem is to establish tolerable operating limits and optimize performance within them.

Assessment can draw on deterministic validation, reference answers, evaluation sets, rubrics, human judgments, adversarial cases, and statistical measures of performance.
The objective is not to establish that every future output will be correct, but that the system’s distribution of behavior is sufficiently reliable for its intended use.

The unit of trust is the engineered system.

AI-mediated knowledge work

A knowledge worker using AI may instead produce a novel artifact: a report, analysis, design, argument, or body of software.
Such artifacts are often not tractable to evaluation against a representative distribution or predetermined ground truth.
Their quality ultimately requires expert judgment.

AI can make their production dramatically cheaper, but this creates a corresponding problem: how can the resulting increase in output be assessed without making verification the new bottleneck?

Here, the production process itself can help.

AI-mediated work can preserve sources, calculations, intermediate artifacts, tests, revisions, validation results, and other provenance.
These provide evidence from which an expert can assess the final artifact rather than reconstructing its production independently.

This suggests several distinct concepts:

* Quality — how well the artifact satisfies its requirements.
* Assurance — the strength of the grounds for justified confidence in its quality.
* Assessability — how readily an expert can evaluate its quality and the evidence supporting it.
* Confidence — the expert’s belief about its quality.
* Calibration — the degree to which that confidence appropriately tracks actual quality.

High-quality AI-mediated knowledge work should therefore optimize not only the artifact, but its assurance and assessability.
The goal is not to induce trust in AI, but to make it inexpensive for an expert to determine when trust in the resulting work is warranted.

The unit of trust is the artifact and the evidence supporting it.

Two transformations of work

These approaches describe two complementary ways AI changes work.

Engineering: build probabilistic systems whose aggregate behavior can be characterized, bounded, and improved, allowing software to perform increasingly flexible classes of work at scale.

Knowledge work: use AI to increase the productivity of experts while preserving sufficient provenance, assurance, and assessability for them to maintain well-calibrated confidence in the resulting artifacts.

In one case, we learn to trust the behavior of a system within established limits.

In the other, we make individual artifacts easier to trust appropriately.

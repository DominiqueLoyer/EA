# RFP Solution Copilot (sysCRED-Enhanced FDE Submission)

An enterprise-grade, agentic LLM application that ingests Request for Proposal (RFP) briefs and produces structured solution summaries (requirements, approach, and risk assessments) backed by neuro-symbolic validation and rigorous evaluation.

---

## Architecture Overview

# EY Forward Deployed Engineering (FDE) — Demo Assets & Script

This document contains the presentation slide specification and the complete, corrected English narration script for the 3–4 minute RFP Copilot technical recruitment demo video.

---

## Part 1: Architecture Slide Specification

Use these parameters to construct or generate the single architecture slide for your recruitment presentation.

### Visual Constraints & Palette
* **Format:** Single image, 16:9 landscape, high resolution.
* **Background:** Clean white.
* **Colors:** Dark navy text and structure; restrained teal accents.
* **Style:** Flat vector-style diagram, generous spacing, precise typography.
* **Exclusions:** No company logos, fake terminal output, fake dashboards, metrics, benchmark scores, or compliance badges.

### Content Structure

```
+---------------------------------------------------------------------------------------------------+
|                                            RFP Copilot                                            |
|                                      Prototype Architecture                                       |
|               LangGraph orchestration with a sysCRED-inspired symbolic validation layer           |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ Raw RFP Text ]  ──(solid teal)──>  [ Parser Node ]  ──(solid teal)──>  [ Requirements Analyst ] |
|                                                                                    │              |
|                                                                               (solid teal)        |
|                                                                                    ▼              |
|  [ Structured Proposal ] <──(Passed)── [ Symbolic Validator ] <──(solid teal)── [ Solution Architect ]
|                                                │                                   ▲              |
|                                                └───(Failed: Feedback / Orange)─────┘              |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
|  Planned Integrations (Separate Box):                                                             |
|  PDF Ingestion  |  LLM Generation  |  Retrieval (RAG)  |  Telemetry  |  Evaluation Harness       |
+---------------------------------------------------------------------------------------------------+
|  Note: Prototype demonstration: parsing and proposal generation are currently stubbed.            |
|        Symbolic checks validate declared fields, not legal compliance.                            |
+---------------------------------------------------------------------------------------------------+
```

* **Main Flow (Left to Right):**
  1. Raw RFP Text
  2. Parser Node
  3. Requirements Analyst
  4. Solution Architect
  5. Symbolic Validator
* **Branching Logic:**
  * **Passed:** Route to `Structured Proposal`
  * **Failed:** Route back to `Solution Architect` via `Feedback` loop
* **Visual Distinction:**
  * **Solid Teal Arrows:** Forward execution workflow.
  * **Orange Curved Arrow:** Refinement loop (Failed path).
* **Bottom Note (Mandatory):**
  > *Prototype demonstration: parsing and proposal generation are currently stubbed. Symbolic checks validate declared fields, not legal compliance.*
* **Planned Integrations (Small Separate Box):**
  > *Planned integrations: PDF ingestion | LLM generation | Retrieval | Telemetry | Evaluation harness*

---

## Part 2: Corrected English Narration Script (3–4 Minutes)

This narration script aligns strictly with the actual code behavior, clearly distinguishing implemented prototype logic from planned production features.

---

### Section 1: Introduction and Architecture
**Timestamp:** `0:00 – 0:45`  
**Visual Target:** Architecture slide, then switching to the Python code repository in VS Code/Editor.

> "Hi team, I’m Dominique Loyer. This demonstration presents the orchestration prototype for my RFP Copilot: a workflow designed to turn RFP requirements into a structured technical proposal.
>
> The architecture uses LangGraph to separate parsing, requirements analysis, solution drafting, and symbolic validation.
>
> The validation layer is inspired by my research on hybrid neuro-symbolic systems. The goal is to distinguish what a language model proposes from what explicit rules can actually check.
>
> In this version, parsing and proposal generation are stubbed so that the graph structure and routing logic can be inspected clearly. I’ll distinguish those implemented elements from the planned integrations."

---

### Section 2: Code Walkthrough and Symbolic Validation
**Timestamp:** `0:45 – 1:45`  
**Visual Target:** Focusing on state definitions, node functions, and the symbolic validator predicate in `main.py`.

> "The shared state carries the input text, extracted requirements, proposed solution, validation status, and feedback.
>
> The workflow moves through the parser, the requirements analyst, and the solution architect before reaching the symbolic validator.
>
> In this sample, the proposed solution already includes a GDPR marker, so the validator follows the successful path.
>
> This is deliberately a narrow check. It confirms the presence of a declared field; it does not establish legal compliance or prove that the architecture satisfies every requirement.
>
> A stronger implementation would replace this string check with typed fields, explicit requirement-to-evidence mappings, and separate predicates for each constraint."

---

### Section 3: Refinement Loop & Implementation Limits
**Timestamp:** `1:45 – 2:45`  
**Visual Target:** Highlight `should_loop_back`, `iteration_count`, and the return edge to `solution_architect`.

> "The conditional router defines a refinement path when validation fails.
>
> There is an important limitation in the current implementation: the iteration counter is incremented in the parser, while the refinement loop returns directly to the architect.
>
> That means the counter does not yet enforce the intended retry limit. The correction is to increment an attempt counter within the refinement cycle and terminate explicitly when the budget is exhausted.
>
> The architect also needs to consume the validator’s feedback so that another attempt can make a meaningful change.
>
> At exhaustion, the output should remain clearly marked as unvalidated rather than being presented as an approved proposal."

---

### Section 4: Evaluation, Design Trade-offs, and Conclusion
**Timestamp:** `2:45 – 3:40`  
**Visual Target:** Showing `tests/test_eval_harness.py`, `DECISIONS.md`, and final terminal execution output.

> "The next implementation milestone is an evaluation harness covering the successful path, missing fields, unsuccessful refinement, and retry exhaustion.
>
> Observability should record node execution, validation failures, and retry counts. Once real model calls are integrated, it should also capture token usage, latency, and estimated model cost.
>
> Those measurements are planned here; this prototype does not yet provide production telemetry or benchmark results.
>
> The central design trade-off is flexibility versus verifiability. Generative components can draft a proposal, while explicit rules check a defined subset of constraints.
>
> This prototype establishes the workflow structure. The remaining work is to connect real ingestion and generation, strengthen the predicates, and demonstrate the complete system with reproducible tests.
>
> Thank you for your time."

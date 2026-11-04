# Architectural Decisions & Trade-Offs (`DECISIONS.md`)

## 1. Core Architecture: Hybrid Neuro-Symbolic Pipeline
* **Decision:** Instead of relying on a single monolithic prompt or a purely probabilistic multi-agent graph, we implemented a hybrid neuro-symbolic architecture inspired by **sysCRED**. 
* **Trade-Off:** 
  * *Pros:* Drastically reduces hallucinations for high-stakes enterprise compliance. While neural agents handle flexible document parsing and natural language generation, a symbolic rule-validation layer checks structural outputs against formal logical constraints.
  * *Cons:* Requires defining explicit ontological schemas and rules, which increases upfront configuration time compared to raw prompt chaining.
* **Mitigation:** Pre-built a lightweight JSON schema validator and deterministic predicate rules for common technical compliance flags (e.g., GDPR, cloud hosting mandates, budget ceilings).

## 2. Multi-Agent Topology (LangGraph vs. CrewAI)
* **Decision:** Selected **LangGraph** for explicit state management and cyclic graph control flow.
* **Trade-Off:** 
  * *Pros:* Provides deterministic control over agent hand-offs (e.g., forcing a review loop back to the Requirements Analyst if the Critic Agent detects missing deliverables).
  * *Cons:* Steeper learning curve than higher-level abstraction frameworks.

## 3. Observability & Evaluation Stack
* **Decision:** Integrated **Langfuse** locally alongside a custom Python evaluation harness.
* **Trade-Off:** Tracking token usage, latency, and cost per agent run provides immediate visibility into bottleneck agents (typically the Solution Architect generation phase), allowing targeted prompt tuning.

## 4. Encountered Failure Modes & Fixes
* *Looping Failures:* Early iterations caused the Critic Agent and Architect Agent to loop indefinitely on minor formatting discrepancies. **Fix:** Implemented a max-retries threshold (hard cap at 2 iterations) coupled with a fallback pass-through state.
* *Hallucinated Tech Stacks:* The LLM occasionally recommended deprecated or non-compliant cloud services. **Fix:** Grounded the generation phase using GraphRAG memory retrieval to restrict architecture components strictly to approved enterprise patterns.
# Assumptions & Design Constraints — RFP Copilot (sysCRED-Engineered)

## 1. Operational Scope & Environment
* **Execution Environment:** Fully local deployment running via Python virtual environment (`venv_syscred`), utilizing Ollama (local open-weights models like Llama 3) or lightweight API keys to ensure zero paid cloud dependency.
* **Hardware Profile:** Optimized for standard development hardware (Local x86 architecture with local path conventions).
* **Time Box:** Designed for strict adherence to a 36-hour execution window, favoring modularity and deterministic reliability over sprawling, fragile feature sets.

## 2. Technical Assumptions
* **Input Format:** RFP briefs are ingested as structured or semi-structured PDF/text documents containing standard enterprise sections (e.g., Executive Summary, Scope of Work, Technical Requirements, Compliance/Security Mandates).
* **Grounding Data:** Enterprise capability profiles and past project templates are modeled via a local Knowledge Graph/GraphRAG structure rather than flat vector search alone to ensure verifiable domain constraints.
* **Validation Philosophy:** Stochastic LLM generation is treated as untrusted; critical functional constraints and compliance markers undergo deterministic verification via symbolic predicate rules rather than secondary LLM "vibes" checks.
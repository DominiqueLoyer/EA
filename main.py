"""
RFP Copilot Multi-Agent Architecture using LangGraph & sysCRED Validation
"""
"""RFP Copilot Multi-Agent Architecture using LangGraph & sysCRED Validation"""

import os
import operator
from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END

# --- CONFIGURATION DE LA CLÉ GROQ ---
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("⚠️ Attention : La variable d'environnement GROQ_API_KEY n'est pas définie !")
else:
    print("✅ Clé Groq détectée avec succès.")

# 1. Define the shared state across agents
class RFPState(TypedDict):
    raw_rfp_text: str
    parsed_sections: Dict[str, Any]
    requirements: List[str]
    proposed_solution: Dict[str, Any]
    validation_passed: bool
    feedback_notes: List[str]
    iteration_count: int

import operator
from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END

# 1. Define the shared state across agents
class RFPState(TypedDict):
    raw_rfp_text: str
    parsed_sections: Dict[str, Any]
    requirements: List[str]
    proposed_solution: Dict[str, Any]
    validation_passed: bool
    feedback_notes: List[str]
    iteration_count: int

# 2. Initialize the graph
workflow = StateGraph(RFPState)

# --- Define Agent Node Functions ---

def ingestion_parser_node(state: RFPState) -> dict:
    """Agent 1: Parses raw RFP text into structured JSON metadata."""
    print("--- [Parser Agent] Extracting sections from RFP brief ---")
    return {
        "parsed_sections": {"scope": "Digital Transformation", "budget_cap": "Standard"},
        "iteration_count": state.get("iteration_count", 0) + 1
    }

def requirements_analyst_node(state: RFPState) -> dict:
    """Agent 2: Breaks down functional and non-functional requirements."""
    print("--- [Requirements Analyst] Identifying mandatory compliance points ---")
    extracted_reqs = [
        "Must comply with GDPR data residency",
        "Must support multi-tenant cloud deployment",
        "Sub-second response latency for core APIs"
    ]
    return {"requirements": extracted_reqs}

def solution_architect_node(state: RFPState) -> dict:
    """Agent 3: Drafts the technical solution and architecture stack (Grounding via GraphRAG)."""
    print("--- [Solution Architect] Drafting architecture & deliverables ---")
    solution = {
        "architecture": "Microservices on Private Cloud",
        "tech_stack": ["Python", "FastAPI", "Supabase PostgreSQL", "Docker"],
        "compliance_checked": "GDPR Compliant"
    }
    return {"proposed_solution": solution}

def syscred_symbolic_validator_node(state: RFPState) -> dict:
    """
    sysCRED Integration: Deterministic symbolic rule check. 
    Validates structural JSON against strict logical constraints (replacing fuzzy LLM critiques).
    """
    print("--- [sysCRED Symbolic Engine] Running predicate rule validation ---")
    solution = state.get("proposed_solution", {})
    
    # Deterministic rule: check if GDPR requirement is explicitly satisfied in the solution
    gdpr_satisfied = any("GDPR" in str(v) for v in solution.values())
    
    if gdpr_satisfied:
        return {"validation_passed": True, "feedback_notes": []}
    else:
        return {
            "validation_passed": False, 
            "feedback_notes": ["Missing mandatory GDPR compliance marker in architectural stack."]
        }

# --- Define Conditional Routing Logic ---

def should_loop_back(state: RFPState) -> str:
    """Routes back to the architect if symbolic validation fails, up to a max limit."""
    if not state["validation_passed"] and state["iteration_count"] < 2:
        print("--- [Router] Validation failed. Loop back to Solution Architect ---")
        return "refine"
    print("--- [Router] Validation passed or limit reached. Proceeding to final output ---")
    return "end"

# --- Add Nodes to Graph ---
workflow.add_node("parser", ingestion_parser_node)
workflow.add_node("requirements_analyst", requirements_analyst_node)
workflow.add_node("solution_architect", solution_architect_node)
workflow.add_node("symbolic_validator", syscred_symbolic_validator_node)

# --- Set Graph Edges ---
workflow.set_entry_point("parser")
workflow.add_edge("parser", "requirements_analyst")
workflow.add_edge("requirements_analyst", "solution_architect")
workflow.add_edge("solution_architect", "symbolic_validator")

# Conditional edge based on symbolic validation
workflow.add_conditional_edges(
    "symbolic_validator",
    should_loop_back,
    {
        "refine": "solution_architect",
        "end": END
    }
)

# Compile the application graph
app_graph = workflow.compile()

if __name__ == "__main__":
    print("Initializing RFP Copilot Graph...")
    initial_state = {
        "raw_rfp_text": "Sample Enterprise RFP Brief...",
        "parsed_sections": {},
        "requirements": [],
        "proposed_solution": {},
        "validation_passed": False,
        "feedback_notes": [],
        "iteration_count": 0
    }
    final_output = app_graph.invoke(initial_state)
    print("\nFinal Pipeline Execution Result:")
    print(final_output)
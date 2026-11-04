"""
Custom Evaluation Harness for RFP Agentic Pipeline.
Measures Requirement Coverage, Constraint Adherence, and Faithfulness.
"""

import json

def evaluate_requirement_coverage(generated_solution: dict, rfp_ground_truth: dict) -> float:
    """
    Scores percentage of explicit RFP requirements addressed in the solution summary.
    """
    required_items = set(rfp_ground_truth.get("mandatory_requirements", []))
    if not required_items:
        return 1.0
        
    addressed_items = set(generated_solution.get("addressed_requirements", []))
    intersection = required_items.intersection(addressed_items)
    
    score = len(intersection) / len(required_items)
    return round(score, 2)

def evaluate_constraint_adherence(generated_solution: dict, constraints: dict) -> bool:
    """
    Symbolic validation check ensuring hard constraints (budget, compliance) are met.
    """
    for key, rule_value in constraints.items():
        if generated_solution.get(key) != rule_value:
            return False
    return True

def test_evaluation_metrics():
    sample_solution = {"addressed_requirements": ["GDPR", "Multi-tenant"]}
    ground_truth = {"mandatory_requirements": ["GDPR", "Multi-tenant", "Sub-second latency"]}
    
    score = evaluate_requirement_coverage(sample_solution, ground_truth)
    assert score == 0.67, f"Expected 0.67 coverage score, got {score}"
    print("Evaluation harness test passed successfully!")

if __name__ == "__main__":
    test_evaluation_metrics()
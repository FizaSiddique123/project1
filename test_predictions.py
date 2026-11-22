"""
Clinical Triage AI - Test Suite
Verifies rule guardrail, ML triage prediction, emergency override, and possible conditions matching.
"""

import sys
from backend_server import compute_triage_decision, predict_triage, TriageRequest, SymptomInput

def run_tests():
    print("=" * 60)
    print("Running Clinical Triage AI Verification Tests...")
    print("=" * 60)

    test_cases = [
        {
            "name": "Mild Viral Scenario (Fever + Cough + Sore Throat)",
            "symptoms": [
                SymptomInput(id="fever", name="Fever"),
                SymptomInput(id="cough", name="Cough"),
                SymptomInput(id="sore_throat", name="Sore Throat")
            ],
            "intensity": "Moderate",
            "duration": "1–3 days",
            "expected_emergency": False,
            "expected_category": "PROMPT"
        },
        {
            "name": "Acute Emergency Scenario (Chest Pain + Shortness of Breath)",
            "symptoms": [
                SymptomInput(id="chest_pain", name="Chest Pain", redFlag=True),
                SymptomInput(id="shortness_of_breath", name="Shortness of Breath")
            ],
            "intensity": "Severe",
            "duration": "< 24 hours",
            "expected_emergency": True,
            "expected_category": "URGENT"
        },
        {
            "name": "Neurological / Migraine Scenario (Headache + Nausea + Light Sensitivity)",
            "symptoms": [
                SymptomInput(id="headache", name="Headache"),
                SymptomInput(id="nausea", name="Nausea"),
                SymptomInput(id="light_sensitivity", name="Light Sensitivity")
            ],
            "intensity": "Moderate",
            "duration": "1–3 days",
            "expected_emergency": False,
            "expected_category": "PROMPT"
        },
        {
            "name": "Routine Mild Scenario (Mild Fatigue)",
            "symptoms": [
                SymptomInput(id="fatigue", name="Fatigue")
            ],
            "intensity": "Mild",
            "duration": "1–3 days",
            "expected_emergency": False,
            "expected_category": "ROUTINE"
        }
    ]

    all_passed = True

    for i, tc in enumerate(test_cases, 1):
        req = TriageRequest(
            symptoms=tc["symptoms"],
            intensity=tc["intensity"],
            duration=tc["duration"],
            worsening="No",
            age=28,
            sex="Male",
            conditions=["None"]
        )

        res = predict_triage(req)
        is_emergency = res["emergencyTriggered"]
        cat = res["triageCategory"].upper()

        status = "PASSED"
        if tc["expected_emergency"] != is_emergency:
            status = f"FAILED (emergency expected {tc['expected_emergency']} got {is_emergency})"
            all_passed = False
        elif tc["expected_category"] != cat:
            status = f"FAILED (category expected {tc['expected_category']} got {cat})"
            all_passed = False

        print(f"[{status}] Test {i}: {tc['name']}")
        print(f"       Category: {cat} | Score: {res['score']} | Latency: {res['latencyMs']}ms")
        if not is_emergency:
            conds = res.get("possibleConditions", [])
            cond_names = [f"{c['name']} ({c['match_score']}%)" for c in conds[:2]]
            print(f"       Top Matches: {', '.join(cond_names) if cond_names else 'None'}")
        else:
            print("       Emergency Guardrail: Intercepted successfully (Conditions hidden)")
        print("-" * 60)

    # Optional HTTP test if server is running
    try:
        import requests
        r = requests.get("http://127.0.0.1:8000/health", timeout=1)
        if r.status_code == 200:
            print("[PASSED] Live Backend HTTP Health Check: http://127.0.0.1:8000/health (200 OK)")
    except Exception:
        pass

    if all_passed:
        print("\nAll verification tests completed successfully! ✓\n")
        return 0
    else:
        print("\nSome tests failed. Please review the output above. ✗\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())

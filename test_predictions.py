import requests
import json

tests = [
    {"name": "Fever + Vomiting", "symptoms": [{"id": "fever", "name": "Fever"}, {"id": "vomiting", "name": "Vomiting"}]},
    {"name": "Fever + Cough + Sore Throat", "symptoms": [{"id": "fever", "name": "Fever"}, {"id": "cough", "name": "Cough"}, {"id": "sore_throat", "name": "Sore Throat"}]},
    {"name": "Headache + Nausea + Light Sensitivity", "symptoms": [{"id": "headache", "name": "Headache"}, {"id": "nausea", "name": "Nausea"}, {"id": "light_sensitivity", "name": "Light Sensitivity"}]},
    {"name": "Chest Pain + Shortness of Breath", "symptoms": [{"id": "chest_pain", "name": "Chest Pain", "redFlag": True}, {"id": "shortness_of_breath", "name": "Shortness of Breath"}]},
]

for t in tests:
    payload = {
        "symptoms": t["symptoms"],
        "intensity": "Moderate",
        "duration": "1–3 days",
        "worsening": "No",
        "age": 30,
        "sex": "Male",
        "conditions": ["None"]
    }
    
    # Check if we should trigger the emergency override
    if "Chest Pain" in t["name"]:
        payload["intensity"] = "Severe"
        
    try:
        r = requests.post("http://127.0.0.1:8000/api/predict", json=payload)
        res = r.json()
        print(f"--- TEST: {t['name']} ---")
        if res.get("emergencyTriggered"):
            print("EMERGENCY TRIGGERED (Conditions hidden)")
        else:
            conds = res.get("possibleConditions", [])
            if not conds:
                print("NO MATCHING CONDITIONS")
            else:
                for c in conds:
                    print(f"{c['name']}: {c['match_score']}% - Matched: {', '.join(c['matched_symptoms'])}")
                print(f"TOTAL: {sum(c['match_score'] for c in conds)}%")
        print("")
    except Exception as e:
        print(f"Error for {t['name']}: {e}")

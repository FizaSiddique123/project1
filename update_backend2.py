import re

with open('backend_server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything from `CONDITION_CATALOG = [` to the end of `calculate_possible_conditions(req: TriageRequest) -> List[Dict[str, Any]]:`
# Let's find the boundaries.
start_str = "CONDITION_CATALOG = ["
end_str = "# ---------------------------------------------------------------------------"

start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx + len(start_str))

if start_idx != -1 and end_idx != -1:
    new_code = """CONDITION_CATALOG = [
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Common Cold",
        "description": "Commonly associated with mild upper respiratory symptoms like sore throat and congestion.",
        "strong_symptoms": ["runny_nose", "nasal_congestion", "sneezing", "sore_throat", "cough"],
        "supporting_symptoms": ["fever", "fatigue", "headache"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Influenza",
        "description": "Often presents with sudden onset fever, body aches, fatigue, and respiratory symptoms.",
        "strong_symptoms": ["fever", "chills", "body_ache", "fatigue", "headache", "cough"],
        "supporting_symptoms": ["sore_throat", "runny_nose", "nausea"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Viral Upper Respiratory Infection",
        "description": "Involves congestion, sore throat, and mild systemic symptoms.",
        "strong_symptoms": ["cough", "sore_throat", "runny_nose", "nasal_congestion"],
        "supporting_symptoms": ["fever", "fatigue", "headache"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Acute Bronchitis",
        "description": "Characterized by cough, mucus production, and mild chest discomfort.",
        "strong_symptoms": ["cough", "productive_cough", "chest_discomfort"],
        "supporting_symptoms": ["fatigue", "fever", "shortness_of_breath"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Pneumonia",
        "description": "A deeper lung infection typically causing fever, cough, and shortness of breath.",
        "strong_symptoms": ["fever", "cough", "shortness_of_breath", "chest_pain"],
        "supporting_symptoms": ["fatigue", "chills"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Asthma Exacerbation",
        "description": "Involves airway inflammation presenting as wheezing and shortness of breath.",
        "strong_symptoms": ["wheezing", "shortness_of_breath", "chest_tightness", "cough"],
        "supporting_symptoms": []
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Sinusitis",
        "description": "Inflammation of the sinuses causing facial pressure and nasal discharge.",
        "strong_symptoms": ["nasal_congestion", "facial_pressure", "headache"],
        "supporting_symptoms": ["runny_nose", "sore_throat", "fever"]
    },
    {
        "category": "RESPIRATORY / INFECTIOUS",
        "name": "Pharyngitis",
        "description": "Inflammation of the back of the throat causing soreness and pain when swallowing.",
        "strong_symptoms": ["sore_throat", "difficulty_swallowing"],
        "supporting_symptoms": ["fever", "headache"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Viral Gastroenteritis",
        "description": "Commonly associated with nausea, vomiting, diarrhea, and abdominal discomfort.",
        "strong_symptoms": ["vomiting", "diarrhea", "nausea", "abdominal_cramping"],
        "supporting_symptoms": ["fever", "fatigue", "abdominal_pain"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Food Poisoning",
        "description": "Often causes rapid onset of nausea, vomiting, and diarrhea after consuming contaminated food.",
        "strong_symptoms": ["vomiting", "diarrhea", "nausea", "abdominal_pain"],
        "supporting_symptoms": ["fever", "abdominal_cramping"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Gastritis",
        "description": "Stomach inflammation causing upper abdominal pain and nausea.",
        "strong_symptoms": ["upper_abdominal_pain", "nausea", "vomiting"],
        "supporting_symptoms": ["heartburn", "loss_of_appetite", "bloating"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "GERD",
        "description": "Typically presents as heartburn or chest discomfort, often after meals.",
        "strong_symptoms": ["heartburn", "acid_reflux", "chest_discomfort"],
        "supporting_symptoms": ["nausea", "bloating"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Irritable Bowel Syndrome",
        "description": "A chronic condition characterized by recurrent abdominal pain and changes in bowel habits.",
        "strong_symptoms": ["abdominal_pain", "abdominal_cramping", "bloating"],
        "supporting_symptoms": ["diarrhea", "constipation"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Constipation",
        "description": "Difficulty passing stool, often causing abdominal pain or bloating.",
        "strong_symptoms": ["constipation", "abdominal_pain", "bloating"],
        "supporting_symptoms": ["loss_of_appetite"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Migraine",
        "description": "Severe headaches often accompanied by nausea and sensitivity to light or sound.",
        "strong_symptoms": ["headache", "light_sensitivity", "sound_sensitivity", "nausea"],
        "supporting_symptoms": ["vomiting", "dizziness"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Tension Headache",
        "description": "Presents as a steady ache or band-like pressure around the head.",
        "strong_symptoms": ["headache"],
        "supporting_symptoms": ["neck_pain", "fatigue", "stress_related_symptoms"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Viral-Associated Headache",
        "description": "Headaches occurring secondary to a systemic viral infection with fever.",
        "strong_symptoms": ["headache", "fever", "fatigue"],
        "supporting_symptoms": ["body_ache", "nausea"]
    },
    {
        "category": "URINARY",
        "name": "Urinary Tract Infection",
        "description": "Often presents with painful and frequent urination.",
        "strong_symptoms": ["painful_urination", "frequent_urination"],
        "supporting_symptoms": ["lower_abdominal_pain", "fever", "blood_in_urine"]
    },
    {
        "category": "URINARY",
        "name": "Kidney Stone",
        "description": "Causes severe flank pain that may radiate, along with nausea.",
        "strong_symptoms": ["flank_pain", "severe_abdominal_pain"],
        "supporting_symptoms": ["nausea", "vomiting", "blood_in_urine"]
    },
    {
        "category": "CARDIOVASCULAR",
        "name": "Palpitations",
        "description": "Sensation of a racing, fluttering, or pounding heart.",
        "strong_symptoms": ["palpitations"],
        "supporting_symptoms": ["dizziness", "fatigue", "shortness_of_breath"]
    },
    {
        "category": "CARDIOVASCULAR",
        "name": "Angina-like Chest Pain Pattern",
        "description": "Exertional chest discomfort that resolves with rest. Emergency check required.",
        "strong_symptoms": ["chest_pain", "chest_tightness"],
        "supporting_symptoms": ["shortness_of_breath", "sweating", "fatigue"]
    },
    {
        "category": "DERMATOLOGICAL",
        "name": "Allergic Skin Reaction",
        "description": "Skin inflammation often caused by allergens.",
        "strong_symptoms": ["rash", "itching", "swelling"],
        "supporting_symptoms": ["redness"]
    },
    {
        "category": "DERMATOLOGICAL",
        "name": "Contact Dermatitis",
        "description": "Localized rash or irritation from direct contact with a substance.",
        "strong_symptoms": ["rash", "itching"],
        "supporting_symptoms": ["localized_swelling", "redness"]
    },
    {
        "category": "MUSCULOSKELETAL",
        "name": "Muscle Strain",
        "description": "Pain or soreness from overstretched or torn muscle.",
        "strong_symptoms": ["muscle_pain", "localized_pain"],
        "supporting_symptoms": ["swelling"]
    },
    {
        "category": "MUSCULOSKELETAL",
        "name": "Tension / Musculoskeletal Neck Pain",
        "description": "Neck pain typically related to posture or muscle tension.",
        "strong_symptoms": ["neck_pain", "muscle_pain"],
        "supporting_symptoms": ["headache"]
    },
    {
        "category": "GENERAL / SYSTEMIC",
        "name": "Viral Infection",
        "description": "Systemic infection causing a combination of fever, fatigue, and body aches.",
        "strong_symptoms": ["fever", "fatigue", "body_ache"],
        "supporting_symptoms": ["headache", "nausea", "cough"]
    },
    {
        "category": "GENERAL / SYSTEMIC",
        "name": "Dehydration",
        "description": "Fluid loss leading to weakness, dizziness, and fatigue.",
        "strong_symptoms": ["dizziness", "weakness", "fatigue"],
        "supporting_symptoms": ["vomiting", "diarrhea"]
    }
]

def normalize_symptom(symptom_name: str) -> str:
    s = symptom_name.lower().strip()
    mapping = {
        "head pain": "headache",
        "pain in head": "headache",
        "breathlessness": "shortness_of_breath",
        "difficulty breathing": "shortness_of_breath",
        "throwing up": "vomiting",
        "stomach ache": "abdominal_pain",
        "belly pain": "abdominal_pain",
        "loose motion": "diarrhea",
        "loose stools": "diarrhea",
        "high temperature": "fever",
        "mild fever": "fever"
    }
    s = mapping.get(s, s)
    s = s.replace(" ", "_")
    return s

def calculate_possible_conditions(req: TriageRequest) -> List[Dict[str, Any]]:
    user_symptoms_norm = {normalize_symptom(s.name) for s in req.symptoms}
    
    results = []
    
    for cond in CONDITION_CATALOG:
        strong = set(cond["strong_symptoms"])
        supporting = set(cond["supporting_symptoms"])
        
        matched_strong = user_symptoms_norm.intersection(strong)
        matched_supporting = user_symptoms_norm.intersection(supporting)
        
        if len(matched_strong) == 0 and len(matched_supporting) == 0:
            continue
            
        # Avoid false matches: 
        # Require minimum 2 meaningful matching symptoms OR 1 highly specific symptom with strong weight
        if len(matched_strong) + len(matched_supporting) < 2 and len(matched_strong) == 0:
            continue
            
        score = (len(matched_strong) * 3) + (len(matched_supporting) * 1)
        
        # We also boost based on coverage of condition
        # Max possible condition score:
        max_possible = (len(strong) * 3) + (len(supporting) * 1)
        if max_possible == 0: max_possible = 1
        
        match_quality = score / max_possible
        
        # Final raw score is a combination of absolute score and match quality
        raw_score = score + (match_quality * 5)
        
        matched_names = [s.replace("_", " ").title() for s in (matched_strong | matched_supporting)]
        
        results.append({
            "name": cond["name"],
            "description": cond["description"],
            "raw_score": raw_score,
            "matched_symptoms": matched_names
        })
        
    # Sort descending
    results.sort(key=lambda x: x["raw_score"], reverse=True)
    top_results = results[:3]
    
    if not top_results:
        return []
        
    # Percentage Distribution
    total_score = sum(r["raw_score"] for r in top_results)
    if total_score == 0:
        return []
        
    for r in top_results:
        r["match_score"] = int(round((r["raw_score"] / total_score) * 100))
        del r["raw_score"] # clean up
        
    # ALWAYS ENSURE TOTAL = 100
    current_total = sum(r["match_score"] for r in top_results)
    if current_total != 100 and top_results:
        diff = 100 - current_total
        # Add the diff to the one with the highest score
        top_results[0]["match_score"] += diff
        
    return top_results
\n"""
    
    content = content[:start_idx] + new_code + content[end_idx:]
    
    with open('backend_server.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated backend_server.py successfully.")
else:
    print("Could not find the insertion points.")

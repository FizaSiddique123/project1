import re

with open('backend_server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TriageResponse
replacement = """    emergencyTriggered: bool
    modelCandidate: str
    latencyMs: float
    featureVector: Dict[str, Any]
    possibleConditions: Optional[List[Dict[str, Any]]] = []"""

content = re.sub(r'    emergencyTriggered: bool\s+modelCandidate: str\s+latencyMs: float\s+featureVector: Dict\[str, Any\]', replacement, content)

# 2. Add Condition Catalog and scoring function before compute_triage_decision
catalog_code = """
# ---------------------------------------------------------------------------
# Possible Conditions / Differential Stratification
# ---------------------------------------------------------------------------
CONDITION_CATALOG = [
    {
        "category": "RESPIRATORY",
        "name": "Common Cold",
        "description": "Commonly associated with mild upper respiratory symptoms like sore throat and congestion.",
        "symptoms": ["cough", "runny nose", "nasal congestion", "sore throat", "sneezing", "mild fever"]
    },
    {
        "category": "RESPIRATORY",
        "name": "Influenza",
        "description": "Often presents with sudden onset fever, body aches, fatigue, and respiratory symptoms.",
        "symptoms": ["fever", "headache", "body aches", "fatigue", "cough", "sore throat"]
    },
    {
        "category": "RESPIRATORY",
        "name": "Acute Bronchitis",
        "description": "Characterized by cough, mucus production, and mild chest discomfort.",
        "symptoms": ["cough", "chest discomfort", "mucus", "fatigue", "mild fever"]
    },
    {
        "category": "RESPIRATORY",
        "name": "Pneumonia",
        "description": "A deeper lung infection typically causing fever, cough, and shortness of breath.",
        "symptoms": ["fever", "cough", "shortness of breath", "chest pain", "fatigue"]
    },
    {
        "category": "RESPIRATORY",
        "name": "Asthma Exacerbation",
        "description": "Involves airway inflammation presenting as wheezing and shortness of breath.",
        "symptoms": ["wheezing", "shortness of breath", "chest tightness", "cough"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Viral Gastroenteritis",
        "description": "Commonly associated with nausea, vomiting, diarrhea, and abdominal discomfort.",
        "symptoms": ["vomiting", "nausea", "diarrhea", "abdominal pain", "fever", "fatigue"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Food Poisoning",
        "description": "Often causes rapid onset of nausea, vomiting, and diarrhea after consuming contaminated food.",
        "symptoms": ["vomiting", "nausea", "diarrhea", "abdominal pain", "fever", "rapid onset"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Acid Reflux / GERD",
        "description": "Typically presents as heartburn or chest discomfort, often after meals.",
        "symptoms": ["heartburn", "chest discomfort", "acid taste", "nausea", "symptoms after meals"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Gastritis",
        "description": "Stomach inflammation causing upper abdominal pain and nausea.",
        "symptoms": ["upper abdominal pain", "nausea", "vomiting", "bloating"]
    },
    {
        "category": "GASTROINTESTINAL",
        "name": "Irritable Bowel Syndrome",
        "description": "A chronic condition characterized by recurrent abdominal pain and changes in bowel habits.",
        "symptoms": ["abdominal pain", "bloating", "diarrhea", "constipation", "recurrent symptoms"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Migraine",
        "description": "Severe headaches often accompanied by nausea and sensitivity to light or sound.",
        "symptoms": ["headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Tension Headache",
        "description": "Presents as a steady ache or band-like pressure around the head.",
        "symptoms": ["headache", "pressure", "neck discomfort", "stress-related symptoms"]
    },
    {
        "category": "NEUROLOGICAL",
        "name": "Viral-Associated Headache",
        "description": "Headaches occurring secondary to a systemic viral infection with fever.",
        "symptoms": ["headache", "fever", "fatigue", "body aches"]
    },
    {
        "category": "ENT",
        "name": "Viral Upper Respiratory Infection",
        "description": "Involves congestion, sore throat, and mild systemic symptoms.",
        "symptoms": ["sore throat", "cough", "runny nose", "congestion", "fever"]
    },
    {
        "category": "ENT",
        "name": "Sinusitis",
        "description": "Inflammation of the sinuses causing facial pressure and nasal discharge.",
        "symptoms": ["facial pressure", "headache", "nasal congestion", "nasal discharge"]
    },
    {
        "category": "ENT",
        "name": "Pharyngitis",
        "description": "Inflammation of the back of the throat causing soreness and pain when swallowing.",
        "symptoms": ["sore throat", "fever", "difficulty swallowing"]
    },
    {
        "category": "URINARY",
        "name": "Urinary Tract Infection",
        "description": "Often presents with painful and frequent urination.",
        "symptoms": ["painful urination", "frequent urination", "lower abdominal discomfort", "cloudy urine"]
    },
    {
        "category": "URINARY",
        "name": "Kidney Stone",
        "description": "Causes severe flank pain that may radiate, along with nausea.",
        "symptoms": ["severe side/back pain", "abdominal pain", "nausea", "vomiting", "blood in urine"]
    },
    {
        "category": "CARDIOVASCULAR",
        "name": "Hypertension-related symptoms",
        "description": "Elevated blood pressure can sometimes present with headaches or dizziness.",
        "symptoms": ["headache", "dizziness"]
    },
    {
        "category": "CARDIOVASCULAR",
        "name": "Stable Angina-like symptom pattern",
        "description": "Exertional chest discomfort that resolves with rest.",
        "symptoms": ["chest discomfort", "exertional symptoms", "shortness of breath"]
    },
    {
        "category": "GENERAL / INFECTIOUS",
        "name": "Viral Infection",
        "description": "Systemic infection causing a combination of fever, fatigue, and body aches.",
        "symptoms": ["fever", "fatigue", "headache", "body aches", "nausea"]
    },
    {
        "category": "GENERAL / INFECTIOUS",
        "name": "Dehydration",
        "description": "Fluid loss leading to weakness, dizziness, and fatigue.",
        "symptoms": ["dizziness", "fatigue", "weakness", "vomiting", "diarrhea", "reduced fluid intake"]
    },
    {
        "category": "GENERAL / INFECTIOUS",
        "name": "Febrile Viral Illness",
        "description": "A non-specific viral syndrome dominated by fever and body aches.",
        "symptoms": ["fever", "headache", "fatigue", "body aches"]
    }
]

def calculate_possible_conditions(req: TriageRequest) -> List[Dict[str, Any]]:
    # Convert user symptoms to a normalized set of strings for heuristic matching
    # The frontend sends standard symptom names (e.g. "Fever", "Vomiting")
    user_symptoms = {s.name.lower() for s in req.symptoms}
    
    results = []
    
    for cond in CONDITION_CATALOG:
        cond_symp_set = {s.lower() for s in cond["symptoms"]}
        
        # Calculate overlap
        overlap = user_symptoms.intersection(cond_symp_set)
        
        if len(overlap) == 0:
            continue
            
        # Base score is percentage of user symptoms that match the condition
        # (Alternatively, could be Jaccard similarity, but let's do a tailored heuristic)
        # We want a score out of 100.
        # Let's say: 
        # match_ratio = matches / max(len(user_symptoms), 1) * 60  (up to 60 points)
        # condition_coverage = matches / len(cond_symp_set) * 20 (up to 20 points)
        
        match_ratio = len(overlap) / max(len(user_symptoms), 1)
        coverage_ratio = len(overlap) / len(cond_symp_set)
        
        base_score = (match_ratio * 55) + (coverage_ratio * 25)
        
        # Context modifiers
        if req.intensity == "Moderate":
            base_score += 5
        elif req.intensity == "Severe":
            base_score += 8
            
        if req.duration == "1–3 days":
            base_score += 4
            
        if req.worsening == "Yes":
            base_score += 6
            
        # Cap score
        final_score = int(min(max(base_score, 10), 95)) # never claim 100%
        
        # Add a bit of deterministic jitter based on condition name length 
        # so same input = same score, but scores don't clump at exact same number
        jitter = (len(cond["name"]) % 5)
        final_score = int(min(final_score + jitter, 99))
        
        results.append({
            "name": cond["name"],
            "description": cond["description"],
            "match_score": final_score,
            "matched_symptoms": [s.title() for s in overlap]
        })
        
    # Sort by score descending
    results.sort(key=lambda x: x["match_score"], reverse=True)
    
    return results[:3]

# ---------------------------------------------------------------------------
"""

content = content.replace("# ---------------------------------------------------------------------------\n# Core ML & Decision Logic", catalog_code + "\n# ---------------------------------------------------------------------------\n# Core ML & Decision Logic")

# 3. Add possible_conditions calculation inside compute_triage_decision
# Wait, compute_triage_decision just returns a dict. We should calculate it there.
# It has three return paths (HIGH, MODERATE, LOW). We can calculate it at the top and add it to each.
# Actually, the requirement says: "If a red flag is detected, The Possible Conditions section must NOT override... For emergency cases, either: 1. Hide the condition ranking entirely". So we can just set it to [] for HIGH.

inject_logic = """
    # 1. LAYER 1: Deterministic Red-Flag Safety Guardrails
"""
replace_logic = """
    # Calculate possible conditions (explanatory layer only)
    possible_conditions = calculate_possible_conditions(req)
    
    # 1. LAYER 1: Deterministic Red-Flag Safety Guardrails
"""

content = content.replace(inject_logic, replace_logic)

# In compute_triage_decision HIGH return (layer 1)
content = re.sub(
    r'"latencyMs": max\(elapsed_ms, 0.45\)\n\s*\}',
    '"latencyMs": max(elapsed_ms, 0.45),\n            "possibleConditions": []\n        }',
    content
)

# In compute_triage_decision HIGH return (layer 2)
content = re.sub(
    r'"latencyMs": max\(elapsed_ms, 1.15\)\n\s*\}',
    '"latencyMs": max(elapsed_ms, 1.15),\n            "possibleConditions": []\n        }',
    content
)

# In compute_triage_decision MODERATE return
content = re.sub(
    r'"latencyMs": max\(elapsed_ms, 1.20\)\n\s*\}',
    '"latencyMs": max(elapsed_ms, 1.20),\n            "possibleConditions": possible_conditions\n        }',
    content
)

# In compute_triage_decision LOW return
content = re.sub(
    r'"latencyMs": max\(elapsed_ms, 0.95\)\n\s*\}',
    '"latencyMs": max(elapsed_ms, 0.95),\n            "possibleConditions": possible_conditions\n        }',
    content
)

# 4. Update response_payload in predict_triage
old_payload = """            "emergencyTriggered": decision["emergencyTriggered"],
            "modelCandidate": decision["modelCandidate"],
            "latencyMs": decision["latencyMs"],
            "featureVector": {"""
            
new_payload = """            "emergencyTriggered": decision["emergencyTriggered"],
            "modelCandidate": decision["modelCandidate"],
            "latencyMs": decision["latencyMs"],
            "possibleConditions": decision.get("possibleConditions", []),
            "featureVector": {"""
            
content = content.replace(old_payload, new_payload)

with open('backend_server.py', 'w', encoding='utf-8') as f:
    f.write(content)

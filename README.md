# Clinical Triage AI
**Autonomous Clinical Symptom Triage & Risk Prediction Platform**

Clinical Triage AI is an enterprise-grade Clinical Decision Support System (CDSS) providing dual-layer risk stratification and symptom triage. It combines a deterministic safety guardrail (zero false-negative acute emergency override) with a calibrated multi-factor risk matrix and differential symptom pattern matching across 27+ clinical conditions.

---

## Key Features

- **Public Landing Page**: Modern healthcare presentation with video banner and Clerk authentication.
- **Patient Dashboard**: Authenticated patient portal showing triage history, health status, and quick access to new assessments.
- **Dual-Layer Triage Engine**:
  - *Layer 1 (Safety Guardrail)*: Deterministic red-flag screening for critical cardiopulmonary and neurological presentations (< 0.5 ms override).
  - *Layer 2 (Risk Prediction Matrix)*: Multi-factor clinical severity scoring (0–100) classifying patient urgency into **Routine**, **Prompt**, or **Emergency** categories.
- **Differential Pattern Matching**: Intelligent condition association providing match percentages and symptom overlap explanations for non-emergency presentations.
- **Explainable Clinical Factors**: Transparent clinical explanations and recommended next steps for patients.
- **Session Audit & Intake Note**: Printable clinical intake note for triage nurses and healthcare providers.

---

## Technology Stack

- **Frontend**: HTML5, Vanilla JavaScript, CSS3, Google Fonts (Plus Jakarta Sans, JetBrains Mono, Outfit, Inter)
- **Authentication**: Clerk Authentication (JWT session management)
- **Frontend Server**: Node.js HTTP server (`frontend_server.js`) with reverse-proxy routing
- **Backend API**: Python 3 (FastAPI, Uvicorn, Pydantic)
- **Machine Learning & Triage Logic**: Multi-factor feature weighting, SNOMED-CT symptom catalog, and differential scoring

---

## Directory Structure

```text
├── .env                  # Environment configuration (Clerk publishable & secret keys)
├── package.json          # Node.js project manifest & scripts
├── README.md             # Project documentation
├── start_all.py          # Unified runner starting both backend and frontend servers
│
├── frontend_server.js    # Node.js static & API proxy server (Port 3000)
├── landing.html          # Public landing & authentication entry point
├── dashboard.html        # Patient dashboard, symptom assessment wizard & results SPA
├── app.css               # Application component styling & design tokens
├── dashboard.css         # Patient dashboard, sidebar & differential cards layout
├── app.js                # Client application controller & triage state management
│
├── backend_server.py     # FastAPI backend server with clinical triage engine (Port 8000)
├── test_predictions.py   # Verification test suite for triage engine & emergency override
│
└── public/
    └── bgvideo.mp4       # Background video asset for landing page hero
```

---

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.10+)
- Python dependencies: `pip install fastapi uvicorn pydantic requests`

### Installation & Launch

1. **Start Both Frontend and Backend Servers (Recommended)**:
   ```bash
   npm run start:all
   # or
   python start_all.py
   ```

2. **Access the Application**:
   - **Main Website / Landing Page**: [http://localhost:3000](http://localhost:3000)
   - **Patient Dashboard**: [http://localhost:3000/dashboard](http://localhost:3000/dashboard)
   - **Backend API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Run Individual Services (Optional)**:
   ```bash
   # Run only Node.js frontend server (Port 3000)
   npm start

   # Run only FastAPI backend API (Port 8000)
   npm run backend
   ```

### Running Tests

```bash
npm test
# or
python test_predictions.py
```

---

## REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check endpoint returning service status |
| `GET` | `/api/status` | Detailed platform architecture, model candidates & benchmark metrics |
| `POST` | `/api/predict` | Executes dual-layer clinical triage & differential condition matching |
| `GET` | `/api/history` | Fetches historical triage assessment sessions |

---

## Medical Disclaimer

Clinical Triage AI provides preliminary AI-assisted decision support and triage classification based strictly on reported symptoms. It does not provide definitive medical diagnoses, prescriptions, or clinical certifications. Users experiencing life-threatening emergencies must immediately contact their national emergency medical services.

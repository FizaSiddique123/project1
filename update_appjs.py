import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the renderPossibleConditions function right after renderResultScreen
# Let's find the end of renderResultScreen
match = re.search(r'  updateTechInspectorJSON\(\);\n}', content)
if match:
    replacement = """  updateTechInspectorJSON();
  
  // Render Possible Conditions (if any)
  renderPossibleConditions(result.possibleConditions, result.emergencyTriggered);
}

function renderPossibleConditions(conditions, isEmergency) {
  const container = document.getElementById('possible-conditions-container');
  if (!container) return;
  
  // Hide completely if emergency
  if (isEmergency || !conditions || conditions.length === 0) {
    container.style.display = 'none';
    return;
  }
  
  container.style.display = 'block';
  container.innerHTML = `
    <hr style="border: 0; border-top: 1px solid var(--color-border); margin: 32px 0;">
    <div style="margin-bottom: 24px;">
      <h3 style="font-size: 1.1rem; color: var(--color-text); margin-bottom: 8px;">Possible Conditions</h3>
      <p style="font-size: 0.9rem; color: var(--color-grey); margin: 0;">
        Based on the symptoms and information you provided, these conditions may share similar symptom patterns.
      </p>
    </div>
    
    <div class="conditions-grid">
      ${conditions.map(cond => `
        <div class="condition-card">
          <div class="condition-card-header">
            <h4 class="condition-name">${cond.name}</h4>
          </div>
          <p class="condition-desc">${cond.description}</p>
          
          <div class="condition-match-row">
            <span class="condition-match-label">Symptom Match</span>
            <span class="condition-match-percent">${cond.match_score}%</span>
          </div>
          
          <div class="condition-progress-bg">
            <div class="condition-progress-fill" style="width: ${cond.match_score}%;"></div>
          </div>
          
          <details class="condition-details">
            <summary>Why this matched</summary>
            <div class="condition-details-content">
              <strong>Matched Symptoms:</strong>
              <ul>
                ${cond.matched_symptoms.map(s => `<li>${s}</li>`).join('')}
              </ul>
            </div>
          </details>
        </div>
      `).join('')}
    </div>
    
    <div class="condition-disclaimer">
      <strong>Disclaimer:</strong> Symptom Match scores are informational compatibility scores, not diagnostic probabilities. This assessment does not provide a medical diagnosis. Only a qualified healthcare professional can diagnose a medical condition.
    </div>
  `;
}
"""
    content = content.replace(match.group(0), replacement)
    
    # Also update completeAssessmentWithBackend to pass possibleConditions to resultData
    old_payload = """      latencyMs: apiResponse.latencyMs,"""
    new_payload = """      latencyMs: apiResponse.latencyMs,
      possibleConditions: apiResponse.possibleConditions,"""
    content = content.replace(old_payload, new_payload)
    
    # Update fallback predictRisk to include possibleConditions: []
    old_fallback = """    const localResult = predictRisk(inputPayload);
    resultData = {
      ...localResult,
      latencyMs: 1.8,"""
    new_fallback = """    const localResult = predictRisk(inputPayload);
    resultData = {
      ...localResult,
      possibleConditions: [],
      latencyMs: 1.8,"""
    content = content.replace(old_fallback, new_fallback)
    
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated app.js successfully.")
else:
    print("Could not find the insertion point in app.js")

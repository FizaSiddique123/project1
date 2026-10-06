import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace `function renderPossibleConditions(conditions, isEmergency) { ... }` 
# I will use regex to find the function and replace it entirely.
match = re.search(r'function renderPossibleConditions\(conditions, isEmergency\) \{.*?\n\}', content, re.DOTALL)

new_func = """function renderPossibleConditions(conditions, isEmergency) {
  const container = document.getElementById('possible-conditions-container');
  if (!container) return;
  
  // Hide completely if emergency
  if (isEmergency) {
    container.style.display = 'none';
    return;
  }
  
  container.style.display = 'block';
  
  if (!conditions || conditions.length === 0) {
    container.innerHTML = `
      <hr style="border: 0; border-top: 1px solid var(--color-border); margin: 32px 0;">
      <div style="margin-bottom: 24px;">
        <h3 style="font-size: 1.1rem; color: var(--color-text); margin-bottom: 8px;">Possible Conditions</h3>
        <p style="font-size: 0.95rem; color: var(--color-grey); margin-bottom: 12px; font-weight: 500;">
          No strong symptom pattern match was identified.
        </p>
        <p style="font-size: 0.9rem; color: var(--color-grey); margin: 0;">
          Please consult a qualified healthcare professional if symptoms persist, worsen, or concern you.
        </p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = `
    <hr style="border: 0; border-top: 1px solid var(--color-border); margin: 32px 0;">
    <div style="margin-bottom: 24px;">
      <h3 style="font-size: 1.1rem; color: var(--color-text); margin-bottom: 8px;">Possible Conditions</h3>
      <p style="font-size: 0.9rem; color: var(--color-grey); margin: 0;">
        Based on the symptoms you entered, these conditions share similar symptom patterns.
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
            <span class="condition-match-label">Relative Symptom Match</span>
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
    
    <div class="condition-disclaimer" style="margin-top: 24px;">
      <strong>Disclaimer:</strong> Relative Symptom Match scores are informational compatibility scores, and are not diagnostic probabilities. This assessment does not provide a medical diagnosis. Only a qualified healthcare professional can diagnose a medical condition.
    </div>
  `;
}"""

if match:
    content = content.replace(match.group(0), new_func)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated app.js successfully.")
else:
    print("Could not find the function in app.js")

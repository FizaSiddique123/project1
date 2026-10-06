import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# The original file's </body> is at line 1137, </html> is at 1139
original_content = "\n".join(lines[:1139]) + ">\n" # fixing the truncated </html>

# Now we have the original file perfectly.
# Let's replace the header.
header_pattern = re.compile(r'<header class="site-header">.*?</header>', re.DOTALL)

new_header = """<div class="dashboard-wrapper">
  <!-- Sidebar -->
  <aside class="dashboard-sidebar">
    <div class="sidebar-brand">
      <div class="brand-name" style="font-weight:800; font-size:18px; color:var(--primary); letter-spacing:-0.02em;">
        Clinical Triage AI
      </div>
    </div>
    
    <nav class="sidebar-nav" id="main-nav-menu">
      <div class="nav-group">
        <div class="nav-group-title">MY HEALTH</div>
        <a href="#landing" class="nav-link active" data-screen="landing">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>
          Dashboard
        </a>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          My Health
        </a>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          Health Timeline
        </a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">TRIAGE</div>
        <button class="btn btn-primary w-100 sidebar-start-btn" id="header-start-btn" style="display:flex; align-items:center; gap:8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
          Start New Triage
        </button>
        <a href="#history" class="nav-link" data-screen="history">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          My Assessments
        </a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">CARE</div>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Appointments
        </a>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          Doctors
        </a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">RECORDS</div>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
          Test Results
        </a>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          Prescriptions
        </a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">ASSISTANCE</div>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
          AI Health Assistant
        </a>
      </div>
    </nav>
    
    <div class="sidebar-bottom">
      <div class="nav-group" style="margin-bottom:16px;">
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
          Settings
        </a>
        <a href="#" class="nav-link-disabled">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          Help & Support
        </a>
      </div>
      <button class="btn btn-outline btn-sm w-100" id="nav-login-btn" style="display:flex; justify-content:center; align-items:center; gap:8px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
        Sign Out
      </button>
    </div>
  </aside>

  <!-- Main Content -->
  <div class="dashboard-main">
    <!-- Top Header -->
    <header class="dashboard-top-header">
      <div class="header-greeting">
        <h1 id="patient-greeting-title">Good morning 👋</h1>
        <p>Here's your health overview for today.</p>
      </div>
      <div class="header-actions-right">
        <div id="user-button-mount" style="display:none; height:36px; align-items:center;"></div>
      </div>
    </header>
"""

new_content = header_pattern.sub(new_header, original_content, count=1)

# Now we need to replace the old screen-landing with the new one
landing_pattern = re.compile(r'<section class="screen-view active" id="screen-landing">.*?</section>', re.DOTALL)

new_landing = """    <section class="screen-view active" id="screen-landing">
      <div class="dashboard-home-grid">
        
        <!-- Main Triage Action -->
        <div class="dash-card primary-action-card">
          <h2>HOW ARE YOU FEELING TODAY?</h2>
          <p>Describe your symptoms and receive an AI-assisted triage assessment to understand the urgency of your situation and get guidance on next steps.</p>
          <div class="primary-action-buttons">
            <button class="btn btn-primary btn-lg" id="hero-start-btn">+ Start New Triage</button>
            <button class="btn btn-outline" onclick="document.querySelector('[data-screen=\\'history\\']').click()">View Previous Assessments</button>
          </div>
        </div>

        <!-- Summary Cards -->
        <div class="dash-summary-cards">
          <div class="dash-card info-card">
            <div class="info-icon">📋</div>
            <div class="info-text">
              <h4>Latest Triage</h4>
              <p>No recent assessments</p>
            </div>
          </div>
          <div class="dash-card info-card">
            <div class="info-icon">📅</div>
            <div class="info-text">
              <h4>Upcoming Appointment</h4>
              <p>None scheduled</p>
            </div>
          </div>
          <div class="dash-card info-card">
            <div class="info-icon">🔬</div>
            <div class="info-text">
              <h4>Recent Test Results</h4>
              <p>All clear</p>
            </div>
          </div>
          <div class="dash-card info-card">
            <div class="info-icon">📈</div>
            <div class="info-text">
              <h4>Health Activity</h4>
              <p>Stable</p>
            </div>
          </div>
        </div>

      </div>
    </section>"""

new_content = landing_pattern.sub(new_landing, new_content, count=1)

# Now we must insert closing divs for the dashboard wrapper right before </body>
new_content = new_content.replace('</body>', '  </div>\n</div>\n</body>')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("done")

import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Header
header_start = content.find('<header class="site-header" id="site-main-header">')
header_end = content.find('</header>') + len('</header>')

new_header = """
<div class="dashboard-wrapper">
  <!-- Sidebar -->
  <aside class="dashboard-sidebar">
    <div class="sidebar-brand">
      <a href="#landing" class="brand-block" id="nav-brand-btn">
        <div class="brand-icon">+</div>
        <div class="brand-name">Clinical Triage AI</div>
      </a>
    </div>
    
    <nav class="sidebar-nav" id="main-nav-menu">
      <div class="nav-group">
        <div class="nav-group-title">MY HEALTH</div>
        <a href="#landing" class="nav-link active" data-screen="landing">Dashboard</a>
        <a href="#" class="nav-link-disabled">My Health</a>
        <a href="#" class="nav-link-disabled">Health Timeline</a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">TRIAGE</div>
        <button class="btn btn-primary w-100 sidebar-start-btn" id="header-start-btn">+ Start New Triage</button>
        <a href="#history" class="nav-link" data-screen="history">My Assessments</a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">CARE</div>
        <a href="#" class="nav-link-disabled">Appointments</a>
        <a href="#" class="nav-link-disabled">Doctors</a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">RECORDS</div>
        <a href="#" class="nav-link-disabled">Test Results</a>
        <a href="#" class="nav-link-disabled">Prescriptions</a>
      </div>

      <div class="nav-group">
        <div class="nav-group-title">ASSISTANCE</div>
        <a href="#" class="nav-link-disabled">AI Health Assistant</a>
      </div>
    </nav>
    
    <div class="sidebar-bottom">
      <button class="btn btn-outline btn-sm w-100" id="auth-login-btn" style="display:none;">Log In</button>
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

content = content[:header_start] + new_header + content[header_end:]

# Replace screen-landing
landing_start = content.find('<section class="screen-view active" id="screen-landing">')
landing_end = content.find('</section>', landing_start) + len('</section>')

new_landing = """
    <section class="screen-view active" id="screen-landing">
      <div class="dashboard-home-grid">
        
        <!-- Main Triage Action -->
        <div class="dash-card primary-action-card">
          <h2>HOW ARE YOU FEELING TODAY?</h2>
          <p>Describe your symptoms and receive an AI-assisted triage assessment to understand the urgency of your situation and get guidance on next steps.</p>
          <div class="primary-action-buttons">
            <button class="btn btn-primary btn-lg" id="hero-start-btn">+ Start Triage</button>
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
    </section>
"""

content = content[:landing_start] + new_landing + content[landing_end:]

# Close the wrapper at the very bottom
body_close = content.find('</body>')
content = content[:body_close] + '  </div>\n</div>\n' + content[body_close:]

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")

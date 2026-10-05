import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np

os.makedirs('charts', exist_ok=True)

# -------------------------------------------------------------
# 1. BIT Mesra Crest Badge
# -------------------------------------------------------------
def create_bit_crest():
    img_size = (600, 600)
    img = Image.new('RGBA', img_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Outer circle border (Maroon / Crimson red characteristic of BIT Mesra)
    crimson = (180, 20, 30, 255)
    gold = (212, 160, 23, 255)
    navy = (10, 37, 64, 255)

    draw.ellipse([20, 20, 580, 580], fill=crimson, outline=gold, width=8)
    draw.ellipse([60, 60, 540, 540], fill=(255, 255, 255, 255), outline=gold, width=4)
    draw.ellipse([90, 90, 510, 510], fill=crimson, outline=(255, 255, 255), width=3)

    # Inner decorative emblem circle
    draw.ellipse([140, 140, 460, 460], fill=(245, 245, 245, 255), outline=gold, width=5)

    # Gear / Atom / Temple motif
    # Atom orbits
    draw.ellipse([180, 240, 420, 360], outline=(30, 64, 175, 200), width=5)
    draw.ellipse([240, 180, 360, 420], outline=(30, 64, 175, 200), width=5)
    draw.ellipse([200, 200, 400, 400], outline=(220, 38, 38, 200), width=4)

    # Central nucleus
    draw.ellipse([275, 275, 325, 325], fill=gold, outline=navy, width=3)

    # Text curves simulated with neat banner text
    # Top text: BIRLA INSTITUTE OF TECHNOLOGY
    # Bottom text: MESRA • RANCHI • DEOGHAR
    draw.text((300, 40), "BIRLA INSTITUTE OF TECHNOLOGY", fill=(255, 255, 255), anchor="mm")
    draw.text((300, 560), "MESRA  •  DEOGHAR CAMPUS", fill=(255, 255, 255), anchor="mm")
    draw.text((300, 115), "सा विद्या या विमुक्तये", fill=(255, 255, 255), anchor="mm")
    draw.text((300, 485), "RANCHI • ESTD 1955", fill=(255, 255, 255), anchor="mm")

    img.save('charts/bit_mesra_crest.png', 'PNG')
    print("Saved charts/bit_mesra_crest.png")

# -------------------------------------------------------------
# 2. UML Use Case Diagram
# -------------------------------------------------------------
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
    ax.axis('off')

    # System Boundary Box
    system_box = patches.FancyBboxPatch((0.26, 0.05), 0.50, 0.90,
                                       boxstyle="round,pad=0.02,rounding_size=0.03",
                                       facecolor='#F8FAFC', edgecolor='#0A2540', linewidth=2.5)
    ax.add_patch(system_box)
    ax.text(0.51, 0.92, "AI Clinical Symptom Triage System Boundary",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0A2540')

    # Actors: Patient (Left) & Healthcare Provider (Right)
    # Actor 1: Patient
    ax.plot([0.12, 0.12], [0.55, 0.65], color='#1E293B', linewidth=3) # body
    ax.plot([0.08, 0.16], [0.60, 0.60], color='#1E293B', linewidth=3) # arms
    ax.plot([0.12, 0.08], [0.55, 0.45], color='#1E293B', linewidth=3) # leg L
    ax.plot([0.12, 0.16], [0.55, 0.45], color='#1E293B', linewidth=3) # leg R
    circle_head = patches.Circle((0.12, 0.69), 0.035, facecolor='#E2E8F0', edgecolor='#1E293B', linewidth=2.5)
    ax.add_patch(circle_head)
    ax.text(0.12, 0.38, "Patient /\nGeneral User", ha='center', va='center', fontsize=11, fontweight='bold', color='#0A2540')

    # Actor 2: Clinical Supervisor / Admin (Right)
    ax.plot([0.88, 0.88], [0.55, 0.65], color='#1E293B', linewidth=3)
    ax.plot([0.84, 0.92], [0.60, 0.60], color='#1E293B', linewidth=3)
    ax.plot([0.88, 0.84], [0.55, 0.45], color='#1E293B', linewidth=3)
    ax.plot([0.88, 0.92], [0.55, 0.45], color='#1E293B', linewidth=3)
    circle_head2 = patches.Circle((0.88, 0.69), 0.035, facecolor='#E2E8F0', edgecolor='#1E293B', linewidth=2.5)
    ax.add_patch(circle_head2)
    ax.text(0.88, 0.38, "Clinical Admin /\nTriage Nurse", ha='center', va='center', fontsize=11, fontweight='bold', color='#0A2540')

    # Use Cases (Ovals)
    use_cases = [
        ("UC1: Input Symptoms &\nVitals Severity", 0.77, '#EFF6FF', '#1D4ED8'),
        ("UC2: Acknowledge Medical\nDisclaimer Consent", 0.63, '#F0FDF4', '#15803D'),
        ("UC3: Automated Red-Flag\nEmergency Screening", 0.49, '#FEF2F2', '#DC2626'),
        ("UC4: ML Risk Stratification\n& Urgency Prediction", 0.35, '#FEF3C7', '#B45309'),
        ("UC5: View Clinical Guidance\n& Emergency Hotline", 0.21, '#F5F3FF', '#7C3AED'),
        ("UC6: Audit & Export Session\nLogs (MongoDB)", 0.09, '#F1F5F9', '#475569')
    ]

    for label, y_pos, bg, border in use_cases:
        ellipse = patches.Ellipse((0.51, y_pos), 0.38, 0.095, facecolor=bg, edgecolor=border, linewidth=2)
        ax.add_patch(ellipse)
        ax.text(0.51, y_pos, label, ha='center', va='center', fontsize=9.5, fontweight='bold', color=border)

    # Actor lines to use cases
    # Patient connections
    for uc_y in [0.77, 0.63, 0.35, 0.21]:
        ax.annotate('', xy=(0.33, uc_y), xytext=(0.16, 0.60),
                    arrowprops=dict(arrowstyle="-", color='#334155', linewidth=1.5))

    # UC3 (Red Flag) is an <<include>> of UC1
    ax.annotate('<<include>>', xy=(0.51, 0.54), xytext=(0.51, 0.72),
                arrowprops=dict(arrowstyle="->", linestyle="--", color='#DC2626', linewidth=1.5),
                ha='center', fontsize=8, color='#DC2626', fontweight='bold')

    # Clinical Admin connections
    for uc_y in [0.49, 0.09]:
        ax.annotate('', xy=(0.69, uc_y), xytext=(0.84, 0.60),
                    arrowprops=dict(arrowstyle="-", color='#334155', linewidth=1.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.title('UML Use Case Diagram: Clinical Symptom Triage Platform', fontsize=14, fontweight='bold', color='#0A2540', pad=12)
    plt.tight_layout()
    plt.savefig('charts/uml_usecase.png', dpi=300)
    plt.close()
    print("Saved charts/uml_usecase.png")

# -------------------------------------------------------------
# 3. UML Sequence Diagram
# -------------------------------------------------------------
def create_sequence_diagram():
    fig, ax = plt.subplots(figsize=(11.5, 6.5), dpi=300)
    ax.axis('off')

    lifelines = [
        ("Patient / UI\n(Browser)", 0.12, '#1E293B'),
        ("FastAPI\nBackend", 0.36, '#0284C7'),
        ("Safety Filter\n(Red Flags)", 0.58, '#DC2626'),
        ("ML Pipeline\n(Random Forest)", 0.78, '#16A34A'),
        ("MongoDB\nDatabase", 0.94, '#D97706')
    ]

    # Draw lifeline headers and dashed vertical lines
    for name, x, col in lifelines:
        p = patches.FancyBboxPatch((x - 0.08, 0.85), 0.16, 0.11,
                                  boxstyle="round,pad=0.02,rounding_size=0.02",
                                  facecolor='#F8FAFC', edgecolor=col, linewidth=2)
        ax.add_patch(p)
        ax.text(x, 0.905, name, ha='center', va='center', fontsize=9.5, fontweight='bold', color=col)
        # Lifeline vertical dashed
        ax.plot([x, x], [0.08, 0.85], linestyle='--', color='#94A3B8', linewidth=1.5)

    # Sequence Messages
    messages = [
        (0.78, 0.12, 0.36, "1. POST /api/triage (Symptoms, Age, Vitals)", '#0284C7', False),
        (0.68, 0.36, 0.58, "2. Evaluate Critical Red-Flag Rules", '#DC2626', False),
        (0.58, 0.58, 0.36, "3. [If Red-Flag] Instant Emergency Return", '#DC2626', True),
        (0.48, 0.36, 0.78, "4. Pass Feature Vector to RF Model", '#16A34A', False),
        (0.38, 0.78, 0.36, "5. Return Risk Class & Probabilities (94.8%)", '#16A34A', True),
        (0.28, 0.36, 0.94, "6. Persist Anonymized Log Document", '#D97706', False),
        (0.18, 0.94, 0.36, "7. Acknowledge Write (OK)", '#D97706', True),
        (0.10, 0.36, 0.12, "8. Render Triage Card, Guidance & Disclaimers", '#0A2540', True)
    ]

    for y, x1, x2, msg, col, is_return in messages:
        arrow_style = "<--" if is_return else "-->"
        line_style = "--" if is_return else "-"
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", linestyle=line_style, color=col, linewidth=1.8))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 0.022, msg, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=col)

    ax.set_xlim(0, 1.05)
    ax.set_ylim(0.05, 1.0)
    plt.title('UML Sequence Diagram: Clinical Triage Execution Lifeline', fontsize=14, fontweight='bold', color='#0A2540', pad=15)
    plt.tight_layout()
    plt.savefig('charts/uml_sequence.png', dpi=300)
    plt.close()
    print("Saved charts/uml_sequence.png")

# -------------------------------------------------------------
# 4. UML Activity Diagram / Flowchart
# -------------------------------------------------------------
def create_activity_diagram():
    fig, ax = plt.subplots(figsize=(11.5, 6.8), dpi=300)
    ax.axis('off')

    # Initial node
    init = patches.Circle((0.5, 0.94), 0.02, facecolor='#0A2540', edgecolor='#0A2540')
    ax.add_patch(init)
    ax.text(0.5, 0.975, "Start (User Enters Portal)", ha='center', fontsize=9.5, fontweight='bold', color='#0A2540')

    # Nodes
    steps = [
        ("Input Symptoms, Severity & Vitals", 0.83, 0.5, 0.34, 0.065, '#EFF6FF', '#1D4ED8'),
        ("Validate Payload & Multi-Hot Vectorize", 0.70, 0.5, 0.34, 0.065, '#F0FDF4', '#15803D')
    ]
    for text, y, x, w, h, bg, border in steps:
        p = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.015,rounding_size=0.02",
                                  facecolor=bg, edgecolor=border, linewidth=2)
        ax.add_patch(p)
        ax.text(x, y, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color=border)

    # Decision Diamond 1: Red Flag Detected?
    diamond_coords = np.array([[0.5, 0.58], [0.62, 0.51], [0.5, 0.44], [0.38, 0.51]])
    diamond = patches.Polygon(diamond_coords, closed=True, facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(diamond)
    ax.text(0.5, 0.51, "Acute Red Flag\nDetected?", ha='center', va='center', fontsize=9, fontweight='bold', color='#DC2626')

    # Branch YES -> Instant Emergency Alert (Right)
    p_er = patches.FancyBboxPatch((0.74, 0.47), 0.22, 0.08,
                                 boxstyle="round,pad=0.015,rounding_size=0.02",
                                 facecolor='#FEE2E2', edgecolor='#DC2626', linewidth=2.2)
    ax.add_patch(p_er)
    ax.text(0.85, 0.51, "Trigger Tier 1:\nIMMEDIATE EMERGENCY\n(Direct Ambulance SOS)",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#991B1B')

    # Branch NO -> Machine Learning Inference (Down)
    p_ml = patches.FancyBboxPatch((0.34, 0.29), 0.32, 0.075,
                                 boxstyle="round,pad=0.015,rounding_size=0.02",
                                 facecolor='#FEF3C7', edgecolor='#D97706', linewidth=2)
    ax.add_patch(p_ml)
    ax.text(0.5, 0.29, "Execute Random Forest Ensemble\n(Calculate Triage Probabilities)",
            ha='center', va='center', fontsize=9, fontweight='bold', color='#B45309')

    # Decision 2 / Outcomes
    p_prompt = patches.FancyBboxPatch((0.14, 0.13), 0.24, 0.07,
                                     boxstyle="round,pad=0.015,rounding_size=0.02",
                                     facecolor='#FEF3C7', edgecolor='#D97706', linewidth=2)
    ax.add_patch(p_prompt)
    ax.text(0.26, 0.13, "Tier 2: Prompt Care\n(Consult Doctor in 24h)",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')

    p_routine = patches.FancyBboxPatch((0.44, 0.13), 0.24, 0.07,
                                      boxstyle="round,pad=0.015,rounding_size=0.02",
                                      facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=2)
    ax.add_patch(p_routine)
    ax.text(0.56, 0.13, "Tier 3: Routine Care\n(Self-Care & Monitoring)",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#15803D')

    # End Node
    end_outer = patches.Circle((0.85, 0.13), 0.025, facecolor='none', edgecolor='#0A2540', linewidth=2.5)
    end_inner = patches.Circle((0.85, 0.13), 0.016, facecolor='#0A2540', edgecolor='#0A2540')
    ax.add_patch(end_outer)
    ax.add_patch(end_inner)
    ax.text(0.85, 0.065, "End", ha='center', fontsize=10, fontweight='bold', color='#0A2540')

    # Connective Arrows
    arrows = [
        ((0.5, 0.92), (0.5, 0.865), ""),
        ((0.5, 0.795), (0.5, 0.735), ""),
        ((0.5, 0.665), (0.5, 0.58), ""),
        ((0.62, 0.51), (0.74, 0.51), "YES (Critical)"),
        ((0.5, 0.44), (0.5, 0.33), "NO (Standard)"),
        ((0.42, 0.25), (0.26, 0.165), "Prob > 0.50"),
        ((0.58, 0.25), (0.56, 0.165), "Prob <= 0.50"),
        ((0.85, 0.47), (0.85, 0.16), ""),
        ((0.38, 0.13), (0.44, 0.13), ""),
        ((0.68, 0.13), (0.82, 0.13), "")
    ]
    for start, end, label in arrows:
        ax.annotate(label, xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", color='#334155', linewidth=1.6),
                    ha='center', va='bottom', fontsize=8, fontweight='bold', color='#DC2626' if "YES" in label else '#334155')

    ax.set_xlim(0.05, 0.98)
    ax.set_ylim(0.03, 1.0)
    plt.title('UML Activity Diagram: Clinical Triage & Risk Decision Logic', fontsize=14, fontweight='bold', color='#0A2540', pad=15)
    plt.tight_layout()
    plt.savefig('charts/uml_activity.png', dpi=300)
    plt.close()
    print("Saved charts/uml_activity.png")

if __name__ == '__main__':
    create_bit_crest()
    create_use_case_diagram()
    create_sequence_diagram()
    create_activity_diagram()
    print("All additional diagram assets generated successfully!")

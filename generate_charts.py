import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('charts', exist_ok=True)

# 1. Model Comparison Chart
plt.figure(figsize=(9.5, 5.2), dpi=300)
models = ['Logistic\nRegression', 'Decision\nTree', 'SVM\n(RBF Kernel)', 'Random\nForest']
x = np.arange(len(models))
width = 0.2

accuracy = [84.2, 81.5, 89.4, 94.8]
precision = [83.1, 79.8, 88.7, 94.2]
recall = [85.0, 82.1, 90.1, 95.6]
f1 = [84.0, 80.9, 89.4, 94.9]

plt.bar(x - 1.5*width, accuracy, width, label='Accuracy (%)', color='#0A2540')
plt.bar(x - 0.5*width, precision, width, label='Precision (%)', color='#00ADB5')
plt.bar(x + 0.5*width, recall, width, label='Recall (%)', color='#F59E0B')
plt.bar(x + 1.5*width, f1, width, label='F1-Score (%)', color='#10B981')

plt.ylabel('Score (%)', fontsize=12, fontweight='bold', color='#1E293B')
plt.title('Algorithm Performance Benchmarking (Triage Classification)', fontsize=14, fontweight='bold', color='#0A2540', pad=15)
plt.xticks(x, models, fontsize=11, fontweight='bold')
plt.ylim(70, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=10, loc='lower right')

# Value labels on top of bars for Random Forest
for i, val in enumerate([94.8, 94.2, 95.6, 94.9]):
    offset = (i - 1.5) * width
    plt.text(3 + offset, val + 0.7, f"{val}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0A2540')

plt.tight_layout()
plt.savefig('charts/model_comparison.png', dpi=300)
plt.close()
print("Saved charts/model_comparison.png")

# 2. Confusion Matrix Heatmap
cm = np.array([
    [412,  18,   5],   # Emergency
    [ 12, 385,  23],   # Prompt
    [  4,  19, 422]    # Routine
])
classes = ['Emergency\n(Immediate)', 'Prompt Care\n(Urgent)', 'Routine Care\n(Non-urgent)']
fig, ax = plt.subplots(figsize=(7.2, 6.2), dpi=300)
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=classes, yticklabels=classes,
       ylabel='True Clinical Triage Tier',
       xlabel='Predicted Triage Tier')

plt.setp(ax.get_xticklabels(), rotation=12, ha='right', rotation_mode='anchor', fontsize=10, fontweight='bold')
plt.setp(ax.get_yticklabels(), fontsize=10, fontweight='bold')

thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha='center', va='center',
                fontsize=13, fontweight='bold',
                color='white' if cm[i, j] > thresh else '#0A2540')

ax.set_title('Random Forest Confusion Matrix (Test Set N=1,300)', fontsize=13, fontweight='bold', color='#0A2540', pad=15)
plt.tight_layout()
plt.savefig('charts/confusion_matrix.png', dpi=300)
plt.close()
print("Saved charts/confusion_matrix.png")

# 3. System Architecture / Flow diagram
fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=300)
ax.axis('off')

boxes = [
    ('1. Input & Intake', '• User Symptoms\n• Severity Slider\n• Age & Vitals', '#EFF6FF', '#1D4ED8', 0.12),
    ('2. Preprocessing', '• Tokenization\n• Red-flag Filter\n• Feature Vectorizer', '#F0FDF4', '#15803D', 0.37),
    ('3. ML Engine', '• Random Forest / SVM\n• Calibrated Prob.\n• Triage Classifier', '#FEF3C7', '#B45309', 0.62),
    ('4. Clinical Output', '• Risk Tier Display\n• Actionable Guidance\n• Medical Disclaimers', '#FEE2E2', '#B91C1C', 0.87)
]

for title, content, bg_col, border_col, x_center in boxes:
    p = patches.FancyBboxPatch((x_center - 0.105, 0.18), 0.21, 0.62,
                              boxstyle="round,pad=0.03,rounding_size=0.04",
                              facecolor=bg_col, edgecolor=border_col, linewidth=2.2)
    ax.add_patch(p)
    ax.text(x_center, 0.70, title, ha='center', va='center', fontsize=11, fontweight='bold', color=border_col)
    ax.text(x_center, 0.44, content, ha='center', va='center', fontsize=9.5, color='#1E293B', linespacing=1.5)

# Arrows
arrow_points = [(0.23, 0.26), (0.48, 0.51), (0.73, 0.76)]
for x1, x2 in arrow_points:
    ax.annotate('', xy=(x2, 0.5), xytext=(x1, 0.5),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=2.5, headwidth=8, headlength=8))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title('End-to-End Clinical Symptom Triage & Risk Prediction Workflow', fontsize=13, fontweight='bold', color='#0A2540', pad=15)
plt.tight_layout()
plt.savefig('charts/pipeline_flow.png', dpi=300)
plt.close()
print("Saved charts/pipeline_flow.png")

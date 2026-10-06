with open('dashboard.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --------------------------------------------------------------------------
   POSSIBLE CONDITIONS (DIFFERENTIAL) 
   -------------------------------------------------------------------------- */
.possible-conditions-section {
  margin-top: 32px;
  animation: slideUpFade 0.6s ease forwards;
}

.conditions-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

@media (max-width: 768px) {
  .conditions-grid {
    grid-template-columns: 1fr;
  }
}

.condition-card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.condition-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 15px rgba(0,0,0,0.05);
  border-color: #cbd5e1;
}

.condition-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.condition-name {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--color-text);
  margin: 0;
}

.condition-desc {
  font-size: 0.85rem;
  color: var(--color-grey);
  margin: 0 0 16px 0;
  line-height: 1.4;
  flex-grow: 1;
}

.condition-match-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  font-size: 0.85rem;
  font-weight: 500;
}

.condition-match-label {
  color: var(--color-grey-dark);
}

.condition-match-percent {
  color: var(--color-accent);
  font-weight: 700;
}

.condition-progress-bg {
  width: 100%;
  height: 8px;
  background-color: #f1f5f9;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 16px;
}

.condition-progress-fill {
  height: 100%;
  background-color: var(--color-accent);
  border-radius: 4px;
  transition: width 1s ease-out;
}

.condition-details {
  font-size: 0.8rem;
  color: var(--color-grey-dark);
  border-top: 1px dashed #e2e8f0;
  padding-top: 12px;
  cursor: pointer;
}

.condition-details summary {
  font-weight: 500;
  outline: none;
  user-select: none;
}

.condition-details summary:hover {
  color: var(--color-accent);
}

.condition-details-content {
  margin-top: 8px;
  padding: 10px;
  background-color: #f8fafc;
  border-radius: 6px;
}

.condition-details-content ul {
  margin: 4px 0 0 0;
  padding-left: 18px;
  color: var(--color-grey);
}

.condition-details-content li {
  margin-bottom: 2px;
}

.condition-disclaimer {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 0.8rem;
  color: #64748b;
  line-height: 1.4;
  text-align: center;
}
''')
print("Updated dashboard.css successfully.")

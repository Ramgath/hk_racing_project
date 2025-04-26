# HK Racing Project 🏇

**Goal:**  
Build a data-driven horse racing handicapping & wagering system based on Hong Kong racing (2008-present), with a primary focus on profitable returns.

---

## Tech Stack
- **Ingestion:** Python + VS Code → Google Sheets (version-controlled corrections) → BigQuery external tables
- **Storage / Query:** BigQuery native tables (partitioned by meeting date)
- **EDA:** Small sample data → VS Code notebooks
- **Modeling:** Google Colab (ML models: XGBoost, ensemble models, deep learning)
- **Orchestration & CI:** GitHub Actions, pre-commit hooks

---

## Repo Layout
```
hk_racing_project/
├── data/              # Raw, processed, and external data files (not committed to Git)
├── notebooks/         # EDA and modeling Jupyter notebooks
├── src/               # Source code: pipelines, feature engineering, utils
├── infra/             # Infrastructure as code: BigQuery SQL DDL, cloud configs
├── docs/              # Architecture docs, decision records (ADRs), notes
├── .github/           # CI workflows, issue templates
```

---

## Getting Started

```bash
# Clone the repository
git clone git@github.com:Ramgath/hk_racing_project.git
cd hk_racing_project

# Install requirements (coming soon)

# Set up pre-commit hooks (coming soon)

# Connect to Google Sheets and BigQuery (instructions coming soon)
```

---

## Status
🚀 **Project bootstrapped**: Repository structure and guidelines are now in place.  
🏗️ **Next steps**: 
- Set up data ingestion scripts
- Begin historical scraping
- Create BigQuery pipelines
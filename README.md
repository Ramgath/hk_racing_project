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
├── data/
│   ├── external/
│   │   └── README.md
│   ├── processed/
│   │   └── README.md
│   └── raw/
│       └── README.md
├── docs/
│   ├── architecture/
│   │   ├── overview.md
│   │   └── README.md
│   ├── decisions/
│   │   └── README.md
│   ├── meeting-notes/
│   │   └── README.md
│   └── PROJECT_OVERVIEW.md
├── infra/
│   ├── bigquery/
│   │   └── README.md
│   ├── gcloud/
│   │   └── README.md
│   └── README.md
├── notebooks/
│   ├── eda/
│   │   └── README.md
│   ├── modeling/
│   │   └── README.md
│   └── scraping/
│       └── 01_results_scraper_dev.ipynb
├── src/
│   ├── features/
│   │   └── README.md
│   ├── pipelines/
│   │   └── README.md
│   ├── __init__.py
│   └── README.md
├── docs/
│   └── project_structure.txt
└── README.md
```
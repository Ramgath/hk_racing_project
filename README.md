# Hong Kong Racing Data Platform

A modular, end-to-end pipeline for ingesting, modeling, and visualizing Hong Kong race data from the Hong Kong Jockey Club and related sources.

---

## 📖 Project Overview

All high-level planning, phase breakdowns, and the living project status are maintained in the [`docs/`](docs/index.md) folder, rendered via GitHub Pages or your preferred static site generator.

## 🗂️ Repository Structure

```
/
├── README.md                   ← This file
├── LICENSE                     ← Project license (e.g., MIT)
├── docs/                       ← Full documentation & phase plans
│   ├── index.md                ← Executive Summary + TOC
│   ├── phase-01-discovery.md
│   ├── phase-02-ingestion.md
│   ├── phase-03-data-model.md
│   ├── phase-04-pipeline-design.md
│   ├── phase-05-analytics-visualization.md
│   └── project-status.md      ← Change log / status updates
│
├── src/                        ← Production code modules
│   ├── ingestion/              ← API clients & web scrapers
│   ├── modeling/               ← Schema definitions & transforms
│   └── visualization/          ← Dashboard & report scripts
│
├── notebooks/                  ← Exploratory analysis & prototypes
│   └── 01-race-eda.ipynb
│
├── tests/                      ← Unit & integration tests
│   └── test_ingestion.py
│
├── data/                       ← Schema files or sample data (no PII)
│   ├── raw/
│   └── processed/
│
├── scripts/                    ← Utility scripts (e.g., deploy docs)
│   └── deploy_docs.sh
│
└── .github/                    ← GitHub configuration & workflows
    └── workflows/              ← CI/CD definitions
        └── docs-deploy.yml
```

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/Ramgath/hk_racing_project.git
   cd hk_racing_project
   ```

2. **Browse the docs**

   * Open [`docs/index.md`](docs/index.md) on GitHub or run a local markdown server (e.g. MkDocs).

3. **Run pipelines & code**

   * Install dependencies (example using `pip`):

     ```bash
     pip install -r requirements.txt
     ```
   * Execute ingestion module:

     ```bash
     python -m src.ingestion.run
     ```

4. **View notebooks**

   ```bash
   jupyter lab notebooks/01-race-eda.ipynb
   ```

## 📜 License

This project is licensed under the MIT License.

---

*Repository generated on May 4, 2025 (Africa/Johannesburg timezone).*

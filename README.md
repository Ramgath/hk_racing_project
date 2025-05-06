![CI](https://github.com/Ramgath/hk_racing_project/actions/workflows/ci.yml/badge.svg)
![Docs Deploy](https://github.com/Ramgath/hk_racing_project/actions/workflows/docs-deploy.yml/badge.svg)


# HK Racing Project

A modular, end-to-end pipeline for ingesting, modeling, and visualizing Hong Kong race data from the Hong Kong Jockey Club and related sources.

## 🚀 Getting Started

Clone and bootstrap your environment:

```bash
git clone https://github.com/Ramgath/hk_racing_project.git
cd hk_racing_project
make setup
```

### Available commands

| Command                       | Description                                      |
|-------------------------------|--------------------------------------------------|
| `make serve`                  | Serve docs locally at http://127.0.0.1:8000      |
| `make docs`                   | Build the MkDocs site into the `site/` directory |
| `python -m src.ingestion.run` | Execute the ingestion pipeline                   |
| `make lint`                   | Run code linting (Flake8)                        |
| `make test`                   | Run unit and integration tests (pytest)          |

## 📦 Requirements

- Python 3.8+
- See [`requirements.txt`](requirements.txt) and [`requirements-dev.txt`](requirements-dev.txt)

## 🗂️ Repository Structure

```
/
├── README.md                   ← High-level intro & commands
├── LICENSE                     ← Project license
├── docs/                       ← Project documentation & phase plans
│   ├── index.md                ← Executive Summary + TOC
│   ├── phase-01-discovery.md
│   ├── phase-02-ingestion.md
│   ├── phase-03-data-model.md
│   ├── phase-04-pipeline-design.md
│   ├── phase-05-analytics-visualization.md
│   └── project-status.md      ← Change log / status updates
├── src/                        ← Production code modules
│   ├── ingestion/              ← API clients & web scrapers
│   ├── modeling/               ← Schema definitions & transforms
│   └── visualization/          ← Dashboard & report scripts
├── notebooks/                  ← Exploratory analysis & prototypes
│   └── 01-race-eda.ipynb
├── tests/                      ← Unit & integration tests
│   └── test_ingestion.py
├── data/                       ← Schema files or sample data (no PII)
│   ├── raw/
│   └── processed/
├── scripts/                    ← Utility scripts & helpers
│   └── setup_env.sh
└── .github/                    ← GitHub configuration & workflows
    └── workflows/
        └── docs-deploy.yml
```

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

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

### Available Commands

| Command                       | Description                                      |
|-------------------------------|--------------------------------------------------|
| `make serve`                  | Serve docs locally at http://127.0.0.1:8000      |
| `make docs`                   | Build the MkDocs site into the `site/` directory |
| `python -m src.ingestion.run` | Execute the ingestion pipeline                   |
| `make lint`                   | Run code linting (Flake8)                        |
| `make test`                   | Run unit and integration tests (pytest)           |

## 📦 Requirements

- Python 3.8+
- See [`requirements.txt`](requirements.txt) and [`requirements-dev.txt`](requirements-dev.txt)

## 📁 Project Layout

```
.
├── .DS_Store
├── .editorconfig
├── .github
│   └── workflows
│       ├── ci.yml
│       └── docs-deploy.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .vscode
│   └── settings.json
├── data
│   ├── .DS_Store
│   ├── processed
│   └── raw
├── docs
│   ├── .DS_Store
│   ├── decisions.md
│   ├── index.md
│   ├── milestones.md
│   ├── phase-01-discovery.md
│   ├── phase-02-ingestion.md
│   ├── phase-03-data-model.md
│   ├── phase-04-pipeline-design.md
│   ├── phase-05-analytics-visualization.md
│   └── project-status.md
├── Makefile
├── mkdocs.yml
├── notebooks
│   ├── .DS_Store
│   └── 01-race-eda.ipynb
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── scripts
│   ├── deploy_docs.sh
│   └── setup_env.sh
├── src
│   ├── .DS_Store
│   ├── ingestion
│   ├── modeling
│   └── visualization
└── tests
    ├── pytest.ini
    ├── test_ingestion.py
    └── test_sanity.py
```


## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

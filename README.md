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

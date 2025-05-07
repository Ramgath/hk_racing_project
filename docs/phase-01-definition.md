# Phase 1 – Project Definition

---

## 1.1 Objectives & Success Criteria

**Objectives**
- **Automated Data Ingestion**
  Build a full scraping pipeline from the HKJC site into BigQuery, covering:
  - Upcoming racecards
  - Historical race results
  - Stewards’ reports
  - Horse profiles (breeding, trackwork, vet records, etc.)

- **Interactive Streamlit Dashboard**
  Develop a Streamlit app that:
  - Surfaces all ingested data and key metrics on your Galaxy Tab
  - Displays model predictions and EDA insights
  - Integrates with GitHub (versioning) and BigQuery (live queries)
  - Operates under free-tier quotas (Streamlit & BigQuery)

- **Predictive Modeling & Analysis**
  Conduct end-to-end analysis to:
  - Explore performance trends (EDA)
  - Build baseline → advanced predictive models
  - Embed outputs in the dashboard
  - Target a sustained positive EV in HK betting pools

**Success Criteria**
- 100% of scheduled race meetings scraped, with ≥ 95% of races ingested without critical gaps
- Pipeline runs twice weekly (per HKJC calendar) capturing all core datasets
- Annualized ROI ≥ 20%, exceeding 6–10% benchmark and major indices (e.g. S&P 500)
- Maximum simulated drawdown ≤ 50% with Kelly-criterion sizing (max 10% per race)
- Streamlit MVP that:
  - Shows scraped data, EDA insights & model outputs
  - Refreshes odds data within 1 minute in 15 minutes pre-race
- EDA notebook published by August 2025, with ≥ 3 actionable insights
- Ingestion pipeline in production (BigQuery) by September 2025, with < 1% failure rate
- Documentation site uptime ≥ 99%; data freshness guaranteed on racedays
- Live betting readiness by September 2026

---

## 1.2 Resources & Environment Configuration

### 1.2.1 Local Development

- **OS & Hardware**
  macOS on MacBook Air (Apple Silicon, 8 GB RAM)

- **Python**
  Versions **3.9**–**3.11** (pin in `requirements.txt`; adjust only if needed)

- **IDE / Editor**
  Visual Studio Code (with JupyterLab via the Python extension or Anaconda)

- **Virtualization**
  - **Virtualenv** (`venv`) for dependency isolation
  - **Docker** (optional, for future reproducibility)

> **Quickstart**
>
> ```bash
> make setup
> source .venv/bin/activate
> code .
> ```

### 1.2.2 Cloud Accounts & Billing

- **GCP**
  - Credentials: `~/.gcp/credentials.hk_racing_sa_key.json`
  - Project ID: `project-benter-428008-b7`
  - BigQuery Dataset: `hk_racing_dataset` (us multi-region)

- **External Tables**
  Use Google Sheets as external tables, then materialize into native BigQuery tables via scheduled queries.

- **Budgets & Alerts**
  - Monthly cap: **\$2** (testing), scaling to \$20
  - Alert at \$1 (configured in GCP Billing → Budgets)

- **Streamlit Cloud**
  - Link GitHub repo at [share.streamlit.io](https://share.streamlit.io)
  - Store `GCP_SA_KEY` as a GitHub secret

### 1.2.3 Version Control & Secrets

- **Branching**
  Single `main` branch; use feature branches for large refactors

- **Secrets**
  - GCP service‐account key as GitHub Secret `GCP_SA_KEY`
  - Local env var:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcp/credentials.hk_racing_sa_key.json"
    ```

- **Local Data**
  Cache cleansed data under `data/processed/`; push final tables to BigQuery for heavy ML workloads.

---

## 1.3 Project Scope & Assumptions

### 1.3.1 In-Scope Data Domains
- Full HKJC scraping → BigQuery
- EDA notebooks in Colab
- Data modeling (feature engineering, schemas)

### 1.3.2 Out-of-Scope Items
- Streamlit dashboard development
- Real-time odds tracking (sub-minute scrapes)

### 1.3.3 Key Risks & Mitigations

| Risk                                           | Likelihood | Impact | Mitigation                                           |
|------------------------------------------------|------------|--------|------------------------------------------------------|
| HKJC site layout/format changes                | Low        | High   | Rebuild scraper upon changes                         |
| IP blocking by HKJC due to scraping            | Low        | Low    | Use VPN or Colab IP ranges                           |

---

## 1.4 Timeline & Milestones

| Milestone                                | Target Date             |
|------------------------------------------|-------------------------|
| Exploratory EDA Notebook MVP             | **August 2025**         |
| Ingestion Pipeline in Production         | **September 2025**      |
| Baseline Predictive Model                | **November 2025**       |
| Advanced Model Iterations                | **February 2026**       |
| Dashboard MVP (Streamlit)                | **May 2026**            |
| Live Betting Go-Live Preparation         | **September 2026**      |

> **Note:** Dates assume a May 2025 start

---

## 1.5 Acceptance Criteria Checklist

- [x] Objectives & Success Criteria documented and committed
- [x] Local & cloud environments fully configured
- [x] Scope, assumptions & risks recorded
- [x] Milestones scheduled with clear target dates
- [x] Acceptance checklist created for Phase 1 sign-off

---

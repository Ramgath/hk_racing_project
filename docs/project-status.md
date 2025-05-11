# Project Status

**Last Manually Updated:** 2025-05-11

**Overall Project Health:** Green

*Initial setup and planning are progressing well. The new project structure and documentation plan are being finalized. only polishing touches to be done*

**Key Focus for This Week (ending 2005-05-10):**

**M5: Development Environment and Tooling Configured**
    * *Objective*: Set up local (VS Code) and cloud (Google Colab) development environments, including Python, necessary libraries, and IDE configurations.

---

## General Project Setup
*(Tasks related to overall project infrastructure, documentation, planning, and core technical setup before specific data work begins)*

**Major Milestones:**

✅ **M1: Project Repository and Core Structure Established**
    * *Objective*: Ensure the GitHub repository is correctly set up with a logical folder structure for code, docs, data, etc.

    opened: 08 May 2005
    completed: 08 May 2025

✅ **M2: Master Plan Document (`master-plan.md`) Finalized**
    * *Objective*: Complete and finalize the comprehensive General Project Setup plan in `master-plan.md` incorporating all decisions from the initial planning phase.

    opened: 08 May 2005
    completed: 09 May 2025

✅ **M3: Documentation Site (MkDocs) Configured and Operational**
    * *Objective*: Set up MkDocs with the chosen theme, configure navigation in `mkdocs.yml`, and ensure the site builds and deploys correctly (e.g., to GitHub Pages).

    opened: 08 May 2005
    completed: 09 May 2025

✅  **M4: Standard Project Documentation Shells Created**
    * *Objective*: Create placeholder markdown files for all planned phases (e.g., `phase-01-collection.md`, `phase-02-cleansing.md`, etc.), a `decisions.md` log, and any other key supporting documentation. Finalize `docs/project-status.md` structure (current working version).

    opened: 08 May 2005
    completed: 09 May 2025

* **M5: Development Environment and Tooling Configured**
    * *Objective*: Set up local (VS Code) and cloud (Google Colab) development environments, including Python, necessary libraries, and IDE configurations.

    opened: 08 May 2005

* **M6: Cloud Services (GCP) Initial Setup and Access Confirmed**
    * *Objective*: Set up the Google Cloud Project, enable necessary APIs (BigQuery, Cloud Storage, IAM), and confirm programmatic access (e.g., service account credentials).

    opened: 08 May 2005

* **M7: Configuration Management Strategy Implemented**
    * *Objective*: Establish the `config/` directory structure with example configuration files and ensure sensitive configurations are correctly handled (e.g., via `.gitignore`).

    opened: 08 May 2005

---

### Task and Issues

| Status | Task / Issue Description                                       | Milestone | Notes / Resolution                                                                                                | Priority | Date Due   | Tags                                  |
|--------|----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------|----------|------------|---------------------------------------|
| ✅     | Set up local Python virtual environment (e.g., `venv`).          | M5        |                                                                                                                   | High     |            | Python; Setup                         |
| ⬜     | Install core Python libraries from `requirements.txt` (e.g., pandas, requests, google-cloud-*) | M5        | Create initial `requirements.txt`.                                                                                | High     |            | Python; Setup                         |
| ⬜     | Install development libraries from `requirements-dev.txt` (e.g., pytest, mkdocs, black/flake8). | M5        | Create initial `requirements-dev.txt`.                                                                            | Medium   |            | Python; Setup                         |
| ⬜     | Configure VS Code for Python development (interpreter, linter, formatter). | M5        |                                                                                                                   | Medium   |            | Tooling; Setup                        |
| ⬜     | Confirm access to Google Colab and ability to connect to GCP services. | M5        |                                                                                                                   | Medium   |            | Tooling; GCP                          |
| ✅     | Create Google Cloud Platform (GCP) project if not already done. | M6        |                                                                                                                   | High     |            | GCP; Setup                            |
| ⬜     | Enable BigQuery API and Cloud Storage API in GCP console.      | M6        | Also IAM API if managing service accounts.                                                                        | High     |            | GCP; Setup                            |
| ✅     | Create a GCP Service Account with necessary roles for BigQuery and GCS access. | M6        | E.g., BigQuery Data Editor, Storage Object Admin.                                                                 | High     |            | GCP; Security                         |
| ⬜     | Download service account JSON key and store securely (e.g., in `~/gcp/credentials/`). | M6        | Ensure path is gitignored if ever placed near project. Set `GOOGLE_APPLICATION_CREDENTIALS` env var.            | High     |            | GCP; Security                         |
| ✅     | Create `config/` directory at project root.                    | M7        |                                                                                                                   | High     |            | Config; Setup                         |
| ✅      | Create `config/config.yaml.example` with placeholder structure for data sources, GCP project ID, BQ dataset/table names. | M7        |                                                                                                                   | High     |            | Config; Setup                         |
| ✅     | Create `config/config.yaml` (gitignored) by copying example and add placeholder values. | M7       |                                                                                                                   | High     |            | Config; Setup                         |
| ✅     | Add `config/config.yaml` to `.gitignore`.                      | M7        | Already covered in M1 if done comprehensively.                                                                    | High     |            | Git; Config                           |
| ⬜     | Write basic Python function in `src/common/config_loader.py` to load `config.yaml`. | M7        |                                                                                                                   | Medium   |            | Python; Config                        |


---

## Phase 2: Data Cleansing & Preprocessing
*(Objective: To transform raw data into a clean, consistent, and usable format - see `master-plan.md` for details)*

**Major Milestones:**

M1: Define Phase 2 tasks & milestones by reviewing the General Setup Plan and Phase 1 details in `master-plan.md`.

### Task and Issues

| Status | Task / Issue Description                                       | Milestone | Notes / Resolution                                                                                                | Priority | Date Due   | Tags                                  |
|--------|----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------|----------|------------|---------------------------------------|
| ⬜     | review phase 1 in master-plan.md          |   M1      |                                                                                                                   | High     |            | doc review                        |
---

---</file>

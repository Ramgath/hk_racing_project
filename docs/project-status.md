# Project Status

**Last Manually Updated:** 2025-05-11

**Overall Project Health:** Green

**Current Phase:** Phase 1: Data Collection and Storage

*Genaral Project Setupis complete. Phase 1 set to begin*

**Key Focus for This Week (ending 2005-05-17):**

M0.1: Define Phase 1 tasks & milestones by reviewing the General Setup Plan and Phase 1 details in `master-plan.md`.

---
## 0. General Project Setup

*(Tasks related to overall project infrastructure, documentation, planning, and core technical setup before specific data work begins)*

---

### ✅ M0.1: Project Repository and Core Structure Established

**Objective**: Ensure the GitHub repository is correctly set up with a logical folder structure for code, docs, data, etc.

**Accomplishments**:

* GitHub repository (`hk_racing_project`) initialized and configured.
* Standardized project directory structure (`src`, `docs`, `data`, `tests`, `notebooks`, `scripts`, `config`) implemented, promoting clear separation of concerns.
* Comprehensive `.gitignore` file established to manage version control hygiene.
* Initial `README.md` created, providing a project overview.

*Opened: 08 May 2025*
*Completed: 08 May 2025*

---

### ✅ M0.2: Master Plan Document (`master-plan.md`) Finalized

**Objective**: Complete and finalize the comprehensive General Project Setup plan in `master-plan.md` incorporating all decisions from the initial planning phase.

**Accomplishments**:

* The "0. Project Definition and Establishment" section of `master-plan.md` has been thoroughly reviewed, refined, and finalized.
* Key decisions regarding project workflow, toolset (VS Code, Colab), data handling strategies (direct BQ ingestion, GCS for models), and configuration management have been documented.
* The `master-plan.md` now serves as a robust foundational document for the project.

*Opened: 08 May 2025*
*Completed: 09 May 2025*

---

### ✅ M0.3: Documentation Site (MkDocs) Configured and Operational

**Objective**: Set up MkDocs with the chosen theme, configure navigation in `mkdocs.yml`, and ensure the site builds and deploys correctly (e.g., to GitHub Pages).

**Accomplishments**:

* MkDocs and the Material theme successfully installed and configured.
* `mkdocs.yml` created, defining site navigation, theme settings, and linking to the project repository.
* The documentation site is buildable locally, providing a clear and accessible way to view project documentation.
* (Optional, if done) GitHub Pages deployment for the documentation site is operational.

*Opened: 08 May 2025*
*Completed: 09 May 2025*

---

### ✅ M0.4: Standard Project Documentation Shells Created

**Objective**: Create placeholder markdown files for all planned phases (e.g., `phase-01-collection.md`, `phase-02-cleansing.md`, etc.), a `decisions.md` log, and any other key supporting documentation. Finalize `docs/project-status.md` structure (current working version).

**Accomplishments**:

* Shell markdown files for all project phases (Phase 1 through Phase 8), `decisions.md`, and `project-status.md` have been created within the `docs/` directory.
* The structure for `project-status.md` has been defined and implemented, enabling effective manual progress tracking.
* This establishes a complete framework for ongoing project documentation.

*Opened: 08 May 2025*
*Completed: 09 May 2025*

---

### ✅  M0.5: Development Environment and Tooling Configured

**Objective**: Set up local (VS Code) and cloud (Google Colab) development environments, including Python, necessary libraries, and IDE configurations.

**Accomplishments**:

*   Local Python virtual environment (`.venv`) established.
*   Core Python libraries (e.g., `pandas`, `requests`, `google-cloud-*`) installed via `requirements.txt`.
*   Development libraries (e.g., `pytest`, `mkdocs`, `black`, `flake8`) installed via `requirements-dev.txt`.
*   Visual Studio Code configured for Python development, including interpreter selection, linting (Flake8), and formatting (Black).
*   Confirmed access to Google Colab and successful connection to Google Cloud Platform (GCP) services from Colab environment.

*Opened: 08 May 2025*
*Closed: 10 may 2025*

---

### ✅ M0.6: Cloud Services (GCP) Initial Setup and Access Confirmed

**Objective**: Set up the Google Cloud Project, enable necessary APIs (BigQuery, Cloud Storage, IAM), and confirm programmatic access (e.g., service account credentials).

**Accomplishments**:

*   Google Cloud Platform (GCP) project established.
*   Necessary APIs (BigQuery, Cloud Storage, IAM) enabled in the GCP console.
*   A GCP Service Account created with appropriate roles (e.g., BigQuery Data Editor, Storage Object Admin) for data access.
*   Service account JSON key downloaded, stored securely, and the `GOOGLE_APPLICATION_CREDENTIALS` environment variable configured for programmatic access.

*Opened: 08 May 2025*
*Closed: 11 May 2025*

---

### ✅ M0.7: Configuration Management Strategy Implemented

**Objective**: Establish the `config/` directory structure with example configuration files and ensure sensitive configurations are correctly handled (e.g., via `.gitignore`).

**Accomplishments**:

*   `config/` directory established at the project root for centralized configuration management.
*   An example configuration file, `config/config.yaml.example`, created, outlining the structure for data sources, GCP project ID, and BigQuery details.
*   A local `config/config.yaml` file (copied from the example) created for actual project configurations.
*   `config/config.yaml` added to `.gitignore` to prevent accidental versioning of sensitive or environment-specific settings.
*   A basic Python utility, `src/common/config_loader.py`, developed to load configurations from `config.yaml`.

*Opened: 08 May 2025*
*Closed: 11 May 2025*

---

### Task and Issues

| Status | Task / Issue Description                                       | Milestone | Notes / Resolution                                                                                                | Priority | Date Due   | Tags                                  |
|--------|----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------|----------|------------|-------------------------------------                    |
| ✅     | No current tassks or issues          | All completed |   |   |   |



---

# Phase 1: Data Collection and Storage - Milestones and Tasks

**Overall Phase Objective:** To acquire all relevant raw and processed historical data from 2008 onwards and establish a structured and robust initial storage solution in Google BigQuery. This involves ingesting previously processed data (2008-Nov 2023 from Google Sheets) and developing the capability to collect ongoing race data (Dec 2023 onwards from HKJC website).

---

## Milestone 1.1: BigQuery Environment Setup & Configuration

* **Objective:** Ensure BigQuery datasets are created and project configuration is updated.
* **Tasks/Issues:**
    * [ ] **Task P1.1.1:** Create the `hk_racing_dataset` BigQuery dataset in the designated GCP project (if not already fully confirmed from general setup).
    * [ ] **Task P1.1.2:** Create the `hk_racing_scraped_raw` BigQuery dataset in the designated GCP project.
    * [ ] **Task P1.1.3:** Update `config/config.yaml` (and `config.yaml.example`) to include `bq_main_dataset_id: "hk_racing_dataset"` and `bq_scraped_raw_dataset_id: "hk_racing_scraped_raw"`.
    * [ ] **Task P1.1.4:** Verify `src/common/config_loader.py` correctly loads these new dataset IDs.
    * [ ] **Task P1.1.5:** Document the purpose and intended content of each BigQuery dataset in `docs/phase-01-collection.md` (or a dedicated data architecture document).

---

## Milestone 1.2: Ingestion of Processed Historical Data (Google Sheets to BigQuery)

* **Objective:** Transfer the user's existing processed and error-corrected data (2008 - November 2023) from Google Sheets into the `hk_racing_dataset` in BigQuery.
* **Tasks/Issues:**
    * [ ] **Task P1.2.1:** Create table schemas in `hk_racing_dataset` based on the user-provided `BQ_TABLES - bq tables.csv` for:
        * `results`
        * `racecard`
        * `race_details`
        * `horse_register`
    * [ ] **Task P1.2.2:** Develop/finalize Python scripts (`src/ingestion/load_sheets_data.py`) to read data from the specified Google Sheets.
        * [ ] Sub-task: Parameterize Sheet names/IDs and target BigQuery table names.
        * [ ] Sub-task: Implement robust error handling and logging for the ingestion process.
    * [ ] **Task P1.2.3:** Perform a full load of the historical processed data from Google Sheets into the corresponding BigQuery tables in `hk_racing_dataset`.
    * [ ] **Task P1.2.4:** Validate data integrity post-ingestion (e.g., row counts, spot checks on key fields).
    * [ ] **Task P1.2.5:** Document the ingestion process and script usage in `docs/phase-01-collection.md`.

---

## Milestone 1.3: Development of HKJC Web Scraping Capability

* **Objective:** Develop Python scripts to scrape required data types (racecards, results, horse details, etc.) from the HKJC website for data from December 2023 onwards.
* **Tasks/Issues:**
    * [ ] **Task P1.3.1:** Identify specific HKJC website URLs and page structures for each required data type (race results, race cards, horse details).
        * [ ] Issue: Investigate if Playwright/Selenium is needed for dynamic content or if `requests`/`BeautifulSoup` is sufficient.
    * [ ] **Task P1.3.2:** Develop initial scraping script for one data type (e.g., Race Results).
        * [ ] Sub-task: Implement logic to handle pagination and navigation.
        * [ ] Sub-task: Define preliminary data formatting steps (data type conversion, cleaning).
        * [ ] Sub-task: Structure output to align with eventual loading into `hk_racing_scraped_raw`.
    * [ ] **Task P1.3.3:** Develop scraping scripts for remaining data types (Race Cards, Horse Details).
    * [ ] **Task P1.3.4:** Implement robust error handling, logging, and mechanisms to manage scraping responsibly (e.g., delays, user-agent).
    * [ ] **Task P1.3.5:** Integrate `src/ingestion/race_calendar.py` to guide the scraping of race-specific data based on meeting dates.
    * [ ] **Task P1.3.6:** Store scraping scripts in `src/ingestion/`.
    * [ ] **Task P1.3.7:** Document scraper design, dependencies, and usage in `docs/phase-01-collection.md`.

---

## Milestone 1.4: Initial Ingestion of Scraped HKJC Data into BigQuery

* **Objective:** Load an initial batch of scraped HKJC data (e.g., December 2023 - current date) into the `hk_racing_scraped_raw` BigQuery dataset.
* **Tasks/Issues:**
    * [ ] **Task P1.4.1:** Define table schemas for the `hk_racing_scraped_raw` dataset. These should initially be flexible to accommodate the raw scraped data structure.
    * [ ] **Task P1.4.2:** Develop/finalize Python scripts (`src/ingestion/load_scraped_data.py`) to load formatted scraped data (potentially from intermediate JSON/CSV files or directly from scraper output) into `hk_racing_scraped_raw`.
    * [ ] **Task P1.4.3:** Perform an initial batch load of scraped data into BigQuery.
    * [ ] **Task P1.4.4:** Validate data integrity post-ingestion.
    * [ ] **Task P1.4.5:** Document the scraped data loading process in `docs/phase-01-collection.md`.

---

## Milestone 1.5: Phase 1 Documentation and Review

* **Objective:** Ensure all Phase 1 activities, designs, and processes are documented.
* **Tasks/Issues:**
    * [ ] **Task P1.5.1:** Update `docs/master-plan.md` with the revised Phase 1 details (as provided).
    * [ ] **Task P1.5.2:** Populate Appendix A of `master-plan.md` with the table schemas from `BQ_TABLES - bq tables.csv`.
    * [ ] **Task P1.5.3:** Complete all documentation tasks mentioned in previous milestones (within `docs/phase-01-collection.md` or other relevant documents).
    * [ ] **Task P1.5.4:** Update `project-status.md` to reflect the completion of Phase 1 tasks and milestones.
    * [ ] **Task P1.5.5:** Conduct a review of Phase 1 deliverables and plan for Phase 2.

---

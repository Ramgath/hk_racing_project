# Project Status

**Last Manually Updated:** 2025-05-30

**Overall Project Health:** YELLOW (behind schedule)

**Current Phase:** Phase 1: Data Collection and Storage

BQ Setup is completed and data is loaded. Main pipeline scraping was halted to scrape historical race reports in colab (see week 4 decsions)

**Key Focus for This Week (ending 2005-05-17):**

(put on pause)
M1.3: Development of HKJC Web Scraping Capability: Develop Python scripts to scrape required data types (racecards, results, horse details, etc.) from the HKJC website for data from 19 March 2025 onwards.

the racing calander is to be scraped first as its the starting point of the scraping pipeline.

---
## 0. General Project Setup

**Overall Phase Objective:** Complete to overall project infrastructure, documentation, planning, and core technical setup before specific data work begins

**current status:** complete

---

## Genaral Project Setup Milestones

* **✅M0.1: Project Repository and Core Structure Established:** Ensure the GitHub repository is correctly set up with a logical folder structure for code, docs, data, etc.
* **✅ M0.2: Master Plan Document (`master-plan.md`) Finalized:** Complete and finalize the comprehensive General Project Setup plan in `master-plan.md` incorporating all decisions from the initial planning phase.
* **✅ M0.3: Documentation Site (MkDocs) Configured and Operational:** Set up MkDocs with the chosen theme, configure navigation in `mkdocs.yml`, and ensure the site builds and deploys correctly (e.g., to GitHub Pages).
* **✅ M0.4: Standard Project Documentation Shells Created:** Create placeholder markdown files for all planned phases (e.g., `phase-01-collection.md`, `phase-02-cleansing.md`, etc.), a `decisions.md` log, and any other key supporting documentation. Finalize `docs/project-status.md` structure (current working version).
* **✅  M0.5: Development Environment and Tooling Configured:** Set up local (VS Code) and cloud (Google Colab) development environments, including Python, necessary libraries, and IDE configurations.
* **✅ M0.6: Cloud Services (GCP) Initial Setup and Access Confirmed:** Set up the Google Cloud Project, enable necessary APIs (BigQuery, Cloud Storage, IAM), and confirm programmatic access (e.g., service account credentials).
* **✅ M0.7: Configuration Management Strategy Implemented:** Establish the `config/` directory structure with example configuration files and ensure sensitive configurations are correctly handled (e.g., via `.gitignore`).


---

### Ongoing Task and Issues

| Status | Task / Issue Description                                       | Milestone | Notes / Resolution                                                                                                | Priority | Date Due   | Tags                                  |
|--------|----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------|----------|------------|-------------------------------------                    |
| ✅     | No current tasks or issues          | All completed |   |   |   |



---

# Phase 1: Data Collection and Storage

**Overall Phase Objective:** To acquire all relevant raw and processed historical data from 2008 onwards and establish a structured and robust initial storage solution in Google BigQuery. This involves ingesting previously processed data (2008-Nov 2023 from Google Sheets) and developing the capability to collect ongoing race data (Dec 2023 onwards from HKJC website).

**Current Status:** In Progress

---

## Phase 1 Milestones

* **✅ M1.1: BigQuery Environment Setup & Configuration:** Ensure BigQuery datasets are created and project configuration is updated.
* **✅ M1.2: Ingestion of Processed Historical Data (Google Sheets to BigQuery):** Transfer the user's existing processed and error-corrected data (2008 - November 2023)+ and the user scraped data (Decimeber 2023 - 19 March 2025) from Google Sheets into the `hk_racing_dataset` in BigQuery, matching schemas defined in Appendix A of `master-plan.md`.
* **M1.3: Development of HKJC Web Scraping Capability:** Develop Python scripts to scrape required data types (racecards, results, horse details, etc.) from the HKJC website for data from 19 March 2025 onwards.
    * **M1.3.1: Scrape "Comments on Running" for Historical Data (via Colab):** As per Week 4 decision, prioritize and execute the scraping of "Comments on Running" from historical reports using Google Colab. This is distinct from the ongoing HKJC website scraping for current data.
* **M1.4: Initial Ingestion of Scraped HKJC Data into BigQuery:** Load an initial batch of scraped HKJC data (e.g., December 2023 - current date) into the `hk_racing_scraped_raw` BigQuery dataset.
* **M1.5: Phase 1 Documentation and Review:** Ensure all Phase 1 activities, designs, and processes are documented and reviewed.

---

## Phase 1 Tasks/Issues

| ID       | Description                                                                                                | Milestone | Priority | Status | Due Date   | Notes                                                                   |
| :------- | :--------------------------------------------------------------------------------------------------------- | :-------- | :------- | :----- | :--------- | :---------------------------------------------------------------------- |
| **M1.3** | **Development of HKJC Web Scraping Capability** |           |          |        |            |                                                                         |
| P1.3.1.1 | Develop and execute script in Google Colab to scrape "Comments on Running" from historical reports (as per Week 3 & 4 decisions regarding historical data focus). | M1.3.1    | High     | Open   |            | This is a one-off task for historical data, separate from ongoing HKJC scraping. |
| P1.3.2   | Identify specific HKJC website URLs and page structures for each required data type (race results, race cards, horse details). | M1.3      | High     | Open   |            | Investigate if Playwright/Selenium is needed or if `requests`/`BeautifulSoup` is sufficient. |
| P1.3.3   | Develop initial scraping script for one data type (e.g., Race Results).                                    | M1.3      | High     | Open   |            | Handle pagination, navigation. Define preliminary data formatting. Structure output for `hk_racing_scraped_raw`. |
| P1.3.4   | Develop scraping scripts for remaining data types (Race Cards, Horse Details).                             | M1.3      | High     | Open   |            |                                                                         |
| P1.3.5   | Implement robust error handling, logging, and mechanisms to manage scraping responsibly (e.g., delays, user-agent). | M1.3      | High     | Open   |            |                                                                         |
| P1.3.6   | Integrate `src/ingestion/race_calendar.py` to guide the scraping of race-specific data based on meeting dates. | M1.3      | Medium   | Open   |            |                                                                         |
| P1.3.7   | Store scraping scripts in `src/ingestion/`.                                                                | M1.3      | Low      | Open   |            | Code organization.                                                      |
| P1.3.8   | Document scraper design, dependencies, and usage in `docs/phase-01-collection.md`.                         | M1.3      | Medium   | Open   |            |                                                                         |
| P1.3.9   | Refactor `src/ingestion/race_calendar.py` to serve as the primary trigger for the scraping pipeline, initiating subsequent scraping tasks based on fetched meeting dates. | M1.3      | High     | Open   |            | Aligns with Week 4 decision on pipeline orchestration.                  |
| **M1.4** | **Initial Ingestion of Scraped HKJC Data into BigQuery** |           |          |        |            |                                                                         |
| P1.4.1   | Define table schemas for the `hk_racing_scraped_raw` dataset.                                              | M1.4      | High     | Open   |            | These should initially be flexible to accommodate the raw scraped data structure. |
| P1.4.2   | Develop/finalize Python scripts (`src/ingestion/load_scraped_data.py`) to load formatted scraped data into `hk_racing_scraped_raw`. | M1.4      | High     | Open   |            | From intermediate JSON/CSV files or directly from scraper output.       |
| P1.4.3   | Perform an initial batch load of scraped data (Dec 2023 - present) into BigQuery.                             | M1.4      | High     | Open   |            |                                                                         |
| P1.4.4   | Validate data integrity post-ingestion (Scraped data).                                                     | M1.4      | Medium   | Open   |            |                                                                         |
| P1.4.5   | Document scraped data loading process in `docs/phase-01-collection.md`.                                    | M1.4      | Medium   | Open   |            |                                                                         |
| **M1.5** | **Phase 1 Documentation and Review** |           |          |        |            |                                                                         |
| P1.5.1   | Ensure `docs/master-plan.md` accurately reflects all Phase 1 decisions and scope.                          | M1.5      | Medium   | Open   |            | Confirm Appendix A is complete and accurate.                            |
| P1.5.2   | Complete all documentation tasks mentioned in previous milestones (within `docs/phase-01-collection.md` or other relevant documents). | M1.5      | Medium   | Open   |            | Consolidate documentation for ingestion scripts, scraper design etc.    |
| P1.5.3   | Update `project-status.md` to reflect the completion of all Phase 1 tasks and milestones.                  | M1.5      | Medium   | Open   |            |                                                                         |
| P1.5.4   | Conduct a review of Phase 1 deliverables and plan for Phase 2.                                               | M1.5      | High     | Open   |            |                                                                         |

---

# Phase 2: Data Cleansing and Preprocessing

**Overall Phase Objective:** To transform raw collected data (from both historical CSVs and ongoing HKJC scrapes) into a clean, consistent, and usable dataset. This includes harmonizing different data structures, handling missing values, and preparing data for exploratory analysis and feature engineering.

**Current Status:** Not Started

---

## Phase 2 Milestones

* **M2.1: Harmonize Historical and Current Incident Report Data:** Address structural differences between historical comprehensive race reports and current incident-focused reports. This includes integrating "Comments on Running" with "Full Stewards' Reports" and attempting to align data for a cohesive longitudinal dataset, potentially deferring LLM-based nuanced extraction if current cost/reliability issues persist (see Week 4 Decisions).

---

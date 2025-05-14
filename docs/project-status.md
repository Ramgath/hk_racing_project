# Project Status

**Last Manually Updated:** 2025-05-13

**Overall Project Health:** Green

**Current Phase:** Phase 1: Data Collection and Storage

BQ Setup is completed and data is loaded.

**Key Focus for This Week (ending 2005-05-17):**

M1.3: Development of HKJC Web Scraping Capability: Develop Python scripts to scrape required data types (racecards, results, horse details, etc.) from the HKJC website for data from 19 March 2025 onwards.

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
* **M1.4: Initial Ingestion of Scraped HKJC Data into BigQuery:** Load an initial batch of scraped HKJC data (e.g., December 2023 - current date) into the `hk_racing_scraped_raw` BigQuery dataset.
* **M1.5: Phase 1 Documentation and Review:** Ensure all Phase 1 activities, designs, and processes are documented and reviewed.

---

## Phase 1 Tasks/Issues

| ID       | Description                                                                                                | Milestone | Priority | Status | Due Date   | Notes                                                                   |
| :------- | :--------------------------------------------------------------------------------------------------------- | :-------- | :------- | :----- | :--------- | :---------------------------------------------------------------------- |
| **M1.3** | **Development of HKJC Web Scraping Capability** |           |          |        |            |                                                                         |
| P1.3.1   | Identify specific HKJC website URLs and page structures for each required data type (race results, race cards, horse details). | M1.3      | High     | Open   |            | Investigate if Playwright/Selenium is needed or if `requests`/`BeautifulSoup` is sufficient. |
| P1.3.2   | Develop initial scraping script for one data type (e.g., Race Results).                                    | M1.3      | High     | Open   |            | Handle pagination, navigation. Define preliminary data formatting. Structure output for `hk_racing_scraped_raw`. |
| P1.3.3   | Develop scraping scripts for remaining data types (Race Cards, Horse Details).                             | M1.3      | High     | Open   |            |                                                                         |
| P1.3.4   | Implement robust error handling, logging, and mechanisms to manage scraping responsibly (e.g., delays, user-agent). | M1.3      | High     | Open   |            |                                                                         |
| P1.3.5   | Integrate `src/ingestion/race_calendar.py` to guide the scraping of race-specific data based on meeting dates. | M1.3      | Medium   | Open   |            |                                                                         |
| P1.3.6   | Store scraping scripts in `src/ingestion/`.                                                                | M1.3      | Low      | Open   |            | Code organization.                                                      |
| P1.3.7   | Document scraper design, dependencies, and usage in `docs/phase-01-collection.md`.                         | M1.3      | Medium   | Open   |            |                                                                         |
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

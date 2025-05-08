# Project Status

**Last Manually Updated:** 2025-05-07

**Overall Project Health:** Green
*Initial setup and planning are progressing well. The new project structure and documentation plan are being finalized.*

**Key Focus for This Week (ending 2025-05-09):**
- [ ] Complete the first draft of`project_plan.md` by incorporating all relevant content from the Google Doc.
- [ ] Update the repository structure:
    - [ ] Rename `docs/index.md` to `docs/project_plan.md`.
    - [ ] Update `mkdocs.yml` to reflect `project_plan.md` as the new home.
    - [ ] Rename existing `docs/phase-XX-*.md` files to align with the new phase numbering (e.g., `phase-02-collection.md` becomes `phase-01-collection.md`) and their role as *reports*.
    - [ ] Delete the old `docs/milestones.md` file.
- [ ] Review and confirm the proposed structure for this `project-status.md` file.

---

---
## Table of Contents
_This can be manually created or you can rely on MkDocs' auto-generated TOC for the page if your theme supports it well for long pages._
- [General Project Setup](#general-project-setup)
- [Phase 1: Data Collection](#phase-1-data-collection)
- [Phase 2: Data Cleansing & Preprocessing](#phase-2-data-cleansing--preprocessing)
- [Phase 3: Exploratory Data Analysis (EDA)](#phase-3-exploratory-data-analysis-eda)
- [Phase 4: Feature Engineering](#phase-4-feature-engineering)
- [Phase 5: Model Development](#phase-5-model-development)
- [Phase 6: Model Evaluation](#phase-6-model-evaluation)
- [Phase 7: Deployment](#phase-7-deployment)
- [Phase 8: Ongoing Management & Iteration](#phase-8-ongoing-management--iteration)

---

## General Project Setup
*(Tasks related to overall project infrastructure, documentation, and planning)*

**Key Milestones:**
- [x] Initial project repository configured (`2025-05-06`)
- [ ] `project_plan.md` created and populated from Google Doc (`YYYY-MM-DD`)
- [ ] `mkdocs.yml` updated for new site structure (Target: `YYYY-MM-DD`)
- [ ] All phase report Markdown files named and structured (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Final review and sign-off on `project_plan.md`.
- [ ] Rename existing `docs/phase-XX-*.md` files to new phase numbers and report focus.
- [ ] Create template/outline for content expected in each phase report.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 1: Data Collection
*(Objective: To gather all necessary raw data from defined sources - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] All data sources and specific data fields fully identified and documented in `project_plan.md`. (Target: `YYYY-MM-DD`)
- [ ] Web scraping scripts for HKJC racecards developed and tested. (Target: `YYYY-MM-DD`)
- [ ] Web scraping scripts for HKJC race results developed and tested. (Target: `YYYY-MM-DD`)
- [ ] Historical data (target: X seasons/Y race days) successfully collected. (Target: `YYYY-MM-DD`)
- [ ] Initial storage solution for raw data implemented (e.g., GCS buckets, specific BigQuery raw tables). (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-01-collection.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Draft `docs/phase-01-collection.md` structure.
- [ ] Research and select Python library for web scraping (e.g., BeautifulSoup, Playwright).
- [ ] Implement `scrape_race_dates()` function.
- [ ] Begin initial scraping runs for a small sample of race days.
- [ ] Define schema for raw racecard data.

**Open Issues / Blockers:**
- [ ] Uncertainty about HKJC website's tolerance for scraping frequency.
- [ ] Need to define error handling and retry logic for scrapers.

---

## Phase 2: Data Cleansing & Preprocessing
*(Objective: To transform raw data into a clean, consistent, and usable format - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Data quality issues and required cleansing steps defined. (Target: `YYYY-MM-DD`)
- [ ] Scripts for data type conversion and standardization developed. (Target: `YYYY-MM-DD`)
- [ ] Strategy for handling missing values and outliers defined and implemented. (Target: `YYYY-MM-DD`)
- [ ] Cleansed dataset validated against defined quality criteria. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-02-cleansing.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Profile raw data to identify anomalies.
- [ ] Develop script to convert date/time fields to consistent format.
- [ ] Research imputation techniques for missing `HORSE_WEIGHT`.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 3: Exploratory Data Analysis (EDA)
*(Objective: To understand data patterns, relationships, and formulate initial hypotheses - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Initial descriptive statistics generated for all key variables. (Target: `YYYY-MM-DD`)
- [ ] Key visualizations (distributions, correlations, etc.) created. (Target: `YYYY-MM-DD`)
- [ ] Initial hypotheses about predictive factors documented. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-03-eda.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Set up EDA Jupyter notebook (`notebooks/01-race-eda.ipynb`).
- [ ] Generate histograms for numerical features.
- [ ] Calculate correlation matrix.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 4: Feature Engineering
*(Objective: To create new predictive features from the cleansed data - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Initial set of engineered features designed and documented. (Target: `YYYY-MM-DD`)
- [ ] Scripts to generate engineered features implemented. (Target: `YYYY-MM-DD`)
- [ ] Feature set validated and stored. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-04-features.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Brainstorm potential features based on EDA insights.
- [ ] Implement rolling average calculations for horse performance.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 5: Model Development
*(Objective: To train and select predictive models - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Baseline model(s) developed and evaluated. (Target: `YYYY-MM-DD`)
- [ ] Advanced model(s) explored and trained. (Target: `YYYY-MM-DD`)
- [ ] Hyperparameter tuning performed. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-05-modeling.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Select initial algorithm for baseline model (e.g., Logistic Regression).
- [ ] Split data into training and testing sets.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 6: Model Evaluation
*(Objective: To rigorously assess model performance and potential profitability - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Comprehensive backtesting strategy implemented. (Target: `YYYY-MM-DD`)
- [ ] Key performance metrics (ROI, accuracy, etc.) calculated. (Target: `YYYY-MM-DD`)
- [ ] Wagering strategy simulated and analyzed. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-06-evaluation.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Define metrics for successful model evaluation.
- [ ] Develop backtesting framework.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 7: Deployment
*(Objective: To set up a system for generating predictions on new races - see `project_plan.md` for details)*
*(This phase might be more about setting up a repeatable prediction pipeline than a live betting system initially)*

**Key Milestones:**
- [ ] Prediction generation pipeline designed. (Target: `YYYY-MM-DD`)
- [ ] Pipeline implemented and tested. (Target: `YYYY-MM-DD`)
- [ ] System for monitoring prediction performance outlined. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-07-deployment.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Design script to take new racecard data and output predictions.

**Open Issues / Blockers:**
- *None currently*

---

## Phase 8: Ongoing Management & Iteration
*(Objective: To maintain the system, monitor performance, and plan for future improvements - see `project_plan.md` for details)*

**Key Milestones:**
- [ ] Retraining schedule and triggers defined. (Target: `YYYY-MM-DD`)
- [ ] Long-term performance monitoring plan in place. (Target: `YYYY-MM-DD`)
- [ ] Roadmap for future enhancements outlined. (Target: `YYYY-MM-DD`)
- [ ] **Report:** `docs/phase-08-management.md` completed and reviewed. (Target: `YYYY-MM-DD`)

**Current Tasks & TODOs:**
- [ ] Review project outcomes against initial objectives.
- [ ] Document lessons learned.

**Open Issues / Blockers:**
- *None currently*

---

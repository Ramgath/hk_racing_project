# Project Status

**Last Manually Updated:** 2025-05-08

**Overall Project Health:** Green

*Initial setup and planning are progressing well. The new project structure and documentation plan are being finalized.*

**Key Focus for This Week (ending 2005-05-09):**
| Status | Task / Issue Description | Milestone |
|--------|---------------------------|-----------|
| 🔄     | Final review and sign-off on `project_plan.md`. | M2 |

---

## General Project Setup
*(Tasks related to overall project infrastructure, documentation, and planning)*

**Major Milestones:**
- ✅ M1: Initial project repository configured (Completed: YYYY-MM-DD)
- ⬜ M2: `project_plan.md` created and populated from Google Doc (Completed: YYYY-MM-DD)
- ⬜ M3: `mkdocs.yml` updated for new site structure (Target: YYYY-MM-DD)
- ⬜ M4: All phase report Markdown files named and structured (Target: YYYY-MM-DD)
- ⬜ M5: This `project-status.md` file structure finalized (Target: YYYY-MM-DD)

**Detailed Tasks & Issues:**

| Status | Task / Issue Description                         | Milestone | Notes / Resolution                               |
|--------|-------------------------------------------------|-----------|-------------------------------------------------|
| ✅     | Draft initial `project_plan.md` content.         | M2        | Moved content from Google Doc.                   |
| 🔄     | Final review and sign-off on `project_plan.md`.  | M2        |                                                  |
| ⬜     | Rename `docs/index.md` to `project_plan.md`.     | M2        |                                                  |
| ⬜     | Update `nav` section in `mkdocs.yml`.            | M3        | Point home to `project_plan.md`.                  |
| ⬜     | Delete old `docs/milestones.md`.                 | M6        |                                                  |
| ⬜     | Rename phase files (e.g., `phase-01-collection.md`)| M4        | Reflect new numbering & report focus.             |

---

## Phase 1: Data Collection
*(Objective: To gather all necessary raw data from defined sources - see `project_plan.md` for details)*

**Major Milestones:**
- ⬜ M1: All data sources and specific data fields fully identified and documented in `project_plan.md`. (Target: YYYY-MM-DD)
- ⬜ M2: Web scraping scripts for HKJC racecards developed and robustly tested. (Target: YYYY-MM-DD)
- ⬜ M3: Web scraping scripts for HKJC race results developed and robustly tested. (Target: YYYY-MM-DD)
- ⬜ M4: Historical data (target: X seasons/Y race days) successfully collected. (Target: YYYY-MM-DD)
- ⬜ M5: Initial storage solution for raw data implemented and populated. (Target: YYYY-MM-DD)
- ⬜ M6: **Report:** `docs/phase-01-collection.md` completed and reviewed. (Target: YYYY-MM-DD)

**Detailed Tasks & Issues:**

| Status | Task / Issue Description                                     | Milestone | Notes / Resolution                                         |
|--------|--------------------------------------------------------------|-----------|------------------------------------------------------------|
| ⬜     | Draft structure for `docs/phase-01-collection.md` report.    | M6        |                                                            |
| ⬜     | Research and select Python library for web scraping.         | M2        | Options: BeautifulSoup, Playwright, Scrapy.                |
| ⬜     | Implement `scrape_race_dates()` function.                    | M2        |                                                            |
| ⬜     | Implement `scrape_racecard(race_date_url)` function.         | M2        |                                                            |
| ⬜     | Implement `scrape_results(race_date_url)` function.          | M3        |                                                            |
| ⬜     | Define error handling and retry logic for scrapers.          | M7        | E.g., for network issues, unexpected page structure.       |
| ⬜     | Test scrapers on a diverse sample of 5-10 race days.         | M8        | Include different tracks, number of races.                  |
| ⬜     | Address Issue: Potential for IP blocking during scraping.    | You       | Monitor, implement delays, consider proxy/VPN if necessary.|
| ⬜     | Define schema for raw racecard data (JSON/CSV).              | M9        |                                                            |
| ⬜     | Define schema for raw results data (JSON/CSV).               | M10       |                                                            |

---

## Phase 2: Data Cleansing & Preprocessing
*(Objective: To transform raw data into a clean, consistent, and usable format - see `project_plan.md` for details)*

**Major Milestones:**
- ⬜ M1: Data quality issues from raw data fully profiled and documented. (Target: YYYY-MM-DD)
- ⬜ M2: Comprehensive data cleansing rules and procedures defined. (Target: YYYY-MM-DD)
- ⬜ M3: Scripts for all data type conversions and value standardizations developed. (Target: YYYY-MM-DD)
- ⬜ M4: Strategy for handling missing values and outliers defined and implemented. (Target: YYYY-MM-DD)
- ⬜ M5: Cleansed dataset validated against defined quality criteria and schema. (Target: YYYY-MM-DD)
- ⬜ M6: **Report:** `docs/phase-02-cleansing.md` completed and reviewed. (Target: YYYY-MM-DD)

**Detailed Tasks & Issues:**

| Status | Task / Issue Description                                     | Milestone | Notes / Resolution                               |
|--------|--------------------------------------------------------------|-----------|-------------------------------------------------|
| ⬜     | Draft structure for `docs/phase-02-cleansing.md` report.     | M6        |                                                 |
| ⬜     | Perform data profiling on raw collected data (from Phase 1). | M1        | Use Pandas Profiling or custom scripts.          |
| ⬜     | Develop script for converting date/time fields.              | M3        | Ensure consistent `YYYY-MM-DD HH:MM:SS` format.  |
| ⬜     | Script to standardize categorical values (e.g., track conditions).| M3        |                                                 |
| ⬜     | Research and select imputation techniques for `HORSE_WEIGHT`.| M4        | Mean, median, model-based?                       |
| ⬜     | Implement chosen imputation for `HORSE_WEIGHT`.              | M4        |                                                 |
| ⬜     | Identify and handle outliers in `FINISH_TIME`.               | M4        | E.g., Capping, removal based on IQR.             |

---

## Phase 3: Exploratory Data Analysis (EDA)
*(Objective: To understand data patterns, relationships, and formulate initial hypotheses - see `project_plan.md` for details)*

**Major Milestones:**
- ⬜ M1: Descriptive statistics generated and analyzed for all key variables. (Target: YYYY-MM-DD)
- ⬜ M2: Key visualizations (distributions, correlations, time series) created and interpreted. (Target: YYYY-MM-DD)
- ⬜ M3: Significant patterns, anomalies, and relationships documented. (Target: YYYY-MM-DD)
- ⬜ M4: Initial hypotheses about predictive factors formulated and listed. (Target: YYYY-MM-DD)
- ⬜ M5: **Report:** `docs/phase-03-eda.md` completed and reviewed. (Target: YYYY-MM-DD)

**Detailed Tasks & Issues:**

| Status | Task / Issue Description                                      | Milestone | Notes / Resolution                                  |
|--------|---------------------------------------------------------------|-----------|----------------------------------------------------|
| ⬜     | Draft structure for `docs/phase-03-eda.md` report.            | M5        |                                                    |
| ⬜     | Set up EDA Jupyter notebook (`notebooks/01-race-eda.ipynb`).  | M1        | Load cleansed data.                                 |
| ⬜     | Generate histograms and density plots for numerical features. | M2        | E.g., `FINISH_TIME`, `STARTING_ODDS`.              |
| ⬜     | Create bar charts for categorical feature frequencies.        | M2        | E.g., `COURSE`, `GOING`.                            |
| ⬜     | Calculate and visualize correlation matrix.                   | M2        | Identify highly correlated features.                |
| ⬜     | Box plots for numerical features grouped by key categories.   | M2        | E.g., `FINISH_TIME` by `CLASS`.                     |
| ⬜     | Investigate any surprising findings from initial plots.       | M3        |                                                    |

---

## Phase 4: Feature Engineering
*(Objective: To create new predictive features from the cleansed data - see `project_plan.md` for details)*

**Major Milestones:**
- ⬜ M1: List of potential engineered features brainstormed and prioritized. (Target: YYYY-MM-DD)
- ⬜ M2: Initial set of ~20-30 engineered features designed and documented. (Target: YYYY-MM-DD)
- ⬜ M3: Scripts to generate these engineered features implemented and tested. (Target: YYYY-MM-DD)
- ⬜ M4: Engineered feature set validated and stored. (Target: YYYY-MM-DD)
- ⬜ M5: **Report:** `docs/phase-04-features.md` completed and reviewed. (Target: YYYY-MM-DD)

**Detailed Tasks & Issues:**

| Status | Task / Issue Description                                     | Milestone | Notes / Resolution                               |
|--------|--------------------------------------------------------------|-----------|-------------------------------------------------|
| ⬜     | Draft structure for `docs/phase-04-features.md` report.      | M5        |                                                 |
| ⬜     | Create rolling average features for horse past performance.  | M3        | E.g., avg finish pos last 3/5 races.             |
| ⬜     | Calculate speed figures based on time and distance.          | M3        |                                                 |
| ⬜     | Encode categorical variables (e.g., one-hot, target encoding).| M3        |                                                 |
| ⬜     | Create interaction features (e.g., jockey-trainer win rate). | M3        |                                                 |

---

## Phase 5: Model Development
*(Objective: To train and select predictive models - see `project_plan.md` for details)*
*(Structure: Major Milestones list, then Detailed Tasks & Issues table)*
... *(Content to be filled similarly)* ...

---

## Phase 6: Model Evaluation
*(Objective: To rigorously assess model performance and potential profitability - see `project_plan.md` for details)*
*(Structure: Major Milestones list, then Detailed Tasks & Issues table)*
... *(Content to be filled similarly)* ...

---

## Phase 7: Deployment
*(Objective: To set up a system for generating predictions on new races - see `project_plan.md` for details)*
*(Structure: Major Milestones list, then Detailed Tasks & Issues table)*
... *(Content to be filled similarly)* ...

---

## Phase 8: Ongoing Management & Iteration
*(Objective: To maintain the system, monitor performance, and plan for future improvements - see `project_plan.md` for details)*
*(Structure: Major Milestones list, then Detailed Tasks & Issues table)*
... *(Content to be filled similarly)* ...

---</file>

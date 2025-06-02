---
title: HK Racing Project Plan
description: Comprehensive plan for the Hong Kong Racing Project, covering objectives, methodology, and all planned phases.
---

# Hong Kong Racing Project: Master Plan

This document outlines the technical plan for building a handicapping and wagering system for thoroughbred horse racing in Hong Kong, with the primary objective of achieving sustainable financial gain through data-driven strategies. It serves as the central reference for project scope, methodology, and planned execution across all phases.

## Project Definition and Establishment

### 0.1. Introduction and Aims

#### 0.1.1. Project Objective
* **Goal**: Develop and implement a machine learning-based handicapping and wagering system aimed at generating a positive return on investment (ROI) from Hong Kong horse racing.
* **Team**: Solo project with assistance from AI (e.g., Google Gemini).
* **Broader Context**: This project focuses on the technical development of a predictive system for financial gain within the domain of horse race wagering. It's acknowledged that this operates within the context of gambling, and responsible practices should guide any potential future application of the system's outputs.

#### 0.1.2. Document Purpose

This `project_plan.md` (and the accompanying MkDocs site) serves several key purposes:

* **Centralized Record**: Acts as the primary repository for documenting all project plans, methodologies, data sources, and strategic decisions made throughout the project lifecycle.
* **Shared Context for AI Collaboration**: Functions as a persistent memory and context for ongoing work and discussions with AI assistants. Referencing and updating this plan and related phase reports ensures continuity.
* **Single Source of Truth**: Establishes a definitive reference point for the project's scope, workflow, tools, and challenges.
* **Tracking Evolution**: While this document outlines the plan, individual phase reports (`docs/phase-XX-name.md`) will track the execution and evolution of the project.

### 0.2. Resource and Environment Configuration

#### 0.2.1. Hardware
* **Local machine**: MacBook Air, 8GB RAM, Apple Silicon (M1 chip).
* **Online**: Standard Colab CPU Environment (e.g., Intel Xeon, ~13 GB RAM). Google Colab free tier also provides variable access to GPU and TPU accelerators.

#### 0.2.2. Software and Cloud Services (Primarily Google Ecosystem)
* **Google BigQuery**: Central data warehouse for storing historical and current race data. Chosen for scalability, Colab integration, and cost-effectiveness within its free tier.
* **Google Colab**: Primary environment for data scraping, cleaning, analysis, feature engineering, visualization, and ML model development.
* **Google Sheets**: Used as an intermediary data hub, for manual input/correction if necessary, and potentially for controlling updates via Apps Script (original plan).
* **Google Apps Script**: Planned for automating data update processes (e.g., Sheets to BigQuery).
* **Google Cloud Storage (GCS)**: Considered for intermediary data storage (e.g., Parquet files) to optimize data transfer between BigQuery and Colab.
* **Python Libraries**:
    * Data Acquisition: Beautiful Soup (or potentially Playwright/Selenium if dynamic content requires it).
    * Data Manipulation & Analysis: pandas, NumPy, Polars.
    * Cloud Interaction: `google-cloud-bigquery`, `gspread`.
    * Visualization: Plotly, Matplotlib, Seaborn.
    * Machine Learning: Scikit-learn, TensorFlow, PyTorch, XGBoost, LightGBM (specific choices in modeling phase).
* **Version Control**: Git, managed via a GitHub repository.
* **Documentation**: MkDocs with the Material theme.

#### 0.2.3. Development Environment
* **Google Colab**: Primary for computationally intensive tasks (data processing, ML).
* **Visual Studio Code (VS Code) - Local**: For developing helper scripts, managing the project repository, and MkDocs site generation/preview.

### 0.3. Proposed Workflow Outline (Original Hybrid Concept)

#### 0.3.1. Rationale for Hybrid Workflow (Sheets -> BigQuery -> Colab)
*(This section reflects the original thinking from the Google Doc. The actual implementation might evolve and will be documented in phase reports.)*
The initially chosen workflow utilized a hybrid approach: Google Sheets (for easily editable data), BigQuery (External Tables linking to Sheets, then materializing into Native Tables for performance), and Google Colab for analysis and ML.

* **Ease of Data Correction**: Sheets as the primary editable source.
* **Analytical Performance**: Native BigQuery tables for querying.
* **Scalability**: BigQuery's inherent scalability.
* **Resource Efficiency**: Colab for computation.
* **Integration & Control**: Google ecosystem synergy.
* **Cost-Effectiveness**: Leveraging free tiers.

#### 0.3.2. Alternative Methodologies Considered (Original Assessment)
* **DuckDB (Local) + Colab**: Rejected due to local RAM limits and less straightforward data correction than Sheets.
* **Pandas/Polars (Local only)**: Rejected due to RAM limits and lack of persistence/scalability.
* **SQLite (Local)**: Rejected due to performance for analytical queries and local resource limits.
* **PostgreSQL (Local)**: Rejected due to overhead on local hardware.
* **Snowflake (Cloud)**: Rejected due to lack of a comparable free tier to BigQuery.

---

## Phase 1: Data Collection and Storage

**Objective:** To acquire all relevant raw and processed historical data from 2008 onwards and establish a structured and robust initial storage solution in Google BigQuery. This phase focuses on ingesting previously processed data and setting up the capability to collect ongoing race data.

### 1.1 Data Sources:

* **Primary Historical Processed Data (2008 - March 2025):**
    * **Source 1:** User-provided Google Sheets from a 3rd party source. This data has undergone previous processing and error correction by the user.
    * **Content:** Includes race results, race cards, race details, and horse register information.
    * **Period:** From 2008 (coinciding with GPS tracking implementation) up to November 2023.

    * **Source 2:** User scraped data using a copy and paste method with the aid of app script for processing.
    * **Content:** Continuation of the 3rd party data.
    * **Period:** From Dec 2023 to 19 March 2025.

* **Primary Ongoing Raw Data (March 2025 onwards):**
    * **Source:** Hong Kong Jockey Club (HKJC) official website (`https://racing.hkjc.com/`).
    * **Content:** Racecards (for upcoming races), race results (historical, post-race), horse details, trackwork records, stewards' reports, and any other relevant data available.
    * **Period:** From March 2025 onwards.

### 1.2. Historical Data Consideration (Pre-2008):

* Data prior to 2008, from the 3rd party source, while available in CSV format, has been deemed **out of scope** for this project.
* **Rationale for Exclusion:**
    * Significant data quality issues (error-prone, missing values for critical fields like win odds, horse weights, and HKJC ratings).
    * Absence of sectional timings and less accurate overall finish times.
    * Fundamental differences in track configurations (e.g., false rail positions) before the consistent GPS tracking system was implemented in 2008.
    * Lack of advanced timing systems (e.g., precision to two decimal places for finish and sectional times).
* Focusing on data from 2008 onwards ensures higher quality, consistency, and relevance to current racing conditions.

### 1.3. Data Acquisition Methodology:

* **Processed Historical Data (Google Sheets):**
    * **Method:** Python scripts utilizing libraries such as `gspread` and `pandas` to read data directly from the user's Google Sheets.
    * **Environment:** Local Python environment or Google Colab.
    * **Note:** While Google Sheets were the initial source for some data, the focus for acquiring bulk historical data (2008-2023), particularly for detailed race reports and "Comments on Running," has shifted to processing CSV files.
* **Historical CSV Report Scraping (One-Off Task - 2008-2023):**
    * **Method:** A one-time scraping effort was undertaken to extract detailed race reports and "Comments on Running" from historical CSV files covering the period 2008-2023. This was prioritized to secure a rich historical dataset (as per Week 3 decisions).
    * **Environment:** Google Colab was utilized for this bulk scraping task to mitigate risks associated with IP address blocking during the large, one-off data extraction.
    * **Code Management:** The Python scripts developed for this specific one-off historical CSV scraping task are intentionally excluded from the main project repository (`hk_racing_project`). This decision keeps the main repository focused on the ongoing, automated data collection pipeline and avoids cluttering it with code for a completed, non-recurring task (as per Week 3 decisions).
* **Ongoing Raw Data (HKJC Website):**
    * **Status Note:** Collection of ongoing raw data from the HKJC website was temporarily paused (as per Week 3 decisions) to prioritize the acquisition of bulk historical reports data (2008-2023) from CSVs. Development of the automated scraping pipeline for new data will resume based on the refined strategy below.
    * **Primary Method:** Web scraping using Python libraries (e.g., `requests`, `Beautiful Soup`, and potentially `Playwright` or `Selenium` if dynamic content rendering is a significant factor).
    * **Primary Trigger & Orchestration:** The `src/ingestion/race_calendar.py` script, which reads race meeting dates from a user-managed Google Sheet, has been redefined as the primary trigger for the scraping pipeline for new race meetings (as per Week 4 decisions). This script will orchestrate subsequent scraping tasks for racecards, results, etc., based on the fetched dates.
    * **Data Scope Expansion (Incident Reports):** To enable a more comprehensive incident analysis for ongoing data collection, scraping will include "Comments on Running" reports in addition to "Full Stewards' Reports" (as per Week 4 decisions).
    * **Environment:** Scripts will be developed locally or in Google Colab and designed for potential future deployment in an automated environment (e.g., Google Cloud Functions).
    * **API Limitations:** The HKJC does not offer a public API, necessitating web scraping.
    * **Scope per Session:** Scraping will be batched, likely per race day or specific data types (e.g., all results for a given day, all upcoming racecards), orchestrated by the race calendar.
    * **Maintenance:** To ensure the scraping scripts continue to function correctly despite potential modifications to the HKJC website, they will need consistent oversight and upkeep. Health status updates for the scraping system will be generated and recorded in `phase-01-collection.md`.

### 1.4. Preliminary Data Formatting (Post-Scraping - for HKJC Data):

* **Environment:** Python scripts (local or Colab).
* **Objective:** For newly scraped data, perform initial transformations to ensure basic consistency before storage in the raw BigQuery dataset. This includes:
    * Data type enforcement (e.g., converting strings to numbers or dates where appropriate).
    * Basic string manipulation (trimming whitespace, standardizing case for certain fields).
    * Structural validation to ensure essential fields are present.
* **Rationale:** Python scripts provide reproducibility, version control, and robust error handling for these initial formatting steps.

### 1.5. Data Storage Strategy:

* **Primary Data Warehouse:** Google BigQuery.
* **BigQuery Datasets:**
    * **`hk_racing_dataset` (Main Dataset):**
        * **Purpose:** To store the processed historical data (2008 - March 2025) from Google Sheets. This dataset will also serve as the target for fully cleansed, integrated, and modeled analytical data in later phases.
        * **Schema:** Tables (`results`, `racecard`, `race_details`, `horse_register`) will adhere to the structures defined by the user (see Appendix A: Data Dictionary).
    * **`hk_racing_scraped_raw` (Staging/Raw Dataset):**
        * **Purpose:** To store the raw data collected from the HKJC website (December 2023 onwards) after preliminary formatting.
        * **Schema:** Table structures in this dataset will initially mirror the scraped data structure closely. Data will be transformed and loaded into the main `hk_racing_dataset` during Phase 2 (Cleansing and Preprocessing).
* **Data Ingestion Pipeline:**
    * **Sheets to BigQuery:** Python scripts will read from Google Sheets and load data directly into the corresponding tables in `hk_racing_dataset`.
    * **HKJC Scrapes to BigQuery:** Python scraping scripts will perform preliminary formatting and then load data directly into tables within `hk_racing_scraped_raw`. Temporary local file storage (e.g., JSON, CSV) or GCS may be used as an intermediate step during the scraping and loading process if beneficial for batching or error handling.
* **Configuration:** GCP project ID, BigQuery dataset IDs, and other relevant parameters will be managed via `config/config.yaml` and accessed using `src/common/config_loader.py`.
* **Update Frequency:** New race data from HKJC will be collected and processed typically twice weekly, aligned with the HKJC racing calendar. Automation of this collection is a future goal (Phase 4).

---

## Phase 2: Data Cleansing and Preprocessing
*(This phase focuses on transforming raw collected data into a clean, consistent, and usable dataset.)*

### 2.1. Overview of Collected Data
The dataset will encompass:
*   **Core Race & Horse Data:** As detailed in Appendix A (Data Dictionary), this includes race identification, horse performance metrics, betting information, jockey/trainer details, and pre-race horse information.
*   **Incident Report Data:**
    *   **Historical (2008-2023 from CSVs):** Comprehensive race reports, often including both stewards' observations and comments on running within single documents.
    *   **Ongoing (HKJC Website):** More granular reports, typically separating "Full Stewards' Reports" (factual incident details) from "Comments on Running" (performance implications).
    *   **Challenge:** A key task in this phase will be to address the structural differences between these historical and current report formats to enable consistent analysis (as per Week 4 decisions).

### 2.2. Cleansing Procedure
* **Environment**: Primarily Google Colab or local Python scripts, with results stored in BigQuery.
* **Key Steps**:
    * **Data Type Enforcement**: Ensure columns match predefined types (integer, float, string, date).
    * **String Manipulation**: Trim whitespace, standardize capitalization, handle special characters.
    * **Categorical Value Standardization**: Ensure consistency in fields like `COURSE`, `CLASS`, `GOING`. Map variations to standard values.
    * **Handling Specific Non-Numeric/Placeholder Strings**: Address values like 'UNRATED', 'GRIFFIN', 'DEBUT' in fields that are otherwise numeric or categorical.
    * **Addressing Known Inconsistencies**: Programmatic fixes for known issues in historical data.
    * **Incident Data Integration & Harmonization:**
        *   Integrate "Comments on Running" with "Full Stewards' Reports" to create a more holistic view of in-race incidents and their consequences (as per Week 4 decisions).
        *   Attempt to harmonize the structure of incident data extracted from historical CSVs and ongoing HKJC website scrapes.
        *   **Note on LLM-based Nuanced Extraction:** The plan to use LLMs (Gemini Flash 2.5, OpenAI GPT-4o mini, Gemini 2.5 Pro Preview) for detailed interpretation and categorization of incidents from textual reports is currently **paused**. This is due to issues encountered during Week 4 testing, including model reliability (hallucinations), unexpected processing token consumption leading to high costs, and overall cost-prohibitive API pricing for bulk historical data. For now, simpler rule-based extraction methods will be employed for incident data, or this highly nuanced extraction task will be deferred until LLM solutions become more viable.

### 2.3. Data Validation and Format Consistency
* **Objective**: Rigorously validate data against the schema in Appendix A.
* **Checks**: Data type verification, value range checks, categorical value consistency, basic relational integrity checks (e.g., consistent IDs).
* **Discrepancy Handling**: Refine cleansing scripts or (as a last resort for historical data) document manual corrections.

### 2.4. Management of Missing Values/Outliers
* **Approach**: Strategies will be determined based on EDA findings (Phase 3) and model requirements.
* **Missing Values**: Options include deletion (rows/columns), mean/median/mode imputation, regression imputation, or model-based imputation.
* **Outliers**: Identification (e.g., IQR, Z-scores) followed by potential capping, transformation, or removal.

### 2.5. Data Transformation (Preparation for Modeling)
* **Encoding Categorical Variables**: Convert string categories (e.g., `CLASS`, `GOING`) into numerical representations (One-Hot, Label, Target Encoding).
* **Numerical Scaling**: Apply standardization or normalization if required by specific models.
* **Other Transformations**: Log transforms, polynomial features, etc., based on EDA and model needs.

---

## Phase 3: Exploratory Data Analysis (EDA)
*(This phase focuses on understanding the data through querying, statistics, and visualizations to uncover patterns and formulate hypotheses.)*

### 3.1. Data Querying
* **Source**: Cleansed data tables in Google BigQuery.
* **Environment**: Google Colab using the `google-cloud-bigquery` Python library.
* **Process**: Construct SQL queries in Colab, execute against BigQuery, load results into Pandas/Polars DataFrames for analysis.

### 3.2. Descriptive Statistics
* **Tools**: Python libraries (Pandas, NumPy) in Colab.
* **Numerical Variables**: Calculate count, mean, median, std dev, min, max, percentiles, skewness, kurtosis.
* **Categorical Variables**: Frequency counts, unique values, mode.

### 3.3. Visualization
* **Primary Tool**: Plotly for interactive plots in Colab. Seaborn and Matplotlib as alternatives.
* **Univariate Analysis**: Histograms, density plots, box plots, bar charts.
* **Bivariate/Multivariate Analysis**: Scatter plots, correlation heatmaps, grouped plots, time series plots (if applicable).

### 3.4. Initial Observations and Hypothesis Formulation
* Synthesize findings from statistics and visualizations.
* Identify significant patterns, trends, anomalies, and correlations.
* Formulate initial hypotheses about factors influencing race outcomes.
* Identify areas needing further investigation. These insights will guide Feature Engineering (Phase 4).

---

## Phase 4: Feature Engineering
*(This phase focuses on creating new, potentially more predictive variables from the cleaned dataset.)*

### 4.1. Methodology
* **Environment**: Google Colab using Pandas, NumPy, Polars, and Scikit-learn.
* **Approach**: Iterative process based on domain knowledge, EDA insights, and preliminary model testing.
* **Goal**: Transform base data into a richer feature set that captures complex racing dynamics.

### 4.2. Initial Feature Set
* The starting point is the cleansed, validated dataset (approx. 40-50 core variables as per Appendix A).

### 4.3. Target Feature Set
* Strategically expand the initial set. The focus is on developing hypothesized predictive features and validating their impact, rather than a fixed target number of features.

### 4.4. Example Categories of Engineered Features
* **Form & Consistency**: Rolling win/place percentages, average finishing position (recent races), days since last win.
* **Speed & Pace**: Calculated speed figures, sectional speed ratings, comparisons to class/distance/track averages.
* **Jockey/Trainer Statistics**: Win/place rates (overall, by course, distance, class, horse combination), recent form.
* **Odds-Based Features**: Odds movement (if available), probability derived from odds, value indicators (odds vs. finish).
* **Class & Weight Related**: Rating relative to class, weight carried relative to past or standard weights.
* **Interaction & Derived Features**: Jockey win rate *on this course*, horse average speed *at this distance*.
* **Lagged Variables**: Performance metrics from the previous race.
* **LLM-Derived Incident Features:** Utilize the Gemini 2.5 Pro Preview API to summarize, interpret, and categorize incidents from textual data in "Full Stewards' Reports" and "Comments on Running." This process aims to generate nuanced features reflecting the nature, severity, and potential impact of in-race events. (Note: Application to bulk historical data is contingent on cost-effectiveness, as explored in `decisions.md` Week 4.).

### 4.5. Feature Engineering Approach
* Iterative: Develop, test (correlation, feature importance from simple models, backtesting), refine/discard.
* New ideas may emerge during modeling and evaluation.

### 4.6. Roles of BigQuery and Colab
* **BigQuery**: Source for cleaned base data. Potentially store validated engineered features in new tables/views for efficient reuse.
* **Colab**: Primary environment for implementing complex feature calculation logic.

---

## Phase 5: Model Development and Training
*(This phase involves selecting, training, and optimizing machine learning models to predict race outcomes.)*

### 5.1. Model Selection
* **Target Variable(s)**: To be clearly defined (e.g., predict win probability, predict top N finish, predict expected ROI).
* **Baseline Models**: Start with simpler, interpretable models (Logistic Regression, Linear Regression, Decision Trees, Random Forests).
* **Advanced Models**: Explore Gradient Boosting Machines (XGBoost, LightGBM, CatBoost), Neural Networks (MLPs, potentially RNNs/LSTMs if sequential data like sectional times are heavily used).
* **Selection Criteria**: Predictive performance (via backtesting), interpretability, computational cost, training time.

### 5.2. Training Environment
* **Primary**: Google Colab, leveraging free-tier GPU/TPU accelerators for computationally intensive models.

### 5.3. Validation Approach
* **Primary Method**: Rigorous Backtesting.
    * Simulate training on historical data up to a point and evaluating on subsequent unseen historical data.
    * Employ time-series aware validation (e.g., walk-forward validation) to prevent data leakage.

### 5.4. Hyperparameter Optimization
* For promising models, optimize hyperparameters to maximize performance on validation sets.
* **Techniques**: Grid Search, Randomized Search, Bayesian Optimization (using libraries like Optuna or Scikit-learn tools).

---

## Phase 6: Model Evaluation and Validation
*(This phase focuses on rigorously evaluating model performance, especially in the context of wagering profitability.)*

### 6.1. Performance Metrics
* **Primary Focus (Wagering Profitability)**:
    * Return on Investment (ROI).
    * Hit Rate (Win Prediction Accuracy, Place Prediction Accuracy).
* **Standard ML Metrics (Task-Dependent)**:
    * Classification: Accuracy, Precision, Recall, F1-score, Log Loss, AUC-ROC, AUC-PR.
    * Regression (if predicting rank/time): MAE, RMSE.

### 6.2. Backtesting Outcomes
* Present detailed quantitative results from backtesting simulations.
* Compare different models and hyperparameter configurations across historical validation periods.

### 6.3. Wagering Strategy Simulation
* Simulate model use within defined wagering strategies during backtesting.
* **Examples**: Fixed Stakes, Percentage Stakes (e.g., fixed percentage of bankroll), Kelly Criterion (adjusting bet size based on perceived edge and odds).
* Simulation must account for historical odds and race results.

### 6.4. Profitability Analysis
* In-depth analysis of simulated financial performance (total profit/loss, ROI, drawdown, risk-adjusted returns).
* Assess feasibility of achieving the project's primary objective (positive ROI).

### 6.5. Iterative Refinement
* Evaluation results drive improvements:
    * Revisit Feature Engineering (Phase 4).
    * Revisit Model Selection (Phase 5.1).
    * Revisit Hyperparameter Optimization (Phase 5.4).
    * Analyze errors to understand model strengths/weaknesses.

---

## Phase 7: Deployment and Monitoring (Future Phase)
*(This phase outlines operationalizing the model and monitoring its ongoing performance.)*

### 7.1. Prediction Generation Workflow
* End-to-end process for generating predictions/insights for upcoming race days:
    * Acquire new racecard data.
    * Apply preprocessing and feature engineering steps consistently.
    * Load trained model.
    * Generate predictions.
    * Store/present predictions for decision-making.
* Define automation level and tools.

### 7.2. Performance Monitoring
* Track real-world effectiveness and profitability:
    * Collect actual race results.
    * Compare outcomes against predictions.
    * Track ROI based on simulated/actual wagers.
    * Monitor for model drift or changes in data distributions.
* Define metrics, frequency, and tools.

### 7.3. Retraining Approach
* Strategy for periodic model retraining:
    * **Triggers**: Performance degradation, fixed schedule, or significant new data accumulation.
    * **Process**: Reuse pipelines from Phases 2-6 with updated data.
    * **Validation**: Retrained models validated via backtesting before deployment.

---

## Phase 8: Project Management and Continuous Improvement
*(This section covers ongoing project aspects, learnings, and future considerations.)*

### 8.1. Potential Challenges and Resolutions (Ongoing Log)
*(This list will be dynamic and updated in phase reports or a dedicated decisions/risks log as they arise.)*
* **Cloud Costs (BigQuery/GCP)**: Monitor usage, optimize queries, leverage free tiers.
* **Feature Engineering Complexity**: Iterative approach, start simple, leverage domain knowledge and EDA.
* **Model Validation & Profitability**: Rigorous backtesting, realistic wagering simulation.
* **Data Pipeline Robustness**: Error handling, logging, monitoring.
* **Data Integrity & Correction**: Ongoing validation checks, clear process for corrections.
* **Web Scraping Maintenance**: Monitor for HKJC site changes, allocate time for script updates.
* **LLM API Integration for Nuanced Data Extraction**: Initial testing with various LLM APIs (Gemini Flash 2.5, OpenAI GPT-4o mini, Gemini 2.5 Pro Preview) for interpreting textual incident reports revealed significant challenges. These included model hallucinations (providing irrelevant or incorrect information), unexpectedly high processing token consumption leading to drastically increased costs, and generally prohibitive API pricing for the bulk processing of historical data. Performance and reliability varied significantly between models. **Resolution**: This approach has been paused for bulk historical data processing, with simpler methods or deferral being the current strategy (as detailed in Week 4 decisions and Phase 2 planning).

### 8.2. Data Size Projections and Growth
* Initial dataset (18 years, ~171k rows, 40-50 cols): ~20-50 MB.
* With engineered features (~150-200 cols): ~50-100 MB.
* Long-term growth (next 15-20 years): Potentially doubling to ~200-400 MB.
* These volumes are manageable within BigQuery free tiers and Colab.

### 8.3. Tools Summary
* **Data Storage & Querying**: Google BigQuery.
* **Data Processing & Modeling**: Python in Google Colab (Pandas, Scikit-learn, etc.).
* **Web Scraping**: Python (Beautiful Soup / Playwright).
* **Version Control**: Git / GitHub.
* **Documentation**: MkDocs (Material theme).
* **Project Management / Task Tracking**: `docs/project-status.md`.
* **(Original) Intermediary Data/Control**: Google Sheets, Google Apps Script (may be revised).

### 8.4. Future Considerations
* **Advanced Deployment**: If successful, explore more sophisticated deployment (e.g., dedicated prediction server, API).
* **Alternative Data Sources**: If HKJC scraping becomes untenable (unlikely to be better external sources).
* **Deeper Model Exploration**: More complex architectures if justified by performance.

### 8.5. Version Control Strategy
* All project code, documentation, and configuration files will be version controlled using **Git**, hosted on a **GitHub** repository.
* Branches will be used for feature development and experimentation (e.g., `feature/new-scraper`, `experiment/new-model-arch`).
* The `main` branch will represent the stable, working version of the project.
* Commits should be descriptive and atomic.

### 8.6. References
*(Placeholder for links to key documentation, research papers, articles, etc., consulted during the project.)*

* HKJC Website: `[Link to be added]`
* Pandas Documentation: `https://pandas.pydata.org/pandas-docs/stable/`
* Scikit-learn Documentation: `https://scikit-learn.org/stable/`
* MkDocs Material Theme: `https://squidfunk.github.io/mkdocs-material/`

---

**Appendix A: Phase 1 Data Dictionary**

*The following tables are from the `hk_racing_dataset`*

#### A.1. `hk_racing_dataset.race_details`

| Column Name           | Data Type | Description                                                                             | Notes / Example                         |
| --------------------- | --------- | --------------------------------------------------------------------------------------- | --------------------------------------- |
| **RACE\_ID**          | INTEGER   | **Primary key.** Unique identifier for each race, combining date and seasonal sequence. | e.g. `20240414581` (YYYYMMDD + `581`)   |
| **DATE**              | DATE      | Calendar date when the race was held.                                                   | `2024-04-14`                            |
| **VENUE**             | STRING    | Name of the racecourse.                                                                 | `Sha Tin`, `Happy Valley`               |
| **SURFACE**           | STRING    | Track surface type.                                                                     | `Turf` or `AWT` (all-weather track)     |
| **RACE\_NUM\_SEASON** | INTEGER   | Sequence number of this race in the current season (3-digit).                           | `581`                                   |
| **CLASS**             | STRING    | Classification of the race by quality/conditions.                                       | `Class 1`, `Group 1`, `Griffin`         |
| **DISTANCE**          | INTEGER   | Race distance in metres.                                                                | `1200`, `1650`                          |
| **RANKING**           | STRING    | Official rating bracket for eligibility (upper-lower).                                  | `85-60`, `100-85`                       |
| **GOING**             | STRING    | Turf going description, or condition of AWT.                                            | `GOOD`, `YIELDING (WET SLOW)`, `AWT`    |
| **RACE\_DESCRIPTION** | STRING    | Official race title.                                                                    | `THE HONG KONG EXCHANGES CHALLENGE CUP` |
| **TRACK\_CONFIG**     | STRING    | Course layout variant (e.g., inside rail offsets).                                      | `A`, `C+2`, `AWT`                       |
| **PRIZE**             | INTEGER   | Total purse awarded (in HKD).                                                           | `1200000`                               |
| **PEN\_READING**      | FLOAT     | Penetrometer reading for turf (strength) or Clegg hammer reading for AWT.               | `2.72` (turf), `8.4` (AWT)              |

---

#### A.2. `hk_racing_dataset.race_card`

| Column Name       | Data Type | Description                                                      | Notes / Example             |
| ----------------- | --------- | ---------------------------------------------------------------- | --------------------------- |
| **RUNNER\_ID**    | STRING    | **Primary key.** Uniquely identifies a horse in a specific race. | `20240414581*CLEARWIN*H255` |
| **RACE\_ID**      | INTEGER   | **Foreign key →** `race_details.RACE_ID`.                        | `20240414581`               |
| **HORSE\_ID**     | STRING    | **Foreign key →** `horse_register.HORSE_ID`.                     | `CLEARWIN*H255`             |
| **WEIGHT**        | INTEGER   | Total impost carried (jockey + equipment), in pounds.            | `126`                       |
| **HORSE\_WEIGHT** | INTEGER   | Declared bodyweight of the horse (taken pre-race), in pounds.    | `1180`                      |
| **DRAW**          | INTEGER   | Barrier (gate) number at start.                                  | `1` (inside rail)           |
| **JOCKEY**        | STRING    | Name of the jockey riding this runner.                           | `Z Purton`                  |
| **TRAINER**       | STRING    | Name of the trainer responsible for this runner.                 | `D J Whyte`                 |
| **RATING**        | INTEGER   | Official HKJC rating at time of race.                            | `112`                       |
| **DEBUT\_BOOL**   | BOOLEAN   | Indicates if this was the horse’s first-ever start in Hong Kong. | `TRUE`, `FALSE`             |
| **REST\_DAYS**    | INTEGER   | Days elapsed since the horse’s previous run.                     | `21`                        |
| **RACE\_AGE**     | INTEGER   | Age of the horse on race day, in years.                          | `6`                         |
| **GEAR**          | STRING    | Codes for equipment fitted (see Gear Key below).                 | `PC/XB/TT`, `E`, `H1`       |

**Gear Key (HKJC standard abbreviations):**

| Code | Meaning                     | Notes              |
| ---- | --------------------------- | ------------------ |
| B    | Blinkers                    |                    |
| BO   | Blinker (one cowl)          |                    |
| CC   | Cornell Collar              |                    |
| CP   | Sheepskin Cheek Pieces      |                    |
| CO   | Sheepskin (one side)        |                    |
| E    | Ear Plugs                   |                    |
| H    | Hood                        |                    |
| P    | Pacifier                    |                    |
| PC   | Pacifier + cowls            |                    |
| PS   | Pacifier (one cowl)         |                    |
| SB   | Sheepskin Browband          |                    |
| SR   | Shadow Roll                 |                    |
| TT   | Tongue Tie                  |                    |
| V    | Visor                       |                    |
| VO   | Visor (one cowl)            |                    |
| XB   | Crossed Nose Band           |                    |
| \*1  | First time use of that gear | Suffix, e.g. `H1`  |
| \*2  | Gear replaced               | Suffix, e.g. `B2`  |
| -\*  | Gear removed                | Suffix, e.g. `CC-` |

---

#### A.3. `hk_racing_dataset.race_results`

| Column Name        | Data Type | Description                                                                                     | Notes / Example             |
| ------------------ | --------- | ----------------------------------------------------------------------------------------------- | --------------------------- |
| **RUNNER\_ID**     | STRING    | **Foreign key →** `race_card.RUNNER_ID`. Matches each runner to its card entry.                 | `20240414581*CLEARWIN*H255` |
| **RACE\_ID**       | INTEGER   | **Foreign key →** `race_details.RACE_ID`.                                                       | `20240414581`               |
| **HORSE\_ID**      | STRING    | **Foreign key →** `horse_register.HORSE_ID`.                                                    | `CLEARWIN*H255`             |
| **FINISH\_POS**    | INTEGER   | Official finishing position. Codes ≥90 may indicate non-finishers (e.g. DNS, UR).               | `1`, `2`, `DNF`             |
| **STARTING\_ODDS** | FLOAT     | Decimal odds at race start.                                                                     | `1.8`, `10.5`               |
| **PLACE\_PAYOUTS** | FLOAT     | Dividend payout for a successful “place” bet. `0` or `NULL` if unplaced or no payout available. | `2.5`, `NULL`               |
| **FINISH\_TIME**   | FLOAT     | Winner’s official finishing time in seconds.                                                    | `71.52`                     |
| **SEC\_TIME\_1**   | FLOAT     | Sectional time for first segment (varies by course layout).                                     | `22.15`                     |
| **SEC\_TIME\_2**   | FLOAT     | Sectional time for second segment.                                                              | `23.00`                     |
| **SEC\_TIME\_3**   | FLOAT     | Sectional time for third segment.                                                               | `26.37`                     |
| **SEC\_TIME\_4**   | FLOAT     | Sectional time for fourth segment (if applicable).                                              | —                           |
| **SEC\_TIME\_5**   | FLOAT     | Sectional time for fifth segment (if race >1,600 m).                                            | —                           |
| **SEC\_TIME\_6**   | FLOAT     | Sectional time for sixth segment (if race >2,200 m).                                            | —                           |

---

#### A.4. `hk_racing_dataset.horse_register`

| Column Name             | Data Type | Description                                                           | Notes / Example                                    |
| ----------------------- | --------- | --------------------------------------------------------------------- | -------------------------------------------------- |
| **HORSE\_ID**           | STRING    | **Primary key.** Stable identifier for each horse across all races.   | `DEANSANGEL*D123`                                  |
| **HORSE\_CODE**         | STRING    | Unique alphanumeric code assigned by HKJC (distinguishes duplicates). | `D466`, `H255`                                     |
| **HORSE\_NAME**         | STRING    | Official registered name of the horse.                                | `DEAN’S ANGEL`                                     |
| **SEX**                 | STRING    | Gender classification.                                                | `MALE`,`FEMALE` |
| **COLOR**               | STRING    | Coat colour.                                                          | `Bay`, `Chestnut`                                  |
| **COUNTRY\_OF\_ORIGIN** | STRING    | Country where the horse was foaled (ISO 3-letter code).               | `AUS`, `NZ`, `IRE`                                 |
| **IMPORT\_TYPE**        | STRING    | Means by which horse entered HK racing.                               | `PP`, `PPG`, `ISG`, `VIS`                          |
| **SIRE**                | STRING    | Registered name of the horse’s father.                                | `ALL TOO HARD`                                     |
| **DAM**                 | STRING    | Registered name of the horse’s mother.                                | `ANGEL IN MY HEART`                                |
| **DAM\_SIRE**           | STRING    | Registered sire of the dam (maternal grandsire).                      | `SEBRING`                                          |
| **OWNER**               | STRING    | Name(s) of the owner(s) as recorded by HKJC.                          | `Mr & Mrs John Smith`                              |

---

**Key relationship summary:**

* `race_details.RACE_ID` → parent of both `race_card` and `race_results`.
* `race_card.RUNNER_ID` → referenced by `race_results.RUNNER_ID`.
* `horse_register.HORSE_ID` → parent of both `race_card.HORSE_ID` and `race_results.HORSE_ID`.


**Import Type Key:**

* `PP`: Privately Purchased Horses (previously raced elsewhere).
* `PPG`: Privately Purchased Griffins (unraced young horses).
* `ISG`: International Sale Griffins (unraced horses from approved sales).
* `VIS`: Visiting Invitational Horses (invited for specific major races).
---

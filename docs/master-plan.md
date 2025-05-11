---
title: HK Racing Project Plan
description: Comprehensive plan for the Hong Kong Racing Project, covering objectives, methodology, and all planned phases.
---

# Hong Kong Racing Project: Master Plan

This document outlines the technical plan for building a handicapping and wagering system for thoroughbred horse racing in Hong Kong, with the primary objective of achieving sustainable financial gain through data-driven strategies. It serves as the central reference for project scope, methodology, and planned execution across all phases.

## 0. Project Definition and Establishment

*(This foundational phase covers the project's aims, documentation strategy, resource configuration, core development environment, and the overall workflow. It is numbered '0' to distinguish it from the sequential execution phases that follow.)*

### 0.1. Introduction and Aims

#### 0.1.1. Project Objective
* **Goal**: Develop and implement a machine learning-based handicapping and wagering system aimed at generating a positive return on investment (ROI) from Hong Kong horse racing.
* **Team**: Solo project with assistance from AI (e.g., Google Gemini).
* **Broader Context**: This project focuses on the technical development of a predictive system for financial gain within the domain of horse race wagering. It's acknowledged that this operates within the context of gambling, and responsible practices should guide any potential future application of the system's outputs.

#### 0.1.2. Document Purpose

This `master-plan.md` (and the accompanying MkDocs site) serves several key purposes:

* **Centralized Record**: Acts as the primary repository for documenting all project plans, methodologies, data sources, and strategic decisions made throughout the project lifecycle.
* **Shared Context for AI Collaboration**: Functions as a persistent memory and context for ongoing work and discussions with AI assistants. Referencing and updating this plan and related phase reports ensures continuity.
* **Single Source of Truth**: Establishes a definitive reference point for the project's scope, workflow, tools, and challenges.
* **Tracking Evolution**: While this document outlines the plan, individual phase reports (`docs/phase-XX-name.md`) will track the execution and evolution of the project.

### 0.2. Resource and Environment Configuration

#### 0.2.1. Hardware
* **Local machine**: MacBook Air, 8GB RAM, Apple Silicon (M1 chip).
* **Online**: Standard Colab CPU Environment (e.g., Intel Xeon, ~13 GB RAM). Google Colab free tier also provides variable access to GPU and TPU accelerators.

#### 0.2.2. Software and Cloud Services (Primarily Google Ecosystem)
* **Google BigQuery**: Central data warehouse for storing historical and current race data (raw, cleaned, and processed).
    * **Rationale**: Chosen for its scalability, powerful SQL interface, direct integration with Python and Colab, and generous free tier (1TB queries/month, 10GB storage/month), making it cost-effective for this project.
* **Google Cloud Storage (GCS)**: For storing model artifacts (e.g., pickled models, TensorFlow SavedModel directories) and potentially intermediary data files if needed.
    * **Rationale**: Provides a robust, versionable, and accessible storage solution. The free tier (5GB-months standard storage) is expected to be sufficient for model files, offering a significant improvement over local storage or Google Drive for MLOps practices at minimal to no cost.
* **Vertex AI Model Registry**: For registering, versioning, and managing trained machine learning models.
    * **Rationale**: Offers a centralized system to track model lineage and metadata, which is crucial for reproducibility and governance. The core model registration functionality is free and integrates with models stored in GCS. Costs would only be incurred if deploying models to Vertex AI Endpoints, which is not the primary plan.
* **Python Libraries**:
    * Data Acquisition & Interaction: `requests`, `beautifulsoup4` (for scraping), `google-cloud-bigquery`, `google-cloud-storage`, `pandas-gbq`.
    * Data Manipulation & Analysis: `pandas`, `numpy`, `polars` (for exploration).
    * Visualization: `plotly`, `matplotlib`, `seaborn`.
    * Machine Learning: `scikit-learn`, potentially `tensorflow`, `pytorch`, `xgboost`, `lightgbm` (specific choices to be made in the modeling phase).
    * Web Application (Future Consideration): `streamlit`.
* **Version Control**: Git, managed via a GitHub repository.
* **Documentation**: MkDocs with the Material theme.
* **Configuration Management**: YAML files within a `config/` directory, with sensitive values gitignored.

#### 0.2.3. Development Environment Roles
The development environment will leverage the strengths of both local and cloud-based tools:

* **Visual Studio Code (VS Code) - Local**:
    * **Primary Role**: Core development environment for most Python scripts, including data ingestion (scraping), data processing, feature engineering modules, utility functions, and the prediction pipeline. Also used for managing the project repository, Git workflows, local testing, and MkDocs site generation/preview.
    * **Rationale**: Provides a robust and feature-rich local IDE with strong Git integration, debugging capabilities, and direct access to the project's file structure. This is suitable for developing the persistent, production-oriented code in the `src/` directory.
* **Google Colab**:
    * **Primary Role**: Environment for computationally intensive tasks, iterative Exploratory Data Analysis (EDA), rapid prototyping of machine learning models, and training models that benefit from free-tier GPU/TPU access.
    * **Rationale**: Offers a convenient, browser-based environment with pre-installed libraries and easy access to cloud resources (BigQuery, GCS) and hardware acceleration, making it ideal for experimentation and tasks exceeding local hardware capabilities.
* **Rationale for Hybrid Approach**: This delineation allows for structured code development and project management in VS Code, while retaining the flexibility and power of Colab for research, experimentation, and heavy computation. Data exchange will primarily occur via BigQuery and GCS, ensuring consistency.

### 0.3. Proposed Workflow Outline

This workflow outlines the end-to-end process from data acquisition to prediction generation, leveraging the defined tools and environments.

#### 0.3.1. Data Ingestion (Scraping)
* **Environment**: Python scripts developed and executed in VS Code.
* **Process**:
    1. Scrape race data (racecards, results, horse details, etc.) from the Hong Kong Jockey Club (HKJC) website using libraries like `requests` and `BeautifulSoup`.
    2. Perform initial light cleaning and structuring of scraped data within the Python script.
    3. Directly load the structured raw data into designated "raw" tables in Google BigQuery using the `google-cloud-bigquery` Python library (e.g., via `pandas-gbq` or direct API calls).
* **Data Correction**: If discrepancies are found in BigQuery data post-ingestion, they will be addressed by:
    * Prioritized Method: Dedicated Python scripts (developed in VS Code, stored in `src/data_management/`) to execute targeted `UPDATE` statements in BigQuery based on unique row identifiers (e.g., `RACE_ID`, `RUNNER_ID`). This ensures changes are auditable and version-controlled.
    * Secondary/Visual Aid (Consideration): A controlled Google Sheet could be used to *log* desired corrections, which a script then reads to apply to BigQuery. This is not for direct ingestion but as a UI for correction logging if purely script-based updates become cumbersome for many edits.
* **Rationale for Direct BQ Ingestion**:
    * **Robustness & Scalability**: Directly loading to BigQuery from Python scripts is more robust and scalable for automated, periodic scraping tasks compared to using Google Sheets as an intermediary. It reduces potential points of failure, schema mismatch issues, and manual intervention.
    * **Efficiency**: Eliminates the overhead and potential API limitations of writing to and then reading from Sheets.
    * **Control**: Keeps data handling logic within Python scripts, which are version controlled and part of the main project codebase.

#### 0.3.2. Data Cleansing, Preprocessing, and EDA
* **Environment**: Primarily VS Code (using Jupyter notebooks or Python scripts in `src/`) for systematic cleansing and preprocessing; Google Colab for extensive EDA requiring more interactivity or computational power.
* **Process**:
    1. Query raw data from BigQuery into VS Code (or Colab) for analysis.
    2. Perform thorough data cleansing (handling missing values, standardizing categories, type enforcement) and preprocessing (encoding, scaling). This logic will be developed as reusable Python functions/modules in `src/data_processing/` and `src/features/`.
    3. Conduct Exploratory Data Analysis (EDA) to understand data characteristics, identify patterns, and formulate hypotheses. Findings and visualizations will be documented in the relevant `docs/phase-XX-name.md` files (e.g., `docs/phase-03-eda.md`).
    4. Store cleansed and preprocessed data back into new, dedicated tables/views in BigQuery for use in model development.
    5. Store relevant data quality metrics or EDA summary statistics in BigQuery if beneficial for tracking.

#### 0.3.3. Feature Engineering
* **Environment**: Primarily VS Code for defining and scripting feature engineering logic (in `src/features/`); Colab for iterative development and testing of complex features.
* **Process**:
    1. Develop new features based on domain knowledge, EDA insights, and model requirements.
    2. Implement feature creation logic as reusable Python functions.
    3. Apply feature engineering to the cleansed data from BigQuery, storing the engineered feature sets in new BigQuery tables/views.

#### 0.3.4. Model Development and Training
* **Environment**: Google Colab (leveraging GPU/TPU access as needed).
* **Process**:
    1. Load preprocessed data and engineered features from BigQuery into Colab.
    2. Experiment with various machine learning algorithms (from simple baselines to more complex models).
    3. Train models, perform hyperparameter tuning, and use rigorous validation techniques (e.g., time-series aware backtesting).
    4. Save trained model artifacts (e.g., pickled files, SavedModel formats) to **Google Cloud Storage (GCS)**.
        * **Rationale for GCS over Google Drive**: GCS provides better versioning capabilities, programmatic access, and integration with other MLOps tools (like Vertex AI Model Registry). It's a more professional and robust solution for model persistence, and the free tier should cover storage needs.
    5. Register model versions, along with relevant metadata and performance metrics, in **Vertex AI Model Registry**, pointing to the model artifacts in GCS.
        * **Rationale for Vertex AI Model Registry**: Provides a centralized, free-to-use (for registration) service for managing the lifecycle of models, improving organization and reproducibility.

#### 0.3.5. Prediction Generation
* **Environment**: Python scripts developed and executed in VS Code.
* **Process**:
    1. Scrape the latest racecard data (similar to 0.3.1).
    2. Preprocess this new data using the same cleansing and feature engineering logic developed in `src/` and used during training.
    3. Load the desired trained model from Google Cloud Storage (its location potentially retrieved via Vertex AI Model Registry).
    4. Generate predictions for the upcoming races.
    5. Store predictions (e.g., locally as CSV/JSON, or push to a dedicated BigQuery table).

#### 0.3.6. Results Presentation (Future Consideration)
* **Initial**: Predictions might be reviewed via generated files (CSV, text) or simple HTML outputs published to GitHub Pages.
* **Future Enhancement**: Consider developing a simple interactive dashboard using **Streamlit** (run locally or deployed) to display predictions, analyze results, or even provide a UI for specific data management tasks.
    * **Rationale for Streamlit**: Offers a Python-native way to quickly build data-centric web applications without requiring web development expertise, suitable for creating internal tools or simple dashboards as the project matures.

---

## Phase 1: Data Collection and Storage
*(This phase focuses on acquiring all necessary raw data and establishing initial storage.)*

### 1.1. Data Sources
* **Primary Source**: Hong Kong Jockey Club (HKJC) official website.
* **Data Types**: Racecards (upcoming races), race results (historical), horse details, trackwork records, stewards' reports, etc.
* **Historical Data Consideration**: An initial dataset was acquired from a third-party vendor (pre-December 2023) with known minor inconsistencies. Data from December 2023 onwards is to be scraped directly. The project will prioritize direct scraping for ongoing data integrity.

### 1.2. Data Acquisition Methodology
* **Primary Method**: Web scraping using Python libraries (e.g., Beautiful Soup, potentially Playwright/Selenium if needed for dynamic content) executed in Google Colab or local scripts.
* **API Limitations**: HKJC does not offer a public API for comprehensive race data, necessitating web scraping.
* **Scope per Session**: Scraping will likely be batched (e.g., per race day) to manage load and avoid detection.
* **Maintenance**: Scraping scripts will require ongoing maintenance due to potential HKJC website changes.

### 1.3. Preliminary Data Formatting (Post-Scraping)
* **Environment**: Google Colab or local Python scripts.
* **Objective**: Ensure consistency, accuracy, and control over data format before storage. Includes data type enforcement, string manipulation, and basic structural validation.
* **Rationale**: Python scripts provide reproducibility and can handle complex logic more robustly than manual formatting or simple spreadsheet functions.

### 1.4. Data Storage Strategy
* **Raw Data Storage**: Initially, scraped data might be stored in flat files (JSON, CSV) in Google Cloud Storage or locally.
* **Structured Data Storage**: Google BigQuery will serve as the primary data warehouse for cleansed and structured data.
    * **Schema Definition**: A detailed data dictionary (see Appendix A) will define table structures and field types in BigQuery.
* **Intermediary Storage (Original Plan)**: Google Sheets was considered as an editable central repository before loading to BigQuery. This may be revised for a more direct GCS/local files to BigQuery pipeline.
* **Partitioning**: For BigQuery tables, partitioning (e.g., by race date/year) will be considered if data volume grows significantly, to optimize query performance and costs. Not planned initially given projected data sizes.
* **Update Frequency**: New race data will be collected and processed typically twice weekly, aligned with the HKJC racing calendar. The process will be automated as much as possible.

---

## Phase 2: Data Cleansing and Preprocessing
*(This phase focuses on transforming raw collected data into a clean, consistent, and usable dataset.)*

### 2.1. Overview of Collected Data
The dataset will encompass:
* Race identification and context (Date, Course, Race Number, Class, Distance, Going, Prize Money, etc.).
* Horse performance metrics (Finishing Place, Finish Time, Sectional Times, Weight Carried, Draw, etc.).
* Betting information (Win/Place Odds).
* Jockey and Trainer details.
* Pre-race horse information (Horse Weight, Rating, Rest Days, Gear, etc.).
* (Refer to Appendix A: Data Dictionary for detailed schema).

### 2.2. Cleansing Procedure
* **Environment**: Primarily Google Colab or local Python scripts, with results stored in BigQuery.
* **Key Steps**:
    * **Data Type Enforcement**: Ensure columns match predefined types (integer, float, string, date).
    * **String Manipulation**: Trim whitespace, standardize capitalization, handle special characters.
    * **Categorical Value Standardization**: Ensure consistency in fields like `COURSE`, `CLASS`, `GOING`. Map variations to standard values.
    * **Handling Specific Non-Numeric/Placeholder Strings**: Address values like 'UNRATED', 'GRIFFIN', 'DEBUT' in fields that are otherwise numeric or categorical.
    * **Addressing Known Inconsistencies**: Programmatic fixes for known issues in historical data.

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

## Appendix A: Data Dictionary
*(This defines the planned schema for data stored in BigQuery. It may evolve.)*

### A.1. Table: `race_details`
*(Contains details specific to each race event)*

| Column Name      | Data Type | Description                                                                  | Notes/Example                                                                                              |
|------------------|-----------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `RACE_ID`        | INTEGER   | Unique identifier for each race.                                             | Format: `YYYYMMDD` + `RACE_NUM_SEASON` (e.g., `20240414581`). Seasonal race number is 3 digits (e.g., `581`). |
| `DATE`           | DATE      | Date the race was held.                                                      | Format: `YYYY-MM-DD`                                                                                       |
| `COURSE`         | STRING    | Racecourse where the race took place.                                        | Values: `Sha Tin`, `Sha Tin (AWT)`, `Happy Valley`                                                           |
| `RACE_NUM_SEASON`| INTEGER   | The sequential number of the race within the racing season.                    | e.g., `581`                                                                                                |
| `CLASS`          | STRING    | The class of the race.                                                       | e.g., `Class 1`, `Group 1`, `Griffin`                                                                      |
| `DISTANCE`       | INTEGER   | The race distance in meters.                                                 | e.g., `1200`, `1650`                                                                                       |
| `RANKING`        | STRING    | The rating bracket for the race.                                             | e.g., `85-60`                                                                                              |
| `GOING`          | STRING    | Description of surface going.                                                | e.g., `GOOD`, `YIELDING (WET SLOW)`                                                                        |
| `RACE_DESCRIPTION`| STRING   | The official title or name of the race.                                      | e.g., `THE HONG KONG EXCHANGES CHALLENGE CUP HANDICAP`                                                     |
| `TRACK_CONFIG`   | STRING    | The track configuration for the race.                                        | e.g., `TURF - "C" Course`, `ALL WEATHER TRACK`                                                             |
| `PRIZE`          | INTEGER   | The total prize money in HKD for the race.                                   |                                                                                                            |
| `PEN_READING`    | FLOAT     | Penetrometer reading (turf) or Clegg hammer reading (all-weather track).   |                                                                                                            |

### A.2. Table: `race_card` (or `runners`)
*(Contains details for each horse participating in a race, pre-race information)*

| Column Name    | Data Type | Description                                                                    | Notes/Example                                                                                             |
|----------------|-----------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `RUNNER_ID`    | STRING    | Unique identifier for a horse in a specific race.                              | Format: `RACE_ID` + `*` + `HORSE_ID` (e.g., `20240414581*CLEARWIN*H255`)                                    |
| `RACE_ID`      | INTEGER   | Foreign key referencing `race_details.RACE_ID`.                                |                                                                                                             |
| `HORSE_ID`     | STRING    | Unique identifier for the horse (stable across races).                         | Format: `HORSE_NAME` (no spaces/special chars) + `*` + `HORSE_CODE` (e.g., `CLEARWIN*H255`)                 |
| `HORSE_NUM`    | INTEGER   | The number assigned to the horse for that race (usually printed on saddle cloth).| e.g., `1`, `2`, ... `14`                                                                                    |
| `WEIGHT`       | INTEGER   | Total weight carried by the horse (lbs), including jockey and gear.            |                                                                                                             |
| `HORSE_WEIGHT` | INTEGER   | Declared weight of the horse (lbs), usually taken a day or two before the race.|                                                                                                             |
| `DRAW`         | INTEGER   | Starting gate (barrier) number.                                                | Lower numbers are closer to the inside rail.                                                                |
| `JOCKEY`       | STRING    | Jockey's name.                                                                 |                                                                                                             |
| `TRAINER`      | STRING    | Trainer's name.                                                                |                                                                                                             |
| `RATING`       | STRING    | Official HKJC rating of the horse at the time of the race.                     | Numeric string, or `UNRATED` (overseas), `GRIFFIN` (novices).                                               |
| `REST_DAYS`    | STRING    | Number of days since the horse's last run.                                     | Numeric string, or `DEBUT` (first run in HK or ever).                                                       |
| `RACE_AGE`     | STRING    | Age of the horse at the time of the race.                                      | Numeric string, or `UNKNOWN`.                                                                               |
| `GEAR`         | STRING    | Symbols representing gear used by the horse.                                   | e.g., `PC/XB/TT`. See Gear Key below.                                                                     |

**Gear Key (Example - to be confirmed from HKJC source):**

* `B`: Blinkers
* `CP`: Sheepskin Cheek Pieces
* `TT`: Tongue Tie
* `XB`: Crossed Nose Band
* `P`: Pacifier
* `V`: Visor
* `H`: Hood
* `E`: Ear Plugs
* `1` (suffix): First time using this gear.

### A.3. Table: `race_results`
*(Contains the official results for each horse in a race)*

| Column Name     | Data Type | Description                                                              | Notes/Example                                                              |
|-----------------|-----------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `RUNNER_ID`     | STRING    | Foreign key referencing `race_card.RUNNER_ID`.                           |                                                                              |
| `RACE_ID`       | INTEGER   | Foreign key referencing `race_details.RACE_ID`.                          |                                                                              |
| `HORSE_ID`      | STRING    | Foreign key referencing horse identity.                                  |                                                                              |
| `FINISH_POS`    | INTEGER   | Final official finishing position.                                       | `1` for winner, `2` for second, etc. May include codes for non-finishers.  |
| `STARTING_ODDS` | FLOAT     | Decimal odds of the horse just before race start.                        | e.g., `1.8`, `10.5`                                                          |
| `PLACE_PAYOUTS` | FLOAT     | Decimal odds payout for a successful place bet.                            | `0` or `NULL` if unplaced or no payout.                                      |
| `FINISH_TIME`   | FLOAT     | Finishing time of the horse in seconds.                                  | e.g., `71.52`                                                                |
| `SEC_TIME_1`    | FLOAT     | Time taken to finish section 1 (seconds).                                |                                                                              |
| `SEC_TIME_2`    | FLOAT     | Time taken to finish section 2 (seconds).                                |                                                                              |
| `SEC_TIME_3`    | FLOAT     | Time taken to finish section 3 (seconds).                                |                                                                              |
| `SEC_TIME_4`    | FLOAT     | Time taken to finish section 4 (seconds).                                | (Sectional times depend on race distance and course)                         |
| `SEC_TIME_5`    | FLOAT     | Time taken to finish section 5 (seconds).                                |                                                                              |
| `SEC_TIME_6`    | FLOAT     | Time taken to finish section 6 (seconds).                                |                                                                              |
| `DIST_BEATEN`   | FLOAT     | Distance beaten by the winner, in lengths (approx).                      | `0` for winner.                                                              |
| `INCIDENTS`     | STRING    | Notes on any racing incidents involving the horse during the race.         | e.g., "Bumped at start", "Checked near 800m"                               |

### A.4. Table: `horse_register`
*(Contains static details for all registered horses)*

| Column Name         | Data Type | Description                                                              | Notes/Example                                                   |
|---------------------|-----------|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| `HORSE_ID`          | STRING    | Unique identifier for the horse.                                         | Format: `HORSE_NAME` (no spaces/specials) + `*` + `HORSE_CODE`  |
| `HORSE_CODE`        | STRING    | Unique code assigned by HKJC to differentiate horses (esp. same names).  | e.g., `H255`, `D466`                                            |
| `HORSE_NAME`        | STRING    | Official name of the horse.                                              | Raw name, e.g., "DEAN'S ANGEL"                                  |
| `SEX`               | STRING    | Horse's sex.                                                             | `Gelding`, `Mare`, `Colt`, `Filly`, `Horse`, `Rig`              |
| `COLOR`             | STRING    | Color of the horse.                                                      | e.g., `Bay`, `Chestnut`                                         |
| `COUNTRY_OF_ORIGIN` | STRING    | Country where the horse was born.                                        | e.g., `AUS`, `NZ`, `IRE`                                        |
| `IMPORT_TYPE`       | STRING    | Category of entry into Hong Kong racing.                                 | `PP` (Privately Purchased), `PPG` (Privately Purchased Griffin), `ISG` (International Sale Griffin), `VIS` (Visitor) |
| `SIRE`              | STRING    | The horse's father (sire).                                               |                                                                 |
| `DAM`               | STRING    | The horse's mother (dam).                                                |                                                                 |
| `DAM_SIRE`          | STRING    | The sire of the horse's dam (maternal grandsire).                        |                                                                 |
| `OWNER`             | STRING    | Name(s) of the horse's owner(s).                                         |                                                                 |

**Import Type Key (Example):**
* `PP`: Privately Purchased Horses (previously raced elsewhere).
* `PPG`: Privately Purchased Griffins (unraced young horses).
* `ISG`: International Sale Griffins (unraced horses from approved sales).
* `VIS`: Visiting Invitational Horses (invited for specific major races).

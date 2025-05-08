# Phase 1: Project Definition and Establishment

## 1.1 Introduction and Aims

### 1.1.1 Project Objective
* **Goal**: Develop and implement a machine learning-based handicapping and wagering system aimed at generating a positive return on investment (ROI) from Hong Kong horse racing.
* **Team**: Solo project with assistance from Google Gemini.
* **Broader Context**: This project focuses on the technical development of a predictive system for financial gain within the domain of horse race wagering. It's acknowledged that this operates within the context of gambling, and responsible practices should guide any potential future application of the system's outputs.

### 1.1.2 Document Purpose
This document serves several key purposes for the Hong Kong Racing Project:
* **Centralized Record**: Acts as the primary repository for documenting all project plans, methodologies, data sources, findings, and decisions made throughout the project lifecycle. This ensures a comprehensive record of the work undertaken.
* **Shared Memory for AI Collaboration**: Functions as a persistent memory and context for ongoing work and discussions with Google Gemini. By referencing and updating this document, particularly a "Project Status" section (in `docs/project-status.md`), we can ensure continuity across multiple sessions, avoid repeating previous discussions, and efficiently build upon prior work, analyses, and conclusions.
* **Single Source of Truth**: Establishes a definitive reference point for the project's scope, workflow, tools, challenges, and results, reducing ambiguity.
* **Tracking Evolution**: Tracks the project's evolution, including changes in strategy, feature engineering approaches, model selection, and key decisions over time.
* **Workflow for Collaboration**:
    * Start of Session: The latest version of project documentation will be reviewed.
    * Context Review: The "Project Status" section will be reviewed to understand the current project state and immediate next steps.
    * Execution: Work on the project tasks will proceed based on the reviewed status.
    * End of Session Update: The "Project Status" section will be updated to reflect tasks completed, decisions made, and the next steps agreed upon before concluding the session. This ensures the documentation always represents the latest project state.

## 1.2 Resource and Environment Configuration

### 1.2.1 Hardware
* **Local machine**: MacBook Air, 8GB RAM, Apple Silicon (M1 chip).
* **Online**: Standard Colab CPU Environment (e.g., Intel Xeon, ~13 GB RAM).
* **Note**: Google Colab free tier also provides access to GPU (often NVIDIA K80) and TPU accelerators, but availability, specific models, and usage limits are variable and not guaranteed.

### 1.2.2 Software and Cloud Services (Google Ecosystem)
This project primarily utilizes the Google Cloud ecosystem and related tools for data storage, processing, analysis, and machine learning:
* **Google BigQuery**: Serves as the central data warehouse for storing historical and current race data. Used for scalable storage and potentially light data cleaning or querying. Chosen for its scalability, seamless integration with Colab, and cost-effectiveness within the free tier.
* **Google Colab**: The primary environment for data cleaning, analysis, feature engineering, visualization, and machine learning model development and training[cite: 758]. Leverages free tier CPU, GPU, and TPU resources[cite: 759]. Integrates directly with BigQuery and Google Sheets[cite: 759].
* **Google Sheets**: Used as a central hub for managing data before uploading to BigQuery, potentially for manual input or initial formatting, and for controlling updates via Apps Script[cite: 760].
* **Google Apps Script**: Planned for automating the biweekly data update process from Google Sheets to BigQuery[cite: 761].
* **Google Cloud Storage (GCS)**: Considered as an alternative or intermediary step for exporting data from BigQuery (as Parquet files) to Colab, potentially avoiding query costs[cite: 762].
* **Related Python Libraries**:
    * Beautiful Soup: For web scraping HKJC data[cite: 763].
    * pandas, NumPy, Polars: For data manipulation and feature engineering[cite: 764].
    * `google-cloud-bigquery`: For interacting with BigQuery from Colab[cite: 765].
    * Plotly: For interactive data visualization[cite: 765].
    * Machine learning libraries (e.g., Scikit-learn, TensorFlow, PyTorch - specific choices mentioned in Phase 6)[cite: 766].

### 1.2.3 Development Environment (Colab, VS Code)
The project utilizes a combination of cloud-based and local environments for different tasks[cite: 767]:
* **Google Colab**: This is the primary environment for computationally intensive tasks, including[cite: 767]:
    * Data cleaning, exploration (EDA), and visualization (using libraries like Plotly)[cite: 767].
    * Feature engineering using Python libraries (pandas, NumPy, Polars)[cite: 768].
    * Machine learning model development, training, and validation, leveraging Colab's free access to GPU/TPU resources[cite: 768].
    * Direct interaction with Google BigQuery for data querying[cite: 769].
* **Visual Studio Code (VS Code) - Local**: Used on the local machine (MacBook Air) primarily for[cite: 769]:
    * Development of helper scripts, such as those interacting with Google Sheets APIs or potentially Google Apps Script development, if needed outside the cloud editor[cite: 769].
    * Managing code versions locally before potentially pushing to a repository (though version control is currently implicit via Google Docs in the original plan, now shifting to Git with this repo structure)[cite: 770].

## 1.3 Proposed Workflow Outline

### 1.3.1 Rationale for Hybrid Workflow (Sheets -> BigQuery -> Colab)
The chosen workflow utilizes a hybrid approach leveraging Google Sheets, BigQuery (both External and Native tables), and Google Colab[cite: 771]. This specific architecture was selected primarily to balance the critical need for easy data correction with the performance requirements of data analysis and machine learning[cite: 772].
* **Ease of Data Correction**: The primary driver is the need for a straightforward method to correct data inaccuracies[cite: 773]. Historical data contains known minor inconsistencies[cite: 774]. Using Google Sheets as the primary, editable data source allows for quick manual fixes[cite: 775]. BigQuery External Tables link directly to these sheets[cite: 776].
* **Analytical Performance**: To overcome performance limitations of querying Sheets directly, data is periodically materialized into a native BigQuery table[cite: 776]. All downstream analytical tasks query this optimized, native table[cite: 777].
* **Scalability**: Native BigQuery storage provides excellent scalability[cite: 778].
* **Resource Efficiency**: Computationally intensive tasks are offloaded to Google Colab[cite: 779].
* **Integration & Control**: Google ecosystem tools integrate effectively[cite: 780]. Google Sheets, potentially with Apps Script, provides centralized control for refreshing the native BigQuery table[cite: 781].
* **Cost-Effectiveness**: Leverages free tiers of Google Cloud services where possible[cite: 782].
This hybrid model prioritizes straightforward data maintenance via Google Sheets while ensuring query performance for analysis by using native BigQuery tables[cite: 783].

### 1.3.2 Alternative Methodologies Considered
Several alternatives were evaluated and rejected because they didn't adequately balance ease of data correction, analytical performance, scalability, and resource efficiency[cite: 784, 785]:
* **DuckDB (Local) + Colab**:
    * Description: Store data locally in DuckDB, process/clean locally, export to Colab for ML[cite: 785].
    * Pros: Fast local analytics, free[cite: 786].
    * Cons & Why Rejected: Limited by local 8GB RAM; manual data export to Colab; correcting data in DuckDB less straightforward than Sheets[cite: 786, 787].
* **Pandas/Polars (Local only)**:
    * Description: Process data entirely in memory locally[cite: 788].
    * Pros: Flexible for initial exploration[cite: 788].
    * Cons & Why Rejected: Unsustainable on 8GB RAM as data/features grow; lacks BigQuery's persistence and scalability; data correction is ephemeral[cite: 789, 790].
* **SQLite (Local)**:
    * Description: Use SQLite as a local database[cite: 791].
    * Pros: Lightweight, embedded[cite: 791].
    * Cons & Why Rejected: Row-based storage less performant for analytical queries compared to columnar BigQuery; local resource limits still apply[cite: 792, 793].
* **PostgreSQL (Local)**:
    * Description: Run a local PostgreSQL server[cite: 793].
    * Pros: Robust relational database features[cite: 793].
    * Cons & Why Rejected: High overhead and resource demands unsuitable for local hardware[cite: 794, 795].
* **Snowflake (Cloud)**:
    * Description: Use Snowflake as a cloud data warehouse[cite: 796].
    * Pros: Scalable and performant like BigQuery[cite: 796].
    * Cons & Why Rejected: Lacks a comparable free tier to BigQuery, less cost-effective for this project[cite: 797].

The hybrid workflow (Sheets -> External BQ Table -> Native BQ Table -> Colab) was selected as it best balances data correction, performance, scalability, resource efficiency, and cost-effectiveness[cite: 798].

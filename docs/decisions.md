# Key Project Decisions

This document tracks the major design and process decisions for the HK Racing Project, along with context and rationale.

---

### WEEK 1: 2025-05-04

* **Decision:** **Define primary development environment roles: VS Code for core development, Google Colab for EDA & intensive ML.**
    * **Rationale:** Leverages VS Code's strengths for project management & script development, and Colab's strengths for experimentation & hardware acceleration. Clear separation of concerns. (Alternatives: Using only Colab; Using only VS Code).

* **Decision:** **Adopt direct Python-to-BigQuery for raw data ingestion.**
    * **Rationale:** Increases robustness, scalability, and efficiency of the automated scraping pipeline. Reduces manual steps and potential points of failure associated with Sheets intermediary. (Alternatives: Google Sheets as intermediary for raw data; Local files then upload to BQ).

* **Decision:** **Implement data corrections in BigQuery via Python scripts.**
    * **Rationale:** Scripted corrections are version-controllable, auditable, and more robust. A GSheet for *logging* corrections could be a future UI enhancement if needed. (Alternatives: Direct manual edits in BQ console; Google Sheet as a UI for triggering updates).

* **Decision:** **Use Google Cloud Storage (GCS) for storing trained model artifacts.**
    * **Rationale:** GCS offers better versioning, programmatic access, and integration with MLOps tools (like Vertex AI Model Registry). Likely free/low-cost for project scale. (Alternatives: Google Drive; Storing models directly in the Git repository).

* **Decision:** **Utilize Vertex AI Model Registry for model versioning and metadata.**
    * **Rationale:** Provides a centralized, free (for registration) service for managing model lifecycle, improving organization and reproducibility. Points to models in GCS. (Alternatives: Manual tracking in spreadsheets; Custom solution).

* **Decision:** **Defer dashboarding; consider Streamlit for future results presentation.**
    * **Rationale:** Focus on core pipeline first. Streamlit offers a Python-native way to quickly build interactive UIs when predictions are ready. (Alternatives: Dash; Custom HTML/JS; GitHub Pages for static reports).

* **Decision:** **Implement `config/` directory with `config.yaml` (gitignored) and `config.yaml.example` for project settings.**
    * **Rationale:** Centralizes configuration, improves clarity, facilitates different environments (if needed later), and keeps secrets out of version control. (Alternatives: Hardcoding configurations; Environment variables only).

* **Decision:** **Create `src/common/config_loader.py` for loading YAML configurations.**
    * **Rationale:** Provides a standardized, reusable way to access configurations throughout the project. (Alternatives: Ad-hoc loading in multiple scripts).

**Coherence Summary for Week 1:** The decisions in Week 1 collectively establish a robust MLOps foundation. They define clear roles for development environments (VS Code, Colab), establish a direct and script-based data ingestion and correction pipeline (Python to BigQuery), and set up best practices for model artifact storage and versioning (GCS, Vertex AI Model Registry). Configuration management is also addressed systematically. This coherent set of choices prioritizes automation, scalability, and reproducibility from the project's inception, focusing on building a solid technical backbone before tackling UI or dashboarding aspects.

---

### WEEK 2: 2025-05-11

* **Decision:** **Manage `project-status.md` manually instead of script-based generation from Google Sheets for detailed tasks.**
    * **Rationale:** User preference for direct Markdown editing and control. Simplifies tooling if more comfortable with manual updates. (Alternatives: Python script to generate phase-specific task tables; Python script for single task table).

* **Decision:** **Exclude pre-2008 historical data from the project scope.**
    * **Rationale:**
        1.  Data is error-prone and difficult to load/validate in BigQuery.
        2.  Significant missing values for critical data points (win odds, horse weights, HKJC ratings).
        3.  Absence of sectional timings, and concerns about the accuracy of overall finish times.
        4.  Inconsistent false rail configurations prior to the 2008 GPS tracking system introduction, making comparisons with modern data unreliable.
        5.  Lack of advanced timing systems (e.g., precision to two decimal places).
        * The effort to cleanse and integrate this data outweighs the potential benefits, and focusing on 2008+ data ensures higher quality and relevance.
    * **Impact:** Simplifies Phase 1 data collection and Phase 2 cleansing efforts. The `hk_racing_historical_raw` BigQuery dataset will not be created.

* **Decision:** **Refine BigQuery Dataset Strategy for Phase 1.**
    * **`hk_racing_dataset` (Main Dataset):**
        * Will store processed historical data (2008 - November 2023) ingested from user-provided Google Sheets.
        * Target schemas for tables (`results`, `racecard`, `race_details`, `horse_register`) are defined by the user in `Appendix A: Phase 1 Data Dictionary` of the `master-plan`
        * This dataset will also be the target for fully cleansed and integrated analytical data in later phases.
    * **`hk_racing_scraped_raw` (Staging/Raw Dataset):**
        * Will store raw data collected from the HKJC website (December 2023 onwards) after preliminary Python-based formatting.
        * Table structures will initially mirror the scraped data structure.
    * **Rationale:** Clear separation of already processed historical data from newly scraped raw data. Facilitates a focused approach for Phase 1 collection and prepares for Phase 2 cleansing and integration.
    * **Impact:** `config/config.yaml` to be updated with `bq_main_dataset_id` and `bq_scraped_raw_dataset_id`.

* **Decision:** **Confirm target schemas for `hk_racing_dataset` tables.**
    * **Source:** The structure and field definitions provided by the user are adopted as the definitive schemas for the `results`, `racecard`, `race_details`, and `horse_register` tables within the `hk_racing_dataset`.
    * **Impact:** Provides clear targets for the ingestion of processed Google Sheets data. These schemas will be documented in Appendix A of `master-plan.md`.

* **Decision:** **Evaluate Google Cloud Dataform for SQL transformation management in future phases.**
    * **Rationale:** For phases involving significant SQL-based data transformations within BigQuery (e.g., Phase 2: Cleansing, Phase 4: Features), Dataform offers potential benefits for version control, dependency management, testing, and orchestration of SQL workflows. This will be assessed as SQL complexity grows.
    * **Impact:** No immediate change to Phase 1. Local Git repository remains the primary version control for all project assets. Dataform exploration is a consideration for later stages.

**Coherence Summary for Week 2:** The decisions in Week 2 refine the project's data strategy and operational management. Key choices include scoping out problematic pre-2008 data to ensure data quality and relevance, and establishing a clear two-tiered BigQuery dataset structure (`hk_racing_dataset` for processed historical data and `hk_racing_scraped_raw` for new raw data). Confirming the schemas for the main dataset provides a solid foundation for historical data ingestion. The decision to manually manage `project-status.md` reflects a practical choice for task tracking, while the consideration of Dataform for future SQL transformations indicates forward-thinking for later project phases. These decisions collectively streamline the data collection focus and prepare for systematic data processing.

---

### WEEK 3: 2025-05-18

The decisions made in Week 3 demonstrate a clear strategic shift to prioritize the acquisition of a rich historical dataset. They flow logically as follows:

**Strategic Pivot to Historical Data:**

*   **Decision:** Pause scraping of the live HKJC website to prioritize the acquisition of historical data from CSV files spanning 2008-2023.
*   **Rationale:** This recognizes that a deep historical dataset is crucial for robust model training, taking precedence over immediately available current season data.
*   **Impact:** Development focus shifts to tooling for CSV extraction, potentially delaying current data ingestion but significantly enriching the dataset's historical depth.

**Method for Historical Data Acquisition:**

*   **Decision:** Utilize Google Colab for the one-time scraping of these historical CSV reports.
*   **Rationale:** This approach aims to mitigate the risk of IP address blocking during a large, one-off data extraction task by leveraging Colab's environment.
*   **Impact:** Increases the likelihood of successfully acquiring the bulk historical data without interruption.

**Code Management for One-Off Task:**

*   **Decision:** Exclude the historical CSV scraping code from the main project repository and automated pipeline.
*   **Rationale:** As this is a specialized, one-time task dealing with an outdated format, keeping this code separate avoids cluttering the main repository, which is focused on the ongoing, automated pipeline for current data.
*   **Impact:** The main codebase remains lean and focused on reproducible, ongoing processes. The historical scraping script can be archived separately.

**Coherence Summary for Week 3:** These decisions coherently address a strategic goal: secure extensive historical data first. The choice of tool (Colab) supports this goal by minimizing scraping risks, and the decision on code management keeps the main project focused and clean.

---

### WEEK 4: 2025-05-25

Week 4's decisions address the complexities arising from integrating the newly prioritized historical data with current data formats, particularly concerning textual incident reports. There's a clear progression from identifying a problem to exploring a solution and then reacting to implementation challenges:

**Addressing Data Heterogeneity:**

*   **Decision:** Formally acknowledge and plan to address the structural differences between historical race reports (comprehensive, single documents from CSVs) and current HKJC reports (more granular, incident-focused). The goal is to attempt data alignment for a cohesive longitudinal dataset.
*   **Rationale:** To enable consistent analysis and modeling across the entire dataset (2008-present), these different data structures must be reconciled.
*   **Impact:** This necessitates significant data wrangling and transformation efforts. The success of this alignment will heavily influence the analytical capabilities of the combined dataset.

*   **Decision:** **Incorporate "Comments on Running" reports alongside "Full Stewards' Reports" for a comprehensive incident analysis.**
    *   **Rationale:** Initial inspection reveals that Full Stewards' Reports primarily detail the factual nature of incidents (e.g., "horse was bumped, stumbled, and lost lengths"). In contrast, "Comments on Running" often focus on the *implications* or consequences of these incidents from a performance perspective (e.g., "slow in the start"). Utilizing both report types will provide a more holistic understanding of incidents and their impact on a horse's race.
    *   **Impact:** This requires identifying and scraping/extracting "Comments on Running" data, which may have its own distinct format. Data integration strategies will need to account for linking these comments to specific incidents or horses from the stewards' reports. This enriches the dataset for nuanced incident-based feature engineering.

**Proposed Solution for Nuanced Incident Extraction:**

*   **Decision:** Utilize a reasoning model (Large Language Model via API) to interpret and categorize horse-related incidents from textual reports in the historical data.
*   **Rationale:** This approach aims to preserve the nuances often lost in simpler rule-based extraction when trying to map comprehensive older reports to newer, granular incident structures.
*   **Impact:** Introduces an external API dependency and potential costs but offers higher fidelity incident data.

**Challenges and Pausing of API-Based Solution:** This central decision led to a series of sub-decisions based on empirical testing and cost analysis of different LLMs:

*   **Sub-Decision (Gemini Flash 1.5 Preview):** Paused due to hallucination issues (specifically, it provided data related to an incorrect geographical context - South Africa - instead of using the provided Hong Kong data) and potential ongoing API costs beyond initial free tiers. This model (updated on May 20, 2025, offering 500 free prompts) was initially considered the most cost-effective and fast.

    *   **API Pricing:**
        *   **Non-thinking (per 1M tokens):**
            *   Input: $0.15
            *   Output: $0.60
        *   **Thinking (per 1M tokens):**
            *   Input: $0.15
            *   Output: $3.50
    *   **Impact:** Initial preferred cost-effective model proved unreliable for this task.

*   **Sub-Decision (OpenAI GPT-4o mini):** Paused due to slow processing speed and, critically, unexpectedly high "thinking" or processing token consumption (approximately 10 times the input token count). This significantly altered the projected cost, escalating it from an anticipated sub-$20 to over $200 for the required task, making it economically unviable. This was an oversight by the user, unaware that thinking tokens are included in the output token count. (An initial $20 API credit was purchased, only 50c was used, and $19.50 will be used in future if an opportunity arises, or API prices significantly decrease).

    *   **API Pricing (per 1M tokens):**
        *   Input: $1.100
        *   Cached input: $0.275
        *   Output: $4.400
    *   **Impact:** A seemingly viable alternative also became economically unfeasible.

*   **Sub-Decision (Gemini 2.5 Pro Preview):** Paused despite being the best performer in terms of reasoning capabilities among those tested (updated May 06, 2025, offering 25 free messages per day). However, its current API costs are significantly higher than even GPT-4o mini, making it unfeasible for the bulk processing of historical incident reports at this stage.
    *   **API Pricing (per 1M tokens, UI remains free of charge):**
        *   **Input:**
            *   `<=200K tokens`: $1.25
            *   `> 200K tokens`: $2.50
        *   **Output:**
            *   `<=200K tokens`: $10.00
            *   `> 200K tokens`: $15.00
    *   **Impact:** Even the highest quality model tested is currently too expensive for this specific large-scale task.

**Coherence Summary for Week 4:** These decisions coherently outline a problem (differing report structures and the need for comprehensive incident data), a strategy to enrich incident understanding by incorporating both "Stewards' Reports" and "Comments on Running," a sophisticated proposed solution for nuanced data extraction (LLM), and a data-driven rationale for pausing that LLM solution (model unreliability and prohibitive costs identified during testing). This demonstrates a pragmatic approach to R&D and data enrichment within budget constraints. The project will proceed with other alignment tasks while the LLM-dependent component is on hold, but with a clearer path for future incident data integration.

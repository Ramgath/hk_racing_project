# Key Project Decisions

This document tracks the major design and process decisions for the HK Racing Project, along with context, alternatives considered, and rationale.

| Date       | Decision                                                                 | Aspect                      | Alternatives Considered                                                                 | Rationale / Notes                                                                                                                                                              |
|------------|--------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2025-05-10 | Define primary development environment roles: VS Code for core development, Google Colab for EDA & intensive ML. | Development Environment     | Using only Colab; Using only VS Code.                                                   | Leverages VS Code's strengths for project management & script development, and Colab's strengths for experimentation & hardware acceleration. Clear separation of concerns.         |
| 2025-05-10 | Adopt direct Python-to-BigQuery for raw data ingestion.                  | Data Ingestion              | Google Sheets as intermediary for raw data; Local files then upload to BQ.            | Increases robustness, scalability, and efficiency of the automated scraping pipeline. Reduces manual steps and potential points of failure associated with Sheets intermediary. |
| 2025-05-10 | Implement data corrections in BigQuery via Python scripts.               | Data Management             | Direct manual edits in BQ console; Google Sheet as a UI for triggering updates.         | Scripted corrections are version-controllable, auditable, and more robust. A GSheet for *logging* corrections could be a future UI enhancement if needed.                     |
| 2025-05-10 | Use Google Cloud Storage (GCS) for storing trained model artifacts.      | Model Management            | Google Drive; Storing models directly in the Git repository (not suitable for larger models). | GCS offers better versioning, programmatic access, and integration with MLOps tools (like Vertex AI Model Registry). Likely free/low-cost for project scale.                     |
| 2025-05-10 | Utilize Vertex AI Model Registry for model versioning and metadata.        | Model Management            | Manual tracking in spreadsheets; Custom solution.                                       | Provides a centralized, free (for registration) service for managing model lifecycle, improving organization and reproducibility. Points to models in GCS.                   |
| 2025-05-10 | Defer dashboarding; consider Streamlit for future results presentation.    | Visualization / UI          | Dash; Custom HTML/JS; GitHub Pages for static reports.                                  | Focus on core pipeline first. Streamlit offers a Python-native way to quickly build interactive UIs when predictions are ready.                                              |
| 2025-05-10 | Implement `config/` directory with `config.yaml` (gitignored) and `config.yaml.example` for project settings. | Configuration Management    | Hardcoding configurations; Environment variables only.                                    | Centralizes configuration, improves clarity, facilitates different environments (if needed later), and keeps secrets out of version control.                               |
| 2025-05-10 | Create `src/common/config_loader.py` for loading YAML configurations.    | Configuration Management    | Ad-hoc loading in multiple scripts.                                                     | Provides a standardized, reusable way to access configurations throughout the project.                                                                                         |
| 2025-05-11 | Manage `project-status.md` manually instead of script-based generation from Google Sheets for detailed tasks. | Project Management          | Python script to generate phase-specific task tables; Python script for single task table. | User preference for direct Markdown editing and control. Simplifies tooling if more comfortable with manual updates.                                                               |

### 2025-05-11: Refinement of Data Scope and Storage for Phase 1

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
        * Target schemas for tables (`results`, `racecard`, `race_details`, `horse_register`) are defined by the user in `BQ_TABLES - bq tables.csv`.
        * This dataset will also be the target for fully cleansed and integrated analytical data in later phases.
    * **`hk_racing_scraped_raw` (Staging/Raw Dataset):**
        * Will store raw data collected from the HKJC website (December 2023 onwards) after preliminary Python-based formatting.
        * Table structures will initially mirror the scraped data structure.
    * **Rationale:** Clear separation of already processed historical data from newly scraped raw data. Facilitates a focused approach for Phase 1 collection and prepares for Phase 2 cleansing and integration.
    * **Impact:** `config/config.yaml` to be updated with `bq_main_dataset_id` and `bq_scraped_raw_dataset_id`.

* **Decision:** **Confirm target schemas for `hk_racing_dataset` tables.**
    * **Source:** The structure and field definitions provided by the user in the `BQ_TABLES - bq tables.csv` file (uploaded 2025-05-11) are adopted as the definitive schemas for the `results`, `racecard`, `race_details`, and `horse_register` tables within the `hk_racing_dataset`.
    * **Impact:** Provides clear targets for the ingestion of processed Google Sheets data. These schemas will be documented in Appendix A of `master-plan.md`.

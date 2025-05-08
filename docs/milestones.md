# Milestones & Tasks

This document tracks the key milestones and tasks for the HK Racing project. Each task is broken down with goals, reasons for the task, tags, and expected output. As tasks are completed, links to corresponding GitHub Issues will be added.

---

## Phase 1 – Project Definition

 - [ ] **Define Objectives & Success Criteria**
   - **Goal**: Outline the project's primary objectives and success criteria.
   - **Why**: To clearly define the project’s direction and measurable outcomes.
   - **Tags**: project, objectives, success criteria
   - **Output**: A documented list of objectives and success criteria.

 - [ ] **Configure Local & Cloud Environments**
   - **Goal**: Set up local development environment, GCP project, and associated services.
   - **Why**: Ensures all dependencies and cloud services are ready for the project.
   - **Tags**: setup, environment, GCP, local
   - **Output**: Fully configured local dev environment and GCP project with necessary access.

---

## Phase 2 – Data Collection & Storage

 - [ ] **Implement Basic Race Results Scraper**
   - **Goal**: Develop a scraper to retrieve race results from HKJC’s website.
   - **Why**: This scraper will serve as the foundation for data collection.
   - **Tags**: scraping, race results, HTML
   - **Output**: A working scraper saving data in raw format (CSV/JSON).

 - [ ] **Create Raw Data Storage Schema**
   - **Goal**: Design the folder structure for storing raw scraped data.
   - **Why**: Consistent organization of data will simplify processing.
   - **Tags**: storage, data management, schema
   - **Output**: Defined directory structure for raw data in BigQuery/GCS.

 - [ ] **Implement Retry Logic for Scraper Functions**
   - **Goal**: Add retry mechanisms (e.g., tenacity, exponential backoff) to scraper functions.
   - **Why**: To make the scraper more resilient to network failures and HTML structure changes.
   - **Tags**: scraping, retry logic, resilience
   - **Output**: A retry decorator or class that can be reused across scrapers.

---

## Phase 3 – Data Cleansing & Pre-processing

 - [ ] **Implement Data Validation Checks**
   - **Goal**: Ensure the scraped data is valid and clean before processing.
   - **Why**: To ensure that we work with high-quality data from the start.
   - **Tags**: data quality, validation, cleansing
   - **Output**: Validation scripts for data checking.

---

## Future Phases (To be defined later)

 - [ ] **Exploratory Data Analysis (EDA)**
   - **Goal**: Perform initial analysis to understand trends and patterns.
   - **Why**: EDA will guide the feature engineering and modeling steps.
   - **Tags**: analysis, EDA, data exploration
   - **Output**: EDA notebook with key insights.

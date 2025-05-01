# HK Handicapper — Project Overview

*A data science system for modeling, forecasting, and back-testing outcomes in Hong Kong horse racing.*

---

## 📍 Project Purpose

This project aims to build an end-to-end pipeline for collecting, processing, analyzing, and modeling Hong Kong horse racing data to identify value-based wagering strategies. The primary focus is predictive performance modeling, ROI analysis, and deployment of algorithmic betting strategies.

---

## 📅 Planning System

This project is managed using a simple Markdown-based planning structure. We organize work using the following sections:

- **Milestones** – Key deliverables with rough deadlines.
- **Tasks** – Concrete steps to complete under each milestone.
- **Decisions** – Architectural, modeling, or strategy decisions with rationale.
- **Accomplishments** – Completed items with dates and notes.

---

## 🎯 Milestones

| ID   | Name                                | Target Date | Status       |
|------|-------------------------------------|-------------|--------------|
| M1   | Project Bootstrap                   | ✅ Complete  | ✔ Done       |
| M2   | End-to-End Data Ingestion Pipeline  | TBD         | 🔄 In Progress |
| M3   | Exploratory Data Analysis           | TBD         | ⏳ Not Started |
| M4   | First Baseline Model (Win/Place)    | TBD         | ⏳ Not Started |
| M5   | ROI-Positive Backtest (3+ seasons)  | TBD         | ⏳ Not Started |
| M6   | Deployment-Ready Betting Strategy   | TBD         | ⏳ Not Started |

---

## 🛠 Tasks (by Milestone)

### 🔹 M2: End-to-End Ingestion

- [ ] Scrape recent HKJC race meeting data
- [ ] Push sample race to Google Sheets
- [ ] Create BigQuery dataset and table schema
- [ ] Upload historical race card JSONs
- [ ] Write tests for parsing functions
- [ ] Validate schema matches ingestion format
- [ ] Add retry/delay logic to scraper
- [ ] Convert notebook to CLI-friendly script

### 🔹 M3: EDA

- [ ] Create initial EDA notebook
- [ ] Summarize data availability by field and by year
- [ ] Compute race-level and runner-level distributions
- [ ] Plot bias by barrier, rail, and track config

---

## ⚖️ Decisions

| ID       | Decision Area      | Summary                                                   | Date       |
|----------|--------------------|------------------------------------------------------------|------------|
| ADR-0001 | Storage Engine     | Continue using **BigQuery** due to ease of use and flexibility; PostgreSQL may be considered later if needed for local testing or specific workflows. | 2025-05-01 |
| ADR-0002 | Model Target       | TBD – considering win vs. place vs. exotic classification | –          |

---

## ✅ Accomplishments

| Date       | Item                               | Notes                             |
|------------|------------------------------------|-----------------------------------|
| 2025-04-26 | Repo initialized + docs structured | README, LICENSE, .gitignore added |
| 2025-04-30 | Project overview file created      | Initial planning structure adopted|

---

## 📌 Notes

- Historical discontinuity: major Happy Valley renovation in 1995; GPS tracking introduced in Nov 2022.
- Pre-1995 data excluded from predictive model training to reduce noise.
- Planning updates are managed in this file going forward.

---

*Last updated: 2025-05-01*

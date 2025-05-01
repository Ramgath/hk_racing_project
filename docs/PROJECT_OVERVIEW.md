

# HK Handicapper — Project Overview
[![Open issues](https://img.shields.io/github/issues/Ramgath/hk_racing_project)](../../issues) 
[![Last commit](https://img.shields.io/github/last-commit/Ramgath/hk_racing_project)](../../commits/main) 
[![License](https://img.shields.io/github/license/Ramgath/hk_racing_project)](LICENSE)

*A data-science pipeline for Hong Kong horse-racing analytics & ROI-focused wagering.*

---

## 🌍 High-Level Roadmap (Milestones)

| ID | Milestone | Status | Issues linked |
|----|-----------|--------|---------------|
| **M2** | **First end-to-end ingestion**  *(Scraper → Google Sheet → BigQuery)* | 🔄 0 / 8 closed | [#1](../../issues/1) [#2](../../issues/2) [#3](../../issues/3) [#4](../../issues/4) [#8](../../issues/8) [#9](../../issues/9) [#10](../../issues/10) [#11](../../issues/11) |
| **M3** | **Clean EDA notebooks produced** | ⏳ 0 / 1 closed | [#5](../../issues/5) |
| **M4** | **Baseline predictive model trained** *(win-probability)* | ⏳ 0 / 1 closed | [#6](../../issues/6) |
| **M5** | **First positive ROI back-test** | ⏳ 0 / 0 closed | – |
| **M6** | **Deployment of first wagering system** *(simulated bets)* | ⏳ 0 / 0 closed | – |

---

## 📋 Current Backlog & Sprint

<details>
<summary>Open issues (10)</summary>

| ID | Title | Labels | Milestone |
|---:|-------|--------|-----------|
| #11 | **[SCRAPER]** Write unit tests for parsing functions | `scraper` `testing` | M2 |
| #10 | **[SCRAPER]** Validate output schema matches BQ ingestion | `bigquery` `data` | M2 |
| #9  | **[SCRAPER]** Add retry logic and delay handling | `infra` `scraper` | M2 |
| #8  | **[SCRAPER]** Parameterize notebook into Python module | `data` `scraper` | M2 |
| #6  | **[DECISION]** ADR-0002 — Choose primary modeling target | `decision` `modeling` `docs` | M4 |
| #5  | **[TASK]** Create EDA Notebook 01: Data Overview | `docs` `notebook` | M3 |
| #4  | **[TASK]** Set up SQL / dbt for native tables | `bigquery` `infra` | M2 |
| #3  | **[TASK]** Create BigQuery dataset & external table connection | `bigquery` `infra` | M2 |
| #2  | **[TASK]** Push sample meeting into Google Sheet | `data` `scraper` | M2 |
| #1  | **[TASK]** Scrape one recent HK race meeting into DataFrame | `data` `scraper` | M2 |

</details>

---

## ✅ Recently Done
| Date | PR / Issue | Summary |
|------|-----------|---------|
| _yyyy-mm-dd_ | #7 | **GitHub repo bootstrap** |

---

## 🏗️ Architecture Snapshot
```
┌────────────┐      daily          ┌──────────────┐
│   Scraper  ├──────JSON──────────▶│ Google Sheet │
└────────────┘                     └──────┬───────┘
        ▲                                 ▼
        │                       External table
        │    batch load          ┌──────────────┐
        └────────────────────────▶│  BigQuery    │
                                  └─────┬────────┘
                                        ▼
                                Feature matrices ➜  ML / Back-test
```

---

## 🔄 How to update this file
1. Close or open issues ➜ status bars & tables auto-refresh via badges / links.  
2. Edit **`PROJECT_OVERVIEW.md`** when you add a milestone or restructure the board.  
3. Big changes? Tag **@ChatGPT-helper** in a comment and paste the diff — I’ll regenerate the doc.

---


import json
import os
from datetime import datetime

# --- Configuration ---
# Update these values as the project progresses
CURRENT_PHASE = "Phase 1: Definition & Setup"
CURRENT_FOCUS_SUMMARY = (
    "Finalizing project definition, setting up the dynamic project status reporting, "
    "and preparing for initial data collection strategies."
)
# --- End Configuration ---

# Relative paths from the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LAST_SCRAPED_FILE = os.path.join(PROJECT_ROOT, "data", "state", "last_scraped.json")
OUTPUT_MD_FILE = os.path.join(PROJECT_ROOT, "docs", "project-status.md")


def get_last_scraped_date():
    """Fetches the last successful scrape date from the JSON file."""
    try:
        with open(LAST_SCRAPED_FILE, "r") as f:
            data = json.load(f)
        return data.get("last_successful_scrape_date", "N/A")
    except FileNotFoundError:
        return "N/A (file not found)"
    except json.JSONDecodeError:
        return "N/A (invalid JSON)"


def generate_markdown_content():
    """Generates the Markdown content for the project status page."""
    now = datetime.now()
    last_updated_timestamp = now.strftime("%Y-%m-%d %H:%M:%S SAST")  # Added SAST
    last_scraped_date = get_last_scraped_date()

    content = f"""---
title: Project Status
description: Live overview of the HK Racing Project metrics and progress.
---

# Project Status

*Last Updated: {last_updated_timestamp}*

---

## 1. Overall Project Status

- **Current Phase:** {CURRENT_PHASE}
- **Current Focus:** {CURRENT_FOCUS_SUMMARY}

---

## 2. Data Ingestion Metrics

- **Last Successful Scrape Date:** {last_scraped_date}
- **Number of Race Days Scraped:** `[Placeholder - Requires BigQuery query]`
- **Total Number of Races in BigQuery:** `[Placeholder - Requires BigQuery query]`
- **Total Number of Unique Horses in BigQuery:** `[Placeholder - Requires BigQuery query]`
- **Date Range of Data in BigQuery:** `[Placeholder - Oldest Race] - [Placeholder - Newest Race]`

---

## 3. Data Quality Metrics (from BigQuery)

*Examples - to be populated via BigQuery queries:*

- **Missing `FINISH_TIME` (%):** `[Placeholder]`
- **Missing `STARTING_ODDS` (%):** `[Placeholder]`
- **Missing `HORSE_WEIGHT` (%):** `[Placeholder]`
- **Count of 'UNRATED' Horses:** `[Placeholder]`
- **Count of 'GRIFFIN' Entries:** `[Placeholder]`

---

## 4. Feature Engineering Metrics

*To be populated once feature engineering phase begins:*

- **Number of Engineered Features:** `[Placeholder]`
- **Most Impactful Features (Preliminary):** `[Placeholder]`
- **Link to Feature Engineering Notebook:** `[Placeholder]`

---

## 5. Model Performance Metrics

*To be populated once modeling phase begins:*

- **Current Lead Model:** `[Placeholder]`
- **Key Metric (e.g., ROI):** `[Placeholder]`
- **Accuracy:** `[Placeholder]`
- **LogLoss:** `[Placeholder]`
- **Link to Latest Evaluation Report:** `[Placeholder]`

---

## 6. Key Blockers / Risks

*Manual update or link to a dedicated risk log if needed:*

1.  `[Placeholder - e.g., HKJC website structure change impacting scraper]`
2.  `[Placeholder - e.g., Reaching BigQuery free tier limits]`

---

## 7. Upcoming Milestones

*Consider fetching from milestones.md or a structured file:*

- **Next Milestone 1:** `[Placeholder - e.g., Complete initial data ingestion script]`
  - **Target Date:** `[Placeholder - YYYY-MM-DD]`
- **Next Milestone 2:** `[Placeholder - e.g., First EDA notebook published]`
  - **Target Date:** `[Placeholder - YYYY-MM-DD]`

---
"""
    return content


if __name__ == "__main__":
    markdown = generate_markdown_content()
    try:
        with open(OUTPUT_MD_FILE, "w") as f:
            f.write(markdown)
        print(f"Successfully updated: {OUTPUT_MD_FILE}")
    except Exception as e:
        print(f"Error writing to {OUTPUT_MD_FILE}: {e}")

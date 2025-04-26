

# System Architecture Overview 🏗️

## Overview
This project builds a horse racing handicapping and wagering system based on Hong Kong horse races (2008-present).

The **data flow** is structured for high version control, easy human correction, and scalable querying.

---

## High-Level Architecture

```
Web Scraping (VS Code Python)
            ↓
Google Sheets (corrected & versioned data)
            ↓
BigQuery External Table (connected to Sheets)
            ↓
BigQuery Native Tables (cleaned, transformed)
            ↓
VS Code (EDA)         Google Colab (Modeling)
```

---

## Key Design Choices
- Use **Google Sheets** as an intermediate version-controlled source of truth.
- Ingest into **BigQuery** using **External Tables** first.
- Later materialize cleaned data into **Native BigQuery Tables**.
- Model and analyze using both **VS Code** and **Google Colab**.

---

*Document version: v0.1 (Initial bootstrapping phase)*
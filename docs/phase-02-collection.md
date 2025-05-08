# Phase 2 – Data Collection & Storage

---

## 2.1 Source Inventory
- **Racecards pages** (upcoming races)
- **Historical result pages** (per race)
- **Stewards’ reports pages** (meeting summaries)
- **Horse profile pages** (breeding, trackwork, vet records, etc.)
- **Betting odds pages** (pre-race odds snapshots)

---

## 2.2 Access & Authentication
- No API keys required (public website scraping)
- Respect robots.txt and site terms of service
- Rate-limit throttling to avoid hammering the site
- Optional VPN or IP-rotation strategy to mitigate blocking

---

## 2.3 Web-Scraping Design
- **Stack**: BeautifulSoup / Selenium / Playwright choice
- **Pagination & dynamic content** (JS-rendered pages)
- **Retry logic** & exponential back-off on failures
- **HTML parsing**: robust CSS/XPath selectors and schema validation

---

## 2.4 Raw Storage Schema
- **Storage**: Google Cloud Storage (GCS) or BigQuery staging
- **Folder layout**:
  ```
  raw/
  ├── racecards/YYYY-MM-DD/
  ├── results/YYYY-MM-DD/
  ├── stewards/YYYY-MM-DD/
  └── horses/YYYY-MM-DD/
  ```
-- **Formats**: JSON or Parquet for downstream processing

---

## 2.5 Incremental vs Full Loads
- **Full refresh** when meeting date changes or schema updates
- **Delta detection** via on-page timestamps or URL patterns
- **Schedule**: twice weekly (per HKJC calendar) or on-demand before each race meeting

---

## 2.6 Data Ingestion Orchestration
- **Orchestration**: Airflow / Cloud Composer
- **DAG design**:
1. Fetch racecards
2. Scrape results & reports
3. Scrape horse profiles & odds
4. Store raw files in GCS / BQ staging
- **Monitoring & Alerts**: track success/failure counts, notify on missed scrapes

---

## 2.7 Collection Success Metrics
- [ ] ≥ 95% of pages scraped successfully (per meeting)
- [ ] Retry count ≤ 3 per page before alerting
- [ ] SLA: all data available within 1 hour of meeting close

---

> **Next Steps:**
> 1. Review these headings and adjust any items.
> 2. Create GitHub Issues for the first tasks (e.g. “Implement racecards scraper”, “Set up raw storage bucket”).
> 3. As each Issue is closed, fill in its subsection with code snippets and example outputs.

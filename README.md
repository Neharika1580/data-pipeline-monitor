# Data Pipeline Breakage Monitor

## Project Overview
Automated data pipeline that fetches live weather data, runs quality checks, logs results to SQLite, and visualizes pipeline health in Power BI. Scheduled to run daily via GitHub Actions.

## Tech Stack
- **Python** (Requests, Pandas, SQLAlchemy)
- **SQLite** (logging and audit trail)
- **GitHub Actions** (daily automation)
- **Power BI** (dashboard and visualization)

## Quality Checks Implemented
| Check | Threshold | Severity |
|-------|-----------|----------|
| Row count anomaly | ±5% from expected (~168 rows) | CRITICAL |
| Null values | >10 nulls in temperature | WARNING |
| Duplicate timestamps | Any duplicates | CRITICAL |

## Dashboard Features
- Health Score (0-100) with conditional coloring
- PASS/FAIL trend analysis
- Row count monitoring over time
- Filterable by status (PASS/FAIL)

## How to Run Locally
```bash
git clone https://github.com/Neharika1580/data-pipeline-monitor.git
cd data-pipeline-monitor
pip install requests pandas sqlalchemy
python run.py
python export_to_csv.py
# Open Data_pipeline_health_dashboard.pbix in Power BI
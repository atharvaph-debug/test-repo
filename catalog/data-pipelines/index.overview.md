# Data Pipelines

Operational ingestion pipelines, runbooks, schemas, and scheduled workflows for synchronizing transactional databases.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/data-pipelines/analytics-orders-orders-daily | Analytics Orders Daily Table | file | The target BigQuery data warehouse table holding aggregated and structured daily transaction data. |
| catalog/data-pipelines/orders-daily-v3 | Orders Daily Pipeline | file | An Airflow DAG that runs daily at 03:00 UTC to ingest Shopify and Stripe data into BigQuery analytics tables. |

# Pipeline Orchestration & Operations

Technical details, schemas, and operational runbooks for transactional and analytical data pipelines.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/pipeline-orchestration/analytics-orders-orders-daily-table | analytics.orders.orders_daily Table | file | The final target BigQuery table containing normalized and ingested data from payments and eCommerce platforms. |
| catalog/pipeline-orchestration/orders-daily-v3-dag | orders_daily_v3 DAG | file | Airflow DAG that runs daily at 03:00 UTC to ingest, join, and normalize external payments and Shopify order details. |

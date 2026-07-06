# eCommerce Data Modeling

Data pipelines, SQL-ready metrics, schema designs, and database granularity rules.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/ecommerce-data-modeling/order-item-grain | Order Item Grain | file | The fundamental revenue grain where sales, margins, and unit metrics must be computed, mapped at one row per product unit. |
| catalog/ecommerce-data-modeling/orders-daily-etl-pipeline | Orders Daily ETL Pipeline | file | Daily pipeline landing normalized Stripe and Shopify orders raw data into analytics.orders.orders_daily inside BigQuery. |
| catalog/ecommerce-data-modeling/thelook-ecommerce-platform | theLook eCommerce Platform | file | A multi-brand online apparel and accessories retail platform representing the master data set. |

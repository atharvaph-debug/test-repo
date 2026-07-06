# Orders ETL Pipeline Overview

The Orders ETL Pipeline is a daily BigQuery ETL process managed via Airflow. It synthesizes Shopify orders and Stripe transactions.

## Key Features

This pipeline targets the `analytics.orders.orders_daily` table in Google BigQuery. It is scheduled to run daily at 03:00 UTC, with a Service Level Agreement (SLA) set for 05:00 UTC. The process is orchestrated using the Airflow DAG named `orders_daily_v3`.

## Ownership

The Orders ETL Pipeline is jointly owned by:
*   **Technical Owner**: Data Platform Team (`data-platform@company.example`)
*   **Business Owner**: Revenue Analytics (`revenue-analytics@company.example`)

## Source References
* [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

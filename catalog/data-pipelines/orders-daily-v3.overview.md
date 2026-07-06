# Orders Daily Pipeline Overview

The Orders Daily Pipeline, identified as Airflow DAG `orders_daily_v3`, is an essential data pipeline responsible for ingesting Shopify and Stripe data. This pipeline processes data daily and populates BigQuery analytics tables.

## Key Features

*   **Identifier**: The pipeline is an Airflow DAG identified as `orders_daily_v3` \[[OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)\].
*   **Schedule & SLA**: It runs daily at 03:00 UTC and has an operational completion SLA of 05:00 UTC \[[OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)\].
*   **Target Output**: The pipeline targets the BigQuery table `analytics.orders.orders_daily` \[[OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)\].
*   **System Ownership**:
    *   **Technical Pipeline Owner**: The Data Platform Team (`data-platform@company.example`) is responsible for the technical operation of this pipeline \[[OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)\].
    *   **Business Data Owner**: Revenue Analytics (`revenue-analytics@company.example`) holds the business ownership for the data processed by this pipeline \[[OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)\].

## Lineage

This pipeline ingests data from Shopify and Stripe, consolidating it into a BigQuery analytics table for daily reporting and analysis.

## Source References

*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

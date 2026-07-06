# Analytics Orders Daily Table Overview

The Analytics Orders Daily Table (`analytics.orders.orders_daily`) is a target BigQuery data warehouse table designed to store aggregated and structured daily transaction data. It serves as a central repository for processed order-related information.

## Overview

This table, known by its alias `analytics.orders.orders_daily`, is located within BigQuery and represents the final output of a daily data ingestion pipeline.

## Pipeline Details

The data for this table is ingested via an Airflow DAG identified as `orders_daily_v3`. This pipeline is scheduled to run daily at 03:00 UTC and has an operational completion Service Level Agreement (SLA) of 05:00 UTC.

## Ownership

*   **Technical Pipeline Owner**: Data Platform Team (`data-platform@company.example`)
*   **Business Data Owner**: Revenue Analytics (`revenue-analytics@company.example`)

## Lineage

The `analytics.orders.orders_daily` table integrates data from two primary upstream sources:

*   **Stripe Payments API**: Provides payment-related attributes including `payment_intent_id`, `amount_cents`, and `currency`.
*   **Shopify Orders Export**: Contributes order-specific details such as `order_id`, `customer_id`, `total_amount`, and `status`.

Both sources feed into the `BigQuery: analytics.orders.orders_daily` table as part of the ingestion process.

## Source References

*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

# Orders Daily ETL Pipeline Overview

The Orders Daily ETL Pipeline, also known by its aliases `orders-etl-pipeline` and `orders-daily-v3`, is a daily data pipeline responsible for landing normalized raw data from Stripe and Shopify orders into the `analytics.orders.orders_daily` table within BigQuery. This process is crucial for providing a unified view of order data for analytics.

## Overview
This daily pipeline consolidates order information from two primary e-commerce platforms: Stripe (for payment details) and Shopify (for order and customer specifics). The output is a normalized dataset stored in BigQuery, serving as a foundational layer for revenue analytics and data platform operations.

## Operational Details
The pipeline runs daily at 03:00 UTC with a Service Level Agreement (SLA) for completion by 05:00 UTC. It is managed via the Airflow DAG `orders_daily_v3` and is under the ownership of the Data Platform and Revenue Analytics teams.

## Data Sources
The pipeline extracts specific fields from its source systems:
*   **Stripe Payments API**:
    *   `payment_intent_id`
    *   `amount_cents`
    *   `currency`
*   **Shopify Orders Export**:
    *   `order_id`
    *   `customer_id`
    *   `total_amount`
    *   `status` (which can be `pending`, `paid`, or `refunded`)

## Target Schema (`analytics.orders.orders_daily`)
The normalized data is landed into the `analytics.orders.orders_daily` table with the following schema:

*   `order_id` (STRING): Represents the Shopify order ID and serves as the Primary Key for the table.
*   `customer_id` (STRING): Represents the Shopify customer ID and acts as a Foreign Key, joining to the `customers.customer_dim` table.
*   `total_amount_usd` (NUMERIC): The normalized total amount of the order, expressed in USD.
*   `payment_status` (STRING): Indicates the payment state of the order, which can be `pending`, `paid`, or `refunded`.
*   `created_at` (TIMESTAMP): The UTC timestamp when the order was created.

## Source References
*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

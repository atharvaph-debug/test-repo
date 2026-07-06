# orders_daily_v3 DAG Overview

The `orders_daily_v3` DAG is an Airflow Directed Acyclic Graph responsible for orchestrating the daily ETL process for order data. It ingests, joins, and normalizes external payment processing and eCommerce logs into the `analytics.orders.orders_daily` BigQuery table.

## Purpose and Function

This DAG primarily handles the ingestion, joining, and normalization of transaction data from two key sources: the Stripe Payments API and Shopify Orders Export. It standardizes disparate payment and order information into a unified schema within BigQuery, making it available for analytics.

## Schedule and Service Level Agreement (SLA)

The `orders_daily_v3` DAG runs daily at 03:00 UTC. It has a Service Level Agreement (SLA) requiring its completion by 05:00 UTC.

## Data Sources

The pipeline extracts data from the following sources:
*   **Stripe Payments API:** Extracts transaction payment intents, including `payment_intent_id`, `amount_cents`, and `currency`.
*   **Shopify Orders Export:** Extracts store transactions, including `order_id`, `customer_id`, `total_amount`, and `status`.

## Output Schema (`analytics.orders.orders_daily`)

The DAG populates the BigQuery table `analytics.orders.orders_daily` with the following schema:

*   `order_id` (STRING, Primary Key): Directly maps to the Shopify order identifier.
*   `customer_id` (STRING): The Shopify customer identifier, which can be used to join with `customers.customer_dim`.
*   `total_amount_usd` (NUMERIC): The total transaction amount, normalized to United States Dollars (USD).
*   `payment_status` (STRING): The standardized payment status, with possible values of `pending`, `paid`, or `refunded`.
*   `created_at` (TIMESTAMP): The recorded transaction time in Coordinated Universal Time (UTC).

## Ownership

*   **Data Platform Owner:** Data Platform Team (data-platform@company.example)
*   **Business Sponsor:** Revenue Analytics Team (revenue-analytics@company.example)

## Source References

*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

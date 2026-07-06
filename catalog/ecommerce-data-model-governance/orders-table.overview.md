# Orders Table Overview

The `Orders Table` (aliases: `orders`, `orders table`) represents individual checkout events, with each row corresponding to a single, unique order transaction. This transaction can encompass one or more physical items. Its primary role is to track these checkout events and link them to the customer who initiated the order.

## Key Features

*   **Granularity:** Each row in the `Orders Table` represents a single checkout event or order.
*   **Customer Linkage:** The table links to customer information via a `user_id` (conceptually) or `customer_id` (physically in the BigQuery target).
*   **Role in Data Model:** While it captures order-level information, calculations for revenue, units sold, and margin should be executed at the `order_items` grain, not the overall order grain. This is a crucial governance rule to ensure accuracy, as item-level statuses can differ from the parent order's status.

## Schema (`analytics.orders.orders_daily`)

The `analytics.orders.orders_daily` table, a BigQuery target, defines the following key columns:

*   `order_id` (STRING, Primary Key): A unique identifier for each order, directly mapping to the Shopify order identifier.
*   `customer_id` (STRING): The Shopify customer identifier, which joins to `customers.customer_dim` (conceptually `users.id`).
*   `total_amount_usd` (NUMERIC): The total amount of the order, normalized to USD.
*   `payment_status` (STRING): The standardized payment status of the order, with possible values including `pending`, `paid`, or `refunded`.
*   `created_at` (TIMESTAMP): The recorded transaction time in UTC.

## Relationships

The `orders` table maintains the following relationships within the data model:

*   `orders.user_id` $\rightarrow$ `users.id`: Links an order to the customer who placed it.
*   `order_items.order_id` $\rightarrow$ `orders.order_id`: Establishes a one-to-many relationship where one order can have multiple order items.

## Data Lineage & Processing

This table is populated by an ETL pipeline that ingests, joins, and normalizes external payment processing and e-commerce logs into the BigQuery table `analytics.orders.orders_daily`.

### Data Sources

*   **Stripe Payments API:** Provides transaction payment intents, including `payment_intent_id`, `amount_cents`, and `currency`.
*   **Shopify Orders Export:** Supplies core store transaction data such as `order_id`, `customer_id`, `total_amount`, and `status`.

## Data Governance & Usage Rules

*   **Grain Rule for Metrics:** For accurate calculations of revenue, units-sold, and margin, analyses must be performed at the `order-item grain` using the `order_items` table.
*   **Granular Status Mismatch:** Be aware that `order_items.status` can differ from the parent `orders` table's status due to scenarios like partial shipments or individual item returns. For fulfillment and return analytics, metrics should always be calculated directly from `order_items.status`.
*   **Metric Definitions (Calculated from `order_items`):**
    *   **Gross Revenue:** Sum of `order_items.sale_price` where status is not 'Cancelled'.
    *   **Net Revenue:** Sum of `order_items.sale_price` where status is not 'Cancelled' or 'Returned'.
    *   **Average Order Value (AOV):** Gross Revenue divided by the count of distinct `order_items.order_id` where status is not 'Cancelled'.
    *   **Units Sold:** Count of `order_items.id` where status is not 'Cancelled'.

## Pipeline Orchestration

*   **DAG:** `orders_daily_v3` (managed via Airflow).
*   **Execution Time:** Runs daily at 03:00 UTC.
*   **SLA:** Must complete execution by 05:00 UTC.
*   **Data Platform Owner:** Data Platform Team (data-platform@company.example).
*   **Business Sponsor:** Revenue Analytics Team (revenue-analytics@company.example).

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)
*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

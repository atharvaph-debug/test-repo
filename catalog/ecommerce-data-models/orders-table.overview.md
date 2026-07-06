# Orders Table Overview

The `Orders Table`, also known by its alias `orders`, represents individual checkout events at an `order` grain within the eCommerce data model. It serves as a foundational table, relating each order back to a specific customer.

## Key Features

This table captures the details of customer orders and is linked to other core entities in the data model. It relates to the `Users` table via `user_id` and is the parent of the `Order Items` table, with `order_items.order_id` referencing `orders.order_id`. While `Order Items` acts as the central fact table for revenue, the `Orders` table provides the top-level event details for each transaction.

## Schema

The `Orders` table contains several key columns that define an order and its lifecycle:

*   **`order_id`**: The primary key for the `Orders` table, uniquely identifying each order. This originates from the `Shopify Orders Export`.
*   **`user_id`**: A foreign key that links the order to the `users.id` in the `Users` table, representing the customer who placed the order.
*   **`status`**: Indicates the current lifecycle stage of the parent order.
    *   **Processing**: The order has been placed, payment captured, and preparation is underway but not yet shipped.
    *   **Shipped**: The package has physically departed the distribution center.
    *   **Complete**: The order has been successfully delivered, and the return window has closed.
    *   **Returned**: One or more items from the order were sent back.
    *   **Cancelled**: The order was terminated before fulfillment, yielding zero revenue.
    *   *Note*: An individual line item's status (`order_items.status`) can differ from the parent `orders.status`. For accurate fulfillment and return performance metrics, `order_items.status` should be utilized.
*   **`payment_intent_id`**: A transactional field provided by the Stripe Payments API.
*   **`amount_cents`**: The order amount in cents, sourced from the Stripe Payments API.
*   **`currency`**: The currency of the order, also from the Stripe Payments API.
*   **`customer_id`**: An identifier from the Shopify Orders Export, which joins with `customers.customer_dim`.
*   **`total_amount_usd`**: The total amount of the order, normalized to USD, originally `total_amount` from the Shopify Orders Export.
*   **`payment_status`**: Represents the payment status of the order, mapped from Shopify's `status` to `pending`, `paid`, or `refunded`.

## Lineage

The `Orders` table is materialized as `analytics.orders.orders_daily` in Google BigQuery.

### Data Sources
Data for the `Orders` table is synthesized from two primary upstream sources:
1.  **Stripe Payments API**: Contributes transactional fields such as `payment_intent_id`, `amount_cents`, and `currency`.
2.  **Shopify Orders Export**: Provides operational order data, including `order_id` (mapped to `order_id` STRING), `customer_id` (mapped for joining with `customers.customer_dim`), `total_amount` (normalized to USD as `total_amount_usd`), and `status` (mapped to `payment_status` as `pending`, `paid`, or `refunded`).

### ETL Pipeline
The data pipeline runs daily at 03:00 UTC via the Airflow DAG `orders_daily_v3`, with an SLA of 05:00 UTC.

### Ownership
The ownership of this data asset is shared between:
*   **Technical**: Data Platform Team (`data-platform@company.example`)
*   **Business**: Revenue Analytics (`revenue-analytics@company.example`)

## Operational Incidents Mitigation

To ensure data quality and system stability:
*   **Rate Limiting**: If the Stripe API returns rate-limiting errors during ingestion, the process can be re-run using the CLI flag `--max_rps=5`.
*   **Data Volume Anomalies**: Should the output row count fall below 80% of the calculated 7-day median, the on-call engineer is required to page the business owner for validation before initiating any database backfills.

## Related Metrics

While the `Orders` table tracks parent order status, many critical business metrics are derived from the `Order Items` table due to its finer grain. When calculating metrics such as Gross Revenue, Net Revenue, Average Order Value (AOV), Units Sold, and Return Rate, it is crucial to leverage `order_items.status` to ensure accuracy, especially considering the potential for status divergence between parent orders and individual line items.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [theLook eCommerce — Order Lifecycle and Status](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

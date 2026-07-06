# Orders Table Overview

The `Orders` table, aliased as `orders`, represents individual checkout events at the order grain. It serves as a central point for understanding transactions and linking them back to unique customers.

## Key Features

*   **Order Grain**: Each record in the `Orders` table corresponds to a single checkout event.
*   **Customer Linkage**: It links back to the customer via the `user_id` column, which joins to the `users.id` in the `Users` table. Additionally, `customer_id` is available for joining to `customers.customer_dim`.
*   **Order Status**: The table tracks the lifecycle status of an order, including states like `Processing`, `Shipped`, `Complete`, `Returned`, and `Cancelled`.
    *   **Processing**: Order submitted, payment captured, fulfillment not started.
    *   **Shipped**: Parcel departed a distribution center.
    *   **Complete**: Shipment delivered successfully, return eligibility window closed.
    *   **Returned**: One or more items returned by the customer.
    *   **Cancelled**: Cancelled before warehouse fulfillment (generates zero revenue).
*   **Status Discrepancies**: Order states are tracked concurrently at both the macro order level (`orders.status`) and the micro item level (`order_items.status`). Due to partial fulfillments or returns, `order_items.status` may differ from `orders.status`. For example, an order can be `Complete` while a line-item is `Returned`.
*   **Operational Best Practice**: When item-level precision is required for fulfillment and return metrics, calculations should be performed using `order_items.status` rather than `orders.status`.

## Schema

The `orders` table contains the following key columns:

*   **`order_id`** (STRING): The Shopify order ID, serving as the Primary Key for this table.
*   **`customer_id`** (STRING): The Shopify customer ID, used to join to `customers.customer_dim`. (Note: The table also links to customers via `user_id` which references `users.id`).
*   **`total_amount_usd`** (NUMERIC): The transaction value of the order, standardized and expressed in USD.
*   **`payment_status`** (STRING): The payment ingestion status, mapped to one of three values: `pending`, `paid`, or `refunded`.
*   **`created_at`** (TIMESTAMP): The event timestamp of the order, stored in UTC.

## Lineage and Ingestion

The `Orders` table is populated through an automated ingestion pipeline with specific operational details:

*   **Pipeline Identifier**: The Airflow DAG named `orders_daily_v3` is responsible for this ingestion.
*   **Schedule & SLA**: The pipeline runs daily at 03:00 UTC, with an operational completion Service Level Agreement (SLA) of 05:00 UTC.
*   **Target Warehouse Table**: The data is loaded into `analytics.orders.orders_daily` within BigQuery.
*   **System Ownership**:
    *   **Technical Pipeline Owner**: Data Platform Team (`data-platform@company.example`)
    *   **Business Data Owner**: Revenue Analytics (`revenue-analytics@company.example`)

### Primary Ingestion Lineage

The data flows into the `analytics.orders.orders_daily` BigQuery table from two primary sources:

```
[Stripe Payments API]     ---> (payment_intent_id, amount_cents, currency) \
                                                                            ===> [BigQuery: analytics.orders.orders_daily]
[Shopify Orders Export]   ---> (order_id, customer_id, total_amount, status) /
```

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [theLook eCommerce — Order Lifecycle and Status](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)
*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)

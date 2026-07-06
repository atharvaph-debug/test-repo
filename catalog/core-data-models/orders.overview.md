# Orders Overview

The `Orders` entity represents a single checkout event, containing one row per order. It serves as a central point to link customers to the overall fulfillment status of their purchases.

## Key Features

*   **Granularity**: Each row in the `Orders` table corresponds to a unique checkout event.
*   **Customer Linkage**: It links to the `Customer` (`users`) entity via the `user_id` column.
*   **Fulfillment Tracking**: The table tracks the overall fulfillment status of an order. Fulfillment and return cycles are managed through sequential statuses and timestamps, which are present on this table as well as the `order_items` table. While `order_items.status` is used for precise item-level analysis, `Orders` tracks the comprehensive order status.

## Relationships

The `Orders` entity participates in the following relationships:
*   **`orders.user_id`**: Links to `users.id`, connecting an order to the customer who placed it.
*   **`order_items.order_id`**: The `Order Item` entity links back to `orders.order_id`, allowing for granular details of items within a specific order to be associated with their parent order.

## Metrics

While many revenue and inventory metrics are derived from the `order_items` table, the `Orders` entity is directly used in calculating key aggregated metrics such as:
*   **Average Order Value (AOV)**: Calculated as `Gross Revenue / COUNT(DISTINCT order_id)`.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

# Order Items Table Overview

The `Order Items` table, also aliased as `order_items`, serves as the central fact table within the eCommerce data model. It tracks individual transactions at the `order line / sold unit` grain, providing the foundational data for calculating revenue, units sold, and margins. This table is crucial for tying together customers, orders, products, and physical stock units, making it the recommended starting point for analytical queries.

## Key Features

The `Order Items` table acts as the primary hub for transactional analysis. Its granularity at the order line level allows for detailed tracking of what was sold, at what price, and its specific fulfillment status.

## Relationships

The `Order Items` table links various entities across the eCommerce data model through the following foreign key relationships:
*   `order_items.order_id` relates to `orders.order_id` in the `Orders` table, which represents checkout events.
*   `order_items.user_id` relates to `users.id` in the `Users` table, representing the customer associated with the transaction.
*   `order_items.product_id` relates to `products.id` in the `Products` table, detailing the sellable item (SKU).
*   `order_items.inventory_item_id` relates to `inventory_items.id` in the `Inventory Items` table, representing the specific physical unit of stock involved in the transaction.

## Key Columns

*   **`order_id`**: Links to the `Orders` table, identifying the parent order for this specific item.
*   **`user_id`**: Links to the `Users` table, identifying the customer who placed the order.
*   **`product_id`**: Links to the `Products` table, identifying the product being transacted.
*   **`inventory_item_id`**: Links to the `Inventory Items` table, identifying the specific physical stock unit.
*   **`sale_price`**: Represents the actual transaction amount paid by a customer for this order item. This column is the authoritative figure for all revenue computations.
*   **`status`**: Indicates the current lifecycle stage of the individual order item. Unlike the parent `orders.status`, an individual line item's status can differ from the overall order's status. For instance, an order might be `Complete` while a specific item within it was `Returned`. Accurate fulfillment and return performance metrics should always utilize `order_items.status` for precise reporting. Possible statuses include:
    *   **Processing**: The order item has been placed, payment captured, and preparation for fulfillment is underway, but it has not yet shipped.
    *   **Shipped**: The physical package containing this item has departed the distribution center.
    *   **Complete**: The item has been delivered successfully, and its return window has closed.
    *   **Returned**: The item has been sent back by the customer.
    *   **Cancelled**: The fulfillment of this item was terminated before completion, resulting in zero revenue for this specific item.

## Source References
*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [theLook eCommerce — Order Lifecycle and Status](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

# Order Items Table Overview

The `Order Items Table` (also known as `order_items`) serves as the central fact table for financial revenue and metrics within the e-commerce data model. It tracks individual product units purchased within an order, with a grain of one row per unit of a product (order line or sold unit). This table is critical for accurate revenue, units-sold, and margin calculations.

## Key Characteristics

The `order_items` table represents the atomic revenue grain. A single customer order, recorded in the `orders` table, can contain multiple `order_items` entries. For instance, if a user purchases three items, this generates one order but three distinct order items. This fine-grained level is essential for granular analytics.

## Key Columns

The `order_items` table contains several key columns that define the individual units sold and their transactional details:

*   **`order_items.id`**: A unique identifier for each individual order item. This column is used for counting "Units Sold".
*   **`order_items.order_id`**: A foreign key linking to the `orders` table, identifying the parent order to which this item belongs.
*   **`order_items.user_id`**: A foreign key linking to the `users` table, identifying the customer who placed the order.
*   **`order_items.product_id`**: A foreign key linking to the `products` table, specifying the product SKU purchased.
*   **`order_items.inventory_item_id`**: A foreign key linking to the `inventory_items` table, pointing to the specific physical unit of stock.
*   **`order_items.sale_price`**: The final amount the customer actually paid for a single unit. This column is considered the single source of truth for transactional revenue and may differ from the `products.retail_price` due to promotions or markdowns.
*   **`order_items.status`**: Indicates the current status of the individual order item. This is crucial for accurate financial and operational analytics, as item-level statuses can differ from the parent order's status (e.g., due to partial shipments or individual item returns). Status values mentioned include 'Cancelled' and 'Returned'.

## Relationships

The `order_items` table is connected to several other core entities in the data model via foreign keys:

*   `order_items.order_id` $\rightarrow$ `orders.order_id`
*   `order_items.user_id` $\rightarrow$ `users.id`
*   `order_items.product_id` $\rightarrow$ `products.id`
*   `order_items.inventory_item_id` $\rightarrow$ `inventory_items.id`

## Critical Business Rules and Metrics

*   **Grain Rule**: All revenue, units-sold, and margin calculations **must** be executed at the order-item grain (`order_items`), not at the overall order grain.
*   **Granular Status Mismatch**: For accurate fulfillment and return analytics, metrics must be calculated directly from `order_items.status`, as it can vary independently from the `orders` table's status.

The `order_items` table is foundational for calculating key business metrics:

*   **Gross Revenue**: The sum of `order_items.sale_price` for all items where the status is not 'Cancelled'.
    $$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Net Revenue**: The sum of `order_items.sale_price` for all items where the status is neither 'Cancelled' nor 'Returned'. This represents gross revenue minus returns.
    $$\text{Net Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Average Order Value (AOV)**: Derived by dividing the gross revenue by the count of unique orders (based on `order_items.order_id`) where the status is not 'Cancelled'.
    $$\text{AOV} = \frac{\sum (\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}} \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Units Sold**: The total volume of item-level lines processed, excluding any items with a 'Cancelled' status.
    $$\text{Units Sold} = \text{COUNT}(\text{order\_items.id}) \quad \text{where status} \neq \text{'Cancelled'}$$

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
* [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

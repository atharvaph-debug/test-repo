# Order Items Table Overview

The `Order Items` table, also referred to as `order_items` or `Order Item`, serves as the central fact table within the eCommerce database. It represents individual units of a product purchased within a checkout session, with a grain of one row per product unit in an order. This table is crucial for revenue analysis, tying together identifiers for the customer, the order, the product, and the specific inventory item.

## Key Features and Role

The `order_items` table acts as the revenue grain of the company, meaning that revenue, margin, and units-sold calculations are performed at this item level rather than at the parent order level. This allows for granular analysis of product performance and financial metrics.

## Lineage and Relationships

The `order_items` table is central to understanding the full lifecycle of a purchase. It connects to several other core tables:
*   `order_items.order_id` links to the `orders` table, representing the overarching purchase event.
*   `order_items.user_id` links to the `users` table, identifying the customer who placed the order.
*   `order_items.product_id` links to the `products` table, which represents the sellable product variant (SKU).
*   `order_items.inventory_item_id` links to the `inventory_items` table, representing the specific physical unit of stock that was sold.

In summary, a customer (`users`) places an order (`orders`) comprised of order lines (`order_items`). Each order item links back to a physical product variant (`products`) and the specific stock unit (`inventory_items`) shipped out of a warehouse (`distribution_centers`).

## Key Columns

The `order_items` table contains critical information for transactional and analytical purposes:
*   **`order_id`**: A foreign key linking to the `orders` table, identifying the order this item belongs to.
*   **`user_id`**: A foreign key linking to the `users` table, identifying the customer associated with this order item.
*   **`product_id`**: A foreign key linking to the `products` table, identifying the specific product variant sold.
*   **`inventory_item_id`**: A foreign key linking to the `inventory_items` table, identifying the particular physical stock unit.
*   **`sale_price`**: The actual price paid by the customer after any promotions or markdowns. This is the authoritative figure for all revenue metrics.
*   **`status`**: Tracks the fulfillment cycle of the individual order item. This status can diverge from the parent order's status and must be used for item-level analysis.
*   **`shipped_at`**: A timestamp indicating when the package departed the distribution center.
*   **`delivered_at`**: A timestamp indicating when the package was delivered to the customer.
*   **`returned_at`**: A timestamp indicating when the item was returned by the customer. Setting this reverses the revenue and margin for the line item.

## Item Status Transitions

The `order_items.status` column tracks the lifecycle of an individual item within an order, with possible values including:
*   **`Processing`**: The order has been placed, payment captured, and preparation is underway at the distribution center.
*   **`Shipped`**: The package has departed the distribution center (`shipped_at` is set).
*   **`Complete`**: The package has been delivered to the customer (`delivered_at` is set) and the return window has closed.
*   **`Returned`**: The item has been returned by the customer (`returned_at` is set), which reverses the revenue and margin of that specific line item.
*   **`Cancelled`**: The item was aborted prior to fulfillment, meaning it generates no revenue and is excluded from all metrics.

## Key Metrics and Financial Concepts

The `order_items` table, specifically the `sale_price` and `status` columns, are fundamental for calculating various financial and operational metrics:

*   **Gross Revenue**: The sum of sales prices for all items that were not cancelled.
    $$\text{Gross Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Net Revenue**: Realized revenue after accounting for returns and cancellations.
    $$\text{Net Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Average Order Value (AOV)**: Derived by dividing Gross Revenue by the count of distinct orders.
    $$\text{AOV} = \frac{\sum(\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}} \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Units Sold**: The total physical items purchased.
    $$\text{Units Sold} = \text{COUNT(order\_items.id)} \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Return Rate**: The percentage of sold units that were subsequently returned.
    $$\text{Return Rate} = \frac{\text{COUNT(order\_items with returned\_at IS NOT NULL)}}{\text{COUNT(order\_items where status} \neq \text{'Cancelled')}}$$
*   **Gross Margin**: The dollar profit on a unit prior to operating expenses, requiring a join with `products` to get the `cost`.
    $$\text{Gross Margin} = \sum(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Gross Margin %**: The net margin ratio relative to net sales.
    $$\text{Gross Margin \%} = \frac{\text{Gross Margin}}{\text{Net Revenue}}$$

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

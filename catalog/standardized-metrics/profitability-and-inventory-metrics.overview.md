# Profitability and Inventory Metrics Overview

Profitability and Inventory Metrics define key performance indicators that measure catalog efficiency, profit margins, and distribution times for products. These standardized formulas are crucial for aligning business understanding and ensuring unified reporting across an organization. They rely on detailed transactional and inventory data to provide insights into sales performance, cost effectiveness, and inventory management.

## Key Metrics and Formulas

This catalog entry defines the canonical mathematical formulas for several core profitability and inventory metrics, mapped directly to warehouse schema columns.

### Gross Margin
Gross Margin represents the profit generated from sales after deducting the direct cost of goods sold.
**Formula:**
$$ \text{SUM}(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'}) $$
This calculation requires joining `order_items.product_id` to `products.id`. The `order_items.sale_price` is the actual price paid by the customer, and `products.cost` is the wholesale or landed cost paid by the company for a unit. Orders and items that are 'Cancelled' or 'Returned' are excluded from this metric.

### Gross Margin %
Gross Margin Percentage expresses Gross Margin as a proportion of Net Revenue, indicating the profitability efficiency of sales.
**Formula:**
$$ \frac{\text{Gross Margin}}{\text{Net Revenue}} $$
Net Revenue is calculated as the sum of `order_items.sale_price` for items where the `status` is not 'Cancelled' or 'Returned'.

### Sell-Through Rate
The Sell-Through Rate measures the percentage of inventory sold compared to the total inventory available during a period.
**Formula:**
$$ \frac{\text{COUNT}(\text{inventory\_items WHERE sold\_at IS NOT NULL})}{\text{COUNT}(\text{inventory\_items})} $$
This metric counts inventory items that have a `sold_at` timestamp, indicating they have been sold, against all inventory items.

### Average Days in Inventory
Average Days in Inventory quantifies the average number of days an inventory item remains in stock before being sold.
**Formula:**
$$ \text{MEAN}(\text{sold\_at} - \text{created\_at}) \quad \text{over sold inventory items} $$
This metric calculates the mean difference between the `sold_at` and `created_at` timestamps for all inventory items that have been sold.

### Return Rate
Return Rate indicates the proportion of sold items that are subsequently returned by customers.
**Formula:**
$$ \frac{\text{COUNT}(\text{order\_items WHERE returned\_at IS NOT NULL})}{\text{COUNT}(\text{order\_items WHERE status} \neq \text{'Cancelled'})} $$
The numerator counts `order_items` that have a `returned_at` timestamp, while the denominator includes all `order_items` that were not cancelled, representing items potentially delivered.

## Underlying Data Concepts and Schema

These metrics rely on specific data points and grains within the data warehouse schema. The `order_items` table serves as the central fact table for revenue and item-level status.

### Key Data Elements
*   **`order_items.sale_price`**: The actual price paid by the customer for a single product unit within an order. This is the authoritative figure for realized revenue and may differ from `products.retail_price` due to discounts or promotions.
*   **`products.cost`**: The wholesale or landed cost that the company paid the supplier for a product unit. This cost is never exposed to customers and is found in both `products.cost` and `inventory_items.cost`.
*   **`order_items.status`**: Tracks the lifecycle state of individual product units within an order. It is crucial for accurate financial models, as orders can be partially returned or split. Key statuses affecting these metrics include:
    *   **'Cancelled'**: The order item was halted prior to fulfillment and generates zero revenue.
    *   **'Returned'**: One or more items were returned by the customer, reversing revenue and margin.
*   **`inventory_items.sold_at`**: A timestamp indicating when a specific physical unit of stock was sold.
*   **`inventory_items.created_at`**: A timestamp indicating when a specific physical unit of stock was created or entered inventory.
*   **`order_items.returned_at`**: A timestamp indicating when an `order_item` was returned by the customer. This is leveraged in the Return Rate calculation.

### Data Grains and Relationships
*   **Order Item**: A single unit of a single product within an order, representing the revenue grain where metrics like revenue, margin, and units-sold are computed. The `order_items` table links to `products` via `order_items.product_id` and to `inventory_items` via `order_items.inventory_item_id`.
*   **Product**: Defined in the `products` table, which holds `cost` information.
*   **Inventory Item**: Defined in the `inventory_items` table, tracking individual physical units of stock with `sold_at` and `created_at` timestamps. Product attributes are denormalized onto `inventory_items` (under `product_*` prefix columns) for simplified inventory queries. However, the `products` table remains the authoritative master for product details.

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

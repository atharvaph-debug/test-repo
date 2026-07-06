# Profitability and Efficiency Metrics Overview

This entry outlines the standardized mathematical models and formulations used to assess key business performance indicators, including margins, return rates, inventory sell-through velocity, and warehouse holding times. These canonical metric formulations establish a consistent semantic layer by mapping commerce metrics directly to underlying database columns, supporting robust metadata enrichment.

## Key Metric Formulations

The following are the defined calculations for core profitability and efficiency metrics:

*   **Gross Revenue:** The sum of sales prices for all order items that have not been cancelled. This is derived from `order_items.sale_price` where the item status is not 'Cancelled'.
    $$\text{Gross Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Net Revenue:** Represents the realized revenue after excluding both cancellations and returns. It sums `order_items.sale_price` for items whose status is neither 'Cancelled' nor 'Returned'.
    $$\text{Net Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Average Order Value (AOV):** Calculated as the total Gross Revenue divided by the distinct count of orders, providing the average spending per order at the order level, derived from item-level sale prices.
    $$\text{AOV} = \frac{\text{Gross Revenue}}{\text{COUNT(DISTINCT order\_items.order\_id)}}$$
*   **Units Sold:** The total count of individual items purchased, explicitly excluding any cancelled items.
    $$\text{Units Sold} = \text{COUNT(order\_items.id)} \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Return Rate:** The proportion of units sold that were subsequently returned. It is calculated by dividing the count of inventory items with a `returned_at` timestamp by the total count of sold items (excluding cancellations).
    $$\text{Return Rate} = \frac{\text{COUNT(order\_items WHERE returned\_at IS NOT NULL)}}{\text{COUNT(order\_items WHERE status} \neq \text{'Cancelled')}}$$
*   **Gross Margin:** Represents the profit before operating costs. This calculation requires joining sales data with product catalog information to subtract the wholesale cost from the sale price, specifically for items that were neither cancelled nor returned. `order_items.sale_price` and `products.cost` are the key financial fields.
    $$\text{Gross Margin} = \sum(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Gross Margin %:** The Gross Margin expressed as a percentage of Net Revenue.
    $$\text{Gross Margin \%} = \frac{\text{Gross Margin}}{\text{Net Revenue}}$$
*   **Sell-Through Rate:** The proportion of the total stock that has been successfully sold. This is determined by dividing the count of `inventory_items` that have a `sold_at` timestamp by the total count of `inventory_items`.
    $$\text{Sell-Through Rate} = \frac{\text{COUNT(inventory\_items WHERE sold\_at IS NOT NULL)}}{\text{COUNT(inventory\_items)}}$$
*   **Average Days in Inventory:** The mean duration an individual unit of stock remains in the warehouse inventory from its creation until it is sold. This is calculated as the average difference between `sold_at` and `created_at` timestamps for all sold `inventory_items`.
    $$\text{Average Days in Inventory} = \text{AVG(sold\_at} - \text{created\_at}) \quad \text{over sold inventory items}$$

## Underlying Data Concepts

The accurate calculation of these metrics relies on a clear understanding of several core data definitions and granularities:

*   **Order Item Grains:** `Order Item` is the authoritative revenue grain. Core performance metrics, including revenue and margin, must be computed at this grain using `order_items.sale_price` and linking to `products.cost`.
*   **Sale Price:** The actual amount paid by the customer after markdowns or promotions, recorded in `order_items.sale_price`, which is the authoritative figure for revenue.
*   **Cost:** The wholesale or landed cost paid to the supplier, found in `products.cost` and `inventory_items.cost`. The `products` table is the authoritative source for cost if conflicts arise with `inventory_items`.
*   **Inventory Item:** Represents a specific physical unit of stock, tracked from its receipt (`created_at`) to its sale (`sold_at`), crucial for inventory-related metrics.
*   **Order Status:** Both order-level and item-level status (e.g., 'Cancelled', 'Returned') are critical for filtering items that impact financial metrics. Specifically, line-item status in `order_items` must be used for precision, as an item's status can affect revenue recognition and return rates.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

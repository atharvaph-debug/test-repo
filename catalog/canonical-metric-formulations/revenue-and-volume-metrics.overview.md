# Revenue and Volume Metrics Overview

This entry defines canonical mathematical representations for evaluating sales performance and order sizes, adjusted for cancelled and returned items. These formulations are critical for consistent business intelligence and metadata enrichment, providing clear semantic definitions for key eCommerce metrics.

## Semantic Definitions & Granularity

Accurate metric calculation relies on consistent business definitions and understanding the data's granularity.

*   **Order vs. Order Item Grains:** While an `Order` represents a single purchase event, an `Order Item` represents a single unit of a product within an order and is considered the authoritative revenue grain. Core performance metrics (revenue, margin, units sold) are computed at the `order_items` grain [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)].
*   **Financial Fields:** The `order_items.sale_price` is the actual amount paid by the customer after markdowns or promotions and serves as the authoritative figure for revenue. `products.cost` (or `inventory_items.cost`) represents the wholesale/landed cost paid by theLook, used for margin calculations [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)].

## Data Model & Lineage

The `order_items` table is the central hub of the data model for these metrics, connecting users, orders, products, and inventory units. It is explicitly identified as the "Revenue Fact Grain" [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)].

## Order Lifecycle Impact

The `order_items.status` is crucial for distinguishing between various stages of an order and accurately calculating financial metrics. An item's status, rather than the overall order status, must be used when precision is required for financial impacts [[order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)].

*   **Processing** and **Shipped** statuses represent in-flight revenue.
*   **Complete** status signifies realized revenue.
*   **Returned** items reverse revenue and margin.
*   **Cancelled** items generate no revenue and must be excluded from metrics.

## Core Metric Formulations

These formulations establish a standardized semantic layer by mapping commerce metrics to physical database columns. All revenue-based metrics leverage `order_items.sale_price`, while volume metrics count `order_items.id` or `inventory_items`.

*   **Gross Revenue:**
    The sum of sale prices for all order items that were not cancelled.
    $$\text{Gross Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Net Revenue:**
    Realized revenue after excluding both cancelled and returned items.
    $$\text{Net Revenue} = \sum(\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true), [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)]*

*   **Average Order Value (AOV):**
    The average spending per order, derived from item-level sale prices.
    $$\text{AOV} = \frac{\text{Gross Revenue}}{\text{COUNT(DISTINCT order\_items.order\_id)}}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Units Sold:**
    The count of individual items purchased, excluding those that were cancelled.
    $$\text{Units Sold} = \text{COUNT(order\_items.id)} \quad \text{where status} \neq \text{'Cancelled'}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Return Rate:**
    The proportion of sold units that were subsequently returned, calculated using `returned_at` timestamp.
    $$\text{Return Rate} = \frac{\text{COUNT(order\_items WHERE returned\_at IS NOT NULL)}}{\text{COUNT(order\_items WHERE status} \neq \text{'Cancelled')}}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Gross Margin:**
    Profit before operating costs, computed by subtracting the product cost from the sale price for items that are neither cancelled nor returned. This requires a join between `order_items` and `products` to access `products.cost`.
    $$\text{Gross Margin} = \sum(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Gross Margin %:**
    The Gross Margin expressed as a percentage of Net Revenue.
    $$\text{Gross Margin \%} = \frac{\text{Gross Margin}}{\text{Net Revenue}}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Sell-Through Rate:**
    The proportion of total stock that successfully sold, based on `inventory_items` and their `sold_at` status.
    $$\text{Sell-Through Rate} = \frac{\text{COUNT(inventory\_items WHERE sold\_at IS NOT NULL)}}{\text{COUNT(inventory\_items)}}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

*   **Average Days in Inventory:**
    The mean duration a unit of stock remains in warehouse inventory, calculated from `created_at` to `sold_at` for sold inventory items.
    $$\text{Average Days in Inventory} = \text{AVG(sold\_at} - \text{created\_at}) \quad \text{over sold inventory items}$$
    *Source: [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]*

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

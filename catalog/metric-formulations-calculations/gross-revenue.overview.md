# Gross Revenue Overview

Gross Revenue represents the total sum of `sale_price` for all `order_items`, specifically excluding any transactions where the `status` is 'Cancelled'. This metric provides a view of sales before accounting for returns, discounts, or other adjustments beyond initial cancellations.

## Calculation

Gross Revenue is calculated by summing the `sale_price` for each `order_item` where the transaction status is not 'Cancelled'. All revenue calculations, including Gross Revenue, must be performed at the **order-item grain** (`order_items`).

The formula for Gross Revenue is:

$$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$

## Key Components

The calculation of Gross Revenue relies on the following key data points:

*   **`order_items.sale_price`**: The sales price of an individual item within an order, which is the primary value summed to determine gross revenue.
*   **`status`**: A field indicating the current state of a transaction. For Gross Revenue, transactions with a `status` of 'Cancelled' are explicitly excluded from the sum.
*   **`order_items`**: The granular entity representing individual items within an order. All calculations are performed at this grain.

## Related Metrics

Gross Revenue serves as a foundational metric for other financial calculations and is distinct from similar metrics:

*   **Net Revenue**: While Gross Revenue excludes only 'Cancelled' transactions, Net Revenue further subtracts 'Returned' items.
    $$\text{Net Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Average Order Value (AOV)**: Gross Revenue is a key component in calculating AOV, which is derived by dividing the total Gross Revenue by the count of unique orders (excluding cancelled transactions).
    $$\text{AOV} = \frac{\sum (\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}} \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Units Sold**: Similar to Gross Revenue, Units Sold also excludes cancelled transactions but counts the volume of item-level lines (`order_items.id`) rather than their monetary value.

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

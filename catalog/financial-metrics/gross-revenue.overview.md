# Gross Revenue Overview

Gross Revenue is a key financial metric representing the total sum of sale prices from sold order items, specifically excluding any transactions that were cancelled. It provides a measure of overall sales activity before accounting for returns or other deductions.

## Calculation

Gross Revenue is calculated as the sum of `sale_price` for all `order_items` where the item's `status` is not 'Cancelled'.

$$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$

The `sale_price` refers to the actual price at which an item was sold. Items with a `status` of 'Cancelled' are explicitly excluded from this summation.

## Related Metrics

Gross Revenue serves as a foundational component for other financial metrics:
*   **Net Revenue**: This metric is derived by subtracting returns from Gross Revenue, further excluding both cancelled and returned items.
*   **Average Order Value (AOV)**: AOV is calculated as a ratio measuring the mean gross value of a single order, directly utilizing the summed `order_items.sale_price` which forms the basis of gross revenue.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

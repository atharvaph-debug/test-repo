# Average Order Value Overview

Average Order Value (AOV) is a key financial metric that represents the mean gross monetary value of a single transaction order. It provides insight into the typical amount customers spend per purchase.

## Definition

Average Order Value, also known by its alias AOV, is calculated as the total item sales prices divided by the count of distinct orders. This metric helps understand customer spending habits and the overall financial health of transactions.

## Calculation

The Average Order Value is determined by the following formula:

$$\text{AOV} = \frac{\sum(\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}}$$

Where:
*   The numerator, `SUM(order_items.sale_price)`, represents the sum of the sale prices for all individual items across all orders. This constitutes the total gross monetary value of all transactions.
*   The denominator, `COUNT(DISTINCT order_items.order_id)`, represents the total number of unique orders included in the calculation.

## Related Metrics

*   **Gross Revenue**: While AOV specifically focuses on the *average* value per order, Gross Revenue is defined as the sum of actual sales prices, excluding cancelled items. The numerator of AOV (`SUM(order_items.sale_price)`) is similar to the concept of gross revenue, though the exact status filters might differ.
*   **Net Revenue**: This metric represents gross revenue minus returns, explicitly excluding both cancelled and returned items from the sum of `order_items.sale_price`.
*   **Units Sold**: This refers to the count of order lines that represent successful product shipments, excluding cancelled items.

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

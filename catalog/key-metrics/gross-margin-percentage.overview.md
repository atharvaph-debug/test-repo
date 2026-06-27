# Gross Margin % Overview

Gross Margin % is a key metric that expresses the gross margin as a percentage of net revenue. It provides insight into the profitability of sales after accounting for the cost of goods sold.

## Definition

Gross Margin % is calculated by dividing Gross Margin by Net Revenue.

The components are defined as follows:
*   **Gross Margin:** Calculated as `SUM(order_items.sale_price - products.cost)` for items that are neither `Cancelled` nor `Returned`.
*   **Net Revenue:** Calculated as `SUM(order_items.sale_price)` for items that are neither `Cancelled` nor `Returned`.

## Source References
*   [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

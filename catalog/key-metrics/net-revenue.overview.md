# Net Revenue Overview

Net Revenue represents the total revenue generated after accounting for returned items. It is a key financial metric used to understand the actual income from sales activities, excluding any revenue from cancelled or returned orders.

## Definition and Calculation

Net Revenue is calculated by summing the `sale_price` for items that have not been `Cancelled` and have not been `Returned`.

The formula for Net Revenue is:
```sql
SUM(order_items.sale_price) for items that are neither 'Cancelled' nor 'Returned'
```

## Relationships with Other Metrics

Net Revenue is a foundational component for calculating other financial performance indicators. For example, it is used in the calculation of **Gross Margin %**:
*   **Gross Margin %:** `Gross Margin / Net Revenue`

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

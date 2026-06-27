# Gross Revenue Overview

Gross Revenue represents the total revenue generated from all sold items before accounting for any returns. It is calculated based on the `sale_price` of items from `order_items`.

## Calculation

Gross Revenue is defined as the sum of the `sale_price` for all items in `order_items` where the item's status is not 'Cancelled'.

```sql
SUM(order_items.sale_price) WHERE order_items.status IS NOT 'Cancelled'
```

## Related Metrics

Gross Revenue is a foundational metric used in the calculation of other key performance indicators. For instance, **Average Order Value (AOV)** is derived from Gross Revenue, specifically as `SUM(order_items.sale_price) / COUNT(DISTINCT order_items.order_id)` over non-cancelled items.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

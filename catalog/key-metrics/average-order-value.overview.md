# Average Order Value Overview

Average Order Value (AOV), also known by its alias AOV, represents the average gross revenue generated per order. It is a key metric calculated by dividing the total gross revenue by the number of unique orders.

## Key Features

Average Order Value is calculated using the following formula:
`SUM(order_items.sale_price) / COUNT(DISTINCT order_items.order_id)`

This calculation is performed specifically over non-cancelled items, making it an order-grain metric that utilizes Gross Revenue.

### Related Metrics

*   **Gross Revenue:** This component of AOV is defined as `SUM(order_items.sale_price)` for items whose status is not `Cancelled`.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

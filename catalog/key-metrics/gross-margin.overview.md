# Gross Margin Overview

Gross Margin represents the total profit from sales, calculated as the sum of `sale_price` minus `cost` for all net sales. It is a key metric in the "theLook eCommerce" context, focusing on items that are neither cancelled nor returned.

## Key Features

Gross Margin is calculated using the formula:
`SUM(order_items.sale_price - products.cost)` for items that are not `Cancelled` and not `Returned`.

A related metric, **Gross Margin %**, is also defined as:
`Gross Margin / Net Revenue`.
Net Revenue itself is defined as `SUM(order_items.sale_price)` for items that are neither `Cancelled` nor `Returned`.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

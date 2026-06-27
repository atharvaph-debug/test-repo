# Return Rate Overview

Return Rate is a key metric that quantifies the percentage of units sold that were subsequently returned by customers. It provides insight into product satisfaction and operational efficiency within an eCommerce context.

## Definition

The Return Rate is calculated as the ratio of returned units to sold units. Specifically, it is defined by the following formula:

`COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status <> 'Cancelled')`

*   **Returned units**: Represented by `COUNT(order_items WHERE returned_at IS NOT NULL)`, indicating items for which a return date has been recorded.
*   **Sold units**: Represented by `COUNT(order_items WHERE status <> 'Cancelled')`, referring to items that were not cancelled, thus considered sold. This aligns with the definition of "Units Sold" as `COUNT(order_items.id)` for non-cancelled items.

This metric is one of the core metric definitions for the theLook eCommerce dataset.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

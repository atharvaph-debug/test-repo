# Sell-Through Rate Overview

Sell-Through Rate is a key metric representing the percentage of inventory units that have been sold over a period of time. It provides insight into the efficiency of inventory management and sales performance.

## Definition and Calculation

The Sell-Through Rate is calculated as the ratio of inventory items that have been sold to the total number of inventory items.

It is formally defined as:
`COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)`

This calculation tracks units by counting items from `inventory_items` where a `sold_at` timestamp exists, divided by the total count of all items in `inventory_items`.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

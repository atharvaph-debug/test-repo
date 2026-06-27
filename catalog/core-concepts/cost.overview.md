# Cost Overview

Cost represents the wholesale or landed cost that theLook pays for a product. This value is a crucial component in calculating product profitability and is specifically recorded in the `products.cost` field.

## Key Features

*   **Definition**: Cost refers to the price paid by theLook for a product before any markups for retail sale. This encompasses the wholesale price and any associated landed costs.
*   **Location**: The cost for each product is stored in the `products` table, within the `cost` column.
*   **Role in Profitability**: It is a fundamental element in determining financial metrics like `Gross Margin`. Specifically, `Gross Margin` is calculated as the sum of `(order_items.sale_price - products.cost)` for items that are neither cancelled nor returned.

## Source References

*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

# Inventory Items Table Overview

The `inventory_items` table tracks each physical unit of stock from its creation to its sale, with one row representing a single physical unit. It is a core component of theLook eCommerce data model, providing granular detail on the inventory lifecycle and serving as a critical link between products and customer orders.

## Key Features

The `inventory_items` table provides a detailed record for each physical unit of a product held in stock. Its grain is one row per physical unit, and it tracks the lifecycle of this unit from its creation to its sale. While it may denormalize some product attributes for convenience, the `products` table should always be considered the authoritative source for product attribute data if discrepancies arise.

## Schema and Relationships

This table's primary purpose is to track individual units and their status. Key columns include:

*   **`id`**: A unique identifier for each physical inventory item.
*   **`product_id`**: A foreign key that links the inventory item to its corresponding product in the `products` table.
*   **`created_at`**: A timestamp indicating when the physical unit was first held in stock.
*   **`sold_at`**: A timestamp indicating when the physical unit was sold. This field tracks the completion of the inventory item's lifecycle.

The `inventory_items` table forms crucial relationships within the data model:
*   It is linked to the `products` table via `inventory_items.product_id` to provide product details for each unit.
*   Each `order_item` references the specific `inventory_item` that fulfilled it through the foreign key `order_items.inventory_item_id`.

## Usage for Metrics

The `inventory_items` table is essential for calculating inventory-related metrics:

*   **Sell-Through Rate**: Calculated as `COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)`, this metric indicates the proportion of stock that has been sold.
*   **Average Days in Inventory**: Determined by the mean of `(sold_at - created_at)` over all sold inventory items, this measures how long a unit typically remains in stock before being sold.

## Source References
*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

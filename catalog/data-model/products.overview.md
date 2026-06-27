# Products Table Overview

The `products` table serves as the authoritative source for product attributes within theLook eCommerce data model. Each row in this table represents a single sellable product SKU (Stock Keeping Unit), making its grain one row per product variant ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw), [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).

## Key Features

*   **Product Identifier (SKU)**: The `products.sku` column holds the Stock Keeping Unit, which is the identifier used to track a sellable product variant. This ensures that one SKU uniquely corresponds to one row in the `products` table ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Product Taxonomy**: Products are organized into a three-level hierarchy, allowing for structured classification. This hierarchy includes Department (e.g., Men, Women), Category (e.g., Jeans, Outerwear), and Brand ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Pricing & Cost Information**:
    *   `products.cost`: Represents the wholesale or landed cost paid by theLook for the product ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
    *   `products.retail_price`: Indicates the advertised catalog price for the product ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Distribution**: Each product is assigned to a specific Distribution Center, which is a physical warehouse responsible for stocking and shipping products ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Source of Truth**: While the `inventory_items` table may denormalize product attributes for convenience, the `products` table should be considered the primary source of truth for these attributes if any discrepancies arise ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).

## Relationships

The `products` table is central to understanding order items and inventory:
*   Each `order_item` references a specific product via `order_items.product_id` → `products.id` ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).
*   Each `inventory_item` (a single physical unit of stock) also references a product via `inventory_items.product_id` → `products.id` ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).
*   Products are linked to the warehouses they are stocked in via `products.distribution_center_id` → `distribution_centers.id` ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).

## Usage in Core Metrics

The cost information stored in the `products` table is crucial for financial analysis:
*   **Gross Margin**: Calculated as `SUM(order_items.sale_price - products.cost)` for non-cancelled and non-returned items ([theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)).

## Source References
* [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
* [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)

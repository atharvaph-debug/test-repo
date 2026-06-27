# Stock Keeping Unit Overview

A **Stock Keeping Unit (SKU)** is a unique identifier used to track a sellable product variant. It represents a specific product and its attributes, corresponding to a single row in the `products` table. SKUs are fundamental for managing inventory and sales within the e-commerce system.

## Key Features and Role

*   **Unique Identifier**: Each SKU uniquely identifies a specific product variant, allowing for precise tracking and management.
*   **Product Variant**: It represents a "sellable product variant" ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Core for Products**: One SKU corresponds to one row in the `products` table, which serves as the "authoritative source for product attributes" ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).
*   **Order Item Basis**: An "Order Item" is defined as a "single unit of a single product within an order," and this product is identified by its SKU ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).
*   **Pricing**: Information such as the wholesale/landed `Cost` and the advertised `Retail Price` are associated with the product (and thus the SKU) in the `products` table ([theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)).

## Data Model Integration

The SKU is primarily found in the `products` table as `products.sku`. This table's grain is "one row per sellable product (SKU)," making it the central repository for all product-related attributes ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)). While `inventory_items` may denormalize product attributes, the `products` table should be considered the source of truth for any discrepancies ([theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)).

## Source References

*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)

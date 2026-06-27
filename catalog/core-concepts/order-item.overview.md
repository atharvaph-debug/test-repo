# Order Item Overview

An Order Item represents a single unit of a specific product contained within a customer's order. It serves as the fundamental grain for all revenue, margin, and units-sold calculations within the eCommerce system.

## Key Features

The `Order Item` is a critical entity for understanding sales and product performance. It captures the specific details of a product as it was sold.

*   **Calculation Grain**: It is the granular level at which revenue, margin, and units-sold are calculated.
*   **Pricing**: The `sale_price` attribute records the actual price a customer paid for a unit, making it the basis for all revenue calculations. This can differ from the `retail_price` or `cost` of a product.
*   **Relationship to Products and Inventory**: Each `Order Item` references a `Product` (via its `product_id`) and the specific `Inventory Item` (via `inventory_item_id`) that fulfilled that unit of the order.

## Relationships

An `Order Item` is an integral part of the overall eCommerce data model, linking several core concepts:

*   A **Customer** places an **Order**, which in turn is composed of one or more **Order Items**.
*   Each `Order Item` is associated with a specific **Product** and the individual **Inventory Item** that was sold.
*   Products are stocked in and shipped from **Distribution Centers**.

## Schema

The `order_items` table contains key columns that establish its relationships and record transactional details:

*   `order_items.order_id`: A foreign key referencing `orders.order_id`, linking the item to the overall purchase event.
*   `order_items.user_id`: A foreign key referencing `users.id`, indicating the customer who placed the order.
*   `order_items.product_id`: A foreign key referencing `products.id`, identifying the specific product that was purchased.
*   `order_items.inventory_item_id`: A foreign key referencing `inventory_items.id`, pinpointing the exact physical unit of the product sold.
*   `order_items.sale_price`: The actual price paid by the customer for this specific unit, used for all revenue calculations.

## Source References

*   [theLook eCommerce — Business Glossary](https://drive.google.com/corp/drive/u/0/folders/1e_dIMRmc1PWKxzYQKKp-5lV02hN1dk9L?resourcekey=0-Gfp-QcVibNIPzOiAJ3_tg#1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Data Model and Relationships](https://drive.google.com/corp/drive/u/0/folders/1e_dIMRmc1PWKxzYQKKp-5lV02hN1dk9L?resourcekey=0-Gfp-QcVibNIzPzOiAJ3_tg#1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)

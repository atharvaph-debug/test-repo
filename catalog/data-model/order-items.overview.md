# Order Items Table Overview

The `order_items` table serves as the central fact table within the theLook eCommerce data model, designed to capture each product unit included in an order. It connects all major entities involved in a purchase event, making it the primary starting point for most analytical queries aimed at building a comprehensive knowledge base about the business.

## Key Features and Role

This table's grain is defined as one row per unit of a product within an order, which is crucial for all revenue, margin, and units-sold calculations. It establishes direct links to the customer, the order itself, the specific product purchased, and the inventory item that fulfilled the purchase.

## Schema and Key Columns

The `order_items` table contains critical information about each purchased item, including pricing, status, and event timestamps:

*   **`sale_price`**: This column records the actual price a customer paid for a specific unit. It is the definitive value used for all revenue calculations.
*   **`status`**: This column indicates the item-level fulfillment and return status, and is preferred over `orders.status` for accuracy, especially when an order might be partially returned. Possible statuses include:
    *   **Processing**: The order has been placed and is being prepared, but not yet shipped.
    *   **Shipped**: The order item has left a distribution center.
    *   **Complete**: The order item has been delivered, and its return window has closed.
    *   **Returned**: The item was returned, reversing its associated revenue.
    *   **Cancelled**: The order item was cancelled before fulfillment, resulting in zero revenue.
*   **Event Timestamps**: Key lifecycle events are tracked through specific timestamp columns, enabling detailed cycle-time analysis:
    *   **`created_at`**: The timestamp when the order item was created.
    *   **`shipped_at`**: The timestamp when the order item was shipped.
    *   **`delivered_at`**: The timestamp when the order item was delivered.
    *   **`returned_at`**: The timestamp when the order item was returned.
    These timestamps allow for calculations like Processing Time (`shipped_at - created_at`) and Transit Time (`delivered_at - shipped_at`).

## Table Relationships

The `order_items` table is integral to the overall data model, linking various business entities through foreign keys:

*   **`order_items.order_id`**: Links to `orders.order_id`, connecting the item to its parent order.
*   **`order_items.user_id`**: Links to `users.id`, identifying the customer who placed the order.
*   **`order_items.product_id`**: Links to `products.id`, providing details about the specific product.
*   **`order_items.inventory_item_id`**: Links to `inventory_items.id`, referencing the specific physical unit of stock that fulfilled the item.

## Core Metric Calculations

The `order_items` table is fundamental for calculating several key business metrics:

*   **Gross Revenue**: Calculated as `SUM(order_items.sale_price)` for items whose status is not `Cancelled`.
*   **Net Revenue**: Calculated as `SUM(order_items.sale_price)` for items that are neither `Cancelled` nor `Returned`.
*   **Average Order Value (AOV)**: Computed as `SUM(order_items.sale_price) / COUNT(DISTINCT order_items.order_id)` over non-cancelled items, reflecting gross revenue per order.
*   **Units Sold**: Determined by `COUNT(order_items.id)` for non-cancelled items.
*   **Return Rate**: Measured as `COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status <> 'Cancelled')`.
*   **Gross Margin**: Calculated as `SUM(order_items.sale_price - products.cost)` on non-cancelled, non-returned items, requiring a join to the `products` table for `cost`.

## Source References

*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)
*   [theLook eCommerce — Order Lifecycle and Status](1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

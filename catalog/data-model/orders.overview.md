# Orders Table Overview

The `Orders Table` contains one row for each order or checkout event, serving as a central entity for tracking customer purchases. It links directly to the customer who placed the order via a user identifier.

## Key Features

*   **Grain:** The table's granularity is one row per order or checkout event.
*   **Customer Linkage:** Each order is linked to a specific customer through the `user_id` column, which is a foreign key referencing the `users.id` column in the `users` table.

## Relationships

The `orders` table is integral to the eCommerce data model, establishing key relationships:

*   **Customer to Order:** A `Customer` (from the `users` table) places an `Order` (`orders`). This relationship is defined by the foreign key `orders.user_id` referencing `users.id`.
*   **Order to Order Items:** An `Order` (`orders`) is composed of `Order Items` (from the `order_items` table). This relationship is established through the foreign key `order_items.order_id` referencing `orders.order_id`.

## Order Lifecycle Context

The `orders` table is part of the broader order lifecycle, which encompasses various statuses and event timestamps:

*   **Order Statuses:** The typical order lifecycle progresses through `Processing`, `Shipped`, and `Complete` statuses. Other possible statuses include `Returned` (for items returned from an order) and `Cancelled` (for orders stopped before fulfillment). It's important to note that `order_items.status` is generally preferred over `orders.status` for accurate item-level fulfillment and return metrics, especially since an order can be partially returned.
*   **Event Timestamps:** Key events in an order's lifecycle are tracked using timestamps such as `created_at`, `shipped_at`, `delivered_at`, and `returned_at`. These timestamps enable detailed cycle-time analysis, allowing calculation of metrics like Processing Time (`shipped_at - created_at`) and Transit Time (`delivered_at - shipped_at`).

## Source References
* [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
* [theLook eCommerce — Order Lifecycle and Status](1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

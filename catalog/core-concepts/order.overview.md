# Order Overview

An Order represents a single purchase event placed by a customer, which can contain multiple items. It signifies a distinct checkout event within the e-commerce system.

## Key Features

An Order is a core business concept in theLook eCommerce system, detailing transactions made by customers.
*   **Structure**: A single Order can encompass many individual `Order Items`.
*   **Customer Link**: Each Order is directly linked to the customer who placed it via a `user_id`.
*   **Lifecycle**: Orders progress through a typical lifecycle, including statuses like `Processing`, `Shipped`, and `Complete`. However, for accurate fulfillment and return metrics, the status is tracked at the `order_items` level (`order_items.status`) because an order can be partially returned. Other possible statuses include `Returned` and `Cancelled`.
*   **Event Timestamps**: Key events related to an Order, such as creation, shipment, delivery, and return, are tracked with timestamps (`created_at`, `shipped_at`, `delivered_at`, `returned_at`). These timestamps enable cycle-time analysis like Processing Time and Transit Time.

## Data Model

The `orders` table stores information about each individual order or checkout event.
*   **Grain**: The `orders` table has a grain of one row per order/checkout event.
*   **Relationships**:
    *   It links to the `users` table via `orders.user_id` to identify the customer who placed the order.
    *   An Order is composed of `Order Items`, which are recorded in the `order_items` table. The `order_items` table is considered the central fact table, connecting customers, orders, products, and inventory.

## Core Metrics

Orders are fundamental for calculating several key business metrics:
*   **Average Order Value (AOV)**: This order-grain metric is calculated as the sum of `order_items.sale_price` for non-cancelled items, divided by the count of distinct `order_items.order_id`. It represents the gross revenue per order.

## Source References
*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
*   [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)
*   [theLook eCommerce — Order Lifecycle and Status](1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

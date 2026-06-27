# Event Timestamps Overview

Event Timestamps refer to a set of timestamps (`created_at`, `shipped_at`, `delivered_at`, `returned_at`) that track key events in an order's lifecycle. These timestamps are crucial for performing cycle-time analysis, allowing for the calculation of various operational metrics.

## Key Timestamps and Their Purpose

These timestamps mark specific stages in the fulfillment and delivery process of an order:
*   **`created_at`**: Records when an order was initially placed.
*   **`shipped_at`**: Indicates the moment an order has left a distribution center.
*   **`delivered_at`**: Marks when an order has been successfully delivered.
*   **`returned_at`**: Captures the time an item or order was returned.

## Cycle-Time Analysis

The Event Timestamps enable the calculation of important cycle-time metrics:
*   **Processing Time**: Calculated as the duration between when an order is shipped and when it was created (`shipped_at - created_at`). This measures the time taken for internal order preparation.
*   **Transit Time**: Calculated as the duration between when an order is delivered and when it was shipped (`delivered_at - shipped_at`). This measures the shipping duration.

## Order Lifecycle Context

These timestamps align with the typical stages of an order's lifecycle, which often progresses from `Processing` (order placed, being prepared) to `Shipped` (order has left the distribution center) and finally to `Complete` (order delivered and return window closed). Other statuses include `Returned` and `Cancelled`. While `orders.status` tracks the overall order, `order_items.status` is preferred for item-level accuracy, particularly for fulfillment and return metrics, as parts of an order can be returned.

## Source References
* [theLook eCommerce — Order Lifecycle and Status](1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

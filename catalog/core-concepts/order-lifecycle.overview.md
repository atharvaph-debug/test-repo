# Order Lifecycle Overview

The Order Lifecycle describes the sequence of stages an order progresses through, typically from placement to completion. This core concept defines the various states an order can be in, as well as the key events that mark its progression, enabling detailed analysis of fulfillment and delivery performance.

## Order Lifecycle Stages and Statuses

The typical progression for an order follows `Processing` → `Shipped` → `Complete`. However, orders can also enter `Returned` or `Cancelled` states. Each status signifies a distinct phase in the order's journey:

*   **Processing:** An order has been placed and is currently being prepared for shipment. It has not yet left a distribution center.
*   **Shipped:** The order has departed from a distribution center.
*   **Complete:** The order has been delivered to the customer, and the designated return window has closed.
*   **Returned:** One or more items from the order have been returned by the customer, which reverses the revenue associated with those specific items.
*   **Cancelled:** The order was cancelled prior to being fulfilled, resulting in zero revenue generated from that order.

## Status Granularity

For accurate measurement of fulfillment and return metrics, particularly in scenarios involving partial returns, the `order_items.status` grain is preferred over `orders.status`. This allows for precise tracking of individual item statuses within a single order.

## Key Event Timestamps and Metrics

Several key event timestamps are tracked to facilitate comprehensive cycle-time analysis of the order lifecycle:

*   `created_at`: The timestamp when the order was initially placed.
*   `shipped_at`: The timestamp when the order left the distribution center.
*   `delivered_at`: The timestamp when the order was delivered to the customer.
*   `returned_at`: The timestamp when items from the order were returned.

These timestamps enable the calculation of important metrics such as:

*   **Processing Time:** Calculated as `shipped_at - created_at`.
*   **Transit Time:** Calculated as `delivered_at - shipped_at`.

## Source References
*   [theLook eCommerce — Order Lifecycle and Status](1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

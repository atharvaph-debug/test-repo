# Order Status Overview

Order Status indicates the current state of an order item within theLook eCommerce system. It tracks an item's progression through its lifecycle, from initial placement to delivery or cancellation, and is crucial for understanding fulfillment, returns, and revenue calculations.

## Key Concepts and Lifecycle

The status of an order item reflects its current stage of fulfillment. The typical order lifecycle for an item is `Processing` → `Shipped` → `Complete`.

The defined statuses are:
*   **Processing**: The order has been placed and is being prepared, but has not yet been shipped from a distribution center.
*   **Shipped**: The order item has left a distribution center and is in transit.
*   **Complete**: The order item has been delivered, and its return window has closed.
*   **Returned**: One or more items from the order were returned, which reverses revenue for that specific line item.
*   **Cancelled**: The order was cancelled before fulfillment began, resulting in zero revenue generated for that item.

The status is typically tracked at the `order_items.status` grain, rather than `orders.status`, to provide item-level accuracy for fulfillment and return metrics. This is important because a single order can be partially returned.

Key events in an order item's lifecycle are also tracked via timestamps, including `created_at`, `shipped_at`, `delivered_at`, and `returned_at`. These timestamps enable analysis of various cycle times, such as "Processing Time" (calculated as `shipped_at - created_at`) and "Transit Time" (calculated as `delivered_at - shipped_at`).

## Impact on Metrics

Order Status is a fundamental component in the calculation of several core business metrics:
*   **Gross Revenue**: Includes `SUM(order_items.sale_price)` for items whose status is not `Cancelled`.
*   **Net Revenue**: Includes `SUM(order_items.sale_price)` for items that are neither `Cancelled` nor `Returned`.
*   **Average Order Value (AOV)**: Calculated over non-cancelled items, specifically `SUM(order_items.sale_price) / COUNT(DISTINCT order_items.order_id)`.
*   **Units Sold**: `COUNT(order_items.id)` for non-cancelled items.
*   **Return Rate**: Defined as `COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status <> 'Cancelled')`.
*   **Gross Margin**: Calculated as `SUM(order_items.sale_price - products.cost)` specifically on non-cancelled, non-returned items.

## Source References
*   [theLook eCommerce — Order Lifecycle and Status](https://drive.google.com/corp/drive/u/0/folders/1e_dIMRmc1PWKxzYQKKp-5lV02hN1dk9L?resourcekey=0-Gfp-QcVibNIpPzOiAJ3_tg/1yWKJ3-TRAzZG7zlDH4lqD02m33Y3O44D7OROCy5ng9A)

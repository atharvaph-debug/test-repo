# Lifecycle Status Matrix Overview

The Lifecycle Status Matrix, also known by aliases such as `order-statuses` or `order-lifecycle-status`, is a critical component within the Order Lifecycle & Funnel Latency category. It serves to define the business implications and financial impact associated with various execution states of an order.

This matrix explicitly defines the following key execution states:
*   Processing
*   Shipped
*   Complete
*   Returned
*   Cancelled

These defined statuses are tracked across different levels of the order hierarchy, specifically at the overall order level via `orders.status` and at the granular item level within an order via `order_items.status`.

## Source References
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

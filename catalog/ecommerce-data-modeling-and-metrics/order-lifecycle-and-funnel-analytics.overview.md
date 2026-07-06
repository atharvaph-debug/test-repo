# Order Lifecycle and Funnel Analytics Overview

Order Lifecycle and Funnel Analytics tracks order statuses and chronological timestamp transformations as items transition from checkout to delivery or return. It focuses on states and durations as orders move from inception to completion.

**Aliases**: Order Lifecycle, Timestamps & Funnel Analytics, Status Transitions, Status Discrepancies, Timestamp Event Sequences, Funnel Durations

## Key Concepts

### Status Transitions
The lifecycle for overall order status (`orders.status`) follows a specific sequence:
*   `Processing` $\rightarrow$ `Shipped` $\rightarrow$ `Complete` $\rightarrow$ `Returned` or `Cancelled`.

### Status Discrepancies
It is important to note that the line-item status (`order_items.status`) can differ from the overall order status (`orders.status`). For accurate financial and fulfillment metrics, analysts should use the item-level status.

### Timestamp Event Sequences
Key timestamps capture significant events in an order's lifecycle:
*   `created_at`: Records when an order was placed.
*   `shipped_at`: Records when the package left the distribution center.
*   `delivered_at`: Records when the package reached the customer.
*   `returned_at`: Records when an item was returned by the customer.
A `NULL` value for any of these timestamps indicates that the respective stage has not yet occurred.

### Funnel Durations
Several duration metrics can be derived from the timestamps to analyze funnel performance:
*   `Processing Time` = `shipped_at - created_at`
*   `Transit Time` = `delivered_at - shipped_at`
*   `Return Latency` = `returned_at - delivered_at`

## Source References
*   [theLook eCommerce — Order Lifecycle and Status](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

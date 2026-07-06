# Transit Time Overview

Transit Time is a lifecycle metric calculated as the difference between the delivery timestamp and the shipped timestamp for an order. It represents the duration an item spends in transit after being shipped until it is delivered.

## Calculation
Transit Time is derived from other key timestamps within an order's lifecycle. Specifically, it is calculated using the formula:
*   **Transit Time:** `delivered_at - shipped_at`

Timestamps are populated sequentially as events occur. A `NULL` value for either `delivered_at` or `shipped_at` would indicate that the respective phase has not yet happened, and thus Transit Time cannot be calculated until both timestamps are available. This metric is part of a broader set of cycle-time calculations that track different phases of an order's journey, alongside Processing Time (`shipped_at - created_at`) and Return Latency (`returned_at - delivered_at`).

## Source References
*   [Cycle-Time Calculations](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

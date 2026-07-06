# Processing Time Overview

Processing Time is a lifecycle and time tracking metric defined as the cycle-time calculated by finding the difference between the shipped timestamp and the creation timestamp. It is one of several cycle-time calculations used to track the duration of various phases in an order's lifecycle.

## Definition and Calculation

Processing Time quantifies the duration an item spends in the processing phase. It is calculated using the following formula:

`Processing Time = shipped_at - created_at`

The underlying timestamps (`shipped_at` and `created_at`) are sequentially populated as events occur. A `NULL` value for any of these timestamps indicates that the corresponding phase has not yet taken place.

This metric is part of a broader set of cycle-time calculations, which also include:
*   **Transit Time:** `delivered_at - shipped_at`
*   **Return Latency:** `returned_at - delivered_at`

## Source References
* [Cycle-Time Calculations](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

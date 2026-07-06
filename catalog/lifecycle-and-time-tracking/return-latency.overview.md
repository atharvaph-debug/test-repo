# Return Latency Overview

Return Latency is a key cycle-time metric categorized under Lifecycle and Time Tracking. It quantifies the delay between an item's delivery to a customer and its subsequent return.

## Key Features

This metric is calculated based on specific event timestamps within the order lifecycle. It is defined as the difference between the `returned_at` and `delivered_at` timestamps.

The calculation for Return Latency is:
`returned_at - delivered_at`

A `NULL` value for any of the timestamps involved indicates that the corresponding phase has not yet occurred.

## Source References
* [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

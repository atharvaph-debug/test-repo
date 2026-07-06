# Operational Latency Timestamps Overview

Operational Latency Timestamps are used to measure cycle times and identify bottlenecks within the order lifecycle. This entry outlines calculations for processing time, transit time, and return latency, based on explicit event timestamps.

## Key Latency Metrics and Their Components

Funnel and cycle-time calculations are derived from event timestamps recorded on `orders` and `order_items`. A `NULL` value for a timestamp indicates that the corresponding state has not yet been reached.

The primary latency metrics are defined as follows:

*   **Processing Time**: Measures the duration from order creation to shipment.
    *   **Formula**: `shipped_at - created_at`
*   **Transit Time**: Measures the duration an order spends in transit from shipment to delivery.
    *   **Formula**: `delivered_at - shipped_at`
*   **Return Latency**: Measures the duration from order delivery to its return.
    *   **Formula**: `returned_at - delivered_at`

These calculations rely on the following key timestamp columns:
*   `created_at`: Timestamp indicating when an order was created.
*   `shipped_at`: Timestamp indicating when an order was shipped.
*   `delivered_at`: Timestamp indicating when an order was delivered.
*   `returned_at`: Timestamp indicating when an order was returned.

## Source References
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

# Operational Latency Calculations Overview

Operational Latency Calculations are standardized formulas that utilize timestamps to compute the execution velocity across the logistic lifecycle of orders and order items. These calculations are critical metadata for understanding operational efficiency, pipeline status tracking, and latency diagnostics, as part of a broader metadata enrichment project.

## Key Latency Calculations

These calculations leverage various timestamps recorded during the order lifecycle. A key metadata detail to remember is that timestamps are set to `NULL` if a particular stage has not yet occurred. The definitions are:

*   **Processing Time**: Measures the duration from when an order is created to when it is shipped.
    *   **Formula**: `shipped_at - created_at`
    *   This covers the stage where an order is placed, inventory is prepared, and payment is captured, but shipping has not yet commenced.
*   **Transit Time**: Measures the duration from when an item is shipped to when it is delivered.
    *   **Formula**: `delivered_at - shipped_at`
    *   This represents the period a package is in transit after leaving the distribution center.
*   **Return Latency**: Measures the duration from when an item is delivered to when it is returned.
    *   **Formula**: `returned_at - delivered_at`
    *   This tracks the time taken for a customer to initiate a return after receiving the product.

## Underlying Lifecycle States

These latency calculations are built upon a series of defined lifecycle states for orders and order items. It's important to note that due to potential splits or partial returns, `order_items.status` is the authoritative grain for tracking these states and for accurate operational and financial models, rather than the parent `orders.status`.

The defined states are:

*   **Processing**: The order has been placed, inventory is being prepared, and payment captured, but it has not yet shipped.
*   **Shipped**: The package has departed from the designated distribution center.
*   **Complete**: The order has been successfully delivered to the customer, and the return window is closed.
*   **Returned**: One or more items from the order have been returned by the customer, which reverses associated revenue and margin.
*   **Cancelled**: The order was halted before fulfillment and generates zero revenue.

## Source References

*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

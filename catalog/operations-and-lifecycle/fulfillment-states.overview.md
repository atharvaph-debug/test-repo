# Fulfillment States Overview

Fulfillment States represent the individual logical phases that an order item undergoes, detailing its journey from creation through processing, delivery, and potential returns. This lifecycle tracking is crucial for downstream logging, pipeline status tracking, latency diagnostics, and accurate financial and operational reporting.

## Defined States

The key fulfillment states and their definitions are:

*   **Processing**: The order has been placed, inventory is being prepared, and payment has been captured, but the item has not yet shipped.
*   **Shipped**: The package containing the item has departed from the designated distribution center.
*   **Complete**: The order has been successfully delivered to the customer, and the return window has closed.
*   **Returned**: One or more items have been returned by the customer, which reverses revenue and margin calculations.
*   **Cancelled**: The order was halted prior to fulfillment and generates zero revenue.

## Lifecycle Flow and Timestamps

The typical flow of fulfillment states is sequential, marked by specific timestamps, with a separate path for cancellations:

```
 [Processing] ──(shipped_at)──> [Shipped] ──(delivered_at)──> [Complete] ──(returned_at)──> [Returned]
      │
      └─────────(Cancelled before fulfillment)─────────────────────────────────────────────> [Cancelled]
```

Timestamps are recorded to mark the transition between states and are set to `NULL` if a particular stage has not yet occurred. These timestamps enable the calculation of operational cycle times:

*   **Processing Time**: `shipped_at - created_at`
*   **Transit Time**: `delivered_at - shipped_at`
*   **Return Latency**: `returned_at - delivered_at`

## Status Granularity

It is critical to note that fulfillment states are tracked at the individual `order_items.status` level rather than solely at the parent `orders.status`. This item-level granularity is necessary because orders can be split or partially returned, ensuring accurate operations and financial models.

## Impact on Key Metrics

Fulfillment states play a significant role in the calculation of various business metrics by defining which order items are included or excluded:

*   **Gross Revenue**: Sum of `order_items.sale_price` where `status` is not 'Cancelled'. Cancelled orders generate no revenue.
*   **Net Revenue**: Sum of `order_items.sale_price` where `status` is neither 'Cancelled' nor 'Returned'. Returned and cancelled items are excluded.
*   **Units Sold**: Count of `order_items.id` where `status` is not 'Cancelled'.
*   **Return Rate**: Calculated as the count of `order_items` where `returned_at` is not NULL, divided by the count of `order_items` where `status` is not 'Cancelled'.
*   **Gross Margin**: Sum of (`order_items.sale_price` - `products.cost`) where `status` is neither 'Cancelled' nor 'Returned'. This calculation requires joining `order_items.product_id` to `products.id`.
*   **Gross Margin %**: Calculated as `Gross Margin` divided by `Net Revenue`.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

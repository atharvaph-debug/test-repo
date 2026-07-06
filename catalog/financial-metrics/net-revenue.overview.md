# Net Revenue Overview

Net Revenue is a key financial metric that represents the sum of actual sales prices, after accounting for returns. It specifically excludes both cancelled and returned items from the calculation.

## Definition and Calculation

Net Revenue is defined as the gross revenue minus returns. It is calculated by summing the `sale_price` from `order_items` for all items whose `status` is neither 'Cancelled' nor 'Returned'.

The formula for Net Revenue is:

$$\text{Net Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$

This calculation uses `order_items.sale_price` as the base value for each item and filters out any items with a `status` of 'Cancelled' or 'Returned' to arrive at the final net figure.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

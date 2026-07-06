# Net Revenue Overview

Net Revenue represents the total sum of `sale_price` for order items, specifically excluding those that have been both cancelled and returned. This metric provides a view of actual revenue generated after accounting for items that did not result in a final sale due to cancellation or return.

## Definition and Calculation

Net Revenue is calculated by summing the `sale_price` from `order_items` where the `status` is neither 'Cancelled' nor 'Returned'. It differs from Gross Revenue, which only excludes cancelled items.

The formula for Net Revenue is:

$$\text{Net Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$

## Related Metrics

*   **Gross Revenue**: Gross Revenue is calculated as the sum of `sale_price` for non-cancelled items, making Net Revenue a more refined figure by also accounting for returns.
*   **Average Order Value (AOV)**: While AOV uses the sum of `sale_price` (similar to Gross Revenue) and excludes cancelled items, it normalizes this sum by the distinct count of orders, providing an average value per order rather than a total revenue figure.
*   **Units Sold**: This metric counts the volume of order items, excluding cancellations, but does not aggregate `sale_price` and typically includes returned items if they were not cancelled.
*   **Return Rate**: This metric quantifies the proportion of non-cancelled items that were returned, directly informing one of the exclusions in the Net Revenue calculation.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

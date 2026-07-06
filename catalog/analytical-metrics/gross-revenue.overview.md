# Gross Revenue Overview

Gross Revenue represents the total sum of `sale_price` for all non-cancelled order items. It serves as a fundamental metric for understanding sales performance before accounting for returns or other adjustments.

## Definition and Calculation

Gross Revenue is calculated by summing the `sale_price` for all order items, explicitly excluding any items with a 'Cancelled' status. Items that are returned but not cancelled are included in Gross Revenue.

The calculation is formally defined as:
$$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$

The key components in its calculation are:
*   `order_items.sale_price`: The individual sale price of each item within an order.
*   `status`: An attribute indicating the current state of an order item, with items explicitly filtered to exclude those marked as 'Cancelled'.

## Related Metrics

Gross Revenue forms the basis for several other analytical metrics:
*   **Net Revenue**: While Gross Revenue includes returned items (as long as they are not cancelled), Net Revenue further excludes both 'Cancelled' and 'Returned' items, providing a more refined view of actual revenue.
*   **Average Order Value (AOV)**: Gross Revenue is a key component in calculating AOV, where it is normalized by the distinct count of orders that do not contain cancelled items.
*   **Units Sold**: This metric counts the volume of order items, similar to Gross Revenue, by excluding cancellations.

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

# Net Revenue Overview

Net Revenue is a key financial metric representing the sum of sales prices for transactions, specifically excluding both cancelled and returned items. It is conceptually defined as gross revenue minus returns.

## Metric Formulation

Net Revenue is calculated at the order-item grain, ensuring that all revenue calculations are performed at the individual item level rather than the overall order level. The formula for Net Revenue is:

$$\text{Net Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$

This calculation sums the `sale_price` from the `order_items` table, filtering out any order items with a `status` of 'Cancelled' or 'Returned'. This ensures the metric reflects actual completed sales. The underlying data for this calculation must adhere to the **order-item grain** (`order_items`), as all revenue, units-sold, and margin calculations are performed at this level.

## Related Metrics

*   **Gross Revenue**: Similar to Net Revenue, but only excludes cancelled transactions. Net Revenue further refines this by also excluding returned items.
    $$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$

## Source References

*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

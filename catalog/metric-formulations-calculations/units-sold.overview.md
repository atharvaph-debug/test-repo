# Units Sold Overview

Units Sold represents the total volume of individual item-level lines that have been processed, specifically excluding any items from orders that were cancelled. This metric is a fundamental measure for understanding the quantity of products moved through sales operations.

## Definition and Calculation

Units Sold is calculated by counting the unique identifiers of order items (`order_items.id`), ensuring that only order items whose status is not 'Cancelled' are included. The calculation must be executed at the `order-item grain`.

The formula for Units Sold is:

$$\text{Units Sold} = \text{COUNT}(\text{order\_items.id}) \quad \text{where status} \neq \text{'Cancelled'}$$

## Key Columns

*   **`order_items.id`**: This column provides the unique identifier for each item within an order. The count of these identifiers, after applying the necessary filters, determines the Units Sold.
*   **`status`**: This column, likely found within the `order_items` table or a related orders table, indicates the current state of an order item. For Units Sold, any item with a `status` of 'Cancelled' is explicitly excluded from the count.

## Granularity

All calculations for Units Sold, along with Revenue and Margin, must be performed at the **order-item grain**, meaning the analysis should consider individual items within orders rather than entire orders as a single unit. This ensures accuracy in measuring the precise quantity of items processed.

## Related Metrics

The exclusion of cancelled items and the adherence to the order-item grain are consistent patterns across other sales-related metrics:
*   **Gross Revenue**: Also calculated at the `order-item grain` and excludes transactions where the status is 'Cancelled'.
*   **Average Order Value (AOV)**: Derived using gross revenue, which similarly excludes cancelled statuses and is based on `order_items` data.

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

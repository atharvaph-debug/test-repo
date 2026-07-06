# Average Order Value Overview

Average Order Value (AOV), also known as `aov`, represents the gross revenue divided by the unique count of orders, specifically excluding any transactions that have been cancelled. This metric provides insight into the average amount spent per customer order.

## Metric Formulation

Average Order Value is calculated by dividing Gross Revenue by the count of distinct `order_id` values. All calculations for AOV, including its components like revenue, are executed at the **order-item grain**, leveraging the `order_items` data.

The formula for Average Order Value is:

$$\text{AOV} = \frac{\sum (\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}} \quad \text{where status} \neq \text{'Cancelled'}$$

### Components:

*   **Gross Revenue**: This is the sum of `order_items.sale_price` for all order items where the `status` is not 'Cancelled'.

    $$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$

*   **Unique Orders**: This represents the count of distinct `order_id` values from the `order_items` table, also specifically excluding any items associated with a 'Cancelled' status.

## Aliases

Average Order Value is also referred to by the alias `aov`.

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

# Units Sold Overview

Units Sold represents a count of total order lines that signify successful product shipments and were not cancelled. This metric is categorized under Financial Metrics.

## Definition and Calculation

Units Sold is defined as the count of individual order items (`order_items.id`) that have not been cancelled. This calculation is crucial for transactional analysis and must be performed at the **Order Item** grain.

The formula for Units Sold is:

$$\text{Units Sold} = \text{COUNT}(\text{order\_items.id}) \quad \text{where status} \neq \text{'Cancelled'}$$

*Source:* [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

## Key Columns

*   **`order_items.id`**: This column represents a single unit of a product within an order. Counting these IDs forms the basis of the Units Sold metric.
*   **`status`**: This column indicates the fulfillment status of an order item. For Units Sold, only items where the `status` is not 'Cancelled' are included.

## Granularity

The calculation of Units Sold operates at the **Order Item** level, which is considered the fundamental *revenue grain*. An Order Item represents a single unit of a product within an order. This granularity is essential for all critical transactional calculations, including revenue, margin, and units sold. An **Order**, in contrast, is a single purchase event that may contain multiple physical items (`num_of_item`) and tracks overall fulfillment status and customer metadata (`user_id`).

*Source:* [[theLook eCommerce Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [theLook eCommerce Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

# Units Sold Overview

Units Sold is an analytical metric representing the total count of distinct order items sold, excluding any cancellations. It provides a simple volume count of individual product units purchased by customers.

## Definition and Calculation

Units Sold is defined as the simple volume count of order items. This count specifically excludes any order items that have been cancelled.

The calculation for Units Sold is based on the identifier of individual order items and filters out cancelled items:

$$\text{Units Sold} = \text{COUNT}(\text{order\_items.id}) \quad \text{where status} \neq \text{'Cancelled'}$$

This metric is computed at the **Order Item** grain, which is considered the core revenue grain. An Order Item itself represents a single unit of a single product within a larger order.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

# Cost Overview

Cost represents the wholesale or landed price paid to suppliers, which is intentionally hidden from consumers. This metric is a fundamental financial component for calculating profitability.

## Definition and Storage

The **Cost** refers to the price 'theLook' paid its supplier for products. This value is recorded in two primary locations within the data model:
*   `products.cost`: This column is part of the `Product` entity, which serves as the authoritative master for product attributes, taxonomy, and costs.
*   `inventory_items.cost`: This column is associated with the `Inventory Item` entity, which tracks individual physical units of stock.

It is critical to distinguish **Cost** from customer-facing prices:
*   **Retail Price**: The list or catalog price advertised to customers prior to discounts, found in `products.retail_price`.
*   **Sale Price**: The actual transaction price paid by the customer, recorded in `order_items.sale_price`.

## Related Metrics

Cost is a crucial component in calculating key financial metrics, such as:

### Gross Margin
Gross Margin is calculated as the sum of `sale_price` minus `cost` for non-cancelled and non-returned items.
```sql
SUM(sale_price - cost)
-- Filter: status NOT IN ('Cancelled', 'Returned')
```

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

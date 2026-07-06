# Net Revenue Overview

Net Revenue is a key financial metric representing the total revenue generated after accounting for returned items. It is derived by subtracting the revenue from returned items from the Gross Revenue.

## Business Logic and Formulation

Net Revenue is calculated as the sum of the `sale_price` for all items, excluding those with a `status` of 'Cancelled' or 'Returned'. This ensures that only revenue from successfully completed sales is included.

The SQL formulation for Net Revenue is:
```sql
SUM(sale_price)
```
with the filter:
```sql
status NOT IN ('Cancelled', 'Returned')
```

## Relationships to Other Metrics

Net Revenue serves as a foundational component for other financial metrics:
*   **Gross Margin**: Calculated as Net Revenue minus the product costs.
*   **Gross Margin %**: Represents the profit margin relative to Net Revenue.

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

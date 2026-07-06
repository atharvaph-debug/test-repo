# Gross Revenue Overview

Gross Revenue is a core financial metric representing the total income generated from sales before any deductions. It is calculated as the sum of the sale price for all order items that have not been cancelled.

## Definition and Business Logic

Gross Revenue captures the total value of sales transactions. It includes the sum of the `sale_price` for all items, excluding those with a `status` of 'Cancelled'. This ensures that only completed or active sales contribute to the revenue figure.

## Calculation

The mathematical and SQL formulation for Gross Revenue is:

```sql
SUM(sale_price)
```

with a filter applied to include only items where `status` is not 'Cancelled':

```
Filter: status <> 'Cancelled'
```

## Related Metrics

Gross Revenue is a foundational component for other financial analyses:

*   **Average Order Value (AOV)**: This metric is calculated by dividing the Gross Revenue by the count of distinct orders.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

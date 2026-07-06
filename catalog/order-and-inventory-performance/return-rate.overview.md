# Return Rate Overview

Return Rate measures the proportion of sold items that customers have returned. It quantifies the share of non-cancelled order items that have been returned by the customer, indicating the frequency of returns relative to items sold.

## Business Logic

The Return Rate is calculated as the share of items that were returned out of all non-cancelled order items. This metric focuses on items that were initially considered "sold" (not cancelled) and then subsequently returned.

## SQL Formulation

The Return Rate is mathematically formulated as:

```sql
COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status <> 'Cancelled')
```

This formula counts order items where a return date (`returned_at`) is recorded, and divides it by the total count of order items that have a status other than 'Cancelled'.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

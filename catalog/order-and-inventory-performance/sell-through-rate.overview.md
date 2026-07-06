# Sell-Through Rate Overview

Sell-Through Rate measures the share of total warehouse inventory that has successfully been purchased. It quantifies the proportion of inventory that has been sold out of the total inventory available.

## Key Features

The Sell-Through Rate is calculated as the share of inventory that has been purchased. This is mathematically formulated as:

```sql
COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)
```

This formula takes the count of inventory items that have a `sold_at` timestamp (indicating they have been purchased) and divides it by the total count of all inventory items.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

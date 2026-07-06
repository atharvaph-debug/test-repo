# Canonical SQL Metric Formulas Overview

This entry provides standardized SQL and mathematical formula definitions for key business, revenue, and product performance indicators. These standardized rules, applied over warehouse columns, ensure mathematical consistency across operational dashboards and facilitate metadata enrichment.

## Key Metric Definitions and Formulas

The following metrics are defined with their canonical SQL or mathematical formulas:

### Gross Revenue
The total revenue generated from sales before any returns or cancellations.
```sql
SUM(order_items.sale_price) WHERE status IS NOT 'Cancelled'
```

### Net Revenue
The revenue remaining after accounting for both cancelled and returned orders.
```sql
SUM(order_items.sale_price) WHERE status IS NEITHER 'Cancelled' NOR 'Returned'
```

### Average Order Value (AOV)
The average value of orders, calculated by dividing the total sale price by the number of unique orders.
```sql
SUM(order_items.sale_price) / COUNT(DISTINCT order_items.order_id)
```

### Units Sold
The total count of individual order items that have been sold and not cancelled.
```sql
COUNT(order_items.id) WHERE status IS NOT 'Cancelled'
```

### Return Rate
The proportion of order items that have been returned relative to the total number of non-cancelled order items.
```sql
COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status <> 'Cancelled')
```

### Gross Margin %
The profitability of sales, expressed as a percentage, calculated by dividing the Gross Margin by the Net Revenue. Gross Margin is defined as the sum of sale price minus product cost for non-returned, non-cancelled items.
```
Gross Margin / Net Revenue
```
Where Gross Margin is:
```sql
SUM(order_items.sale_price - products.cost) FOR NON-RETURNED, NON-CANCELLED ITEMS
```

### Sell-Through Rate
The percentage of inventory items sold relative to the total inventory available.
```sql
COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)
```

### Average Days in Inventory
The average number of days an inventory item remains in stock before being sold, calculated as the mean duration between an item's creation and its sale date for sold inventory items.
```
Mean of (sold_at - created_at) calculated over sold inventory items
```

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

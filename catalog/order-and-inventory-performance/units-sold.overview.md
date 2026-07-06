# Units Sold Overview

Units Sold represents the total count of individual order item units that have been sold and not subsequently cancelled. This metric provides a fundamental measure of sales volume, focusing purely on the quantity of items moved, irrespective of their price or revenue.

## Business Logic

Units Sold is calculated by counting all non-cancelled order item units. This means any order item whose status is explicitly marked as 'Cancelled' is excluded from the count.

## SQL Formulation

The calculation for Units Sold involves counting the identifiers of order items, applying a filter to exclude any items that have a 'Cancelled' status.

```sql
COUNT(id)
```
*Filter: `status <> 'Cancelled'`*

In this formulation, `id` refers to the unique identifier of an individual order item, and `status` refers to the current status of that order item within the system.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

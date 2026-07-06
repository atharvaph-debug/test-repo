# Average Order Value Overview

Average Order Value (AOV), also known as aov, is a key metric within the Order and Inventory Performance category that measures the average revenue generated per order.

## Business Logic and Calculation

Average Order Value is calculated by dividing the total gross revenue by the count of distinct orders.
The mathematical formulation is: `Gross Revenue / COUNT(DISTINCT order_id)`.

To calculate this, the following components are used:
*   **Gross Revenue**: This is the sum of the sale price for all items that are not cancelled. The SQL formulation for Gross Revenue is `SUM(sale_price)` with a filter `status <> 'Cancelled'`.
*   **Distinct Orders**: This refers to the unique count of `order_id` values.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

# Order Items Overview

The `Order Items` table serves as the revenue grain table, containing one row for each unit of a product within an order. It is a central component, acting as the hub of the star schema for data analysis.

## Key Features

The `Order Items` table is critical for tracking the lifecycle of individual products within an order:

*   **Granularity**: Each row represents a single unit of a product, providing detailed revenue insights.
*   **Star Schema Hub**: Its central role enables comprehensive analysis by linking to various dimension tables.
*   **Status Tracking**: Fulfillment and return cycles are tracked through sequential statuses and timestamps. The `order_items.status` column is particularly important for precise analysis, as individual order items can be partially completed or returned, unlike the order as a whole.

## Schema

The `Order Items` table includes the `status` column, which tracks the item-level status. This granular `status` is vital for accurate analysis when order items undergo partial fulfillment or return processes.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

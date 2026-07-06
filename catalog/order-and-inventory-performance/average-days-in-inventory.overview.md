# Average Days in Inventory Overview

Average Days in Inventory represents the average duration an item spends in stock before being successfully sold. This metric provides insight into inventory turnover efficiency and is crucial for metadata enrichment related to inventory management and performance.

## Definition and Calculation

This metric quantifies the average lifespan of an inventory item from the moment it is received into stock until it is purchased.

The calculation is formulated as:
`AVG(sold_at - created_at)`
*Filter: `sold_at IS NOT NULL`*

This formula is applied to the `inventory_items` table, considering only those items that have been sold. The calculation leverages the `sold_at` and `created_at` timestamps to determine the duration an item was in inventory.

## Data Sources and Schema

The "Average Days in Inventory" metric is derived from the `inventory_items` table, which is a core component of theLook eCommerce dataset. This table contains one row per physical unit of stock and tracks key lifecycle timestamps essential for inventory analysis.

*   **`inventory_items`**: This table is the primary source for tracking individual stock units.
    *   **`created_at`**: This timestamp records when a physical unit of stock was received into inventory [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).
    *   **`sold_at`**: This timestamp records when a physical unit of stock was purchased. For the "Average Days in Inventory" calculation, only items where `sold_at` is not `NULL` are included, indicating a successful sale [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).

The `inventory_items` table also has product-level attributes (e.g., name, category, brand, SKU, retail price) denormalized as `product_*` columns, though the authoritative source for these remains the `products` table [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

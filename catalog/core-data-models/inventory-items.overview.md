# Inventory Items Overview

The `Inventory Items` table tracks individual physical units of stock within theLook eCommerce dataset. Each row in this table represents one unique physical item, providing detailed metadata for inventory management and analysis. It records timestamps for when an item was received into inventory and when it was purchased, along with denormalized product attributes to simplify queries.

## Key Features and Schema
The `inventory_items` table is designed with one row per physical unit of stock.

*   **`created_at`**: This timestamp indicates when the physical unit was received into inventory [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).
*   **`sold_at`**: This timestamp tracks when the physical unit was purchased [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).
*   **`cost`**: Represents the wholesale or landed price that theLook paid its supplier for this item. This cost is hidden from customers [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).
*   **Denormalized Product Attributes**: To simplify inventory queries, product-level attributes such as name, category, brand, SKU, and retail price are denormalized and stored as `product_*` columns directly within the `inventory_items` table. It is crucial to note that the `products` table remains the authoritative source for these attributes; if there is a discrepancy, the `products` table should be trusted [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).

## Relationships & Lineage
The `inventory_items` table is connected to other core entities through foreign keys:
*   `inventory_items.product_id` links to `products.id`, associating each physical unit with its product definition [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).
*   It is linked by `order_items.inventory_item_id` to `order_items.id`, connecting specific inventory units to customer orders [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true).

## Canonical Analytics
The `inventory_items` table is fundamental for calculating key inventory metrics:

*   **Sell-Through Rate**: This metric measures the share of inventory that has been purchased.
    *   **Formula**: `COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)` [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true).
*   **Avg. Days in Inventory**: This calculates the average lifespan of an item in stock before it is sold.
    *   **Formula**: `AVG(sold_at - created_at)` with a filter where `sold_at IS NOT NULL` [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true).

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

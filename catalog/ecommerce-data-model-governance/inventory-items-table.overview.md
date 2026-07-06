# Inventory Items Table Overview

The `Inventory Items Table` (`inventory_items`) tracks individual physical units of stock within the e-commerce system. Each row in this table represents a single unit of stock, providing details on its associated product and wholesale cost.

## Key Features

*   **Grain:** The table is structured at a grain of one row per physical unit of stock.
*   **Purpose:** It serves to track the movement and cost of individual stock items, linking them to their corresponding product catalog entry.

## Schema

The `inventory_items` table includes the following key columns:

*   **`id`**: This column uniquely identifies each physical unit of stock. It is referenced by the `order_items` table to track which specific inventory unit was sold in an order.
*   **`product_id`**: This foreign key links the inventory unit to its corresponding product SKU in the `products` catalog. It maps an inventory item to the product it represents.
*   **`cost`**: Represents the wholesale or landed cost paid to the supplier for this specific inventory unit. This metric is strictly restricted from any customer-facing views.

## Relationships

The `inventory_items` table maintains the following relationships:

*   **`inventory_items.product_id`** refers to **`products.id`**: Each inventory item is associated with a specific product definition from the `Product Catalog`.
*   **`order_items.inventory_item_id`** refers to **`inventory_items.id`**: The `Order Items Table` links to this table to specify the exact physical inventory unit that was part of a customer order.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

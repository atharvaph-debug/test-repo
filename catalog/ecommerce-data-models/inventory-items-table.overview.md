# Inventory Items Table Overview

The `Inventory Items Table` (`inventory_items`) represents individual physical units of stock at a `stock unit` grain within the eCommerce data model. This table captures granular details about each specific piece of inventory.

## Key Features

This table serves as a detailed record for each unique item in stock, allowing for tracking at the individual unit level rather than just at the product (SKU) level.

## Schema

The `inventory_items` table includes the following key columns:

*   **`id`**: A unique identifier for each specific physical unit of stock. This serves as the primary key for the table and is referenced by `order_items` when a unit is sold.
*   **`product_id`**: A foreign key that links each inventory item to its corresponding product definition in the `products` table. This indicates which type of product the physical unit represents.
*   **`cost`**: Represents the wholesale or landed cost that the business paid to suppliers for this specific unit. This metric is intended for internal business analysis and is not exposed to customers.

## Relationships

The `inventory_items` table connects to other key entities in the eCommerce data model:

*   **`Order Items`**: An `inventory_items.id` is linked to `order_items.inventory_item_id`, indicating which specific physical unit was sold in a transaction.
*   **`Products`**: An `inventory_items.product_id` links to `products.id`, providing details about the type of product that each inventory item represents.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

# Inventory Items Table Overview

The Inventory Items Table, also known as `inventory_items`, represents the physical units of stock within the distribution warehouses. It captures data at the stock unit grain, providing detailed information about individual stock items.

## Key Features

This table serves as a detailed record for each physical unit of inventory. It is instrumental in tracking the wholesale cost of individual stock items and linking them to their corresponding products.

## Schema

The table includes the following key columns:

*   **`id`**: This column uniquely identifies each physical unit of stock. It serves as the primary key for the `inventory_items` table and is referenced by `order_items.inventory_item_id`.
*   **`product_id`**: This is a foreign key that links an inventory item to the `products` table, specifically `products.id`. It indicates which sellable stock-keeping unit (SKU) a given physical inventory item belongs to.
*   **`cost`**: Represents the wholesale or landed price paid to the supplier for this specific inventory item. This cost information is hidden from customers.

## Relationships

The `Inventory Items Table` participates in the following relationships:

*   It is referenced by the `Order Items Table` through `order_items.inventory_item_id`, linking sold units to specific physical inventory items.
*   It references the `Products Table` through `inventory_items.product_id`, connecting each inventory item to its broader product definition.

## Financial Attributes

The table includes `cost` as a financial attribute, which signifies the wholesale/landed price paid to the supplier for each physical unit of stock. Unlike `products.retail_price` (the advertised list price) or `order_items.sale_price` (the actual transaction amount), `inventory_items.cost` tracks the internal cost and is not exposed to customers.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [theLook eCommerce Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

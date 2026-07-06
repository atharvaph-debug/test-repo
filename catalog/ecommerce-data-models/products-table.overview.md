# Products Table Overview

The `Products` table contains SKU-level details for all sellable products. It includes information on their retail prices, supplier costs, and the associated warehouse origins, serving as a core dimension in the eCommerce data model.

## Key Features

This table holds details about sellable products (SKUs) at a `product` grain. It acts as a central repository for product-specific metadata, linking various aspects of the eCommerce operations.

## Schema

The `Products` table includes the following key columns:

*   **`id`**: This column uniquely identifies each product. It serves as the primary key for the `Products` table and is referenced by `order_items.product_id` and `inventory_items.product_id`.
*   **`retail_price`**: Represents the catalog or list price advertised to customers for a product before any discounts are applied.
*   **`cost`**: Denotes the wholesale or landed cost that the business paid to suppliers for a unit of the product. This metric is intended for internal use and is never shown to customers.
*   **`distribution_center_id`**: This foreign key links a product to its associated fulfillment warehouse, referring to `distribution_centers.id`.

## Relationships

The `Products` table is integrated into the overall data model through the following relationships:

*   **`order_items.product_id`** refers to **`products.id`**: This links individual sold units in transaction records to the specific product details.
*   **`inventory_items.product_id`** refers to **`products.id`**: This connects specific physical units of stock to their corresponding product definitions.
*   **`products.distribution_center_id`** refers to **`distribution_centers.id`**: This establishes the connection between a product and the distribution center from which it originates or is fulfilled.

Analytical queries often involve joining the `Products` table with `order_items` when analyzing revenue, as `order_items` acts as the central fact table.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%5D&file=business_glossary.docx&action=default&mobileredirect=true)

# Products Catalog Table Overview

The Products Catalog Table, also known by its aliases `products` or `product catalog`, is a core component of the e-commerce data model. It serves as a comprehensive catalog of all sellable Stock Keeping Units (SKUs), providing detailed product information and linking each product to its sourcing origin. This table is essential for managing product metadata, pricing, and supply chain tracking.

## Key Features

*   **Grain**: The table is structured at a grain of one row per unique, sellable SKU.
*   **Product Details**: It contains various product attributes, including specific pricing information like wholesale cost and retail price.
*   **Sourcing Origin**: Each product is linked to its sourcing origin via a distribution center identifier.

## Schema

The `Products Catalog Table` includes the following key columns:

*   **`id`**: A unique identifier for each product SKU. This column serves as the primary key for the table and is referenced by `order_items` and `inventory_items` tables.
*   **`distribution_center_id`**: Identifies the sourcing origin for the product, establishing a link to the `distribution_centers` table.
*   **`cost`**: Represents the wholesale or landed cost paid to the supplier for the product. This value is strictly restricted from customer-facing views.
*   **`retail_price`**: Denotes the standard, non-discounted catalog price at which the product is advertised to customers.

## Relationships

The `Products Catalog Table` maintains the following relationships with other entities in the data model:

*   **`products.distribution_center_id`** is a foreign key referencing `distribution_centers.id`, linking products to their distribution sources.
*   **`order_items.product_id`** is a foreign key referencing `products.id`, indicating which product was part of an order line item.
*   **`inventory_items.product_id`** is a foreign key referencing `products.id`, associating physical stock units with their respective product SKUs.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

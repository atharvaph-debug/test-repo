# Products Table Overview

The `Products Table`, also aliased as `products`, is a core data model entry that tracks sellable stock-keeping units (SKU grain). It serves as a central repository for metadata about individual products, defining their characteristics and linking to their financial attributes.

## Key Features

This table represents individual sellable stock-keeping units, providing the SKU-level granularity for product information.

## Key Columns

The `Products Table` includes the following important columns:

*   **`id`**: This column likely serves as the unique identifier for each product (SKU), as it is referenced as a foreign key by both `order_items.product_id` and `inventory_items.product_id`.
*   **`cost`**: Represents the wholesale or landed price paid to the supplier for the product. This cost is hidden from customers.
*   **`retail_price`**: Denotes the reference catalog or list price advertised to customers for the product, prior to any discounts.
*   **`distribution_center_id`**: This column links to the `distribution_centers` table, indicating the associated fulfillment warehouse for the product.

## Relationships

The `Products Table` participates in several key relationships within the data model:

*   **`order_items`**: The `order_items` table links to `products` via `order_items.product_id` to `products.id`, associating ordered items with specific products.
*   **`inventory_items`**: The `inventory_items` table links to `products` via `inventory_items.product_id` to `products.id`, indicating which product each physical unit of stock belongs to.
*   **`distribution_centers`**: The `products` table links to `distribution_centers` via `products.distribution_center_id` to `distribution_centers.id`, associating products with their fulfillment warehouses.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [theLook eCommerce Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

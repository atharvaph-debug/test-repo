# Products Overview

The `Products` entry represents the authoritative master catalog, with one row per sellable Stock Keeping Unit (SKU). It serves as the definitive source for product attributes, taxonomy, and costs, making it crucial for metadata enrichment.

## Key Features

The `Products` table is designed to hold comprehensive metadata for every sellable product. This includes:
*   **Product Attributes:** Details like name, brand, and SKU.
*   **Product Taxonomy:** A hierarchical classification system (Department, Category, Brand).
*   **Costs:** Both the wholesale cost and the advertised retail price.

## Schema

The `products` table contains the following key columns:
*   **`id`**: The unique identifier for each product. This serves as the primary key and is referenced by `order_items` and `inventory_items` to link to specific products.
*   **`distribution_center_id`**: A foreign key linking the product to the `distribution_centers` table, indicating the physical fulfillment warehouse associated with the product.
*   **`cost`**: The wholesale or landed price paid by the company to its supplier for this product. This value is hidden from customers.
*   **`retail_price`**: The list or catalog price advertised to customers before any discounts are applied.
*   **`name`**: The human-readable name of the product.
*   **`category`**: A classification of the product, part of the three-level taxonomy.
*   **`brand`**: The manufacturer or label of the product, also part of the taxonomy.
*   **`SKU`**: The Stock Keeping Unit, a unique identifier for each distinct product and service that can be purchased.

## Relationships

The `products` table plays a central role in connecting various data entities:
*   **Order Items**: `order_items` link to `products` via `order_items.product_id` $\rightarrow$ `products.id`.
*   **Inventory Items**: `inventory_items` link to `products` via `inventory_items.product_id` $\rightarrow$ `products.id`.
*   **Distribution Centers**: `products` link to `distribution_centers` via `products.distribution_center_id` $\rightarrow$ `distribution_centers.id`.

## Source of Truth

The `products` table is the authoritative source for all product-level attributes (such as name, category, brand, SKU, and retail price). Although some of these attributes may be denormalized as `product_*` columns in the `inventory_items` table to simplify inventory queries, the `products` table remains the primary authority. If there are any discrepancies between `products` and `inventory_items` for these attributes, the data in the `products` table must be trusted.

## Product Taxonomy

Products are organized into a three-level hierarchical classification system:
1.  **Department**: The broadest grouping (e.g., Men, Women).
2.  **Category**: Specifies the product type (e.g., Jeans, Outerwear).
3.  **Brand**: Identifies the manufacturer or label.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

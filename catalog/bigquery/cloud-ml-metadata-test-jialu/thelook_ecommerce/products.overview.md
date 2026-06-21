# products Overview

The `products` table is a core dimension table in theLook fictitious eCommerce dataset. It represents the catalog of sellable products offered by theLook, a multi-brand online apparel and accessories retailer. The grain of this table is **one row per sellable product variant (SKU)**.

The `products` table serves as the authoritative source of truth for all product taxonomy details, costs, and advertised list prices.

## Schema & Key Columns

The table contains the following 9 columns:

*   **`id`** (INTEGER): The unique identifier and primary key for each product.
*   **`cost`**: The wholesale or landed cost that theLook paid its supplier for the unit. This value is never shown to the customers.
*   **`category`**: The product type within a department (e.g., Jeans, Outerwear). Part of the three-level product taxonomy.
*   **`name`**: The name of the product.
*   **`brand`**: The manufacturer or label of the product.
*   **`retail_price`**: The advertised list price of the product in the catalog before any discounts or promotions are applied.
*   **`department`**: The broadest category grouping in the product taxonomy (e.g., Men, Women).
*   **`sku`**: The Stock Keeping Unit identifier used by theLook to track physical inventory. Each SKU corresponds exactly to one row in this table.
*   **`distribution_center_id`** (INTEGER): The foreign key linking the product to the physical warehouse where it is stocked and shipped from.

## Relationships

The `products` table links to several other entities in the dataset:

*   **`distribution_centers`**: Every product is assigned to exactly one physical warehouse. This relationship is established via `products.distribution_center_id` -> `distribution_centers.id`.
*   **`order_items`**: This is the central transaction hub table. It references products via `order_items.product_id` -> `products.id`.
*   **`inventory_items`**: Represents physical units of stock. It references products via `inventory_items.product_id` -> `products.id`.

### Attribute Denormalization Warning
For query convenience, product attributes (including `category`, `name`, `brand`, `retail_price`, `department`, `sku`, and `distribution_center_id`) are denormalized and copied as `product_*` columns directly inside the `inventory_items` table. However, **`products` remains the sole authoritative source of truth**. If there is ever a discrepancy between the product attributes in `inventory_items` and `products`, the values in the `products` table must be trusted.

## Key Business Concepts & Formulas

### 1. Cost vs. Retail Price vs. Sale Price
*   **`cost`** (found on `products` and `inventory_items`): What the company paid for the product.
*   **`retail_price`** (found on `products`): The reference list price advertised in the catalog.
*   **`sale_price`** (found on `order_items`): The price the customer *actually* paid for an item at checkout, which may differ from the retail price due to promotions or markdowns. Realized revenue calculations must always use `order_items.sale_price` rather than the product's catalog list price.

### 2. Gross Margin Calculations
*   **Catalog Gross Margin** (at list price): Computed as `retail_price - cost`.
*   **Realized Gross Margin** (at transaction level): Calculated as `sale_price - cost` per order item.
*   **Gross Margin %**: Computed as `gross_margin / sale_price`.

### 3. Product Taxonomy
The catalog is organized using a strict three-level hierarchy stored on this table:
1.  **Department** (Broadest level, e.g., Men, Women)
2.  **Category** (Product type, e.g., Jeans, Outerwear)
3.  **Brand** (The manufacturer label)

## Source References

*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)

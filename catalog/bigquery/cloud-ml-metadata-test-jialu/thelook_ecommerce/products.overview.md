# products Overview

The `products` table is a core dimension table in the theLook eCommerce dataset. It contains one row per sellable product variant, also referred to as a Stock Keeping Unit (SKU). 

This table serves as the authoritative source of truth for all product taxonomy, pricing, and supplier cost attributes. 

## Key Columns

*   **`id`** (INTEGER): The unique identifier for each product. This ID is used to join products to transactions and physical inventory.
*   **`sku`** (STRING): The Stock Keeping Unit identifier used to track a specific sellable product variant in inventory. Each SKU corresponds to exactly one row in the `products` table.
*   **`name`** (STRING): The name of the product.
*   **`brand`** (STRING): The manufacturer or label of the product.
*   **`category`** (STRING): The specific product type (e.g., Jeans, Outerwear). This is the second level of the product taxonomy.
*   **`department`** (STRING): The broadest classification in the product taxonomy (e.g., Men, Women).
*   **`cost`** (FLOAT): The wholesale or landed cost that theLook paid to its supplier for a single unit of the product. This value is never displayed to customers.
*   **`retail_price`** (FLOAT): The list price advertised by theLook for the product. This represents the catalog price before any markdowns or promotional discounts.
*   **`distribution_center_id`** (INTEGER): The ID of the physical fulfillment warehouse where the product is stocked and shipped from.

## Relationships & Joins

The `products` table acts as a critical hub connecting inventory, orders, and warehousing:

*   **Order Items (`order_items.product_id` → `products.id`)**: Associates individual transaction lines (sold units) with the sellable product SKU.
*   **Inventory Items (`inventory_items.product_id` → `products.id`)**: Connects individual physical items in stock to their corresponding product definition.
*   **Distribution Centers (`products.distribution_center_id` → `distribution_centers.id`)**: Associates each product with its designated fulfillment warehouse. Every product is assigned to exactly one distribution center.

### Denormalization and Source of Truth
The `inventory_items` table contains several denormalized product columns prefixed with `product_` (such as `product_category`, `product_name`, `product_brand`, `product_retail_price`, `product_department`, `product_sku`, and `product_distribution_center_id`). These are copied into the inventory table for querying convenience. However, the **`products` table is the authoritative source for these attributes**. If any values disagree between the two tables, the data in the `products` table must be trusted.

## Financial Concepts & Metrics

Understanding the distinction between the financial attributes in the `products` table and other tables is crucial for correct analysis:

*   **Cost vs. Retail Price vs. Sale Price**:
    *   `products.cost` is the wholesale cost paid to suppliers.
    *   `products.retail_price` is the advertised list price.
    *   `order_items.sale_price` is what the customer actually paid (which may differ from `retail_price` due to promotions).
*   **Gross Margin (Catalog Analysis)**: For catalog-level planning, list-price gross margin can be evaluated as `retail_price - cost`.
*   **Realized Gross Margin**: The actual profit realized on completed transactions is calculated using the formula:
    $$\text{Gross Margin} = \sum(\text{order\_items.sale\_price} - \text{products.cost})$$
    This is evaluated by joining `order_items.product_id` to `products.id` and filtering only for items that have not been returned or cancelled.
*   **Gross Margin %**: Calculated as $\frac{\text{Gross Margin}}{\text{sale\_price}}$.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)

# inventory_items Overview

The `inventory_items` table represents the programmatically generated inventory for "theLook," a fictitious multi-brand online apparel and accessories retailer. The grain of this table is **one row per physical unit of stock** (stock unit). It tracks physical inventory units from the moment they are received in a warehouse until they are sold to a customer.

## Key Columns and Schema

The `inventory_items` table contains 12 columns covering stock identification, tracking timestamps, and denormalized product details:

*   **`id`** (INTEGER): The unique identifier for a specific physical stock unit.
*   **`product_id`** (INTEGER): The foreign key linking the inventory item back to the authoritative product record in the `products` table.
*   **`created_at`** (TIMESTAMP): The timestamp indicating when the physical stock unit was received into inventory.
*   **`sold_at`** (TIMESTAMP): The timestamp indicating when the physical stock unit was purchased. This is null for items that have not yet been sold.
*   **`cost`** (FLOAT): The wholesale or landed cost that theLook paid to its supplier for this specific unit. This value is never shown to customers and is used internally for margin calculations.
*   **Denormalized Product Fields**: 
    The following columns are copied directly from the `products` table for convenience to avoid requiring a join for simple inventory queries:
    *   **`product_category`** (STRING): The product type (e.g., Jeans, Outerwear).
    *   **`product_name`** (STRING): The name of the product.
    *   **`product_brand`** (STRING): The manufacturer or label of the product.
    *   **`product_retail_price`** (FLOAT): The pre-discount catalog list price advertised to customers.
    *   **`product_department`** (STRING): The broadest grouping of the product taxonomy (e.g., Men, Women).
    *   **`product_sku`** (STRING): The Stock Keeping Unit identifier used to track the sellable product variant.
    *   **`product_distribution_center_id`** (INTEGER): The ID of the physical fulfillment warehouse where the product is stocked and shipped from.

### Important Note on Denormalization
The `product_*` columns on `inventory_items` are denormalized copies. The **`products` table remains the authoritative source for all product attributes**. If there is ever a discrepancy between the product attributes in `inventory_items` and those in `products`, the values in the `products` table must be trusted. Do not treat these denormalized columns as independent facts.

## Relationships and Joins

*   **To Products**: `inventory_items.product_id` links to `products.id`.
*   **To Order Items**: `order_items.inventory_item_id` links to `inventory_items.id`. The `order_items` table acts as the central hub of the schema, connecting the customer, the order, the product, and the specific physical inventory unit used to fulfill the purchase.

## Key Metrics

The `inventory_items` table is the primary source of truth for tracking warehouse efficiency and stock turnover. The canonical metrics derived from this table are:

*   **Sell-Through Rate**: Calculated as the count of sold inventory units divided by total inventory units:
    $$\text{Sell-Through Rate} = \frac{\text{COUNT of inventory\_items where sold\_at is not null}}{\text{COUNT of all inventory\_items}}$$
*   **Average Days in Inventory**: The mean duration a unit sits in stock before selling, computed over all sold items:
    $$\text{Average Days in Inventory} = \text{Mean of } (\text{sold\_at} - \text{created\_at})$$
*   **Gross Margin (Item Level)**: Calculated as `sale_price` (from the transaction line on `order_items`) minus the item's `cost` (from `inventory_items`). For list-price catalog analysis, the baseline margin is computed as `product_retail_price` minus `cost`.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
*   [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)

# inventory_items Overview

The `inventory_items` table contains programmatically generated inventory records for **theLook**, a fictitious multi-brand online apparel and accessories retailer. 

The grain of this table is **one row per physical unit of stock** (a stock unit). It tracks when individual inventory items are received, when they are sold, their landed cost, and denormalized details about the products they represent.

---

## Key Columns and Schema

The table contains 12 columns, which can be categorized into direct inventory tracking attributes and denormalized product attributes.

### Inventory Tracking Columns
* **`id`** (INTEGER): The unique identifier for a specific physical unit of stock. This joins directly to the order fulfillment records.
* **`product_id`** (INTEGER): The foreign key referencing the associated product in the `products` table.
* **`created_at`** (TIMESTAMP): The timestamp indicating when the specific physical stock unit was received into inventory.
* **`sold_at`** (TIMESTAMP): The timestamp indicating when the specific unit was purchased/sold. This column is `NULL` for units that remain in inventory and have not yet been purchased.
* **`cost`** (FLOAT): The wholesale or landed cost that theLook paid its supplier for this specific stock unit. This value is strictly internal and is never shown to customers.

### Denormalized Product Columns
To make inventory-specific queries convenient and avoid mandatory joins, several product attributes are denormalized directly onto the `inventory_items` table. 

> ⚠️ **Important Data Integrity Rule:** The `products` table is the single authoritative source of truth for all product attributes. If there is ever a disagreement between the values in these columns and the `products` table, always trust `products`. Do not treat these columns as independent facts.

* **`product_name`** (STRING): The catalog name of the product.
* **`product_brand`** (STRING): The manufacturer or label brand.
* **`product_category`** (STRING): The product type (e.g., Jeans, Outerwear) within its department.
* **`product_department`** (STRING): The broadest grouping of the product taxonomy (e.g., Men, Women).
* **`product_sku`** (STRING): The Stock Keeping Unit identifier theLook uses to track sellable variants.
* **`product_retail_price`** (FLOAT): The advertised catalog list price for the product before any discounts or promotions.
* **`product_distribution_center_id`** (INTEGER): The foreign key linking the product to its home fulfillment warehouse in the `distribution_centers` table.

---

## Relationships and Joins

The `inventory_items` table acts as a key dimension for physical inventory, connecting products to sales:

* **`inventory_items.id`** $\rightarrow$ **`order_items.inventory_item_id`**: This relationship connects a physical unit of stock to the specific transaction line item that fulfilled a customer's purchase. `order_items` acts as the analytical hub, tying the customer, order, product, and inventory unit together.
* **`inventory_items.product_id`** $\rightarrow$ **`products.id`**: Connects the inventory unit to its canonical product definitions.

---

## Key Metrics Derived from Inventory

The fields in `inventory_items` are used to compute core operational and financial metrics:

* **Sell-Through Rate**: Calculated as the count of inventory items where `sold_at` is not null, divided by the total count of inventory items.
* **Average Days in Inventory**: Calculated as the mean difference between `sold_at` and `created_at` over all sold inventory items. This indicates how long a unit typically sits in stock before selling.
* **Gross Margin**: Calculated per order item as `sale_price - cost` (using `inventory_items.cost` or `products.cost`). When evaluated globally, it is computed as the sum of transaction sales prices minus the cost of the products, evaluated over non-returned and non-cancelled items.

---

## Source References

* [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
* [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
* [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)

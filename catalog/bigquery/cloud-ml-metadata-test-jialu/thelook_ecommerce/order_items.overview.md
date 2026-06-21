# order_items Overview

The `order_items` table is the central fact table for revenue and sales performance in the fictitious **theLook eCommerce** dataset. It records data at the **order line / sold unit** grain, meaning there is exactly one row per unit of a product within an order. 

Because it ties together customers, orders, products, and physical inventory units, `order_items` serves as the analytical hub for the warehouse. Most analytical queries start from this table and join outward to other dimensions.

---

## Schema & Key Columns

The table contains 11 columns tracking identifiers, transaction financial details, status, and fulfillment timestamps:

*   **`id`**: The unique identifier for the individual order item (sold unit).
*   **`order_id`**: Foreign key linking the line item to the parent order in the `orders` table.
*   **`user_id`**: Foreign key linking the purchase directly to the customer in the `users` table.
*   **`product_id`**: Foreign key linking to the catalog product in the `products` table.
*   **`inventory_item_id`**: Foreign key linking to the specific physical unit of stock in the `inventory_items` table that fulfilled this line.
*   **`status`**: The current lifecycle state of this specific line item (e.g., Processing, Shipped, Complete, Returned, Cancelled).
*   **`sale_price`**: The price the customer actually paid for the unit, including any promotions or markdowns. This is the authoritative figure for all revenue calculations.
*   **`created_at`**: Timestamp recording when the order line was placed.
*   **`shipped_at`**: Timestamp recording when the item left the distribution center (null if not yet shipped).
*   **`delivered_at`**: Timestamp recording when the item reached the customer (null if not yet delivered).
*   **`returned_at`**: Timestamp recording when the item was returned by the customer (null if not returned).

---

## Relationships & Joins

As the central hub of the schema, `order_items` supports the following foreign key relationships:

*   **To Orders**: `order_items.order_id` $\rightarrow$ `orders.order_id`
*   **To Users (Customers)**: `order_items.user_id` $\rightarrow$ `users.id`
*   **To Products (SKUs)**: `order_items.product_id` $\rightarrow$ `products.id`
*   **To Inventory (Stock Units)**: `order_items.inventory_item_id` $\rightarrow$ `inventory_items.id`

---

## Lifecycle, Status, and Timestamps

The `status` and timestamp columns track how an item moves from checkout to completion or return.

### Order Item Status vs. Order Status
While both `orders` and `order_items` track statuses, `order_items.status` operates at the individual item grain. Because an order can be partially fulfilled or partially returned, individual item statuses can differ from the parent order's status. For example, a parent order may be marked **Complete** while one of its constituent order items is marked **Returned**. Analysts should always compute fulfillment and return metrics from the `order_items.status` column for line-item accuracy.

### The Status Lifecycle
1.  **Processing**: The order has been placed and payment captured; the item is being prepared but has not shipped.
2.  **Shipped**: The item has departed the distribution center.
3.  **Complete**: The item was delivered to the customer, and the return window has closed.
4.  **Returned**: The item was received back from the customer.
5.  **Cancelled**: The order was cancelled before fulfillment; cancelled items generate no revenue.

### Timestamp Funnel Analysis
The sequential timestamp fields (`created_at` $\rightarrow$ `shipped_at` $\rightarrow$ `delivered_at` $\rightarrow$ `returned_at`) can be used to perform cycle-time and funnel analysis:
*   **Processing Time**: Calculated as the difference between `shipped_at` and `created_at`.
*   **Transit Time**: Calculated as the difference between `delivered_at` and `shipped_at`.
*   **Return Latency**: Calculated as the difference between `returned_at` and `delivered_at`.

A `NULL` timestamp indicates that the corresponding lifecycle stage has not occurred.

---

## Key Metrics & Business Logic

The following business rules and formulas apply when aggregating data from the `order_items` table:

### Financial Fields: Sale Price vs. Retail Price vs. Cost
To prevent margin and revenue calculation errors, it is important to distinguish between three distinct money fields:
*   **Sale Price** (found on `order_items.sale_price`): The price the customer actually paid. This is the only price used for realized revenue.
*   **Retail Price** (found on `products.retail_price`): The advertised list price before promotions or markdowns.
*   **Cost** (found on `products.cost` and `inventory_items.cost`): The wholesale or landed cost paid to the supplier.

### Core Formulas

*   **Gross Revenue**: The sum of `sale_price` across all items that are **not Cancelled**. Cancelled items must be excluded from all revenue metrics.
*   **Net Revenue**: The sum of `sale_price` across all items that are **neither Cancelled nor Returned**. This represents gross revenue with returned transactions removed.
*   **Average Order Value (AOV)**: Derived by dividing Gross Revenue by the count of unique `order_id` values.
*   **Units Sold**: The count of `order_items.id` for all non-cancelled items.
*   **Return Rate**: The count of order items where `returned_at` is not null (or where the status is Returned), divided by the count of sold units (all items where status is not Cancelled).
*   **Gross Margin**: Calculated by subtracting `products.cost` from `order_items.sale_price` for all non-returned, non-cancelled items.
*   **Gross Margin %**: Gross Margin divided by Net Revenue. At the individual item level, it is calculated as `(sale_price - cost) / sale_price`.

---

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Order Lifecycle and Status](https://docs.google.com/document/d/1fm5barRArG0T_KLCIXWnpUwXkaVNdlHNFljmcQ4ppfA/edit?usp=drivesdk)
*   [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)

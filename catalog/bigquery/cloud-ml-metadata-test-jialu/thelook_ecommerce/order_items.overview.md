# order_items Overview

The `order_items` table is the central fact table for revenue and fulfillment analysis in the theLook eCommerce dataset. The grain of this table is **one row per unit of a product in an order** (an order line or sold unit). 

As the primary hub of the data model, `order_items` ties together the customer, the parent checkout event, the specific product SKU, and the physical inventory item used to fulfill the order. Most analytical queries starting in theLook data warehouse begin with this table and join outward.

## Key Columns and Schema

| Column Name | Data Type | Business Role / Semantic Meaning |
| :--- | :--- | :--- |
| `id` | INTEGER | The unique identifier for the order item (the individual sold unit). |
| `order_id` | INTEGER | The identifier of the parent checkout event. Multiple order items can share the same `order_id` (e.g., if a customer buys three items at once, they generate one order and three order items). Joins to `orders.order_id`. |
| `user_id` | INTEGER | The identifier of the customer who placed the order. Joins to `users.id`. |
| `product_id` | INTEGER | The product SKU identifier. Joins to `products.id`. |
| `inventory_item_id` | INTEGER | The identifier of the physical stock unit shipped to fulfill this specific line. Joins to `inventory_items.id`. |
| `status` | STRING | The line-item level fulfillment status. Lifecycle states include **Processing**, **Shipped**, **Complete**, **Returned**, and **Cancelled**. |
| `created_at` | TIMESTAMP | The timestamp when the order and line item were placed. |
| `shipped_at` | TIMESTAMP | The timestamp when the item departed the distribution center. `NULL` if the item has not yet shipped. |
| `delivered_at` | TIMESTAMP | The timestamp when the item was delivered to the customer. `NULL` if not yet delivered. |
| `returned_at` | TIMESTAMP | The timestamp when the item was returned by the customer. `NULL` if no return occurred. |
| `sale_price` | FLOAT | The actual price the customer paid for the unit. This is the authoritative figure for realized revenue and may differ from `products.retail_price` due to promotions or markdowns. |

---

## Order Lifecycle and Status Funnel

`order_items.status` tracks the order funnel at the line-item grain. Because an order containing multiple items can be partially fulfilled or partially returned, the item-level status can differ from the parent order's status (e.g., an order may be marked **Complete** while one of its corresponding order items is **Returned**). For item-level accuracy, metrics related to returns and fulfillment must be calculated using `order_items.status` rather than `orders.status`.

The timestamp columns can be used to construct a funnel and perform cycle-time analysis:
*   **Processing Time:** `shipped_at` - `created_at`
*   **Transit Time:** `delivered_at` - `shipped_at`
*   **Return Latency:** `returned_at` - `delivered_at`

---

## Core Business Metrics

### Revenue Types
*   **Gross Revenue:** Computed by summing `sale_price` for all items that are **not Cancelled**. Cancelled items represent unfulfilled transactions and must be excluded.
*   **Net Revenue:** Computed by summing `sale_price` for all items that are **neither Cancelled nor Returned**. This represents gross revenue with the value of returned items removed.

### Average Order Value (AOV)
AOV is calculated at the order level using item-level revenue: 
*   `Gross Revenue / Count of Distinct Orders`

### Units Sold
The total count of sold units, calculated as the total count of `order_items.id` where the status is **not Cancelled**.

### Return Rate
The share of sold units that were later returned:
*   `Count of order items with a non-null returned_at / Count of non-cancelled order items`

### Gross Margin and Margin %
*   **Gross Margin:** The profit on a unit before operating costs, evaluated over non-returned and non-cancelled items. It is calculated by taking `sale_price` from `order_items` and subtracting `cost` (sourced by joining `order_items.product_id` to `products.id` and using `products.cost`).
*   **Gross Margin %:** Calculated as `Gross Margin / Net Revenue` (or `(sale_price - cost) / sale_price` at the item level).

---

## Lineage and Relationships

The `order_items` table connects to the rest of theLook eCommerce ecosystem through the following foreign keys:
*   `order_items.order_id` → `orders.order_id` (Ties line items to the parent checkout event)
*   `order_items.user_id` → `users.id` (Ties line items to the customer profile and their acquisition `traffic_source`)
*   `order_items.product_id` → `products.id` (Associates the transaction with the authoritative master catalog details, such as department, category, brand, and retail price)
*   `order_items.inventory_item_id` → `inventory_items.id` (Links the line item to the physical stock unit that fulfilled the sale)

---

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Order Lifecycle and Status](https://docs.google.com/document/d/1fm5barRArG0T_KLCIXWnpUwXkaVNdlHNFljmcQ4ppfA/edit?usp=drivesdk)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
*   [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)

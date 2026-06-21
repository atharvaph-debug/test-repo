# orders Overview

The `orders` table contains programmatically generated order records for theLook eCommerce, a fictitious multi-brand online apparel and accessories retailer. The grain of this table is **one row per order** (a single checkout event placed by a customer). 

This table tracks the overall state of each checkout event, the customer who placed it, the total number of items included, and the key lifecycle timestamps as the order progresses from placement to fulfillment or return.

## Schema

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **order_id** | INTEGER | The unique identifier for the checkout event / order. |
| **user_id** | INTEGER | The unique identifier of the customer who placed the order. Joins to `users.id`. |
| **status** | STRING | The overall fulfillment and lifecycle state of the order. |
| **gender** | STRING | Gender associated with the order. |
| **created_at** | TIMESTAMP | The timestamp when the order was placed. |
| **returned_at** | TIMESTAMP | The timestamp when the order was returned (if applicable). |
| **shipped_at** | TIMESTAMP | The timestamp when the order shipped from the distribution center. |
| **delivered_at** | TIMESTAMP | The timestamp when the order reached the customer. |
| **num_of_item** | INTEGER | The total number of items purchased in this single checkout event. |

## Order Grain vs. Order Item Grain

It is critical not to confuse the **Order** grain with the **Order Item** grain:
* An **Order** (`orders` table) represents a single checkout event. One order can contain multiple items, and the total count of these items is recorded in `num_of_item`.
* An **Order Item** (`order_items` table) represents a single unit of a single product within that order. The `order_items` table is the true revenue-bearing grain where pricing, cost, and item-level returns are calculated.

Because an order can be partially fulfilled or partially returned, item-level statuses in `order_items` can differ from the parent order's `status` in this table (e.g., a parent order may have a status of **Complete** while one of its constituent order items has a status of **Returned**). For accurate fulfillment, return, and revenue metrics, analysts should calculate metrics at the order-item grain rather than relying solely on the parent order status.

## Order Lifecycle and Statuses

The `status` column represents the overall state of the order. The typical lifecycle stages are:

1. **Processing**: The order has been placed and is being prepared. Payment has been captured, but the items have not yet shipped.
2. **Shipped**: The order has left a distribution center.
3. **Complete**: The order was delivered to the customer, and the return window has closed.
4. **Returned**: One or more items from the order were returned.
5. **Cancelled**: The order was cancelled before fulfillment and generated no revenue.

## The Timestamp Funnel

The sequence of timestamp columns tracks how an order moves through the processing and fulfillment pipeline. They are used to calculate transition latency:
* **Processing Time**: `shipped_at` - `created_at`
* **Transit Time**: `delivered_at` - `shipped_at`
* **Return Latency**: `returned_at` - `delivered_at`

A `NULL` value in any of these timestamp columns indicates that the corresponding stage has not yet occurred.

## Key Relationships

* **`orders.user_id` → `users.id`**: Connects each order to the customer who placed it. This join allows analysts to connect orders to customer demographics (such as age, gender, and location) and attribute order activity to the customer's acquisition marketing channel (`users.traffic_source`).
* **`order_items.order_id` → `orders.order_id`**: Joins individual sold items back to their parent checkout event. This relationship is essential for calculating order-level metrics like Average Order Value (AOV).

## Source References

* [theLook eCommerce — Order Lifecycle and Status](https://docs.google.com/document/d/1fm5barRArG0T_KLCIXWnpUwXkaVNdlHNFljmcQ4ppfA/edit?usp=drivesdk)
* [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
* [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
* [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)

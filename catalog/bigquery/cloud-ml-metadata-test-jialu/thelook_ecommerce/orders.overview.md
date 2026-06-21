# Orders Overview

The `orders` table contains programmatically generated order data for theLook, a fictitious multi-brand online apparel and accessories retailer. It represents transaction events at the checkout level, capturing the lifecycle, progression, and timing of each purchase event placed by a customer. 

## Key Columns

*   **`order_id`** (INTEGER): The unique identifier for each order.
*   **`user_id`** (INTEGER): The identifier of the customer who placed the order, linking directly to the `users` table.
*   **`status`** (STRING): The overall state of the order (e.g., Processing, Shipped, Complete, Returned, Cancelled).
*   **`gender`** (STRING): Demographic gender identifier associated with the order.
*   **`created_at`** (TIMESTAMP): The date and time when the customer placed the order.
*   **`shipped_at`** (TIMESTAMP): The date and time when the order left a distribution center. This field is `NULL` if the order has not yet shipped.
*   **`delivered_at`** (TIMESTAMP): The date and time when the order reached the customer. This field is `NULL` if the order has not yet been delivered.
*   **`returned_at`** (TIMESTAMP): The date and time when the order was returned. This field is `NULL` if no return occurred.
*   **`num_of_item`** (INTEGER): The total number of physical product items included in this single checkout event.

## Order Grain vs. Order Item Grain

It is critical to distinguish between the **Order** grain and the **Order Item** grain:
*   **Order Grain (`orders`)**: Represents a single, distinct purchase checkout event. An order can contain multiple items, tracked in aggregate by the `num_of_item` column. 
*   **Order Item Grain (`order_items`)**: Tracks individual units sold. While the `orders` table tracks the high-level order metadata, financial metrics (such as revenue, margin, and units-sold) are computed at the order-item grain. For example, if a customer purchases three items in a single transaction, it generates **one order** in the `orders` table but **three order items** in the `order_items` table.

## Order Lifecycle and Status

The `status` column describes the current progression of the order. The typical lifecycle stages include:

1.  **Processing**: The order has been placed and is being prepared. Payment has been captured, but the items have not yet shipped.
2.  **Shipped**: The order has departed from a distribution center.
3.  **Complete**: The order has been delivered successfully and the return window is closed.
4.  **Returned**: One or more items from the order were sent back.
5.  **Cancelled**: The order was cancelled prior to fulfillment. Cancelled orders do not generate revenue.

### The Timestamp Funnel
The sequence of timestamps (`created_at` $\rightarrow$ `shipped_at` $\rightarrow$ `delivered_at` $\rightarrow$ `returned_at`) allows for operational funnel and cycle-time analysis:
*   **Processing Time**: Evaluated as `shipped_at - created_at`
*   **Transit Time**: Evaluated as `delivered_at - shipped_at`
*   **Return Latency**: Evaluated as `returned_at - delivered_at`

*Note: A `NULL` value in any of these timestamp columns indicates that the specific lifecycle stage has not yet occurred.*

## Relationships and Joins

*   **Users Connection**: The `orders.user_id` column joins to `users.id`. This link allows analysts to attribute order activity and subsequent revenue to customer demographics and marketing channels (such as grouping by `users.traffic_source`).
*   **Order Items Connection**: The `order_items.order_id` column joins to `orders.order_id`. Although the tables share identical status categories, individual item statuses can deviate from the overall order status (e.g., an entire order may be marked "Complete" while one specific line item is "Returned"). Analysts must look to the item grain (`order_items`) when line-level metric accuracy is required.

## Source References

*   [theLook eCommerce — Order Lifecycle and Status](https://docs.google.com/document/d/1fm5barRArG0T_KLCIXWnpUwXkaVNdlHNFljmcQ4ppfA/edit?usp=drivesdk)
*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
*   [theLook eCommerce — Metric Definitions](https://docs.google.com/document/d/1vN-UzBhsCeC5v7lmzyeVqo131MFddhFuL3BNpy1mAhk/edit?usp=drivesdk)

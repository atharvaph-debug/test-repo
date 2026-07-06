# Transactional Grains Overview

Transactional Grains refer to the distinct levels of detail used to capture purchase events and individual product units. This concept provides clear mappings for understanding the increments that separate overall customer purchase events from the individual products involved, which is crucial for metadata enrichment and analytical accuracy. The two primary transactional grains are 'Order' and 'Order Item'.

## Key Grains

The business defines two distinct transactional grains:

*   **Order**: Represents a single purchase event initiated by a customer (`user_id`). An order carries an overall fulfillment status and records the total number of items purchased via `num_of_item`. An order corresponds to one row in the `orders` table.
*   **Order Item**: Represents a single unit of a single product within an order. This is the actual revenue grain where key metrics such as revenue, margin, and units-sold are computed. For instance, if a customer buys two shirts and one hat in a single transaction, this constitutes one order but three distinct order items. Order items correspond to rows in the `order_items` table.

## Schema & Relationships

The `order_items` table serves as the central fact table for revenue and acts as a primary hub, linking to other key entities:

*   **`orders`**: Contains one row per order (checkout event).
*   **`order_items`**: Contains one row per product unit in an order. It links to:
    *   `orders` via `order_items.order_id` $\rightarrow$ `orders.order_id`.
    *   `users` via `order_items.user_id` $\rightarrow$ `users.id`.
    *   `products` via `order_items.product_id` $\rightarrow$ `products.id`.
    *   `inventory_items` via `order_items.inventory_item_id` $\rightarrow$ `inventory_items.id`.
*   **`users`**: Contains one row per customer, holding demographics, location, acquisition channel (`users.traffic_source`), and signup time.
*   **`products`**: Contains one row per sellable SKU. Products are organized into a three-level hierarchy: `Department`, `Category`, and `Brand`. Each product is mapped to a `Distribution Center` via `products.distribution_center_id` $\rightarrow$ `distribution_centers.id`.
*   **`inventory_items`**: Contains one row per physical unit of stock. Product attributes are denormalized onto `inventory_items` (under `product_*` prefix columns) for simplified inventory queries. The `products` table remains the authoritative master for product attributes.
*   **`distribution_centers`**: Contains one row per fulfillment warehouse, including names and latitude/longitude coordinates for shipping optimization.

## Pricing Metadata

The pricing metadata defines various cost and price points:

*   **Cost**: What the company paid the supplier for a unit (wholesale/landed cost). This is found in `products.cost` and `inventory_items.cost` and is never exposed to customers.
*   **Retail Price**: The catalog or reference list price advertised for a product before discounts, stored as `products.retail_price`.
*   **Sale Price**: The actual price paid by the customer, recorded on the transaction line as `order_items.sale_price`. This figure is authoritative for realized revenue and may differ from the retail price due to markdowns or promotions.

## Transactional Lifecycle & Statuses

Order and item-level statuses track the progression of a transaction:

*   **`Processing`**: Order placed, inventory being prepared, payment captured, but not yet shipped.
*   **`Shipped`**: Package has left the designated distribution center.
*   **`Complete`**: Order successfully delivered to the customer; the return window is closed.
*   **`Returned`**: One or more items returned by the customer, reversing revenue/margin.
*   **`Cancelled`**: Halted prior to fulfillment; generates zero revenue.

For accurate operations and financial models, `order_items.status` should be utilized over the parent `orders.status`, as orders can be split or partially returned. Timestamps (e.g., `shipped_at`, `created_at`, `delivered_at`, `returned_at`) are `NULL` if a stage has not occurred and can be used to calculate operational cycles such as:

*   **Processing Time**: `shipped_at - created_at`
*   **Transit Time**: `delivered_at - shipped_at`
*   **Return Latency**: `returned_at - delivered_at`

## Key Metrics

Transactional grains are fundamental to calculating various business metrics:

*   **Gross Revenue**: `SUM(order_items.sale_price)` where `status` is not 'Cancelled'.
*   **Net Revenue**: `SUM(order_items.sale_price)` where `status` is not 'Cancelled' or 'Returned'.
*   **Average Order Value (AOV)**: `Gross Revenue / COUNT(DISTINCT order_items.order_id)`. This is an order-grain KPI computed using item-grain transaction details.
*   **Units Sold**: `COUNT(order_items.id)` where `status` is not 'Cancelled'.
*   **Return Rate**: `COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status != 'Cancelled')`.
*   **Gross Margin**: `SUM(order_items.sale_price - products.cost)` where `status` is not 'Cancelled' or 'Returned'. This calculation requires joining `order_items.product_id` to `products.id`.
*   **Gross Margin %**: `Gross Margin / Net Revenue`.
*   **Sell-Through Rate**: `COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)`.
*   **Average Days in Inventory**: `MEAN(sold_at - created_at)` over sold inventory items.

## Source References

*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

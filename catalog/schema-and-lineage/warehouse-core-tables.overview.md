# Warehouse Core Tables Overview

The Warehouse Core Tables represent the foundational schema for critical business entities, serving as the base entity grains and relational endpoints within the data warehouse. These tables capture core transactional and master data, providing the building blocks for analytical reporting and operational insights.

## Core Entities and Grains

The core tables define the primary entities and their respective data granularities:

*   **`users`**: Contains one row per customer, storing demographic information (age, gender), location details, the acquisition channel, and the signup timestamp.
*   **`orders`**: Represents a single purchase event or checkout, with one row per order. It includes an overall fulfillment status and records the total number of items via `num_of_item`. Note that `orders.status` is a high-level indicator, and the authoritative status for operations and financial models is `order_items.status`.
*   **`order_items`**: This is the central fact table for revenue, with one row per single unit of a product within an order. It is the grain at which metrics like revenue, margin, and units-sold are computed. For example, a purchase of two shirts and one hat results in one `order` and three `order_items`.
*   **`products`**: Holds one row per sellable Stock Keeping Unit (SKU), defining product attributes and pricing.
*   **`inventory_items`**: Records one row per physical unit of stock, tracking individual inventory units. Product attributes are denormalized onto `inventory_items` using `product_*` prefix columns for simplified inventory queries, though the `products` table remains the authoritative source for product master data.
*   **`distribution_centers`**: Contains one row for each physical fulfillment warehouse, including its name and geographical coordinates (latitude/longitude) used for shipping optimization.

## Key Relationships and Joins

The `order_items` table acts as a central hub, linking to other core entities:

*   `orders.user_id` links to `users.id`
*   `order_items.order_id` links to `orders.order_id`
*   `order_items.user_id` links to `users.id`
*   `order_items.product_id` links to `products.id`
*   `order_items.inventory_item_id` links to `inventory_items.id`
*   `products.distribution_center_id` links to `distribution_centers.id`
*   `inventory_items.product_id` links to `products.id`

## Key Columns and Business Semantics

These tables contain crucial metadata fields that define their business meaning:

*   **`users.traffic_source`**: Identifies the acquisition channel (e.g., Search, Organic, Email, Display, Facebook) for a user, enabling channel-attribution analysis.
*   **`products.cost`**: The wholesale or landed cost paid by the company to the supplier for a product unit.
*   **`inventory_items.cost`**: Similar to `products.cost`, representing the company's cost for a physical inventory unit. This cost is never exposed to customers.
*   **`products.retail_price`**: The advertised catalog or reference list price for a product before any discounts are applied.
*   **`order_items.sale_price`**: The actual price paid by the customer for a product unit, recorded on the transaction line. This is the authoritative figure for realized revenue and may differ from the `retail_price` due to markdowns or promotions.
*   **Product Taxonomy**: Products are organized into a three-level hierarchy using `Department` (broadest, e.g., Men, Women), `Category` (e.g., Jeans, Outerwear), and `Brand` (manufacturer/label).
*   **Order and Item Lifecycle Statuses**:
    *   **`Processing`**: Order placed, inventory prepared, payment captured, but not yet shipped.
    *   **`Shipped`**: Package has left the designated distribution center.
    *   **`Complete`**: Order successfully delivered to the customer, and the return window is closed.
    *   **`Returned`**: One or more items were returned by the customer, reversing revenue/margin.
    *   **`Cancelled`**: Order was halted prior to fulfillment; it generates zero revenue.
    *   **Status Grain Nuances**: Due to partial returns or split orders, `order_items.status` tracks the state at the line item level and is the authoritative status for accurate operations and financial models over `orders.status`.
*   **Timestamps for Lifecycle Events**:
    *   `created_at`: Timestamp when the order item was created.
    *   `shipped_at`: Timestamp when the item was shipped.
    *   `delivered_at`: Timestamp when the item was delivered.
    *   `returned_at`: Timestamp when the item was returned.
    *   `sold_at`: Timestamp when an `inventory_item` was sold.
    These timestamps are `NULL` if a stage has not occurred and are used for funnel and latency calculations.

## Derived Business Metrics

These core tables are essential for calculating key business performance indicators:

*   **Gross Revenue**:
    ```
    SUM(order_items.sale_price) WHERE status != 'Cancelled'
    ```
    Cancelled orders generate no revenue and are strictly omitted.
*   **Net Revenue**:
    ```
    SUM(order_items.sale_price) WHERE status NOT IN ('Cancelled', 'Returned')
    ```
    Net revenue excludes both returned and cancelled items.
*   **Average Order Value (AOV)**:
    ```
    Gross Revenue / COUNT(DISTINCT order_items.order_id)
    ```
    This is an order-grain KPI computed using item-grain transaction details.
*   **Units Sold**:
    ```
    COUNT(order_items.id) WHERE status != 'Cancelled'
    ```
*   **Return Rate**:
    ```
    COUNT(order_items WHERE returned_at IS NOT NULL) / COUNT(order_items WHERE status != 'Cancelled')
    ```
*   **Gross Margin**:
    ```
    SUM(order_items.sale_price - products.cost) WHERE status NOT IN ('Cancelled', 'Returned')
    ```
    Requires joining `order_items.product_id` to `products.id`.
*   **Gross Margin %**:
    ```
    Gross Margin / Net Revenue
    ```
*   **Sell-Through Rate**:
    ```
    COUNT(inventory_items WHERE sold_at IS NOT NULL) / COUNT(inventory_items)
    ```
*   **Average Days in Inventory**:
    ```
    MEAN(sold_at - created_at) over sold inventory items
    ```

## Latency Calculations

Timestamps within `order_items` and `inventory_items` allow for the calculation of operational cycle times:

*   **Processing Time**: `shipped_at - created_at`
*   **Transit Time**: `delivered_at - shipped_at`
*   **Return Latency**: `returned_at - delivered_at`

## Denormalization and Data Lineage

Product attributes are denormalized onto `inventory_items` using `product_*` prefixed columns to simplify inventory-related queries. However, the `products` table remains the authoritative master for product data. In cases of discrepancies between `products` and the denormalized `inventory_items.product_*` columns, queries must rely on the data in the `products` table.

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
* [order_lifecycle.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB678C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

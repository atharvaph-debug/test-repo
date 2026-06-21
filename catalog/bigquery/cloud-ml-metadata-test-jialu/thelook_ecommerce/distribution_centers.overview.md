# distribution_centers Overview

The `distribution_centers` table is a dimension table in theLook eCommerce dataset that represents physical fulfillment warehouses. It serves as the single source of truth for distribution center locations, enabling analysts and engineers to perform logistics, fulfillment, and shipping-time analysis.

The grain of this table is **one row per fulfillment warehouse**.

## Schema & Key Columns

The table contains the following columns:

*   **`id`** (INTEGER): The unique identifier for each distribution center. This acts as the primary key at the warehouse grain.
*   **`name`** (STRING): The name of the fulfillment warehouse.
*   **`latitude`** (FLOAT): The geographic latitude of the distribution center, used to locate the warehouse and calculate shipping distances.
*   **`longitude`** (FLOAT): The geographic longitude of the distribution center, used alongside latitude for mapping and logistics.
*   **`distribution_center_geom`** (GEOGRAPHY): The geospatial representation of the distribution center's location.

## Relationships & Lineage

The distribution center acts as the origin point for the physical inventory and products sold on theLook platform. Its relationships across the schema include:

*   **`products.distribution_center_id` → `distribution_centers.id`**: Every sellable product (SKU) in the `products` table is assigned to exactly one distribution center where its inventory is stored and from which it is shipped.
*   **Denormalization Note**: The `inventory_items` table (which tracks physical units of stock) contains a denormalized column named `product_distribution_center_id`. This column is copied from the `products` table for querying convenience. However, the authoritative source for product-to-warehouse assignments is the `products` table itself. If a discrepancy occurs, trust the relationship defined via `products.distribution_center_id`.

## Business Context

In theLook's multi-brand apparel and accessories retail model, tracking distribution centers is vital for supply chain operations. Every physical product is stocked and shipped from one of these warehouses. By joining the distribution center's geographic coordinates (`latitude` and `longitude`) with customer locations found in the `users` table, analysts can measure shipping performance, analyze regional fulfillment latency, and optimize inventory distribution.

## Source References

* [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
* [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)

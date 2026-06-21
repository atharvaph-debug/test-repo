# distribution_centers Overview

The `distribution_centers` table represents the physical fulfillment warehouses utilized by theLook, a multi-brand online apparel and accessories retailer. It operates at a grain of one row per warehouse. This dataset is primarily used for tracking where products are stocked, managing logistics, and performing shipping-time and fulfillment analyses.

## Key Columns

*   **`id`** (INTEGER): The unique identifier for each distribution center.
*   **`name`** (STRING): The name of the fulfillment warehouse.
*   **`latitude`** (FLOAT): The latitude coordinate of the warehouse's physical location.
*   **`longitude`** (FLOAT): The longitude coordinate of the warehouse's physical location.
*   **`distribution_center_geom`** (GEOGRAPHY): The spatial geography point of the warehouse, used for mapping and geographic analyses.

## Business Context

A distribution center is a physical warehouse that stocks and ships products. Every product in the catalog is assigned to exactly one distribution center. Analysts and logistics teams use the geographic coordinates (latitude and longitude) associated with each center to optimize inventory distribution, track shipping performance, and analyze fulfillment times.

## Relationships

*   **Product Assignment (`products.distribution_center_id` → `distribution_centers.id`):** Every product is mapped to exactly one distribution center. This is the primary relationship used to identify where items are stored.
*   **Denormalization in Inventory (`inventory_items.product_distribution_center_id`):** While the authoritative assignment of a product to a warehouse lives in the `products` table, this relationship is denormalized onto the `inventory_items` table (as `product_distribution_center_id`) for analytical convenience. In the event of any discrepancy between the two tables, the `products` table is the source of truth.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)

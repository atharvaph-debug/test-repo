# users Overview

The `users` table contains records of programmatically generated users for theLook, a fictitious multi-brand online apparel and accessories retailer. The table is structured at the customer level (grain: customer), meaning it contains exactly one row per customer. It serves as the primary source of truth for customer demographics, physical locations, signup details, and acquisition marketing channels.

## Key Columns

* **`id`**: The unique identifier for each customer. This column acts as the primary key for the table.
* **`first_name` & `last_name`**: The customer's first and last name.
* **`email`**: The contact email address of the customer.
* **`age`**: The customer's age, used for demographic analysis.
* **`gender`**: The customer's gender, used for demographic segmentation.
* **`street_address`, `city`, `state`, `postal_code`, & `country`**: The physical mailing address details for the customer.
* **`latitude` & `longitude`**: The geographic coordinates representing the customer's location.
* **`user_geom`**: A geography spatial data type mapping the physical location of the user.
* **`traffic_source`**: The marketing channel that brought the customer to theLook (e.g., Search, Organic, Email, Display, and Facebook). This is the basis for customer-acquisition and channel-attribution analysis.
* **`created_at`**: The timestamp marking when the user account was created (signup time).

## Business Context

The `users` table is heavily leveraged for customer-acquisition and channel-attribution analysis. By analyzing the `traffic_source` column, analysts can evaluate which marketing channels are most successful at driving customer signups and lifetime value. 

Additionally, the demographic and spatial data (`age`, `gender`, and various location attributes like `user_geom`) allow the commerce data and analytics teams to perform spatial queries, cohort analyses, and regional performance reporting.

## Relationships & Lineage

The customer sits at the beginning of the e-commerce lifecycle, establishing relationships with key downstream transactional tables:

* **Orders to Users:** The `orders` table links to the `users` table by joining the `orders.user_id` field to the `users.id` field. This maps checkout events to customer demographics and locations. It is also used to evaluate customer acquisition channel revenue attribution by grouping user records by `traffic_source` and joining them through orders.
* **Order Items to Users:** The central transaction table, `order_items`, directly links to this table by joining `order_items.user_id` to `users.id`. This direct connection bypasses the order-level table, allowing analysts to quickly associate individual sold items and revenue calculations to the customer who purchased them.

## Source References

* [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)
* [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)

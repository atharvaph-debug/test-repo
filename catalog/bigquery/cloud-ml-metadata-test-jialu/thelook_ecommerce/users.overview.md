# users Overview

The `users` table contains programmatically generated user profiles for theLook, a fictitious multi-brand online apparel and accessories retailer. The table maintains a record of customer demographic information, precise geographic location, account registration details, and marketing acquisition channels.

The grain of this table is **one row per customer**.

## Schema & Key Columns

The table consists of the following columns:

*   **`id`**: The unique identifier for each customer (Primary Key).
*   **`first_name`**: The first name of the customer.
*   **`last_name`**: The last name of the customer.
*   **`email`**: The email address associated with the customer's account.
*   **`age`**: The demographic age of the customer.
*   **`gender`**: The demographic gender of the customer.
*   **`street_address`**, **`city`**, **`state`**, **`postal_code`**, and **`country`**: Complete geographic address data representing where the customer resides.
*   **`latitude`** & **`longitude`**: Exact geographic coordinates of the customer's location.
*   **`user_geom`**: The spatial `GEOGRAPHY` object corresponding to the customer's location coordinates.
*   **`traffic_source`**: The marketing acquisition channel that originally brought the customer to theLook.
*   **`created_at`**: The timestamp representing when the customer registered their account.

## Key Concepts

### Traffic Source Analysis
The `traffic_source` column records the specific marketing channel responsible for acquiring the customer. Common values include:
*   Search
*   Organic
*   Email
*   Display
*   Facebook

This attribute is primarily used by analysts and data scientists to evaluate customer acquisition costs, channel-specific conversion rates, and overall marketing channel attribution.

## Relationships & Joins

The `users` table serves as a foundational dimension table for transaction and behavioral analysis, joining out to the core transaction tables:

*   **`orders.user_id` → `users.id`**: Connects customer accounts to checkout events (orders). This mapping is essential for **Customer Acquisition Channel Revenue Attribution**, allowing teams to group purchasing behavior and revenue by marketing channels (`traffic_source`) via the `orders` table.
*   **`order_items.user_id` → `users.id`**: Provides a direct relationship to the central revenue grain (`order_items`). This allows queries to directly link demographic factors (like age or gender) and acquisition sources to specific products sold, unit counts, and gross margins without requiring an intermediate join through the `orders` table.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://docs.google.com/document/d/1MdZqPrd1zg4yXxNzEcpzyr-jfl0WX9jBCZTaQaNsy8U/edit?usp=drivesdk&resourcekey=0-iY-s9PeHf0gtu1K7Bs4UdQ)
*   [theLook eCommerce — Business Glossary](https://docs.google.com/document/d/1YjHrEU7yGpJ4rTduR2KMzKoKYfv72EQtBOpIdgFC3OI/edit?usp=drivesdk&resourcekey=0-hhk4row7bi7ObbSH6vUWoQ)

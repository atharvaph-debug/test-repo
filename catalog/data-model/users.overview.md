# Users Table Overview

The `users` table serves as the primary repository for customer data, with each row representing a unique customer. It stores essential demographic information, geographical location, and details about how the customer was acquired. This table is foundational for understanding customer segments and their behavior within the e-commerce ecosystem.

## Key Features

The `users` table provides key attributes for customer analysis:
*   **Demographics**: Includes data points such as age and gender, allowing for demographic segmentation of the customer base.
*   **Location**: Stores geographical information for each customer.
*   **Acquisition Channel (`traffic_source`)**: This column is crucial for marketing analysis, indicating the specific marketing channel (e.g., Search, Organic, Email, Display, Facebook) that led to a customer's acquisition. It forms the basis for acquisition and channel attribution reporting.

## Schema

The table's grain is one row per customer. Key columns include:
*   **`id`**: A unique identifier for each customer, serving as the primary key for the `users` table.
*   **`traffic_source`**: Defines the marketing channel responsible for acquiring the customer. This field is vital for analyzing customer acquisition costs and channel effectiveness.
*   **Demographic and Location Data**: Other columns capture details such as age, gender, and geographical location.

## Relationships

The `users` table is central to understanding customer interactions and transactions:
*   A `users` record can be linked to `orders` via `orders.user_id` which references `users.id`. This establishes the customer who placed a particular order.
*   Similarly, `users` is directly linked to `order_items` via `order_items.user_id` referencing `users.id`, allowing for direct analysis of customer purchases at the item level.

## Source References
*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)
*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)

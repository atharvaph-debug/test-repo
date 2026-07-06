# Users Table Overview

The `Users` table (also known by its alias `users`) represents individual customers in the eCommerce data model. It operates at a `customer` grain, meaning each row uniquely identifies a customer and contains their demographic details, location information, the source of their acquisition, and their sign-up timestamps.

## Key Features

The `Users` table captures comprehensive customer information, including:

*   **Customer Identifier (`id`):** A unique identifier for each customer, used to link customer data to their orders and order items.
*   **Demographic Details:** Includes `age` and `gender` for customer segmentation and analysis.
*   **Location Information:** Provides geographical details such as `city`, `state`, `country`, and precise `latitude/longitude` coordinates.
*   **Acquisition Channel (`traffic_source`):** Indicates how the customer was acquired.
*   **Sign-up Timestamp (`created_at`):** Records when the customer account was created.

## Relationships

The `Users` table serves as a dimension table that relates to transactional tables within the data model:

*   **Orders:** The `orders` table relates back to `Users` via `orders.user_id` $\rightarrow$ `users.id`, indicating which customer placed a specific order.
*   **Order Items:** The `order_items` table also relates to `Users` via `order_items.user_id` $\rightarrow$ `users.id`, allowing for analysis of individual transaction line items in the context of the customer.

## Source References

*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

# Users Overview

The `Users` table, also known as `customer`, serves as the central repository for customer-specific metadata. It contains one row per customer, detailing demographic information, geographical location, acquisition channel, and the time of signup. This table is crucial for understanding customer segments and their journey.

## Key Features

The `Users` table provides comprehensive metadata for each customer, enabling detailed analysis of user characteristics and behavior.

*   **Customer Grain**: Each row uniquely identifies a single customer.
*   **Demographics**: Includes information such as age and gender.
*   **Geographical Location**: Stores details like city, state, country, and precise latitude/longitude coordinates.
*   **Acquisition Channel**: Captures the `traffic_source`, indicating how the customer was acquired.
*   **Signup Time**: Records the `created_at` timestamp for when the customer account was established.

## Schema

The `users` table includes the following key columns:

*   **`id`**: A unique identifier for each customer. This column is used as a foreign key in other tables, such as `orders` and `order_items`, to link transactions back to a specific customer.
*   **`age`**: The age of the customer.
*   **`gender`**: The gender of the customer.
*   **`city`**: The city where the customer is located.
*   **`state`**: The state where the customer is located.
*   **`country`**: The country where the customer is located.
*   **`latitude`**: The geographical latitude coordinate of the customer's location.
*   **`longitude`**: The geographical longitude coordinate of the customer's location.
*   **`traffic_source`**: The acquisition channel through which the customer first engaged. Typical values include 'Search', 'Organic', 'Email', 'Display', and 'Facebook'. This column is vital for marketing attribution analysis.
*   **`created_at`**: The timestamp indicating when the customer account was created or signed up.

## Relationships

The `users` table is a foundational entity within the data model, connected to transaction data through the `user_id`.

*   **`orders`**: The `orders` table links to `users` via `orders.user_id` $\rightarrow$ `users.id`.
*   **`order_items`**: The `order_items` table also links to `users` via `order_items.user_id` $\rightarrow$ `users.id`.

## Marketing Attribution

The `traffic_source` column within the `users` table is specifically designated for marketing attribution analysis. It provides the channel through which a customer was acquired, with typical values like 'Search', 'Organic', 'Email', 'Display', and 'Facebook'. This allows for evaluating the effectiveness of different marketing campaigns and understanding customer acquisition paths.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

# Users Table Overview

The `Users Table`, also known as `users`, represents customer accounts within the e-commerce data model. Each row in this table corresponds to a single customer, providing a detailed profile of their attributes. It includes customer demographics, geographic location, acquisition channel, and account creation timestamps.

## Key Features

The `Users Table` captures essential customer data at a grain of one row per customer. It includes the following types of information:

*   **Demographic Attributes:** Such as `age` and `gender`.
*   **Geographical Data:** Including `city`, `state`, `country`, and `latitude/longitude`.
*   **Acquisition Channel:** Recorded as `traffic_source`, indicating how the user was acquired.
*   **Account Creation Time:** Stored in the `created_at` field.

## Relationships

The `Users Table` is a central dimension in the e-commerce data model, linking to other tables to provide a complete view of customer activity:

*   **Orders:** The `orders.user_id` column links to the `users.id` column, indicating which customer placed a specific order.
*   **Order Items:** The `order_items.user_id` column also links to the `users.id` column, associating individual product units within an order back to the customer who purchased them.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

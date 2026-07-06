# Users Table Overview

The `Users Table`, also known by the alias `users`, serves as a core data model representing individual customers at the customer grain. It is a central repository for various types of metadata associated with each user, which can be used to enrich analyses across other data models.

## Key Features

This table holds extensive metadata for each customer, providing a comprehensive profile for enrichment purposes:

*   **Customer Grain**: Each record in this table represents a unique individual customer. The primary identifier for a user is implicitly `id`, as other tables link to `users.id`.
*   **Demographic Metadata**: Includes information such as `age` and `gender` for each user.
*   **Geographical Metadata**: Stores location details including `city`, `state`, `country`, `latitude`, and `longitude`.
*   **Acquisition Channel**: Tracks the `traffic_source` through which the user was acquired.
*   **Signup Timestamps**: Records the `created_at` timestamp, indicating when the user signed up.

## Relationships

The `Users Table` is linked to other key data models through foreign keys, allowing for the enrichment of transactional data with user-specific information:

*   `Orders Table`: The `orders` table links back to individual customers via `orders.user_id` which references `users.id`.
*   `Order Items Table`: The `order_items` table also links to individual customers via `order_items.user_id` referencing `users.id`.

## Source References

*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

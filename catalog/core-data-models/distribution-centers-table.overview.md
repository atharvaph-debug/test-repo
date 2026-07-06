# Distribution Centers Table Overview

The `Distribution Centers Table` (`distribution_centers`) tracks individual fulfillment warehouses and their locations, operating at the warehouse grain. This table serves as a metadata catalog for the physical locations where products are stored and fulfilled.

## Key Features

This table represents each distinct fulfillment warehouse. While specific columns are not detailed, it is designed to hold information about these locations.

## Schema

*   **`id`**: This column uniquely identifies each distribution center. It serves as the primary key for this table and is referenced by other tables to link products to their associated distribution centers.

## Relationships

The `Distribution Centers Table` plays a crucial role in understanding product origin and inventory placement within the data model.
*   `products.distribution_center_id` $\rightarrow$ `distribution_centers.id`: Products are linked to their respective distribution centers via the `distribution_center_id` column in the `products` table.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

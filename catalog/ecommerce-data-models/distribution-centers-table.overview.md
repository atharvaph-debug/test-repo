# Distribution Centers Table Overview

The `Distribution Centers` table, also known as `distribution_centers`, represents fulfillment warehouses, operating at a `warehouse` grain. It serves as a dimension table providing details about the physical locations where products are stored and from which they are dispatched.

## Key Features

*   **Grain**: The table captures information at a `warehouse` grain, meaning each record corresponds to a unique fulfillment warehouse.

## Relationships

The `distribution_centers` table is linked to the `products` table.
*   `products.distribution_center_id` is a foreign key that references `distribution_centers.id`, indicating which distribution center is associated with a particular product.

## Source References
*   [theLook eCommerce — Data Model and Relationships](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

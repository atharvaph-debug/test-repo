# Distribution Centers Table Overview

The `distribution_centers` table is a dimension table within theLook eCommerce data model, designed to hold one row for each physical fulfillment warehouse. It serves as a central reference for information about these locations, which are crucial for stocking and shipping products.

## Key Features

*   **Grain**: Each row in this table represents a single fulfillment warehouse.
*   **Definition**: A Distribution Center is a physical warehouse responsible for stocking and shipping products.
*   **Attributes**: Each distribution center has a name and a geographic location, specified by latitude and longitude.
*   **Product Assignment**: Every product is assigned to one specific distribution center.

## Relationships

The `distribution_centers` table is linked to the `products` table via the `distribution_center_id`. Specifically, the `products.distribution_center_id` column acts as a foreign key, referencing the `id` column in the `distribution_centers` table. This relationship indicates which distribution center stocks and ships a particular product.

## Source References

*   [theLook eCommerce — Data Model and Relationships](1ZDPG_VXENJIHBTC63yrlq1Lq58mS6EoYleknZQtvl00)
*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)

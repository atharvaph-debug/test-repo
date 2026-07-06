# Denormalization and Lineage Rules Overview

This entry outlines the rules governing the replication of authoritative attributes and relational mappings within physical staging layers. It describes the key relationships between core data entities and specific denormalization strategies employed to optimize data access while maintaining data integrity and lineage.

## Core Entities

The data model defines several core entities, each with a specific grain:
*   `users`: Represents one row per customer, holding demographic information (age, gender), location, acquisition channel, and signup time.
*   `orders`: Contains one row for each checkout event.
*   `order_items`: Serves as the central fact table for revenue, with one row per product unit in an order.
*   `products`: Stores one row per sellable SKU.
*   `inventory_items`: Represents one row for each physical unit of stock.
*   `distribution_centers`: Holds one row per fulfillment warehouse.

## Key Relationships & Joins

The `order_items` table acts as the primary hub, linking outwards to other related tables through the following relationships:
*   `orders.user_id` links to `users.id`
*   `order_items.order_id` links to `orders.order_id`
*   `order_items.user_id` links to `users.id`
*   `order_items.product_id` links to `products.id`
*   `order_items.inventory_item_id` links to `inventory_items.id`

Additionally, other entities are related as follows:
*   `products.distribution_center_id` links to `distribution_centers.id`
*   `inventory_items.product_id` links to `products.id`

## Denormalization Rules

To simplify inventory queries, certain product attributes are denormalized onto the `inventory_items` table. These denormalized attributes are identified by a `product_*` prefix in their column names within `inventory_items`. The `products` table remains the authoritative master for these attributes. In cases where discrepancies or mismatches occur between attributes in the `products` table and the denormalized `inventory_items.product_*` columns, queries must always trust the data found in the `products` table.

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

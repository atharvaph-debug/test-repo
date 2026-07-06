# Relational Data Models and Table Schemas Overview

This entry defines the database structures, ETL pipelines, and relational constraints crucial for the eCommerce platform, encompassing user, order, product, and inventory entities. It details the standard schemas and entity relationships within the analytical warehouse database to ensure structural integrity.

## ETL Architecture & Lineage

The data model includes specifications for the daily Orders ETL pipeline, which runs at 03:00 UTC with an SLA completion of 05:00 UTC. This pipeline is orchestrated via the Airflow DAG `orders_daily_v3`, owned by the Data Platform team (`data-platform@company.example`), and has business ownership under Revenue Analytics (`revenue-analytics@company.example`).

**Source Inputs:**
*   **Stripe Payments API**: Provides `payment_intent_id`, `amount_cents`, and `currency`.
*   **Shopify Orders Export**: Provides `order_id`, `customer_id`, `total_amount`, and `status` (which can be `pending`, `paid`, or `refunded`).

**Target Output Table: `analytics.orders.orders_daily`**
The processed data lands in the BigQuery table `analytics.orders.orders_daily` with the following schema:
*   `order_id` (STRING): The Shopify order ID, serving as the Primary Key for this table.
*   `customer_id` (STRING): The Shopify customer ID, which joins to the `customers.customer_dim` table.
*   `total_amount_usd` (NUMERIC): The total amount of the order, normalized to USD.
*   `payment_status` (STRING): A mapped status derived from Shopify's statuses, indicating `pending`, `paid`, or `refunded`.
*   `created_at` (TIMESTAMP): The UTC timestamp when the order record was created.

**Operational Recovery:**
In case of Stripe API rate-limits, the pipeline can be re-run with `--max_rps=5`. Business owners are paged if the output row count falls below 80% of the 7-day median before initiating backfills.

## Data Model Grains

Standard schemas are established within the analytical warehouse to maintain structural integrity across the eCommerce platform. The `order_items` table serves as the central "Hub-and-Spoke" grain for revenue analytics, tying together customer, order, product, and specific physical stock unit information. Most analytical queries are designed to start here and join outwards.

**Key Entity Schema Grains:**
*   `users`: Represents customers with one row per customer, containing demographics, location, acquisition channel, and signup timestamp.
*   `orders`: Represents checkout events with one row per event, linking to `users` via `user_id`.
*   `order_items`: Represents the revenue grain with one row per product unit within an order.
*   `products`: Contains product attributes with one row per sellable SKU, acting as the authoritative source for product information.
*   `inventory_items`: Represents physical stock units with one row per unit.
*   `distribution_centers`: Represents fulfillment warehouses with one row per location.

## Foreign Key Relationships

The following foreign key relationships ensure data integrity and enable accurate joins across entities:
*   `orders.user_id` $\rightarrow$ `users.id`
*   `order_items.order_id` $\rightarrow$ `orders.order_id`
*   `order_items.user_id` $\rightarrow$ `users.id`
*   `order_items.product_id` $\rightarrow$ `products.id`
*   `order_items.inventory_item_id` $\rightarrow$ `inventory_items.id`
*   `products.distribution_center_id` $\rightarrow$ `distribution_centers.id`
*   `inventory_items.product_id` $\rightarrow$ `products.id`

## Controlled Denormalization

The `inventory_items` table employs controlled denormalization by including duplicate `product_*` columns (category, name, brand, retail price, department, SKU, and distribution center ID). This strategy aims to bypass the need for joins in common inventory-related queries. However, the `products` table remains the single source of truth for product attributes, resolving any discrepancies that may arise.

## Source References
*   [OrdersPipelineRunbook.txt](https://atharvasptest.sharepoint.com/sites/agent-demo/Shared%20Documents/OrdersPipelineRunbook.txt)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

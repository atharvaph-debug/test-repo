# Denormalization & Source of Truth Policy

This policy establishes the authoritative source for product-related attributes when conflicts arise between denormalized columns in the `inventory_items` table and the canonical `products` table. It is crucial for maintaining data consistency and ensuring data quality across related datasets.

## Policy Details

The `inventory_items` table includes denormalized columns, such as `product_category` and `product_retail_price`, which are prefixed with `product_*`. In the event that the values in these denormalized `product_*` columns within `inventory_items` contradict the corresponding attributes found in the `products` table, the `products` table is designated as the definitive and authoritative source. This policy ensures that the `products` table serves as the single source of truth for all product-specific information.

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

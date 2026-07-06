# E-Commerce Data Model Governance

Core entity tables and structural databases detailing user, transactional, and inventory relations.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/ecommerce-data-model-governance/distribution-centers-table | Distribution Centers Table | file | Houses details for warehouses and product sourcing fulfillment centers. |
| catalog/ecommerce-data-model-governance/inventory-items-table | Inventory Items Table | file | Tracks physical units of stock, wholesale cost metrics, and references to the catalog products. |
| catalog/ecommerce-data-model-governance/order-items-table | Order Items Table | file | The central fact table for financial revenue and metrics, tracking individual product units purchased within an order. |
| catalog/ecommerce-data-model-governance/orders-table | Orders Table | file | Represents checkout events mapping directly to a single unique order transaction containing one or more physical items. |
| catalog/ecommerce-data-model-governance/products-catalog-table | Products Catalog Table | file | Contains product details for each sellable SKU and links to its sourcing origin. |
| catalog/ecommerce-data-model-governance/users-table | Users Table | file | Represents customer accounts with attributes such as demographics, geographic location, acquisition channel, and creation timestamps. |

# Core Data Models

Foundational tables, entity grains, and relational foreign keys representing the enterprise eCommerce schema.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/core-data-models/distribution-centers-table | Distribution Centers Table | file | Tracks individual fulfillment warehouses and their locations at the warehouse grain. |
| catalog/core-data-models/inventory-items-table | Inventory Items Table | file | Represents the physical units of stock within the distribution warehouses at the stock unit grain. |
| catalog/core-data-models/order-items-table | Order Items Table | file | Tracks sold units at the order-line grain, serving as the central fact table for transactional revenue calculations. |
| catalog/core-data-models/orders-table | Orders Table | file | Represents checkout events at the order grain and links transactions back to unique customers. |
| catalog/core-data-models/products-table | Products Table | file | Tracks sellable stock-keeping units at the SKU level of granularity. |
| catalog/core-data-models/users-table | Users Table | file | Represents individual customers at the customer grain, holding demographic and geographical metadata. |

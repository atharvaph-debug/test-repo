# eCommerce Data Models

Core data models, schemas, and relational entities representing warehouse components.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/ecommerce-data-models/distribution-centers-table | Distribution Centers Table | file | Represents fulfillment warehouses at a warehouse grain. |
| catalog/ecommerce-data-models/inventory-items-table | Inventory Items Table | file | Represents specific physical units of stock at a stock unit grain. |
| catalog/ecommerce-data-models/order-items-table | Order Items Table | file | Central fact table tracking transactions at the order line/sold unit grain to calculate revenue, units sold, and margins. |
| catalog/ecommerce-data-models/orders-table | Orders Table | file | Represents checkout events at an order grain and relates back to the customer. |
| catalog/ecommerce-data-models/products-table | Products Table | file | Contains SKU-level details on sellable products and their associated retail prices, supplier costs, and warehouse origins. |
| catalog/ecommerce-data-models/users-table | Users Table | file | Represents customers at a customer grain containing demographic details, location, traffic source, and sign-up timestamps. |

# Data Model

The core tables that constitute the theLook eCommerce data schema.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/data-model/distribution-centers | Distribution Centers Table | file | A dimension table containing one row for each physical fulfillment warehouse. |
| catalog/data-model/inventory-items | Inventory Items Table | file | Tracks each physical unit of stock from its creation to its sale, with one row per unit. |
| catalog/data-model/order-items | Order Items Table | file | The central fact table containing one row per product unit in an order, connecting all major entities. |
| catalog/data-model/orders | Orders Table | file | Contains one row per order or checkout event, linking to the customer via user_id. |
| catalog/data-model/products | Products Table | file | The authoritative source for product attributes, with one row per sellable product SKU. |
| catalog/data-model/users | Users Table | file | Stores customer data, with one row per customer, including demographics, location, and acquisition channel. |

# Core Data Models

Essential database tables and entity grains constituting the database schema of theLook eCommerce.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/core-data-models/distribution-centers | Distribution Centers | file | Represents physical fulfillment warehouses including names and geographical coordinates. |
| catalog/core-data-models/inventory-items | Inventory Items | file | Table tracking physical stock units, receiving timestamps, purchase timestamps, and denormalized product attributes. |
| catalog/core-data-models/order-items | Order Items | file | The revenue grain table holding one row per unit of a product in an order, acting as the hub of the star schema. |
| catalog/core-data-models/orders | Orders | file | Represents a single checkout event linking customers to overall fulfillment status. |
| catalog/core-data-models/products | Products | file | The authoritative master catalog containing one row per sellable SKU, detailing attributes, taxonomy, and costs. |
| catalog/core-data-models/users | Users | file | Customer table housing demographics, geographical location, acquisition channel, and signup time. |

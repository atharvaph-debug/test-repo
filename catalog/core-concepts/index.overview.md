# Core Concepts

Fundamental business entities and terminologies used in theLook eCommerce operations.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/core-concepts/cost | Cost | file | The wholesale or landed cost paid by theLook for a product, stored in products.cost. |
| catalog/core-concepts/event-timestamps | Event Timestamps | file | A set of timestamps (created_at, shipped_at, etc.) that track key events in an order's lifecycle for cycle-time analysis. |
| catalog/core-concepts/order-item | Order Item | file | A single unit of a product within an order, which serves as the grain for revenue and sales calculations. |
| catalog/core-concepts/order-lifecycle | Order Lifecycle | file | The sequence of stages an order progresses through, typically from Processing to Shipped to Complete. |
| catalog/core-concepts/order-status | Order Status | file | Indicates the current state of an order item, such as Processing, Shipped, Complete, Returned, or Cancelled. |
| catalog/core-concepts/order | Order | file | Represents a single purchase event placed by a customer, which can contain multiple items. |
| catalog/core-concepts/product-taxonomy | Product Taxonomy | file | The three-level product hierarchy consisting of Department, Category, and Brand. |
| catalog/core-concepts/retail-price | Retail Price | file | The advertised catalog price for a product before any discounts, stored in products.retail_price. |
| catalog/core-concepts/sale-price | Sale Price | file | The actual price paid by a customer for an item, recorded in order_items.sale_price and used for revenue calculations. |
| catalog/core-concepts/stock-keeping-unit | Stock Keeping Unit | file | The unique identifier used to track a sellable product variant, corresponding to a row in the products table. |
| catalog/core-concepts/traffic-source | Traffic Source | file | The marketing channel that acquired a customer, such as Search, Organic, or Email. |

# Business Glossary and Taxonomy Standards Overview

This entry establishes unified definitions and pricing classifications to avoid data discrepancies across retail analytics systems. It provides standardized definitions, synonyms, and operational logic that translate systems metrics into business concepts, ensuring uniform terminology across different business teams.

## Key Standards and Definitions

### Order vs. Order Item Grain
This standard differentiates between an "Order" and an "Order Item" for consistent analytical reporting.
*   An **Order** represents a single purchase checkout event placed by a customer. It holds an overall status and is recorded with the number of items (`num_of_item`) and linked via `user_id`.
*   An **Order Item** represents a single unit of a product within a given order. For accurate calculation of revenue, margins, and units-sold, computations must be performed at the Order Item grain.

### The Price Hierarchy
This defines the different types of prices used across the business, clarifying their meaning and source:
*   **`Cost`**: This refers to the wholesale or landed cost paid to the supplier. It is typically found in `products.cost` or `inventory_items.cost` and is always hidden from customers.
*   **`Retail Price`**: This is the catalog or list price advertised to customers before any discounts are applied. It is usually found as `products.retail_price`.
*   **`Sale Price`**: This is the actual price paid by the customer after any promotions or markdowns. Recorded as `order_items.sale_price`, this figure is the definitive basis for calculating revenue.

### Product Taxonomy
Products are cataloged using a strict three-level hierarchical structure to ensure consistent classification:
1.  **`Department`**: The broadest classification (e.g., Men, Women).
2.  **`Category`**: Specifies the product type within a department (e.g., Jeans, Outerwear).
3.  **`Brand`**: Identifies the manufacturer label of the product.

### Marketing & Attribution
This standard defines how customer acquisition paths are tracked and utilized for channel-attribution analysis. The `traffic_source` field, located in the `users` table, records these acquisition paths. Values for `traffic_source` include Search, Organic, Email, Display, and Facebook. This field is foundational for understanding and analyzing customer acquisition channels.

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

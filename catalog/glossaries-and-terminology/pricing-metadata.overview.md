# Pricing Metadata Overview

Pricing Metadata refers to the distinctions between various price points associated with products and transactions, including the cost to the company, the advertised reference price, and the actual price paid by the customer. This metadata is crucial for understanding revenue, profitability, and operational costs.

## Key Pricing Fields

The business glossary defines the following key pricing metadata fields:

*   **Cost**: This represents the wholesale or landed cost that the company paid the supplier for a unit of a product. This value is never exposed to customers and can be found in `products.cost` and `inventory_items.cost`.
*   **Retail Price**: This is the catalog or reference list price at which a product is advertised before any discounts are applied. It is stored as `products.retail_price`.
*   **Sale Price**: This is the actual price paid by the customer for a product within a transaction. It is recorded on the transaction line as `order_items.sale_price` and serves as the authoritative figure for realized revenue. The Sale Price may differ from the Retail Price due to markdowns, promotions, or other discounts.

## Relationship to Transactional Grains

Pricing metadata, particularly the `Sale Price`, is closely tied to the `Order Item` transactional grain. An `Order Item` represents a single unit of a single product within an order and is the revenue grain where metrics such as revenue, margin, and units-sold are computed. For example, if a customer purchases two shirts and one hat, these constitute three separate `Order Item` records, each with its `sale_price`.

## Usage in Key Metrics

These pricing metadata fields are fundamental for calculating various financial and operational metrics:

*   **Gross Revenue**: Calculated as the sum of `order_items.sale_price` for orders that are not 'Cancelled'.
    $$\text{SUM}(\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
*   **Net Revenue**: Calculated as the sum of `order_items.sale_price` for items that are neither 'Cancelled' nor 'Returned'.
    $$\text{SUM}(\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Gross Margin**: Represents the profit made on sold items, calculated as the sum of `order_items.sale_price` minus `products.cost` for items not 'Cancelled' or 'Returned'. This calculation requires joining `order_items.product_id` to `products.id` to retrieve the associated cost.
    $$\text{SUM}(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
*   **Gross Margin %**: The percentage of revenue retained after subtracting the cost of goods sold, calculated as Gross Margin divided by Net Revenue.
    $$\frac{\text{Gross Margin}}{\text{Net Revenue}}$$

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

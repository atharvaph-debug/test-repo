# Financial Fields Taxonomy Overview

The Financial Fields Taxonomy defines the semantic distinctions among various monetary values associated with products and sales, specifically differentiating between wholesale/landed cost, advertised retail price, and the actual promotion-adjusted sale price. This entry serves as a glossary for key financial metadata, including aliases like `cost`, `retail-price`, and `sale-price`.

## Key Financial Fields

This taxonomy clarifies the purpose, value, and location of critical financial data points:

*   **Cost**: Represents the wholesale or landed cost paid by "theLook" to its supplier. This value is considered strictly internal and is never displayed to customers.
    *   **Location**: Found in `products.cost` and `inventory_items.cost`.
*   **Retail Price**: Denotes the advertised catalog list price of a product before any promotions or discounts are applied.
    *   **Location**: Defined in `products.retail_price`.
*   **Sale Price**: The definitive amount actually paid by a customer after all markdowns or promotions have been factored in. This is the authoritative figure used for calculating revenue.
    *   **Location**: Recorded on `order_items.sale_price`.

## Relationship to Revenue and Metrics

The `Sale Price` is fundamental as the authoritative revenue grain, meaning core performance metrics like revenue and margin must be computed at the `Order Item` level, which records this price.

For example, **Gross Margin**, which represents profit before operating costs, relies on both the `Sale Price` and the `Cost`. It is calculated by joining sales and product catalogs as follows:

$$\text{Gross Margin} = \sum(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

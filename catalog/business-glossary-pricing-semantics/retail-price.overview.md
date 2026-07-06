# Retail Price Overview

Retail Price represents the standard, non-discounted catalog price that is advertised to public customers for a product. This value is a foundational pricing component within the data landscape.

## Definition

The Retail Price is explicitly defined as the standard, non-discounted manufacturer price advertised to public customers. It serves as the baseline or list price before any potential discounts or promotions are applied.

## Location

In the data system, the Retail Price is located in `products.retail_price`.

## Relationship to Other Pricing Concepts

The Retail Price is distinct from other pricing metrics:
*   **Wholesale Cost (Cost)**: Unlike the Retail Price, which is customer-facing, the Wholesale Cost (recorded as `products.cost` and `inventory_items.cost`) is the landed cost paid to the supplier and is strictly restricted from customer views.
*   **Sale Price**: The Sale Price (captured dynamically in `order_items.sale_price`) is the final amount a customer actually pays for a unit. This transactional value can differ from the Retail Price due to active promotions or markdown strategies, making the Sale Price the single source of truth for transactional revenue.

## Source References
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

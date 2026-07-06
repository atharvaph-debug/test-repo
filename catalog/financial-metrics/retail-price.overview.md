# Retail Price Overview

Retail Price represents the advertised list or catalog price shown to customers prior to any discounts. It is the public-facing price for a product.

## Definition and Usage
The Retail Price is the price at which a product is initially offered to customers. It differs from the **Cost**, which is the wholesale or landed price paid to suppliers and is hidden from customers. It also differs from the **Sale Price**, which is the actual transaction price paid by the customer for an order item, reflecting any discounts applied.

## Data Location and Lineage
The authoritative source for the Retail Price is the `products` table, where it is found in the `products.retail_price` column.
For simplified inventory queries, product-level attributes, including the retail price, are denormalized and stored as `product_*` columns within the `inventory_items` table (e.g., `inventory_items.product_retail_price`). In cases where there is a disagreement between the `products` table and the `inventory_items` table, the `products` table is considered the source of truth for the Retail Price.

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

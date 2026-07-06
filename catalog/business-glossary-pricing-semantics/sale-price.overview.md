# Sale Price Overview

Sale Price represents the final amount a customer actually paid for an individual product unit. It serves as the single source of truth for transactional revenue, providing the definitive value for revenue calculations.

## Key Features

The Sale Price is the final amount the customer paid for a single unit and is dynamically captured in `order_items.sale_price` [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).

*   **Source of Truth**: This value is considered the single source of truth for transactional revenue [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).
*   **Relationship to Order Item**: The Sale Price applies to an *Order Item*, which is defined as the atomic revenue grain representing a single unit of a single product [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).
*   **Distinction from Retail Price**: The Sale Price may differ from the `Retail Price` (the standard, non-discounted catalog price found in `products.retail_price`) due to active promotions or markdown strategies [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).
*   **Distinction from Wholesale Cost**: The Sale Price is distinct from `Wholesale Cost`, which is the cost paid to the supplier and is recorded as `products.cost` and `inventory_items.cost` [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true).

## Source References

*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

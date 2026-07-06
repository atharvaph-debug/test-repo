# Order vs. Order Item Grains Overview

This entry distinguishes between a customer's overall purchase event and the individual product units comprising that purchase. Understanding this distinction is crucial for accurate financial reporting and performance metric calculation.

## Key Definitions

*   **Order**: An **Order** represents a single purchase event initiated by a customer, identified by their `user_id`. Each order carries an overall fulfillment status and records the total number of items purchased through `num_of_item` [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)].
*   **Order Item**: An **Order Item** represents a single unit of a product included within an order. This is considered the authoritative revenue grain. Core performance metrics, such as revenue, margin, and units sold, must be computed at this granular level [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)].

## Key Attributes

The distinction between these grains is particularly relevant for financial calculations:

*   **Order Attributes**:
    *   `user_id`: Identifies the customer who placed the order.
    *   `num_of_item`: Represents the total count of items within the order.
    *   `fulfillment status`: Indicates the current status of the order's fulfillment process.
*   **Order Item Attributes**:
    *   `order_items.sale_price`: This column records the actual amount paid by the customer for that specific product unit after any markdowns or promotions. It serves as the authoritative figure for revenue calculation [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)].

## Source References

*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

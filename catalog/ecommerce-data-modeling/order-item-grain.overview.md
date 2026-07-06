# Order Item Grain Overview

The Order Item Grain represents a single unit of a product that has been sold, serving as the fundamental revenue grain in eCommerce data modeling. It is mapped at one row per product unit, making it the essential level for computing sales, margins, and unit metrics. This data modeling standard is crucial for distinguishing between a high-level order and its constituent items.

## Key Concepts

*   **Definition:** An **Order Item** represents a single unit of a product that has been sold. This is the most granular level for product sales.
*   **Revenue Grain:** It is identified as the fundamental revenue grain where key performance indicators such as sales, margins, and units-sold must be accurately computed.
*   **Granularity:** Each record in the Order Item Grain typically corresponds to one product unit, ensuring precise measurement of individual units.
*   **Distinction from Order:** It is a critical data-modeling standard to distinguish between an Order and an Order Item. An **Order** signifies a single checkout or purchase event that can contain multiple items, tracked via `num_of_item` and linked through a `user_id`. In contrast, an Order Item focuses on individual sold units within that order.
*   **Aliases:** This concept is also referred to as "order-vs-order-item-grains" and "order-items-table".

## Source References

*   [theLook eCommerce — Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [theLook eCommerce — Data Model](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

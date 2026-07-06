# theLook eCommerce Platform Overview

The theLook eCommerce Platform is identified as a multi-brand online apparel and accessories retail platform, representing the master data set for the business.

## Key Concepts

*   **Order vs. Order Item Grains:** A critical data-modeling standard for this platform distinguishes between an "Order" and an "Order Item." An **Order** represents a single checkout or purchase event that can contain multiple items. Orders are tracked using `num_of_item` for the quantity of items and linked via `user_id`. An **Order Item**, on the other hand, signifies a single unit of a product (the sold unit). This "Order Item" grain serves as the fundamental revenue grain, crucial for computing metrics such as sales, margins, and units-sold.
*   **Logistics Terminology:** Within the logistics network of the theLook eCommerce Platform, the terms "Distribution Center" (DC), "fulfillment centers," and "fulfillment nodes" are used interchangeably. These terms all describe facilities responsible for receiving inventory in bulk, storing it, and subsequently fulfilling downstream orders.

## Source References
*   [theLook eCommerce — Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true)

# Reorder Point Overview

The Reorder Point (ROP), also known as Reorder Level, is an automated stock inventory level that triggers a purchase requisition to replenish product supplies. It is a critical metric in inventory management, designed to ensure that stock is replenished before it runs out, balancing supply against demand and lead times. "ROP" and "Reorder Point" are the preferred system fields and terms, while "Reorder Level" is considered legacy or informal jargon.

## Key Concepts and Calculation

The Reorder Point is calculated using a formula that incorporates safety stock and demand during the lead time.

The general formula is:
$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand-over-Lead-Time}$$

More specifically, the formula for Reorder Point (ROP) is detailed as:
$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

### Components of Reorder Point Calculation:

*   **Safety Stock:** This represents the extra buffer inventory held to protect customer service levels from demand spikes and supply chain delays. It acts as the base of the reorder formula, meaning adjusting safety stock targets automatically shifts the Reorder Point. Safety Stock is synonymous with "Buffer Stock". Current targets for safety stock quantities are dictated by velocity category:
    *   **Class A (Fast Movers):** Typically 14 days of supply, but was increased to 21 days of supply following Q3 stockouts for Class-A apparel SKUs at forward distribution centers to match heightened demand variability.
    *   **Class B:** 10 days of supply.
    *   **Class C:** 7 days of supply.
*   **Lead Time:** This is the elapsed time between placing a purchase order and receiving and inspecting the goods for picking. Variances in lead time dictate buffer inventory needs. Lead Time can be categorized as:
    *   **Inbound Lead Time:** Elapsed time from supplier purchase order to regional Distribution Center (DC) arrival.
    *   **Inter-node Lead Time:** Internal transit duration between regional and forward distribution nodes.
*   **Average Daily Demand / Demand-over-Lead-Time:** This represents the expected demand for a product during the lead time required to replenish it.

## Operational Impact

When a Stock Keeping Unit (SKU)'s on-hand inventory matches its defined Reorder Point, the planning system automatically generates a purchase requisition. For manufactured items, this requisition is then "exploded" using the product's Bill of Materials (BOM) to derive precise component requirements and quantities needed for production. The BOM serves as the absolute single source of truth for a product's composition.

## Source References

*   [Copy of Demand Planning Meeting Notes.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B89329718-94BF-4824-8F88-5B2A5E1FC0B8%7D&file=Copy%20of%20Demand%20Planning%20Meeting%20Notes.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Policy Memo.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Policy%20Memo.docx&action=default&mobileredirect=true)
*   [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true)
*   [Copy of Procurement SOP.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B3070B2AC-B110-4099-98F4-E74954ED7817%7D&file=Copy%20of%20Procurement%20SOP.docx&action=default&mobileredirect=true)
*   [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)

# Safety Stock Overview

Safety Stock, also known as Buffer Stock, refers to the extra inventory buffer held above baseline demand. Its primary purpose is to prevent stockouts from unexpected demand surges and supply delays, thereby protecting customer service levels and overall operations.

## Definition and Purpose

Safety Stock is an inventory cushion designed to shield operations from unpredictable events such as demand spikes and supply chain delays, including late inbound supplier deliveries. It acts as a protective layer within the supply chain, ensuring continuity even when forecasts are not perfectly met or lead times vary. Variances in lead time, which is the elapsed time between placing a purchase order and receiving/inspecting goods, directly influence the buffer inventory needs.

## Role in Replenishment and Policy

Safety Stock is a critical component in inventory replenishment strategies, particularly in the calculation of the Reorder Point (ROP). The Reorder Point is the target stock level that triggers new replenishment orders.

The formula for Reorder Point (ROP) is:

$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand-over-Lead-Time}$$

Alternatively, it can be expressed as:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

Because safety stock forms the base of the reorder formula, any adjustment to safety stock targets automatically shifts the Reorder Point without requiring direct modification of the reorder threshold parameter.

The **Safety Stock Policy** dictates the specific quantities of extra buffer inventory to be held. Current targets often classify safety stock quantities by velocity category:

*   **Class A (Fast Movers):** 14 days of supply.
*   **Class B:** 10 days of supply.
*   **Class C:** 7 days of supply.

## Adjustments and Impact

Safety stock parameters can be adjusted based on performance and market conditions. For instance, following an investigation into Q3 stockouts of Class-A apparel SKUs at forward distribution centers, safety stock parameters were increased from 14 days of supply to 21 days of supply. This change was implemented to match heightened demand variability and automatically recalibrates reorder points via standard planning formulas.

## Source References

*   [Copy of Demand Planning Meeting Notes.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B89329718-94BF-4824-8F88-5B2A5E1FC0B8%7D&file=Copy%20of%20Demand%20Planning%20Meeting%20Notes.docx&action=default&mobileredirect=true)
*   [Inventory Management Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true)
*   [Inventory Policy Memo](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Policy%20Memo.docx&action=default&mobileredirect=true)
*   [Copy of Procurement SOP.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B3070B2AC-B110-4099-98F4-E74954ED7817%7D&file=Copy%20of%20Procurement%20SOP.docx&action=default&mobileredirect=true)
*   [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)

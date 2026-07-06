# Safety Stock Overview

Safety Stock refers to the inventory cushion maintained above forecast levels to absorb unexpected demand spikes, demand variability, and late inbound shipments. This critical buffer is calibrated dynamically to ensure continuous supply and prevent stockouts.

## Purpose and Definition

Safety Stock serves as an inventory cushion to mitigate the impact of unforeseen events such as fluctuations in market demand and delays in lead times for replenishment. It is held in addition to the regular forecast inventory to ensure that customer orders can still be fulfilled even when actual demand exceeds forecasts or supply chain disruptions occur.

## Calibration and Calculation

Safety Stock is not a static value but is sized dynamically. Its calibration is primarily based on "days of supply" and is influenced by SKU velocity classifications:

*   **Velocity Class Safety Stock Thresholds**:
    *   **Class A (Fast Movers)**: 14 days of supply
    *   **Class B**: 10 days of supply
    *   **Class C**: 7 days of supply

This dynamic sizing ensures that inventory levels are appropriate for the sales velocity of each SKU.

Safety Stock is also a key component in the **Reorder Point (ROP) calculation**, which determines when new inventory should be ordered. The formula for ROP is:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

The planning system is designed to automatically calculate ROP, rather than relying on manual input.

## Importance and Risk

Proper calibration of Safety Stock is crucial for supply chain resilience. It is designed to cover the gap between a reorder point trigger and the arrival of physical replenishment. If historical parameters for Safety Stock become outdated or "stale" due to shifts in market demand variability, the safety stock can become undersized, leading to stockouts. For example, Q3 stockouts in apparel SKUs were attributed to Safety Stock guidelines, previously set at 14 days, failing to cover rising demand variability.

## Aliases

This concept is also referred to as "safety-stock-calibration" or "days-of-supply."

## Source References

*   [Copy of Demand Planning Meeting Notes.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B89329718-94BF-4824-8F88-5B2A5E1FC0B8%7D&file=Copy%20of%20Demand%20Planning%20Meeting%20Notes.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Policy Memo.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Memo.docx&action=default&mobileredirect=true)
*   [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)

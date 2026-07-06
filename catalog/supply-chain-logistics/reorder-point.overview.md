# Reorder Point Overview

The Reorder Point (ROP) is an automated system trigger for replenishment within an ERP system, calculated mathematically. It serves to initiate the process of ordering new stock when inventory levels drop to a predetermined point, preventing stockouts while optimizing inventory holding costs. The ROP is never set manually; instead, any sustained shift in monitored lead times or safety stock parameters automatically recalculates and shifts the ROP within the ERP.

## Definition and Calculation

The Reorder Point is calculated using the following formula:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

This calculation directly incorporates three critical supply chain parameters: Average Daily Demand, Lead Time in Days, and Safety Stock.

## Key Components

### Lead Time
Lead Time is defined as the total elapsed time from the placement of a purchase order (PO) to the moment goods are received, inspected, and posted as available to pick in the system (not merely physical dock arrival). It encompasses:
*   **Inbound Lead Time:** The time from a supplier PO to regional distribution center (DC) receipt, managed by procurement.
*   **Inter-Node Lead Time:** The transit time required to move stock between a Regional DC (which holds broad inventory) and a Forward DC/fulfillment node (located closer to customer demand).

### Safety Stock
Safety stock, also known as buffer stock, represents extra inventory held to mitigate risks such as unexpected demand spikes or variability in lead times. Its parameters are crucial to the ROP calculation.
*   **Velocity Class Policy:** Safety stock is typically sized in days of supply based on velocity classes:
    *   **Class A:** Fast-moving items, with a standard policy of 14 days of supply.
    *   **Class B:** 10 days of supply.
    *   **Class C:** 7 days of supply.
*   **Dynamic Policy Updates:** Safety stock parameters can be dynamically updated. For instance, following Q3 Class-A apparel stockouts caused by rising demand variability, Class-A safety stock parameters were raised to 21 days of supply. Such adjustments automatically influence the ROP.

## Relationship with Inventory Policy

The ROP acts as a direct reflection of underlying inventory policies related to demand, lead times, and safety stock. Raising safety stock parameters, for example, automatically increases the reorder point. For instance, increasing Class-A safety stock to 21 days automatically lifted the ROP for those SKUs. A case study involving Q3 apparel stockouts highlighted that the remedy for near-miss incidents was to recalibrate the safety stock formula against current demand variability rather than directly adjusting reorder points.

## Source References
*   [Copy of Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg)
*   [Copy of Procurement SOP](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)
*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

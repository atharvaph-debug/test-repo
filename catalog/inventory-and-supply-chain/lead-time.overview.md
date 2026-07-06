# Lead Time Overview

Lead Time is a dynamic metadata point that represents the full elapsed duration from the placement of a purchase order (PO) with a supplier to the moment goods are received, inspected, put away, and posted as available to pick. It is not merely the time until goods arrive at the dock but encompasses the entire process until they are available for use or fulfillment. This dynamic property is critical for dictating safety stock and buffer requirements across different network nodes.

## Definition and Dynamics

Lead time is considered a dynamic metadata point rather than a static property, which impacts how inventory levels are managed. Its definition explicitly includes:
*   **PO placement**: The starting point of the measurement.
*   **Goods received**: The physical arrival.
*   **Inspected, put away, and posted as available to pick**: The final stage when inventory is truly ready for use.

## Types of Lead Time

Within a structured physical logistics network, two distinct types of lead time are tracked:
*   **Inbound Lead Time**: The transit time from a supplier PO until receipt at a Regional Distribution Center (DC). Regional DCs typically hold broad assortments.
*   **Inter-node Lead Time**: The transit time required to move stock from a Regional DC to a Forward DC. Forward DCs are fulfillment nodes strategically located closer to demand.

## Verification and Drift

Lead times are subject to verification and drift:
*   **Verification**: When onboarding new suppliers, their quoted lead times are validated against the actual performance observed during trial orders. This validated performance then becomes the baseline for planning.
*   **Drift**: Lead times are not constant; they can drift due to changes in supplier capacities. It is essential to update lead times dynamically rather than relying solely on historical averages to maintain accuracy in planning.

## Role in Inventory Management

Lead Time is a fundamental input in critical inventory management calculations:
*   **Reorder Point (ROP)**: Lead Time is a key variable in the Reorder Point formula, which determines the inventory level at which a new purchase order is automatically triggered. The formula is:
    $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    Because of this mathematical relationship, the ROP is not set manually; any change made to the Lead Time metadata, or to Safety Stock metadata, automatically adjusts the ROP.
*   **Safety Stock (Buffer Stock)**: While Lead Time is an input to ROP, Safety Stock (extra inventory held to protect service levels) is directly impacted by Lead Time variability. Recent inventory instability, particularly for apparel Class-A SKUs, has been attributed to safety stock levels sized against outdated demand variability rather than changes in supplier lead times. Safety stock is sized in "days of supply" and segmented by the item's velocity class (e.g., Class A, B, C).

## Source References
*   [Copy of Procurement SOP](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt5Fg)
*   [Copy of Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)
*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

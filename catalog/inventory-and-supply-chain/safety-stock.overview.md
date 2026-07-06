# Safety Stock Overview

Safety Stock, also known as `buffer-stock` or `safety-stock-targets`, represents the extra inventory held to protect service levels against demand spikes and lead-time variability. It functions as a dynamic metadata point crucial for inventory management, dictating buffer requirements across different network nodes.

## Key Characteristics and Policies

Safety Stock is sized in "days of supply" and segmented by the velocity class of the item. Standard policies for safety stock targets are tiered based on these classifications:

*   **Class A (Fast Movers):**
    *   Standardized at 14 days of supply.
    *   *Note:* Following a Q3 stockout analysis of apparel Class-A SKUs due to rising demand variability, this parameter was adjusted to 21 days of supply, superseding the default standing memo.
*   **Class B:** Standardized at 10 days of supply.
*   **Class C:** Standardized at 7 days of supply.

Safety Stock is considered a dynamic metadata point because changes to it or related factors like lead time automatically adjust other critical inventory metrics.

## Relationship with Reorder Point (ROP)

Safety Stock is an integral component of the Reorder Point (ROP) formula. ROP is the system-calculated inventory level that automatically triggers a purchase order (PO) and is modeled as:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

Because of this direct mathematical relationship, ROP is never set manually; any change to lead time or safety stock metadata automatically adjusts the ROP. Safety stock serves as the inventory cushion held above the average forecast to absorb demand spikes and late inbound deliveries, and bumping the safety stock automatically raises the reorder point.

## Inventory Stability and Drivers

The sizing of safety stock is critical for maintaining inventory stability. Reviews have shown that inventory instability, such as near-misses where inventory dipped close to zero, can be caused by safety stock levels sized against outdated demand variability rather than accurately reflecting changes in supplier lead times.

## Source References

*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

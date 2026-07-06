# Reorder Point Overview

The Reorder Point (ROP) is a system-calculated inventory level that automatically triggers replenishment purchase orders (PO). It is a critical component of inventory management, ensuring that stock levels are maintained to meet demand without requiring manual intervention for reordering.

## Key Features

*   **Automated Trigger:** The ROP serves as an automated threshold; when inventory levels fall to or below the Reorder Point, a new purchase order is automatically generated to replenish stock.
*   **System-Calculated:** ROP is not set manually. Instead, it is dynamically calculated based on other core inventory metadata, specifically Average Daily Demand, Lead Time in Days, and Safety Stock. Any changes to these underlying metadata points automatically adjust the ROP.
*   **Formulaic Definition:** The Reorder Point is modeled by the following formula:
    $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    This formula highlights its direct dependency on lead time and safety stock metadata.

## Metadata Dependencies and Relationships

The Reorder Point is a derived metric, heavily reliant on other critical metadata points:

*   **Lead Time:** Defined as a dynamic metadata point, lead time dictates the buffer requirements and is a direct input into the ROP calculation.
*   **Safety Stock (Buffer Stock):** This is extra inventory held to protect service levels against demand spikes and lead-time variability. Safety stock is sized in "days of supply" and segmented by the velocity class of the item. An increase in safety stock will automatically raise the reorder point.
    *   **Velocity Classification Policies for Safety Stock:** Under standard policy, safety stock targets are tiered based on item velocity:
        *   **Class A (Fast Movers):** Standardized at 14 days of supply. *Note: Following a Q3 stockout analysis of apparel Class-A SKUs, this parameter was adjusted to 21 days of supply due to rising demand variability.*
        *   **Class B:** Standardized at 10 days of supply.
        *   **Class C:** Standardized at 7 days of supply.

The mathematical relationship means that changes to input metadata, such as Lead Time or Safety Stock, directly enrich and update the Reorder Point, making it a dynamic rather than static value.

## Source References

*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)

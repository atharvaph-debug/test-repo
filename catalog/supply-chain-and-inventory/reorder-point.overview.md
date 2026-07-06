# Reorder Point Overview

The Reorder Point (ROP), also known by its alias `rop`, represents the calculated inventory level that automatically triggers a purchase order. It is a critical metadata element within supply chain planning, driving replenishment decisions based on daily demand, lead times, and safety stock.

## Key Characteristics and Role

The Reorder Point is defined as the ERP-labeled on-hand inventory level that automatically initiates a purchase order to replenish stock. It is not set manually but is calculated by the planning system, emphasizing its role as a dynamic metadata element derived from other inventory parameters. This calculated value is essential for ensuring timely replenishment and maintaining optimal inventory levels.

## Calculation

The Reorder Point is mathematically determined by the following formula:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

Alternatively, it can be conceptualized as:

$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand-Over-Lead-Time}$$

Any change to the underlying metadata elements—namely, safety stock or lead times—automatically updates the Reorder Point without requiring direct modifications to the reorder trigger itself.

## Dependencies and Related Metadata

The Reorder Point's calculation is directly dependent on and reflects changes in other crucial supply chain metadata:

### Lead Time Parameters
Lead Time is defined as the total duration from the placement of a purchase order until goods are received, inspected, and posted as available to pick. This includes the entire process, not just dock arrival. Planning systems use actual trial lead times, including observed variability, rather than optimistic supplier quotes. Buyers must monitor for "Lead Time Drift," using current quoted lead times and flagging sustained increases, as these directly impact safety stock and Reorder Points.

### Safety Stock Policy
Safety Stock is the extra buffer inventory (also known as "buffer stock" or inventory cushion) held to protect against demand spikes or lead-time variability. Its value is a metadata element sized according to standing policy based on SKU velocity class:
*   **Class A (Fast Movers):** The standing policy is 21 days of supply, updated from an earlier 14-day policy following a postmortem on Q3 stockouts.
*   **Class B:** 10 days of supply.
*   **Class C:** 7 days of supply.

Adjusting the safety stock value automatically scales the Reorder Point.

## Source References
*   [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)
*   [Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt5Fg)
*   [Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)

# Safety Stock Overview

Safety Stock, also known as buffer stock, represents the extra inventory held to protect against demand variability and lead-time fluctuations. Defined within system metadata, it plays a crucial role in replenishment decisions and is a key component in calculating reorder points.

## Definition and Role

Safety Stock is an inventory cushion maintained above standard forecasts to absorb demand spikes or lead-time variability. It safeguards against late inbound deliveries and unexpected increases in demand ([Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU); [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)). Alongside lead times and reorder points, safety stock is a fundamental parameter defined within system metadata that drives replenishment decisions ([Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)).

## Policy and Calculation

The company's standing policy sizes safety stock based on SKU velocity class, typically expressed as days of supply:

*   **Class A (Fast Movers):** The policy was initially set at 14 days of supply ([Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)). Following a postmortem analysis of Q3 stockouts caused by rising apparel demand variability, this was updated to **21 days of supply** ([Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)). An investigation revealed that Q3 Class-A Apparel SKUs' safety stock targets were based on outdated historical demand variability, emphasizing the need for updated demand variability modeling ([Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)).
*   **Class B:** 10 days of supply ([Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)).
*   **Class C:** 7 days of supply ([Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)).

## Relationship with Reorder Point (ROP)

Safety Stock is a critical input to the Reorder Point (ROP) calculation, which is the inventory level that automatically triggers a purchase order ([Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)). The ROP is calculated by the planning system and is never set manually. The formula for ROP is:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

This can also be expressed as:

$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand-Over-Lead-Time}$$

A key metadata interaction is that any change to the safety stock value, or to lead times, automatically updates the Reorder Point without requiring direct modifications to the reorder trigger itself ([Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY); [Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU); [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)). This highlights the importance of maintaining accurate and current safety stock metadata for effective inventory management.

## Source References
* [Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg)
* [Procurement Standard Operating Procedure](1IXn1QX1n7lJ7kn6yGnQi8At_hhbBKsHuPGbs5SFUUI0)
* [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
* [Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
* [Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
* [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

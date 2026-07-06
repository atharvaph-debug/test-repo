# Stock Keeping Unit (SKU) Overview

A Stock Keeping Unit (SKU) is an internal identifier that serves as the central hub linking engineering, planning, procurement, and warehouse operations within an organization. It forms the foundation of the inventory system's metadata architecture, representing a distinct, sellable configuration of a product, often characterized by specific size, color, or pack details.

## Key Characteristics and Distinctions

While merchandising may launch "products," engineering and planning primarily interact with SKUs. The SKU is an internal identifier that never leaves company systems. Demand is forecast, stock is held, and replenishment occurs at the SKU level ([Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4); [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)).

The SKU is distinct from external identifiers such as UPC/GTINs (Universal Product Codes/Global Trade Item Numbers). UPCs/GTINs are external barcode standards from a global registry used for retail scanning, stored as an attribute mapped to a SKU. It is critical not to treat SKUs and UPCs/GTINs as interchangeable to avoid double-counting errors, as a single product line can have one UPC but map to several internal SKUs over its lifecycle ([Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4); [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)).

## Associated Metadata

SKUs are central to various metadata structures and operational parameters:

### Bill of Materials (BOM)
For finished-good SKUs, the Bill of Materials (BOM) is an authoritative, engineering-controlled specification that translates the SKU into its component parts for downstream procurement. BOMs are multi-level hierarchical trees, where a finished-good SKU is composed of sub-assemblies, which themselves reference their own BOMs down to purchased raw components. This structure allows sub-assemblies to be defined once and reused across multiple products ([Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4); [Bill of Materials — Engineering Specification](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)).

When demand is planned for a finished SKU, the planning system "explodes" the SKU through its hierarchical BOM to derive component procurement quantities. Total component procurement quantity is calculated by multiplying parent SKU demand by the per-unit quantities of every component at each level of the tree ([Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4); [Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)). To preserve data integrity, a finished-good SKU has exactly one active, versioned BOM revision at a time, and manual editing of component quantities on purchase orders without an Engineering-released BOM revision is prohibited ([Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0); [Bill of Materials — Engineering Specification](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)).

### Lead Time Parameters
Lead time for an SKU is defined as the total duration from Purchase Order (PO) placement to when goods are received, inspected, and posted as available to pick. Planning systems use actual trial lead times, including observed variability, rather than optimistic supplier quotes, to ensure accurate replenishment dates. Sustained lead-time increases directly impact safety stock and reorder points for the SKU and must be flagged to planning ([Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg); [Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0); [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)).

### Safety Stock Policy
Safety stock, or "buffer stock," is extra inventory carried to absorb demand spikes or lead-time variability for an SKU ([Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)). Standing policy sizes safety stock by SKU velocity class:
*   **Class A (Fast Movers):** 21 days of supply (updated from 14 days following Q3 stockouts) ([Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU); [Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)).
*   **Class B:** 10 days of supply ([Inventory Policy Memo](132WG298COjjbV1PJMJ01cnXFeQfTSdF30a1tlf9YjhU)).
*   **Class C:** 7 days of supply ([Inventory Policy Memo](132WG298COjjbV1PJMJ01cnXFeQfTSdF30a1tlf9YjhU)).

### Reorder Point (ROP) Formula
The Reorder Point (ROP) is the ERP-labeled on-hand level that automatically triggers a purchase order for an SKU ([Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)). The ROP is never set manually but is calculated by the planning system using the formula:
$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
Any metadata change to an SKU's safety stock or lead times automatically updates its ROP ([Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY); [Inventory Policy Memo](132WG298COjjbV1PJMJ01cnXFeQfTSdF30a1tlf9YjhU)).

### Logistics Network Integration
In a two-tier network architecture, SKUs are managed across Regional DCs (holding broad assortment and replenishing downstream nodes) and Forward DCs (fulfillment nodes located close to demand). Every DC holds, counts, and replenishment-plans its inventory independently at the SKU level, meaning a single SKU can have vastly different on-hand counts across different nodes ([Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc); [Warehouse Operations Runbook](1tcp-BhUCYXWiKrsrTBRST5Umu6_13ib7m_viXBggsYk)). Buffer inventory calculations at forward nodes must account for a combined "Lead Time Stack" including inbound lead time from supplier to Regional DC and inter-node lead time from Regional DC to Forward DC ([Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)).

Order routing metadata relies on SKU availability. When demand occurs, the order router evaluates active DC nodes, preferring the node holding the required SKU with the shortest fulfillment lead time, and falling back to alternative nodes if the primary is out of stock ([Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc); [Warehouse Operations Runbook](1tcp-BhUCYXWiKrsrTBRST5Umu6_13ib7m_viXBggsYk)).

## Inventory Anomaly Context
An analysis of Q3 performance highlighted that safety stock targets for Class-A Apparel SKUs were based on outdated historical demand variability, leading to near-miss stockouts. This confirmed that the issues were demand-side, necessitating updated demand variability modeling for these SKUs ([Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)).

## Source References
*   [Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4)
*   [Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Bill of Materials — Engineering Specification](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)
*   [Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)
*   [Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg)
*   [Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Postmortem: Q3 Apparel Class-A Stockouts](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)
*   [Warehouse Operations Runbook](1tcp-BhUCYXWiKrsrTBRST5Umu6_13ib7m_viXBggsYk)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

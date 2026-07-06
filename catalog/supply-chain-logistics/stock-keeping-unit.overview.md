# Stock Keeping Unit (SKU) Overview

The Stock Keeping Unit (SKU) is the central internal identifier for a distinct, sellable product variant, precisely representing its specific size, color, and pack configuration. It serves as the foundational element around which all internal inventory, forecasting, stock-holding, and replenishment processes revolve. While merchandising may launch a "product," engineering and planning strictly track and manage it as a set of individual SKUs.

## Key Characteristics and Distinctions

*   **Internal Identifier**: Unlike Universal Product Codes (UPC) or Global Trade Item Numbers (GTINs), which are external barcode standards assigned from a global registry for retail scanning, the SKU is an identifier used exclusively within a company's systems.
*   **Variant Specificity**: The SKU uniquely identifies a specific variant of a product, ensuring precise tracking for inventory movements. For instance, every warehouse putaway must be scanned to the exact SKU, not just the product family, to prevent downstream pick failures.
*   **System Mapping**: While a UPC/GTIN is stored as an attribute pointing to an SKU, it's critical to note that a single product can map to several SKUs over its lifecycle. Treating them as identical can lead to double-counting errors in inventory.

## Relationship with Bill of Materials (BOM)

The SKU is intrinsically linked to the Bill of Materials (BOM), particularly for manufactured goods.
*   **Finished-Good BOM**: The BOM provides an engineering-controlled, structured definition of all components and sub-assemblies, along with their quantities, required to build one unit of a finished-good SKU.
*   **Hierarchical Structure**: BOMs are multi-level and hierarchical. A sub-assembly defined within one BOM can itself have its own BOM, enabling the reuse of sub-assemblies across various finished products.
*   **Procurement and Planning**: Planning systems forecast demand at the finished-good SKU level. To calculate component demand, these systems "explode" the SKU through its BOM hierarchy, multiplying parent demand by per-unit quantities at all levels. The BOM is considered the absolute single source of truth; buyers and planners are prohibited from manually editing component quantities on a Purchase Order (PO) without verifying against the BOM.

## Inventory Management and Planning

SKUs are fundamental to advanced inventory management and planning parameters:

*   **Lead Time Calculations**: Although not an attribute of the SKU itself, lead time is a critical metric tracked *for* SKUs. It represents the total elapsed time from Purchase Order (PO) placement until goods are received, inspected, and posted as available to pick. This includes:
    *   **Inbound Lead Time**: From supplier PO to regional distribution center (DC) receipt, managed by procurement.
    *   **Inter-Node Lead Time**: Transit time between a regional DC (broad inventory) and a forward DC/fulfillment node (close to demand).
*   **Safety Stock**: This is the extra inventory held for an SKU to absorb demand spikes or lead-time variability. Safety stock is typically sized in days of supply based on SKU velocity classes:
    *   **Class A**: Fast movers, initially 14 days of supply, later raised to 21 days due to increased demand variability.
    *   **Class B**: 10 days of supply.
    *   **Class C**: 7 days of supply.
    Dynamic policy updates, such as the increase for Class-A apparel SKUs following Q3 stockouts, directly impact safety stock levels. Failures can result from safety stock levels being sized to outdated demand variability figures.
*   **Reorder Point (ROP)**: The ROP is the automated system trigger for replenishment, calculated using the formula:

    $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

    The ROP is never set manually; any sustained shift in monitored lead times or safety stock parameters automatically recalculates and adjusts the ROP within the ERP system. Raising Class-A safety stock to 21 days, for example, automatically lifted the ROP for those SKUs.

## Source References
*   [Copy of Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of Warehouse Ops Runbook](1tcp-BhUCYXWiKrsrTBRST5Umu6_13ib7m_viXBggsYk)
*   [Copy of Procurement SOP](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)
*   [Copy of BOM Spec](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)
*   [Copy of Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg)
*   [Copy of Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)
*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

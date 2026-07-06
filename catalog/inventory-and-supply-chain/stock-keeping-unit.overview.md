# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU) is the core internal identifier for a distinct, sellable product variant. It encompasses specific attributes like size, color, and pack configuration, serving as a central hub around which all inventory systems revolve. SKUs are the fundamental level at which demand is forecast, stock is held, and replenishment decisions are made.

## Key Metadata Relationships

The SKU is heavily enriched by and linked to various metadata across inventory, procurement, and planning systems, crucial for accurate management and operational decisions.

### Product Identification & Structure
*   **Distinct Variant Definition:** An SKU uniquely identifies a product variant by specific attributes such as its size, color, and pack configuration.
*   **External Identifiers:** While internal, SKUs are mapped to external barcode standards like UPC/GTIN. These external identifiers are stored as attributes of the SKU but are not interchangeable with it.
*   **Bill of Materials (BOM):** SKUs are linked to their component parts and sub-assemblies via the Bill of Materials. For finished goods, a BOM defines the "recipe" and allows planning systems to "explode" parent SKUs to derive component demand.

### Inventory Management Parameters
*   **Reorder Point (ROP):** The system-calculated inventory level that automatically triggers a purchase order for a SKU. The ROP is never set manually and is determined by the formula: $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$. Changes to associated metadata like lead time or safety stock automatically adjust the ROP.
*   **Safety Stock (Buffer Stock):** Extra inventory held per SKU to protect service levels against demand spikes and lead-time variability. It is sized in "days of supply" and segmented by the velocity class of the item.
*   **Velocity Classification Policies:** Safety stock targets for SKUs are tiered based on their velocity class:
    *   **Class A (Fast Movers):** Standardized at 14 days of supply, though this was adjusted to 21 days of supply for apparel Class-A SKUs following a Q3 stockout analysis.
    *   **Class B:** Standardized at 10 days of supply.
    *   **Class C:** Standardized at 7 days of supply.
*   **Node-Independent Inventory:** SKUs have inventory managed independently at each holding node (e.g., distribution centers). On-hand quantities can vary significantly across locations, and replenishment decisions are calculated individually for each SKU at each node.

### Procurement & Supplier Management
*   **Supplier Scorecards (Vendor Ratings):** When a SKU requires replenishment, buyers consult supplier scorecards, which combine On-Time Delivery %, Quality, and Price Competitiveness. Higher-rated suppliers receive a larger share of order volume for the SKU. New suppliers are restricted from production orders until an initial provisional scorecard is established.

### Data Cleanliness & Accuracy
*   **Metadata Cleanliness at Putaway:** During inbound operations, items must be scanned directly to the specific SKU (not a generic product family) to prevent picking failures. Continuous cycle counts reconcile discrepancies at the SKU + location level, ensuring accurate on-hand inventory data for the planning system.

## Source References
*   [Copy of Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4)
*   [Copy of Inventory Management Glossary](1VR5cX-s-EA9fwFyVH9BVPmlLB59qd-UtL0LRZGfNBNU)
*   [Copy of BOM Spec](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)
*   [Copy of Supplier Onboarding Guide](1Obu3LNs7aVPvtEEuKbgiD7b553zn-LOE5xe3KuWt6Fg)
*   [Copy of Procurement SOP](1IXn1QX1m7lJ7kn6yGnQi8At_hhbBKsHuPGbs5SFUUI0)
*   [Copy of Inventory Policy Memo](132WG298COjjbV1PqmJ01cnXFeQfTSdF30a1tlf9YjhU)
*   [Copy of Q3 Stockout Postmortem](1LGv8kJwGMxFmrObzlWWabfavoaapl24zaFbXiQXU_aY)
*   [Copy of Logistics Network Overview](1FFaghxSz7YKUakJzBsGu_u_C1ZeNPXBG38apWoU0Xdc)
*   [Copy of Warehouse Ops Runbook](1tcp-BhUCYXWiKrsrTBRST5Umu6_13ib7m_viXBggsYk)
*   [Copy of Demand Planning Meeting Notes](1jI6HhNVjOkkpuUYDDZ3xhpUlgzqtjg1lTaBQt9OeImQ)

# Stock Keeping Unit Tracking Overview

Stock Keeping Unit (SKU) Tracking refers to the management of internal identifiers and their mapping to external barcode standards, which are crucial for running inventory, cycle counts, and logistics routing. This entry describes the core metadata related to product identification and how it underpins inventory management and supply chain operations.

## Key Identifiers and Their Roles

### SKU (Stock Keeping Unit)
The **SKU** is the internal identifier for a distinct, sellable product variant, encompassing specific attributes such as size, color, and pack configuration. It serves as the central hub of the planning stack and represents the fundamental unit at which inventory is held, forecasted, and replenished across all distribution centers. It is important not to confuse a SKU with a UPC/GTIN; a product can have one UPC but multiple SKUs over its lifecycle, and treating them as identical can lead to system double-counting. Putaway and cycle counts must be executed and scanned at the precise SKU level to prevent downstream picking failures. Each distribution center (DC) independently holds, tracks, and counts inventory, meaning SKU quantities can vary across DCs, and replenishment decisions are made per-DC. Real-time on-hand SKU positions directly feed planning system reorder calculations, making accurate cycle counts vital.

### UPC / GTIN (Universal Product Code / Global Trade Item Number)
**UPC / GTIN** refers to an external, industry-wide barcode standard primarily used for retail scanning. In internal systems, it is stored purely as an attribute that is mapped back to an internal SKU.

### Bill of Materials (BOM)
The **Bill of Materials (BOM)** is a multi-level structured recipe that provides the authoritative definition for a finished-good SKU. It lists every component, sub-assembly, and the corresponding quantities required to build a single finished unit. The BOM serves as the single source of truth, linking finished SKUs to component material procurement. Its hierarchy represents a tree structure of finished goods, sub-assemblies, and components. BOMs are defined once for sub-assemblies and referenced globally. Revisions are strictly versioned, ensuring production operates on a known recipe, and only engineering may modify these specifications. When a demand forecast is entered at the finished-good SKU level, the planning system utilizes the BOM to "explode" the requirements, multiplying parent demand by per-unit quantities at every sub-assembly and component level to generate procurement purchase demands.

## Metadata Parameters for Replenishment

SKUs are central to inventory replenishment, which relies on specific metadata parameters:

*   **Safety Stock (Buffer Stock):** This represents extra inventory held to protect against demand spikes and lead-time variability. It is typically sized in days of supply and categorized by SKU velocity class:
    *   Class A (Fast Movers): Standard 14 days of supply, though apparel SKUs were updated to **21 days of supply** due to increased demand variability.
    *   Class B: 10 days of supply.
    *   Class C: 7 days of supply.
*   **Reorder Point (ROP):** This is an ERP-labeled system field that indicates the on-hand inventory level which automatically triggers a replenishment order. The formula for ROP is:
    $ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$
*   **Lead Time:** This is the total elapsed time from when a purchase order (PO) is placed with a supplier until the goods are received, inspected, and posted as available ("good" quantity) to pick. It includes supplier processing, transit, and inbound handling.
    *   Inbound Lead Time: Time from supplier PO to receipt at a Regional DC.
    *   Inter-node Lead Time: Transit time required to move stock from a Regional DC to a Forward DC.

## Operational Impact

Inaccurate cycle counts of SKUs negatively affect the timing of replenishment triggers. Persistent stockouts of fast-moving SKUs necessitate escalation to Demand Planning to re-evaluate safety stock levels and reorder points. Discrepancies between physical inbound counts and the Purchase Order for SKUs must be escalated to Procurement.

## Source References
*   Bill of Materials — Engineering Specification
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Logistics Network Overview
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Procurement Standard Operating Procedure
*   Warehouse Operations Runbook

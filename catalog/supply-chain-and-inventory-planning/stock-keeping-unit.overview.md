# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU), also known as an "Item number", is the fundamental internal identifier representing a distinct, sellable product variant. It encompasses specific attributes such as size, color, and pack configurations, serving as the granular level at which inventory levels, location balances, and various metadata attributes are tracked.

## Key Characteristics and Distinctions

The SKU is an *internal* identifier assigned and managed by a company. This distinguishes it from external standards like the Universal Product Code (UPC) or Global Trade Item Number (GTIN), which are barcode standards for retail scanning. A single UPC can map to multiple SKUs over its lifecycle, and treating these as interchangeable can lead to analytical double-counting errors.

## Role in Inventory Management Metadata

The SKU is central to inventory operations and data integrity:
*   **Tracking and Counting**: Inventory is tracked, counted, and scanned at the exact SKU level.
*   **Location Management**: Replenishment decisions and cycle count reconciliation are performed at the SKU plus location level.
*   **Planning System Feed**: A Distribution Center's (DC) real-time on-hand SKU position directly feeds the planning system's automated reorder calculations.
*   **Data Integrity**: Scanning to the exact SKU is critical to prevent downstream pick failures.

## Role in Planning and Replenishment Metadata

SKU metadata drives critical inventory planning and replenishment processes:
*   **Safety Stock**: Extra inventory held to cushion against demand spikes and lead-time variability. Safety stock is configured as "days of supply" and parameterized by SKU velocity:
    *   **Class A (Fast Movers)**: Requires 14 days of safety stock supply (historically); updated to **21 days of supply** for apparel Class-A SKUs due to high demand variability, superseding the standing *Inventory Policy Memo*.
    *   **Class B (Medium Movers)**: Requires 10 days of safety stock supply.
    *   **Class C (Slow Movers)**: Requires 7 days of safety stock supply.
*   **Reorder Point (ROP)**: The automated inventory threshold that triggers a replenishment order. The formula for ROP is:
    $$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    System alerts and order actions are automated based on these parameters. If Safety Stock metadata fails to scale dynamically with current-year variability, downstream reorder triggers may fail to prevent stockouts. Persistent stockouts on fast-moving SKUs prompt a review of safety stock and reorder point calculations by Demand Planning.

## Role in Bill of Materials (BOM) Metadata

The SKU represents the finished product within the Bill of Materials (BOM) structure:
*   The BOM is a multi-level hierarchical metadata tree linking a finished-good SKU to its component and sub-assembly metadata.
*   It captures specific component identity and per-parent quantity metadata.
*   This structure allows for "exploding" finished-good demand across multiple parent relationships to derive exact component-level purchasing schedules. The planning system uses this to calculate component replenishment quantities for procurement when demand is forecast at the finished-SKU level.

## Role in Logistics and Routing Metadata

SKU availability is a key factor in logistics and order fulfillment:
*   **Order Routing**: When demand is placed, the order router selects the nearest Forward DC containing the SKU in its on-hand inventory metadata.
*   **Fallback Routine**: If a SKU is out of stock at the nearest DC, the system executes a fallback routine to the next nearest node holding active inventory for that SKU.
*   **Shipping Constraints**: A Distribution Center can only ship SKUs it physically holds.

## Workflow Integration

SKUs are integrated into core warehouse workflows:
*   **Inbound Inventory**: During the inbound inventory intake workflow, the SKU is assigned and scanned to its specific storage location during putaway.
*   **Outbound Fulfillment**: A DC's physical holding of a SKU determines its ability to fulfill outbound orders.

## Source References
*   Bill of Materials — Engineering Specification
*   Demand Planning — Weekly Sync Notes
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Logistics Network Overview
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Procurement Standard Operating Procedure
*   Warehouse Operations Runbook

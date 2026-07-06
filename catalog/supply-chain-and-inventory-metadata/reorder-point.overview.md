# Reorder Point Overview

The Reorder Point (ROP), also known as "reorder level," is a critical inventory management metadata configured as the inventory level that triggers an automated replenishment purchase order within an Enterprise Resource Planning (ERP) system. It is calculated to ensure continuous supply by factoring in daily demand, lead times, and safety stock.

## Aliases
Reorder Point is also referred to as `rop` and `reorder-level`. While "reorder level" is an informal synonym, ERP systems and planning documents should use the term "Reorder Point".

## Key Features and Calculation
The Reorder Point is a calculated metadata parameter essential for automated inventory replenishment. It prevents stockouts by initiating orders when inventory reaches a predefined minimum.

The authoritative formula for Reorder Point is:
$ROP = (\text{average daily demand} \times \text{lead time in days}) + \text{safety stock}$

Key components contributing to the Reorder Point calculation include:

*   **Average Daily Demand**: The average consumption rate of an item per day.
*   **Lead Time**: The total elapsed time from placing a supplier purchase order (PO) to when the goods are inspected and made available ("good" quantity) in the warehouse. This differs from mere dock arrival. Lead times are continuously monitored by procurement, and significant shifts (lead-time drift) should trigger metadata updates in the planning system to recalculate both Safety Stock and ROP automatically. Lead time can involve:
    *   *Inbound Lead Time*: Transit from supplier PO to receipt at a Regional Distribution Center (DC).
    *   *Inter-node Lead Time*: Transit from a Regional DC to a Forward DC (fulfillment node).
    Actual lead times derived from trial orders are prioritized over vendor-quoted estimates.
*   **Safety Stock (Buffer Stock)**: This is extra inventory held to absorb demand spikes or supplier delays, serving as buffer inventory above baseline forecast demand. "Safety stock" and "buffer stock" are recognized synonyms. Safety stock values are policy-driven metadata, sized as days of supply based on SKU velocity classifications:
    *   **Class A (Fast Movers):** Historically 14 days of supply, but a new parameter establishes **21 days of supply** to counter modern demand variability.
    *   **Class B:** 10 days of supply.
    *   **Class C:** 7 days of supply.
    Adjusting the Class-A safety stock parameter upward automatically raises the Class-A Reorder Point (ROP) via standard inventory planning formulas.

## Metadata Role
Reorder Point serves as a crucial piece of metadata for inventory policy control. Correcting safety stock values automatically recalibrates downstream "reorder points" without requiring manual manipulation of replenishment triggers. Similarly, lead-time drift can trigger a metadata update, leading to recalculations of both safety stock and ROP. The system-configured inventory level then triggers an automated replenishment purchase order in the ERP.

## Source References
*   Churn Analysis — Quarterly Report
*   Customer Care Handbook
*   Demand Planning — Weekly Sync Notes
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Logistics Network Overview
*   Postmortem: Metro Region Dropped-Calls Incident
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Procurement Standard Operating Procedure
*   Quality of Service (QoS) Policy
*   Roaming Partner Agreement — Summary
*   Supplier Onboarding Guide

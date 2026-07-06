# Reorder Point Overview

The Reorder Point (ROP), also known as reorder level, is an automated inventory threshold calculated from daily demand, lead times, and safety buffers that triggers a replenishment order execution. It serves as a critical metadata attribute within inventory policy to manage warehouse stock levels.

## Key Features

The Reorder Point acts as a key piece of metadata for inventory management, enabling automated system alerts and order actions based on its value.

*   **Definition**: The ROP is the automated inventory threshold that triggers a replenishment order. While "reorder level" is a synonym, "reorder point" is the preferred terminology as it aligns with ERP field labels.
*   **Calculation**: The Reorder Point is calculated using the following formula:
    $$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    This formula incorporates the average daily demand for an item, the lead time (total elapsed time from placing a purchase order to availability of goods), and the safety stock (extra inventory held to cushion against demand spikes and lead-time variability).
*   **Relationship with Safety Stock**: ROP is directly linked to Safety Stock metadata. Safety stock is a metadata attribute that represents the cushion held to absorb demand variability. If Safety Stock metadata fails to scale dynamically with current-year variability, the downstream reorder triggers may fail to prevent stockouts.
*   **Dynamic Adjustment**: The Reorder Point automatically adjusts when underlying metadata, such as Safety Stock, changes. For instance, an update to Class A (Fast Movers) SKUs increased the safety stock from 14 days to 21 days of supply due to high demand variability in apparel, which automatically adjusted and raised the Reorder Point through standard planning formulas. This update supersedes the standing *Inventory Policy Memo* for Class-A SKUs, while Class B and C parameters remain unchanged.
*   **Input for Calculation**: A distribution center's (DC) real-time on-hand SKU position directly feeds the planning system's automated reorder calculations.
*   **Troubleshooting**: Persistent stockouts on fast-moving SKUs trigger notifications to Demand Planning to review safety stock and reorder point calculations, highlighting the operational importance of accurate ROP metadata.

## Source References
* Billing & Charging System Overview
* Bill of Materials — Engineering Specification
* Churn Analysis — Quarterly Report
* Customer Care Handbook
* Demand Planning — Weekly Sync Notes
* Inventory Management Glossary
* Inventory Policy Memo
* Inventory Systems Overview
* Postmortem: Metro Region Dropped-Calls Incident
* Postmortem: Q3 Apparel Class-A Stockouts
* Procurement Standard Operating Procedure
* Quality of Service (QoS) Policy
* SIM Provisioning Runbook
* Telecom Systems & Terminology Overview
* Warehouse Operations Runbook

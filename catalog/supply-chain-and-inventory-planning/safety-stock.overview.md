# Safety Stock Overview

Safety Stock, also known as Buffer Stock, represents the extra inventory intentionally held above anticipated baseline demand. Its primary purpose is to act as a cushion, protecting supply flows from unpredictable demand spikes and variability in lead times. This crucial component of inventory policy serves to maintain warehouse stock levels and prevent stockouts.

## Role as a Metadata Attribute

Safety Stock is explicitly identified as a metadata attribute used by inventory policy to manage warehouse stock levels. It is a critical input that, alongside the Reorder Point, drives automated system alerts and order actions. The dynamic scaling of Safety Stock metadata is essential; if it fails to adapt to current-year variability, downstream reorder triggers can fail to prevent stockouts.

## Configuration and Calculation

Safety Stock is parameterized and configured as "days of supply," often adjusted based on SKU velocity classes to tailor inventory policy to different product types:
*   **Class A (Fast Movers):** Requires 14 days of safety stock supply. An updated standard, superseding the standing *Inventory Policy Memo* for Class-A SKUs, increased this to **21 days of supply** due to high demand variability in apparel, which led to stockouts despite correct reorder point firing.
*   **Class B (Medium Movers):** Requires 10 days of safety stock supply.
*   **Class C (Slow Movers):** Requires 7 days of safety stock supply.

Safety Stock is a key component in calculating the Reorder Point (ROP), the automated inventory threshold that triggers a replenishment order. The formula is:

$$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

## Influencing Factors

The target levels for Safety Stock are directly influenced by factors such as:
*   **Lead Time Variability:** Lead Time, defined as the total elapsed time from placing a purchase order to when goods are available, directly dictates safety stock targets. Higher variability in observed lead times (validated through trial orders rather than just supplier quotes) necessitates higher safety stock buffers.

## System Impact and Monitoring

Safety Stock metadata directly impacts inventory planning and replenishment systems. A DC's real-time on-hand SKU position feeds into the planning system's automated reorder calculations, which rely on correctly configured safety stock. In cases of persistent stockouts on fast-moving SKUs, the Demand Planning department is notified to review and adjust safety stock and reorder point calculations.

## Source References
*   Bill of Materials — Engineering Specification
*   Demand Planning — Weekly Sync Notes
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Procurement Standard Operating Procedure
*   Supplier Onboarding Guide
*   Warehouse Operations Runbook

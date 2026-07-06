# Safety Stock Overview

Safety Stock, also known as **buffer stock**, represents the additional inventory held above baseline forecast demand to mitigate the impact of demand volatility and supplier delays. It plays a critical role in inventory management by absorbing unexpected spikes in demand or disruptions in the supply chain, thereby preventing stockouts. This value is dynamically sized based on SKU velocity classifications and is a key component in determining replenishment triggers.

## Key Characteristics and Policy
Safety Stock is a policy-driven metadata parameter, meaning its value is determined by predefined rules and classifications. It is typically expressed as days of supply, varying by SKU velocity class:
*   **Class A (Fast Movers):** Policy was initially 14 days of supply, but has been updated to **21 days of supply** to counteract modern demand variability, as evidenced by post-mortem analysis of stockouts. Adjusting this parameter upward automatically raises the Class-A Reorder Point (ROP).
*   **Class B:** 10 days of supply.
*   **Class C:** 7 days of supply.

## Relationship with Reorder Point (ROP)
Safety Stock directly influences the Reorder Point (ROP), which is the system-configured inventory level that triggers an automated replenishment purchase order. The authoritative formula for ROP is:

$ROP = (\text{average daily demand} \times \text{lead time in days}) + \text{safety stock}$

Correcting safety stock values automatically recalibrates downstream "reorder points" without requiring manual manipulation.

## Metadata-Driven Dynamic Recalculation
Safety Stock values are subject to dynamic recalculation based on various metadata inputs, ensuring they remain relevant to current operational conditions:
*   **Lead-Time Drift:** Lead times, defined as the duration from Purchase Order (PO) placement to goods availability, are continuously monitored. A material shift in a supplier-part combination's lead time must trigger a metadata update in the planning system, which then automatically recalculates both Safety Stock and ROP. Actual lead times derived from trial orders are prioritized over vendor-quoted estimates to protect safety stock levels.
*   **SKU Velocity Classification Changes:** Changes in an SKU's velocity class (e.g., from B to A) will lead to an adjustment in its associated Safety Stock days of supply.
*   **Supplier Performance:** While not directly calculating Safety Stock, supplier scorecards (metadata on on-time delivery, quality, and price competitiveness) inform sourcing models. These models, in turn, utilize metadata to dynamically recalculate safety stock thresholds and vendor reliability, influencing the inputs or parameters used in Safety Stock calculations.
*   **Post-Mortem Analysis:** As seen with Class-A stockouts, historical performance analysis (a form of metadata) can drive policy changes, leading to an increase in Safety Stock parameters to address evolving demand variability.

## Source References
*   Demand Planning — Weekly Sync Notes
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Logistics Network Overview
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Procurement Standard Operating Procedure
*   Supplier Onboarding Guide

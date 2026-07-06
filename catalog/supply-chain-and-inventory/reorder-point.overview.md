# Reorder Point Overview

The Reorder Point (ROP) is a critical inventory management metric representing the designated on-hand inventory level for a specific SKU that automatically triggers a replenishment action, typically a purchase order (PO). Its primary purpose is to ensure timely stock replenishment, preventing stockouts by accounting for expected demand during lead times and providing a buffer for demand variability.

## Definition and Purpose

The Reorder Point is a calculated inventory threshold that initiates the automated generation of a purchase requisition when the physical inventory of an SKU falls to or below this level. It is built upon core inventory parameters, specifically safety stock, average daily demand, and the lead time required for replenishment.

## Calculation Mechanics

The operational formula for the Reorder Point (ROP) is defined as:

$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand-Over-Lead-Time}$$

Which can also be expressed as:

$$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

Here, the components are:
*   **Average Daily Demand**: The typical quantity of the SKU consumed or sold per day.
*   **Lead Time in Days**: The duration between placing an order and receiving the inventory.
*   **Safety Stock**: A buffer of inventory held to prevent stockouts due to unexpected variations in demand or lead time. Postmortem analysis indicates that undersized safety stock cushions can lead to inventory failures even if ROP triggers correctly.

## Operational Policy

Demand planning guidelines stipulate that the Reorder Point should not be modified directly. Instead, adjustments to the ROP are managed by updating the Safety Stock value, which then causes the system to automatically recalculate the Reorder Point.

## Integration with Procurement

When a SKU's physical inventory drops to its designated Reorder Point, the planning system generates a purchase requisition. For manufactured or assembled items, this requisition is then "exploded" against the Bill of Materials (BOM) for that SKU. This process ensures that component raw materials are ordered in the correct matching and proportional quantities required to build the target SKU.

## Source References
*   [Demand Planning — Weekly Sync Notes](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8486956)
*   [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
*   [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)
*   [Procurement Standard Operating Procedure](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9043969)

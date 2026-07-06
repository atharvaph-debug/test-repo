# Inventory Replenishment Parameters Overview

Inventory Replenishment Parameters are critical planning variables that configure order triggers, lead-time variances, and buffer inventory rules across distribution centers (DCs). These parameters, also known as safety stock, reorder point (ROP), and lead time, are fundamental to managing inventory levels effectively and preventing stockouts.

## Key Replenishment Parameters

### Safety Stock

**Safety Stock**, also referred to as **Buffer Stock**, is an inventory cushion held above the demand forecast to absorb variability in demand or late inbound shipments. It is extra inventory maintained to protect against demand spikes and lead-time variability.

*   **Sizing**: Safety stock is typically sized in days of supply or against target service levels, categorized by SKU velocity class:
    *   **Class A (Fast Movers)**: Requires 14 days of supply.
    *   **Class B**: Requires 10 days of supply.
    *   **Class C**: Requires 7 days of supply.

### Reorder Point (ROP)

The **Reorder Point (ROP)** is an inventory trigger, often an ERP-labeled system field, that indicates the on-hand inventory level at which an automatic replenishment order is initiated. Rather than modifying the reorder point directly, planners recalculate the safety stock based on current demand variability, allowing the ROP to adjust automatically.

*   **Formula**: The Reorder Point is calculated using the following formula:
    $ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$

### Lead Time

**Lead Time** represents the total elapsed time from when a purchase order (PO) is placed with a supplier until the goods are received, inspected, and posted as available ("good" quantity) to pick. It encompasses supplier processing, transit time, and inbound handling.

*   **Types of Lead Time**:
    *   **Inbound Lead Time**: The time from supplier PO issuance to receipt at a Regional DC.
    *   **Inter-node Lead Time**: The transit time required to move stock from a Regional DC to a Forward DC.

## Source References
*   Demand Planning — Weekly Sync Notes
*   Inventory Policy Memo
*   Inventory Management Glossary
*   Procurement Standard Operating Procedure
*   Logistics Network Overview

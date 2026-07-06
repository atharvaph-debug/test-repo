# Stock Keeping Unit (SKU) Overview

A Stock Keeping Unit (SKU), also known by its alias `sku`, is the core internal identifier used to track unique sellable product variants at the individual size, color, and packaging level. It serves as the fundamental unit for inventory management and supply chain operations.

## Core Definition and Purpose

A Stock Keeping Unit (SKU) serves as the primary internal identifier for distinct, sellable product variants. Product lines, such as apparel, are meticulously broken down into separate SKUs for each unique combination of size, color, and packaging. This granularity ensures precise tracking and management of individual product items.

## Operational Usage

SKUs are critical for various operational processes:
*   **Strict Inventory Tracking**: Inventory tracking must occur strictly at the individual SKU level. This prevents grouping items under broader product families, which could lead to downstream order pick failures.
*   **Inbound Processes**: Inbound processes require items to be scanned directly to their exact SKU. Scanning to a product family instead of a specific SKU can cause significant operational issues.
*   **Discrepancy Reconciliation**: Periodic cycle counts, executed continuously by zone, reconcile any identified discrepancies using a composite key of `SKU + location` to pinpoint exact stock variances.

## Supply Chain Integration

The SKU is central to several supply chain and manufacturing processes:
*   **Bill of Materials (BOM) Connection**: For manufactured or assembled items, each finished-good SKU is bound to a Bill of Materials (BOM). This BOM acts as a structural recipe, detailing the exact components, sub-assemblies, and quantities required to build a single unit of the target SKU.
*   **Automated Requisition Exploding**: When a SKU's physical inventory drops to its designated reorder point, the planning system generates a purchase requisition. For manufactured goods, this requisition is automatically "exploded" against its BOM, ensuring that component raw materials are ordered in matching, proportional quantities.
*   **Reorder Point (ROP) and Safety Stock Calculations**: The SKU is a key parameter in inventory policy. The Reorder Point (ROP) is the designated on-hand inventory level that automatically triggers a purchase order (PO) replenishment for a specific SKU. The operational formula for ROP is defined as:
    $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    Postmortem analyses have shown that inventory failures can occur if safety stock cushions are undersized against actual demand variability for a given SKU, even if ROP triggers fire correctly.

## Source References
* [Bill of Materials — Engineering Specification](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8355883)
* [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
* [Inventory Management Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8945665)
* [Inventory Systems Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8978433)
* [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)
* [Procurement Standard Operating Procedure](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9043969)
* [Warehouse Operations Runbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8814594)

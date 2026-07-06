# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU) is the primary internal identifier for a distinct, sellable product variant. It serves as a foundational piece of metadata, differentiating products based on attributes such as size, color, or packaging combinations.

## Key Characteristics and Role

While a product line represents a general item, it translates into multiple distinct SKUs once specific variants—like size, color, and pack combinations—are accounted for. Each variant is tracked independently within inventory systems through its unique SKU identifier.

## Systemic Centrality

The SKU is central to many operational and planning activities, anchoring every inventory record, warehouse procedure, and planning event.

### Manufacturing Relationships (Bill of Materials - BOM)
For manufactured or assembled items, each finished-good SKU is programmatically linked to a multi-level Bill of Materials (BOM). The BOM documents every component, sub-assembly, and precise quantities required to construct a single finished unit of that SKU. This linkage serves as a primary metadata translation layer between engineering design and procurement activities.

### Distribution Center (DC) Operations
Within Distribution Centers, key metadata events are tracked at the SKU level. These include inbound receipts, storage tracking, and outbound shipping, providing granular visibility into product movement and status.

### Replenishment and Inventory Management
Inventory planning systems rely on SKUs for replenishment triggers. When a SKU's on-hand inventory position drops to its designated reorder point, the planning system initiates a purchase requisition. For manufactured products, this requisition is then automatically 'exploded' against the SKU's Bill of Materials (BOM) to determine component requirements.

## Impact on Inventory Policy

SKUs are fundamental to inventory policy calculations, such as the reorder point (ROP) formulation:

$$ROP = (\text{average daily demand} \times \text{lead time in days}) + \text{safety stock}$$

Safety stock, intended as a buffer against demand volatility, is often managed at the SKU level. However, static safety stock policies can lead to vulnerabilities, as evidenced by failures to prevent stockouts of high-priority SKU classes (e.g., Class-A apparel) when demand variability significantly increases over time.

## Aliases
* sku
* product-variants

## Source References
* [Bill of Materials — Engineering Specification](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8355883)
* [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
* [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)
* [Inventory Management Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8945665)
* [Inventory Systems Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8978433)
* [Warehouse Operations Runbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8814594)
* [Logistics Network Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9011201)
* [Procurement Standard Operating Procedure](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9043969)

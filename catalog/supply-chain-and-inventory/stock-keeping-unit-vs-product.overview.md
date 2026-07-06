# Stock Keeping Unit vs. Product Overview

The "Stock Keeping Unit (SKU) vs. Product" entry defines a core classification distinction within supply chain metadata models, mapping a conceptual, top-level product line down to unique, granular inventory tracking identifiers based on individual variations. This distinction is critical for precise inventory management and operational metadata.

## Key Concepts

*   **Product:** Refers to the conceptual merchandising line, representing a top-level item without specific variations.
*   **Stock Keeping Unit (SKU):** Represents the granular internal identifier for a distinct, sellable product variant. A single product, such as a t-shirt, can translate to multiple unique SKUs. Each SKU is based on specific combinations of attributes like size, color, and pack, and each variation is tracked independently within inventory systems.

## Metadata Usage

The SKU serves as a foundational identifier in various supply chain metadata structures:

*   **Bill of Materials (BOM):** For any finished-good SKU, the BOM acts as authoritative, structured engineering metadata, documenting every component, sub-assembly, and the exact quantity needed to construct one unit. This bridges engineering designs with procurement activities and enables "requisition explosion" in manufacturing workflows.
*   **Inventory Policies:** SKUs are central to managing inventory levels. The **Reorder Point (ROP)**, which is the specific on-hand inventory level that triggers a replenishment order, is calculated for individual SKUs. Safety stock policies, such as setting safety stock for Class-A items to 21 days of supply to reflect demand variability, are also applied at the SKU level.

## Source References
*   [Inventory Management Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8945665)
*   [Inventory Systems Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8978433)
*   [Bill of Materials — Engineering Specification](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8355883)
*   [Procurement Standard Operating Procedure](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9043969)
*   [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
*   [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)

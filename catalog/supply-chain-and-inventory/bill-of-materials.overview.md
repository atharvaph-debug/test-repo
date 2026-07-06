# Bill of Materials Overview

The Bill of Materials (BOM), also known as BOM Spec or BOM Structuring, is the authoritative hierarchical specification detailing the components and assemblies required to construct a finished product. It serves as a foundational piece of metadata, describing the exact composition and structure of a manufactured item within supply chain and inventory management systems.

## What is a Bill of Materials?

The BOM is defined as the authoritative engineering specification that maps a finished-good Stock Keeping Unit (SKU) to its parent sub-assemblies and raw purchased components, including their exact build quantities. It is considered a hierarchical recipe for manufacturing, connecting forecasted SKU demand directly to raw-material procurement requisitions.

## Key Characteristics and Relationships

*   **Hierarchical Structure:** The BOM details a product's structure in a hierarchical manner, outlining all constituent parts at various levels of assembly.
*   **One-to-Many Mappings:** While a single manufactured SKU is associated with exactly one active BOM revision at any given time, a single lower-level component can be utilized across the hierarchical BOM structures of many different parent SKUs.
*   **SKU Integration:** The BOM is intrinsically linked to the SKU, which is an internal identifier for a distinct, sellable product variant. The BOM specifies what goes into creating a particular SKU.
*   **Data Integrity:** The BOM acts as the absolute single source of truth for a product's composition. Manual modifications to purchase order component quantities by buyers are strictly prohibited without validation against the official BOM.

## Role in Supply Chain Operations

The Bill of Materials is critical for several supply chain and procurement functions:

*   **Material Demand Calculation:** Downstream procurement planning systems leverage the BOM for "explosion calculations." This process recursively multiplies parent demand rates through every tier of the BOM hierarchy to calculate material demand when finished-good forecast volumes are provided.
*   **Replenishment Execution:** When a SKU's on-hand inventory reaches its defined reorder point, the planning system generates a purchase requisition. For manufactured items, this requisition is "exploded" using the product's Bill of Materials to derive precise component requirements and quantities needed for replenishment.
*   **Procurement Planning:** It directly informs raw material procurement, ensuring that the correct components are ordered in the right quantities to meet production needs derived from SKU demand.

## Source References

*   [Copy of BOM Spec.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDE339165-24EA-4C49-B810-DCF0DDE671B4%7D&file=Copy%20of%20BOM%20Spec.docx&action=default&mobileredirect=true)
*   [Copy of Procurement SOP.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B3070B2AC-B110-4099-98F4-E74954ED7817%7D&file=Copy%20of%20Procurement%20SOP.docx&action=default&mobileredirect=true)
*   [Inventory Systems Overview](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)

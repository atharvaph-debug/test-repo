# Bill of Materials Specification Overview

The Bill of Materials (BOM), also known as a BOM Specification, is a multi-level hierarchical structure that serves as the authoritative definition for manufacturing finished goods, sub-assemblies, and the components required to build a product. It is the single source of truth for linking finished Stock Keeping Units (SKUs) to component material procurement.

## Purpose and Definition

The Bill of Materials provides a structured recipe for a finished-good SKU, detailing every component, sub-assembly, and their corresponding quantities needed to build a single finished unit. It explicitly maps finished goods to their raw materials and sub-assemblies, forming a crucial piece of metadata for inventory and supply chain operations.

## Structure and Characteristics

The BOM is structured as a multi-level tree, reflecting the hierarchical nature of product assembly. Key characteristics include:

*   **Hierarchy:** It explicitly defines the parent-child relationships between finished goods, sub-assemblies, and individual components.
*   **Reusability:** A sub-assembly's BOM is defined once and can be referenced globally across different product BOMs, promoting standardization and efficiency.
*   **Versioning:** Revisions to BOM specifications are strictly versioned to ensure that production always operates on a known, approved recipe. Modifications to these specifications are restricted to engineering personnel.

## Role in Inventory and Planning

The BOM is central to inventory management and production planning systems:

*   **SKU Linkage:** It directly links the internal identifier for a distinct product variant (SKU) to the necessary materials. While SKUs are internal identifiers for planning and inventory, BOMs provide the detailed breakdown of what constitutes each SKU. It's important to note that a product can have one UPC/GTIN (an external barcode standard), but multiple SKUs over its lifecycle, and the BOM is defined at the SKU level.
*   **MRP Explosion:** In Material Requirements Planning (MRP), the BOM enables the "explosion" of requirements. When a demand forecast is entered for a finished-good SKU, the planning system uses the BOM to automatically multiply parent demand by the per-unit quantities at every sub-assembly and component level, thereby generating precise procurement purchase demands.

## Source References
*   Bill of Materials — Engineering Specification
*   Inventory Management Glossary
*   Inventory Systems Overview
*   Procurement Standard Operating Procedure

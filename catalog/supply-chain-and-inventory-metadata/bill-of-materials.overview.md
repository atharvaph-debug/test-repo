# Bill of Materials Overview

A Bill of Materials (BOM), also known by the alias "bom," represents the hierarchical, multi-level engineering specification recipe that links a finished-good SKU to its component materials and sub-assemblies. This critical piece of metadata functions as an authoritative engineering tree, detailing every component, sub-assembly, and the specific quantity required to manufacture a single finished-good SKU.

## Key Characteristics

The Bill of Materials is defined by its:
*   **Hierarchical Structure**: It is an engineering tree that organizes components and sub-assemblies in a multi-level structure, outlining the build relationships.
*   **Comprehensive Specification**: It lists every component and sub-assembly needed for a finished product, along with their precise quantities.
*   **Recipe Metadata**: It serves as the definitive "recipe" metadata, linking a finished-good SKU to all its constituent parts.

## Functional Role in Supply Chain

The BOM plays a crucial role in supply chain planning and procurement through its metadata propagation capabilities:
*   **Demand Explosion**: Planning systems utilize the multi-level BOM hierarchy to "explode" finished-good demand. This process involves multiplying parent demand by the per-unit quantities specified at every sub-level of the BOM.
*   **Component Procurement**: By propagating demand through the BOM metadata, it enables the calculation of component-level demand for procurement, thereby establishing the precise needs for all constituent materials. Demand is initially forecast at the finished SKU level and subsequently processed through the BOM to determine requirements for individual components.

## Source References
* Bill of Materials — Engineering Specification
* Inventory Systems Overview
* Procurement Standard Operating Procedure

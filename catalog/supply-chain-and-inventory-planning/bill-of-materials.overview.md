# Bill of Materials Overview

The Bill of Materials (BOM), also known by its alias BOM, is the authoritative, multi-level hierarchical metadata tree that details the component sub-assemblies and specific quantity recipes required to manufacture a finished parent SKU. It serves as a structured "recipe" or hierarchy, linking a finished-good SKU to its component and sub-assembly metadata, specifically capturing component identity and per-parent quantity information.

## Key Features

*   **Hierarchical Structure**: The BOM is a multi-level hierarchical metadata tree. It represents a finished-good SKU and its constituent components and sub-assemblies.
*   **Authoritative Metadata**: It is the authoritative source for component identity and the exact quantities required for each parent SKU. No downstream buyer or planner is permitted to alter these quantities outside of its version-controlled schema.
*   **Demand Explosion**: The BOM enables the "exploding" of finished-good demand across multiple parent relationships. When demand is forecast at the finished-SKU level, the planning system utilizes the BOM to calculate the exact component-level purchasing schedules and replenishment quantities for procurement.
*   **SKU Definition**: The finished products detailed by a BOM are identified by a Stock Keeping Unit (SKU), which is the fundamental internal identifier representing a distinct, sellable product variant.

## Source References

*   Bill of Materials — Engineering Specification
*   Inventory Management Glossary

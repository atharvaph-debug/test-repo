# Bill of Materials Overview

The Bill of Materials (BOM) is an authoritative, engineering-controlled specification that translates a finished-good SKU into its component parts for downstream procurement. It serves as crucial metadata, defining the precise composition of products.

## Key Characteristics and Functions

### Hierarchical Tree Structure
BOMs are structured as multi-level trees, reflecting the nested composition of products. A finished-good SKU is comprised of sub-assemblies, which themselves reference their own BOMs, extending down to individual purchased raw components. This hierarchical design allows for sub-assemblies to be defined once and subsequently reused across various products, streamlining product data management and consistency.

### Deriving Component Demand
The BOM is essential for planning and procurement. When demand is established for a finished SKU, planning systems "explode" the SKU through its hierarchical BOM. This process calculates the total component procurement quantity by multiplying the demand for the parent SKU by the per-unit quantities of every component at each level of the product tree.

### System Integrity and Governance
To maintain data integrity and control, each finished-good SKU is associated with exactly one active, versioned BOM revision at any given time. Strict governance protocols prohibit buyers and planners from manually editing component quantities on purchase orders. Any necessary changes to component quantities must be formally introduced by checking and releasing a new BOM revision through Engineering, ensuring that procurement always aligns with the official engineering specification.

## Source References
*   [Inventory Systems Overview](1Tp3jIXE-_Wfeb3gbFbouX0seOyi15etrylUYMzGWyh4)
*   [Bill of Materials — Engineering Specification](1DqruUuQIFjaVVYoBKmXnppaFmqCXj6PVZMom_hVOxxM)
*   [Procurement Standard Operating Procedure](1IXn1QX1m7lJ7kn6yGnQi8At_hhvBKsHuPGbs5SFUUI0)

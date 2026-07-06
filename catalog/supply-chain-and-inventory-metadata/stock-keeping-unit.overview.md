# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU) is the granular internal identifier used to track, forecast, and reconcile distinct, sellable product variants. It accounts for specific attributes such as size, color, and pack combination, serving as the central hub for planning, forecasting, holding, and replenishment systems within an organization. "SKU" should be preferred over the more casual "item number" in planning documentation.

## Key Characteristics and Role

*   **Internal Identifier**: The SKU is an internal code used to distinguish between product variations, providing a unique identifier for each distinct, sellable variant.
*   **Planning Hub**: It acts as the central data point for all planning, forecasting, holding, and replenishment activities.
*   **Granularity**: SKUs define products at a granular level, reflecting specific combinations of attributes like size, color, and packaging.

## Relationships

*   **Bill of Materials (BOM)**: A finished-good SKU is linked to its component materials and sub-assemblies through the multi-level BOM metadata. Demand for finished SKUs is forecast and then "exploded" through the BOM to calculate component-level demand for procurement.
*   **UPC/GTIN**: SKUs are distinct from external identifiers like UPC/GTIN. While a single product might have one UPC, it can map to several internal SKUs over its lifecycle. UPC/GTIN should be stored as a mapped attribute of the SKU, rather than being treated as interchangeable, to prevent issues like inventory double-counting.
*   **Replenishment Parameters**: Safety Stock, which is extra inventory held to absorb demand spikes or supplier delays, is a policy-driven metadata sized as days of supply based on SKU velocity classifications (e.g., Class A, B, C).

## Operational Use

*   **Inventory Tracking**: Within a Distribution Center (DC) or Fulfillment Center, inventory is tracked and scanned at the SKU level during processes like putaway, cycle counts, and reconciliation.
*   **System Feeding**: The on-hand inventory position per SKU in a DC directly feeds planning systems, informing replenishment and reorder calculations.

## Source References
* Bill of Materials — Engineering Specification
* Inventory Management Glossary
* Inventory Policy Memo
* Inventory Systems Overview
* Procurement Standard Operating Procedure
* Warehouse Operations Runbook

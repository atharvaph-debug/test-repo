# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU) is an internal identifier used to track distinct, sellable product variants such as specific sizes, colors, or pack configurations. It serves as the fundamental unit at which inventory is managed and forecasted within company systems, and it is never exposed externally. SKUs are also known by the alias `sku`. Other terms like `upc` and `gtin` are related external identifiers but are not interchangeable with SKU.

## Key Characteristics and Usage

*   **Internal Identifier**: An SKU is assigned internally within a company and does not leave its systems.
*   **Product Variant Representation**: Each SKU represents a distinct variant of a product (e.g., a specific size, color, or pack configuration).
*   **Inventory Management Unit**: It is the primary unit for managing inventory levels and for forecasting demand.
*   **Bill of Materials (BOM)**: SKUs are integral to Bill of Materials, which define the components of a product. BOMs are hierarchical, listing parent SKUs down to lower-level sub-assemblies and raw components, allowing for reuse across different products.
*   **Warehouse Operations**: While SKUs are unified globally across an organization, each Distribution Center (DC) counts and manages its inventory independently. This means that identical SKUs will have distinct on-hand quantities at different DCs, and replenishment decisions must be made specifically for each individual DC.

## Relationship with External Identifiers (UPC/GTIN)

It is crucial to distinguish SKUs from external identifiers like UPC (Universal Product Code) and GTIN (Global Trade Item Number).
*   **UPC/GTIN**: These are external barcode standards assigned by a global registry for retail scanning.
*   **Mapping Rule**: A product can map to one UPC but multiple SKUs over its lifecycle. Treating UPC/GTIN and SKU as interchangeable in inventory databases can lead to severe double-counting errors.

## Role in Inventory Planning and Calculations

SKUs are central to various inventory planning calculations and policies:

*   **Reorder Point (ROP) Calculation**: The ROP, which defines the replenishment trigger for an item, is dynamically calculated per SKU using the formula:
    $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    This calculation is performed automatically by the planning system.
*   **Safety Stock Calibration**: Safety stock, which is an inventory cushion to absorb demand spikes, is sized based on an SKU's velocity classification in "days of supply":
    *   **Class A (Fast Movers):** 14 days of supply
    *   **Class B:** 10 days of supply
    *   **Class C:** 7 days of supply
    Historical parameters for safety stock, such as those previously set at 14 days, can become undersized if market demand variability shifts, potentially leading to stockouts.

## Data Model Grains

In the data model:
*   The `products` table is grained at one row per sellable SKU.
*   The `inventory_items` table is grained at one row per physical stock unit, which implicitly relates to a specific SKU.

## Source References
*   [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Systems Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)
*   [Bill of Materials — Engineering Specification](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDE339165-24EA-4C49-B810-DCF0DDE671B4%7D&file=Copy%20of%20BOM%20Spec.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Policy Memo.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Memo.docx&action=default&mobileredirect=true)
*   [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true)

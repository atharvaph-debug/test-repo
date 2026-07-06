# Stock Keeping Units Overview

A Stock Keeping Unit (SKU) is an internal identifier assigned by an organization's systems to represent a distinct, sellable product variant, differentiating items by attributes such as size, color, or pack configuration. Often casually referred to as an "item number," the SKU serves as a foundational entity for inventory management and supply chain operations.

## Key Distinctions and Metadata

A critical distinction is made between an **SKU** and a **UPC/GTIN**:
*   **SKU** is an *internal* identifier, used within the company for inventory, sales, and forecasting systems.
*   **UPC/GTIN** is an *external* barcode standard, assigned by a global registry for retail scanning and external trade.

Treating UPC/GTIN and SKU as identical identifiers can lead to critical double-counting errors in inventory analytics.

## SKU as a Central Entity Hub

The SKU acts as a central hub for various logistics and supply chain activities. Every transaction, forecasting model, stock-holding record, and replenishment activity across the logistics network revolves around the SKU.

### Role in Bill of Materials (BOM)
Each finished-good SKU is associated with a Bill of Materials (BOM), which details the component SKUs, sub-assemblies, and quantities required for its manufacture. BOMs can be multi-level, forming a structural parts tree. Demand forecasting for finished-good SKUs "explodes" through this BOM tree to calculate precise component demand for procurement.

## Data Model Representation

In the analytical warehouse database, the SKU is represented across several key tables:
*   The `products` table serves as the authoritative source for product attributes, with one row per sellable SKU.
*   The `inventory_items` table tracks individual physical units of stock. This table includes `product_id` as a foreign key linking to the `products` table and contains denormalized `product_*` columns (including SKU) to optimize inventory queries, though `products` remains the single source of truth for potential discrepancies.
*   The `order_items` table, a central fact table for revenue, links specific physical stock units shipped to `inventory_items` via `order_items.inventory_item_id`.
*   Products are mapped to a specific distribution center via `products.distribution_center_id`, which assists in logistics and shipping-time analysis.

## Operational Significance

SKUs are fundamental to several operational processes:
*   **Safety Stock Classification**: Safety stock allocations are structured by SKU velocity classes, based on historical demand variability. For instance, "Class A" (Fast Movers) SKUs might require 14 days of supply, "Class B" (Medium Velocity) 10 days, and "Class C" (Slow Movers) 7 days.
*   **Warehouse Operations**: Inbound processes and putaway accuracy rely on scanning items at the specific SKU level, not just the product family. Inaccurate scans can lead to pick failures. Reconciled SKU positions directly inform reorder and stock planning calculations.

## Source References

*   [Copy of BOM Spec.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDE339165-24EA-4C49-B810-DCF0DDE671B4%7D&file=Copy%20of%20BOM%20Spec.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Systems Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)
*   [Inventory Policy Memo](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Policy%20Memo.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true)

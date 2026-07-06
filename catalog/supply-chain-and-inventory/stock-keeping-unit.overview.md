# Stock Keeping Unit Overview

A Stock Keeping Unit (SKU), also known informally as an Item Number, is an internal foundational identifier representing a unique, distinct, and sellable product variant. It spans specific attributes like size, color, and pack configurations, making it the granular unit at which core inventory and supply chain operations occur.

## Key Characteristics and Role

*   **Foundational Identifier:** The SKU is the foundational unit for all forecasting, stock-holding, and fulfillment activities across distribution centers.
*   **Internal and Proprietary:** SKUs are created internally within company systems and are designed to never leave those systems.
*   **Granularity:** Each SKU uniquely identifies a specific variant of a product (e.g., a "Red Large T-Shirt" would have a distinct SKU from a "Blue Medium T-Shirt").
*   **Differentiation from UPC/GTIN:** Unlike a Universal Product Code (UPC) or Global Trade Item Number (GTIN), which are external barcode standards from a global registry used for retail scanning, the SKU is internal. Treating SKU and UPC as identical can lead to analytical double-counting errors, as one UPC may map to several SKUs over a product's lifecycle.
*   **Product Taxonomy:** SKUs fit within a broader product taxonomy structured as Department (e.g., Men, Women) → Category (e.g., Jeans) → Brand (manufacturer).

## Integration in Supply Chain & Inventory Management

The SKU plays a central role in several critical supply chain processes:

*   **Bill of Materials (BOM):** For manufactured items, a finished-good SKU is mapped to an authoritative Bill of Materials (BOM). The BOM is a hierarchical recipe detailing parent sub-assemblies and raw purchased components with exact build quantities required to construct one finished-good SKU. While a single manufactured SKU has one active BOM revision, a single lower-level component can reside in the BOM structures of many different parent SKUs. BOMs are crucial for "explosion calculations" to determine material demand by multiplying forecast volumes recursively through the BOM hierarchy. The BOM serves as the single source of truth for a product's composition, connecting forecasted SKU demand to raw-material procurement.
*   **Replenishment and Safety Stock:** SKUs are central to inventory replenishment planning.
    *   **Reorder Point (ROP):** When a SKU’s on-hand inventory matches its defined reorder point, the planning system generates a purchase requisition. The ROP is calculated as:
        $$\text{ROP} = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    *   **Safety Stock:** Extra buffer inventory held at the SKU level to protect customer service levels from demand spikes and supply chain delays. Safety stock quantities are dictated by velocity categories: Class A (Fast Movers) has a target of 21 days of supply (adjusted from 14 days following a Q3 stockout investigation), Class B 10 days, and Class C 7 days of supply.
    *   **Lead Time:** The elapsed time between placing a purchase order and receiving goods, impacting buffer inventory needs. This includes Inbound Lead Time (supplier PO to DC arrival) and Inter-node Lead Time (internal transit between distribution nodes).
*   **Warehouse Operations:**
    *   **Inbound and Putaway:** Received quantities are verified against Purchase Orders (POs) and scanned to specific warehouse bin locations at the individual SKU level to prevent picking errors.
    *   **On-Hand Accuracy:** Cycle counts track on-hand SKU counts, which dynamically feed replenishment calculations in demand planning systems. Out-of-stock SKUs at a local distribution center trigger automated routing to source from alternative logistics network nodes.

## Data Model Representation

In the data model:

*   The `products` table represents sellable product variants, with one row mapping 1:1 with a SKU. This table would typically hold attributes like `products.cost`, `products.retail_price`, and `products.SKU`.
*   The `inventory_items` table represents individual physical units of stock and denormalizes product attributes by copying `product_*` columns, including SKU, for query convenience.
*   The `order_items` table represents individual sold units of a product within an order and serves as a central fact table, linking customer, order, product (via SKU), and inventory identifiers. It records the `order_items.sale_price`.

## Source References
* [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
* [Copy of Inventory Systems Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)
* [Copy of BOM Spec.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDE339165-24EA-4C49-B810-DCF0DDE671B4%7D&file=Copy%20of%20BOM%20Spec.docx&action=default&mobileredirect=true)
* [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true)
* [Inventory Policy Memo](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Policy%20Memo.docx&action=default&mobileredirect=true)
* [Copy of Procurement SOP.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B3070B2AC-B110-4099-98F4-E74954ED7817%7D&file=Copy%20of%20Procurement%20SOP.docx&action=default&mobileredirect=true)
* [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)

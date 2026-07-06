# Replenishment and Bill of Materials Overview

This entry describes the foundational concepts and processes for manufacturing and inventory management, encompassing the hierarchical Bill of Materials (BOM) structure and quantitative formulas for calculating inventory safety stocks and reorder points. It details how products are built from components and how inventory levels are managed to ensure continuous supply while mitigating risks.

## Bill of Materials (BOM)

The **Bill of Materials (BOM)** is an authoritative, multi-level hierarchical tree structure that defines every component, sub-assembly, parent SKU, and quantity required to manufacture one unit of a finished good. It serves as the bridge between design engineering and procurement planning. Each finished-good SKU is associated with a BOM, which acts as the single source of truth for component configurations. Purchasing agents are restricted from hand-editing component quantities without validating against the BOM structure.

The concept of **BOM Explosion** refers to a system execution where demand for a parent SKU is multiplied through every layer of the BOM hierarchy to calculate the exact raw material and component procurement requirements. BOMs can be multi-level, meaning sub-assemblies can point to their own sub-BOMs, forming a structural parts tree. Forecasting systems project demand at the finished-good SKU level, which then "explodes" through this BOM tree to compute component demand for procurement.

## Inventory Replenishment

### Safety Stock

**Safety Stock** is the calculated inventory buffer held above expected forecasts. Its primary purpose is to absorb demand spikes or supplier delays, acting as a safeguard against stockouts. While "Buffer stock" is sometimes used as a synonym, **Safety stock** is the preferred and authoritative term for supply chain planning.

### Reorder Point (ROP)

The **Reorder Point (ROP)** is the inventory quantity threshold that initiates replenishment. It is constructed as safety stock plus estimated demand-over-lead-time. "Reorder level" is an informal synonym, but **Reorder point** or **ROP** is the authoritative term, as it maps directly to ERP system database fields.

The Reorder Point is calculated using the following formula:

$$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$

In this formula, the first term computes the expected consumption during active replenishment, while the second term (safety stock) acts as the buffer against lead time and demand variability.

## Safety Stock Classification and Overrides

Safety stock allocations are structured by SKU velocity classes, which are based on last year's demand variability:

*   **Class A (Fast Movers):** Typically allocated 14 days of supply.
*   **Class B (Medium Velocity):** Allocated 10 days of supply.
*   **Class C (Slow Movers):** Allocated 7 days of supply.

There is a specific **Inventory Class-A Safety Stock Override** in place. The previous standard for Class A SKUs was 14 days of supply. However, due to rising demand variability in apparel, the current corrective standard for Class A is **21 days of supply**. This override supersedes the baseline figures in the standing Inventory Policy Memo, and an increase in safety stock automatically elevates the calculated reorder point within the planning system.

## Key Concepts and Terminology

*   **Stock Keeping Unit (SKU):** An internal identifier assigned by internal systems representing a distinct, sellable product variant (e.g., specific size, color, or pack configuration). While sometimes casually referred to as "item number," SKU is an internal construct.
*   **UPC/GTIN:** An external barcode standard assigned by a global registry for retail scanning. It is crucial to note the authoritative distinction: SKU is an internal identifier, whereas UPC/GTIN is an external one. Treating UPC/GTIN and SKU as identical identifiers can cause critical double-counting errors in inventory analytics.
*   **Safety Stock:** Preferred over "Buffer Stock" for supply chain planning.
*   **Reorder Point (ROP):** Preferred over "Reorder level" and maps directly to ERP system database fields.

## Source References

*   [Copy of BOM Spec.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDE339165-24EA-4C49-B810-DCF0DDE671B4%7D&file=Copy%20of%20BOM%20Spec.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Policy Memo.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC0DDADC7-134E-4351-9261-75ECAF4CCE40%7D&file=Copy%20of%20Inventory%20Policy%20Memo.docx&action=default&mobileredirect=true)
*   [Copy of Q3 Stockout Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0577D1E6-D3BA-4BBF-8C8E-07A0D0A0FBC6%7D&file=Copy%20of%20Q3%20Stockout%20Postmortem.docx&action=default&mobileredirect=true)
*   [Copy of Demand Planning Meeting Notes.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B89329718-94BF-4824-8F88-5B2A5E1FC0B8%7D&file=Copy%20of%20Demand%20Planning%20Meeting%20Notes.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Systems Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)
*   [Procurement SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B3070B2AC-B110-4099-98F4-E74954ED7817%7D&file=Copy%20of%20Procurement%20SOP.docx&action=default&mobileredirect=true)

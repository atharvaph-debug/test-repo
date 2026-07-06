# Warehouse and Distribution Operations Overview

The `Warehouse and Distribution Operations` entry models the regional and forward distribution nodes, along with the inbound scanning procedures that feed the supply chain. It represents the logistics network as a graph of independent inventory-holding nodes rather than a single pool of stock, crucial for managing the flow of goods and associated metadata within the supply chain [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true).

## Key Features and Concepts

### Logistics Nodes
Logistics Nodes are distribution centers or fulfillment centers that house and count stock independently [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%5D&file=business_glossary.docx&action=default&mobileredirect=true). This model includes two primary types:

*   **Regional Distribution Centers (Regional DCs):** These nodes hold broad product assortments and are responsible for replenishing forward nodes [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true).
*   **Forward Distribution Centers (Fulfillment Nodes):** Located strategically near high-demand geographic areas, these centers fulfill order requests directly to retail stores or customers [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true).

### Inventory Metadata and Mapping
For effective logistics and shipping-time analysis, every product is meticulously mapped to exactly one warehouse via `products.distribution_center_id` [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%5D&file=business_glossary.docx&action=default&mobileredirect=true). This explicit mapping forms a critical piece of product metadata, enabling accurate tracking and operational decisions.

### Inbound & Putaway Accuracy
Accurate inbound processes are vital for maintaining high-quality inventory metadata. Putaways require scanning at the specific SKU level, not just the product family level [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true). Inaccurate scans directly lead to down-funnel pick failures. The reconciled SKU positions, derived from accurate scanning, directly feed into reorder and stock planning calculations, highlighting the importance of precise metadata capture at this stage [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true).

### Multi-Tier Lead Times
Operational efficiency within the logistics network is also characterized by specific lead times:

*   **Inbound Lead Time:** This refers to the transit time from a supplier purchase order until receiving and inspection at a regional DC [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true).
*   **Inter-node Lead Time:** This measures the transit time required to transfer stock from a Regional DC to a Forward DC [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true).

## Key Columns

*   **`products.distribution_center_id`**: This column is essential for metadata enrichment, mapping each product to its specific distribution center. It allows for detailed logistics and shipping-time analysis by linking product data to its physical warehousing location [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%5D&file=business_glossary.docx&action=default&mobileredirect=true).

## Source References
* [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true)
* [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

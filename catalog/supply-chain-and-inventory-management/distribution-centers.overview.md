# Distribution Centers Overview

Distribution Centers (DCs) are physical facilities responsible for storing bulk inventory and fulfilling customer orders. They are also referred to interchangeably as "fulfillment centers" or "fulfillment nodes". These facilities form a structured logistics network, operating as independent inventory-holding nodes.

## Key Features and Structure

The physical distribution network utilizes a two-tiered system of Distribution Centers:
*   **Regional DCs:** These centers hold broad product assortments and are primarily responsible for replenishing the next tier of facilities.
*   **Forward DCs (Fulfillment Nodes):** Positioned closer to end-demand, these nodes ship directly to stores or customers.

Within this network, the terms "Distribution Center" (DC), "fulfillment centers," and "fulfillment nodes" all describe facilities that receive, store, and fulfill orders.

## Operational Details

Distribution Centers operate independently regarding inventory management. Even for identical Stock Keeping Units (SKUs), each Distribution Center counts and holds its inventory separately. Consequently, replenishment decisions, including the calculation of Reorder Points (ROP), must be determined for each individual DC. Corporate badging protocols and Workplace Services facilities guidelines are administrative and do not apply to the operations of physical warehouses or distribution centers.

## Data Model

The `distribution_centers` table is grained at one row per physical fulfillment warehouse, representing each unique facility within the logistics network.

## Aliases

Distribution Centers are also known by the aliases:
*   dc
*   fulfillment-centers
*   fulfillment-nodes

## Source References
*   [Copy of Logistics Network Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B52B03E10-8250-4D8C-9334-031D6635DFFE%7D&file=Copy%20of%20Logistics%20Network%20Overview.docx&action=default&mobileredirect=true)
*   [Copy of Warehouse Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9BE4104B-79BA-406F-81BF-776090FEBD85%7D&file=Copy%20of%20Warehouse%20Ops%20Runbook.docx&action=default&mobileredirect=true)
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [Copy of Office Badge Facilities Policy.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7E679034-E2E3-48DD-81E3-13572ED27B20%7D&file=Copy%20of%20Office%20Badge%20Facilities%20Policy.docx&action=default&mobileredirect=true)

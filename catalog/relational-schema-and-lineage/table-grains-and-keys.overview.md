# Table Grains and Keys Overview

This entry, also known as `database-schema-grains`, maps keys and defines the row granularity for core physical tables within the data model. It provides essential metadata for understanding the structure and content of key operational entities, including users, orders, order items, products, inventory items, and distribution centers.

## Core Tables and Their Grains

This section details the fundamental tables and specifies what each individual row within these tables represents, providing critical metadata for data understanding and usage.

*   **`users`**: Contains one row for each unique customer. This table stores demographic, location, and acquisition details about users.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]
*   **`orders`**: Each row represents a single checkout event.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]
*   **`order_items`**: Each row corresponds to one unit of a product within an order. This table serves as the central hub of the model, facilitating connections between users, orders, products, and inventory units.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]
*   **`products`**: Each row represents a single sellable product variant (SKU). This table is designated as the authoritative source for product dimensions.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]
*   **`inventory_items`**: Each row corresponds to a single physical item currently in stock.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]
*   **`distribution_centers`**: Each row represents one distinct warehouse location.
    [[data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)]

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)

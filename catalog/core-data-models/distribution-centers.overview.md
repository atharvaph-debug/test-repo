# Distribution Centers Overview

Distribution Centers represent physical fulfillment warehouses within the theLook eCommerce dataset. This entity carries essential metadata, such as the name and geographical coordinates, which are crucial for shipping-time analysis.

## Key Features

Each distribution center is defined by:
*   Its unique identity.
*   A descriptive name.
*   Geographical coordinates (latitude and longitude), specifically noted for their utility in shipping-time analysis.

## Relationships

The `Distribution Centers` entity is integrated into the core data model through its relationship with `products`. Products are linked to their respective distribution centers using `products.distribution_center_id`, which references the `id` of the `distribution_centers` table. This allows for analytical insights into product storage and logistics origins.

## Source References
* [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

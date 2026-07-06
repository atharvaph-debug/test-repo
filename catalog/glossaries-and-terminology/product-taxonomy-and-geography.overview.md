# Product Taxonomy and Geography Overview

This entry describes the structural mapping of products into hierarchical classifications and their association with operational delivery nodes. It defines how products are organized and geographically situated within the business landscape, crucial for metadata enrichment related to product characteristics and fulfillment.

## Key Concepts

Products are organized using a three-level hierarchy to categorize them effectively:
*   **Department**: Represents the broadest classification, such as "Men" or "Women".
*   **Category**: A more specific grouping within a Department, such as "Jeans" or "Outerwear".
*   **Brand**: Identifies the manufacturer or label of the product.

Each product is also mapped to a physical **Distribution Center**, which serves as a warehouse for operational delivery. This mapping is essential for shipping optimization. Distribution Centers contain metadata such as names and latitude/longitude coordinates.

## Key Columns

The following column is central to understanding the geographical mapping of products:
*   `products.distribution_center_id`: This identifies the specific physical warehouse to which a product is mapped. Each product is mapped to exactly one Distribution Center.

## Source References
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

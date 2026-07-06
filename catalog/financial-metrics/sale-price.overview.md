# Sale Price Overview

**Sale Price** represents the actual transaction price paid by the customer. It serves as the authoritative figure for realized revenue, reflecting the final amount exchanged in a sale.

## Key Features

The Sale Price is recorded in the `order_items.sale_price` field. Unlike the `Retail Price`, which is the list or catalog price advertised to customers prior to discounts, the Sale Price accounts for any discounts or promotions, capturing the true price at which a product was sold. It also differs from `Cost`, which is the wholesale or landed price the company paid its supplier and is hidden from customers.

## Related Metrics

The Sale Price is a fundamental component in the calculation of several key financial metrics:

*   **Gross Revenue**: Calculated as the sum of `sale_price` for all non-cancelled items.
    ```sql
    SUM(sale_price) WHERE status <> 'Cancelled'
    ```
*   **Net Revenue**: Represents Gross Revenue with revenue from returned items removed.
    ```sql
    SUM(sale_price) WHERE status NOT IN ('Cancelled', 'Returned')
    ```
*   **Average Order Value (AOV)**: Derived by dividing Gross Revenue by the count of distinct orders.
    ```sql
    Gross Revenue / COUNT(DISTINCT order_id)
    ```
*   **Gross Margin**: Defined as Net Revenue minus the product costs.
    ```sql
    SUM(sale_price - cost) WHERE status NOT IN ('Cancelled', 'Returned')
    ```
*   **Gross Margin %**: The profit margin relative to Net Revenue.
    ```sql
    Gross Margin / Net Revenue
    ```

## Source References
* [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

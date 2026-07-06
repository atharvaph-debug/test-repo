# Gross Margin Overview

Gross Margin represents the financial profitability of sales, calculated as net revenue minus product costs. It is evaluated both as an absolute currency value and as a percentage relative to net revenue, often referred to as Gross Margin Percentage. This metric excludes revenue from cancelled or returned items, providing a clearer picture of profit from completed sales.

## Key Definitions and Calculations

### Gross Margin (Value)
The Gross Margin is defined as the net revenue after deducting the product costs associated with the sold goods.
*   **Business Logic**: Net revenue minus the product costs.
*   **SQL/Mathematical Formulation**:
    ```sql
    SUM(sale_price - cost)
    ```
*   **Filter**: `status NOT IN ('Cancelled', 'Returned')`

### Gross Margin %
The Gross Margin Percentage expresses the profit margin as a proportion of the net revenue.
*   **Business Logic**: Profit margin relative to net revenue.
*   **SQL/Mathematical Formulation**:
    ```sql
    Gross Margin / Net Revenue
    ```

### Net Revenue (Component of Gross Margin)
Net Revenue is a foundational component for calculating Gross Margin. It accounts for gross revenue with any revenue from returned items removed.
*   **Business Logic**: Gross revenue with returned item revenue removed.
*   **SQL/Mathematical Formulation**:
    ```sql
    SUM(sale_price)
    ```
*   **Filter**: `status NOT IN ('Cancelled', 'Returned')`

## Source References
*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

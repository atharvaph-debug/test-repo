# Revenue Metrics Overview

Revenue Metrics are financial evaluations calculated at transaction levels, incorporating purchase cancellation and return boundaries. This category encompasses a set of key performance indicators (KPIs) derived from detailed transactional and product data, providing insights into sales performance and profitability.

## Key Metrics

The following standardized metrics are defined to assess various aspects of revenue and sales:

*   **Gross Revenue:** The total value of all sales where the order status is not 'Cancelled'. Cancelled orders are strictly omitted from this calculation.
    $$\text{SUM}(\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Net Revenue:** Gross revenue adjusted to exclude both 'Cancelled' and 'Returned' items.
    $$\text{SUM}(\text{order\_items.sale\_price}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Average Order Value (AOV):** An order-grain KPI that represents the average revenue generated per order, calculated by dividing Gross Revenue by the total count of distinct orders.
    $$\frac{\text{Gross Revenue}}{\text{COUNT}(\text{DISTINCT order\_items.order\_id})}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Units Sold:** The total count of individual order items where the status is not 'Cancelled'.
    $$\text{COUNT}(\text{order\_items.id}) \quad \text{where status} \neq \text{'Cancelled'}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Return Rate:** The proportion of returned order items compared to all non-cancelled order items.
    $$\frac{\text{COUNT}(\text{order\_items WHERE returned\_at IS NOT NULL})}{\text{COUNT}(\text{order\_items WHERE status} \neq \text{'Cancelled'})}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Gross Margin:** The total profit from sales after subtracting the cost of goods sold, calculated for items that are neither 'Cancelled' nor 'Returned'. This requires joining `order_items.product_id` to `products.id` to access product cost.
    $$\text{SUM}(\text{order\_items.sale\_price} - \text{products.cost}) \quad \text{where status} \notin (\text{'Cancelled'}, \text{'Returned'})$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Gross Margin %:** The Gross Margin expressed as a percentage of Net Revenue.
    $$\frac{\text{Gross Margin}}{\text{Net Revenue}}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Sell-Through Rate:** The ratio of inventory items sold to the total inventory items.
    $$\frac{\text{COUNT}(\text{inventory\_items WHERE sold\_at IS NOT NULL})}{\text{COUNT}(\text{inventory\_items})}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

*   **Average Days in Inventory:** The mean duration an inventory item spends from its creation until it is sold.
    $$\text{MEAN}(\text{sold\_at} - \text{created\_at}) \quad \text{over sold inventory items}$$
    [[metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)]

## Underlying Data Grains

Revenue metrics are primarily computed from two distinct transactional grains:

*   **Order:** Represents a single purchase event initiated by a customer (`user_id`). It tracks the overall fulfillment status and the total quantity of items via `num_of_item`.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]
*   **Order Item:** Refers to a single unit of a specific product within an order. This is the fundamental unit for computing metrics like revenue, margin, and units sold. For example, a single order containing two shirts and one hat would generate one order record and three distinct order item records.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]

## Pricing Metadata Fields

Accurate revenue calculations depend on specific pricing information:

*   **Cost:** The wholesale or landed cost paid by the company to the supplier for a unit. This is stored in `products.cost` and `inventory_items.cost` and is never exposed to customers.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]
*   **Retail Price:** The advertised catalog or list price for a product before any discounts are applied, stored as `products.retail_price`.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]
*   **Sale Price:** The actual price a customer pays for an item, recorded on the transaction line as `order_items.sale_price`. This is the definitive figure for realized revenue and may differ from the retail price due to promotions or markdowns.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]

## Related Metadata

Additional metadata provides context for revenue analysis:

*   **Product Taxonomy:** Products are structured into a three-level hierarchy: `Department` (broadest, e.g., Men, Women), `Category` (e.g., Jeans, Outerwear), and `Brand` (manufacturer/label).
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]
*   **Geography:** Each product is associated with a `Distribution Center` via `products.distribution_center_id`, which includes names and geographical coordinates for shipping optimization.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]
*   **Marketing & Customer Acquisition:** Users are linked to a `Traffic Source` (e.g., Search, Organic, Email, Display, Facebook) stored on `users.traffic_source`, which is crucial for channel-attribution analysis related to customer acquisition costs and revenue generation.
    [[business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)]

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)
*   [business_glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)

# Average Order Value Overview

Average Order Value (AOV), also known as AOV, is an analytical metric that quantifies the average value of each order, excluding cancellations. It is calculated by normalizing the gross revenue by the distinct count of orders.

## Definition and Calculation

Average Order Value represents the total Gross Revenue divided by the number of unique orders from which cancelled items have been excluded.

The formula for Average Order Value is given by:

$$\text{AOV} = \frac{\sum(\text{order\_items.sale\_price})}{\text{COUNT(DISTINCT order\_items.order\_id)}} \quad \text{where status} \neq \text{'Cancelled'}$$

## Key Components

The calculation of Average Order Value relies on the following data elements and derived metrics:

*   **Gross Revenue**: This is the sum of `sale_price` for all items in `order_items` where their `status` is not 'Cancelled'.
    $$\text{Gross Revenue} = \sum (\text{order\_items.sale\_price}) \quad \text{where status} \neq \text{'Cancelled'}$$
*   **`order_items.sale_price`**: Represents the monetary value of an individual item within an order. This is summed to calculate the gross revenue component.
*   **`order_items.order_id`**: Used to count the distinct number of orders. Each unique `order_id` represents a single order.
*   **`status`**: An attribute of `order_items` used to filter out cancelled items. Only items with a `status` other than 'Cancelled' are included in both the sum of `sale_price` and the distinct count of `order_id`.

## Source References

*   [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

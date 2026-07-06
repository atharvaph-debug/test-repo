# Return Rate Overview

Return Rate is an analytical metric that quantifies the proportion of non-cancelled items that were returned. It provides insight into the efficiency of sales and the impact of product returns on the business.

## Definition and Calculation

The Return Rate is calculated as the ratio of the number of returned items to the total number of non-cancelled items. This metric specifically excludes items that were cancelled, focusing only on those that were part of an initial sale attempt.

The formula for Return Rate is:
$$\text{Return Rate} = \frac{\text{COUNT}(\text{order\_items.id where returned\_at is not null})}{\text{COUNT}(\text{order\_items.id where status} \neq \text{'Cancelled'})}$$

In this calculation:
*   The **numerator** represents the count of individual order items (`order_items.id`) that have a `returned_at` timestamp, indicating they have been returned.
*   The **denominator** represents the total count of individual order items (`order_items.id`) where their `status` is not 'Cancelled'. This establishes the baseline of items that were initially sold and not cancelled.

## Related Metrics

The concept of 'returned' items also influences other analytical metrics:
*   **Gross Revenue** and **Units Sold** both consider only non-cancelled items, similar to the denominator of the Return Rate.
*   **Net Revenue** specifically excludes both cancelled and returned items, showing a direct relationship by contrasting with metrics that only exclude cancellations.

## Source References
* [metrics.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BC34B10B9-95D8-4E96-9EF7-5AB91CFBB753%7D&file=metrics.docx&action=default&mobileredirect=true)

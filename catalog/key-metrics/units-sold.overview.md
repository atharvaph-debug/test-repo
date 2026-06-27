# Units Sold Overview

Units Sold represents the total count of individual product units purchased by customers, specifically excluding any cancelled items. This metric quantifies the volume of products moved through sales.

## Definition and Calculation

Units Sold is calculated by counting the unique identifiers of order items (`order_items.id`) where the item's status is not `Cancelled`. This ensures that only successfully transacted units contribute to the total.

The formula for Units Sold is:
```sql
COUNT(order_items.id) WHERE status <> 'Cancelled'
```

This metric uses `Order Item` as the grain for its calculation, meaning each distinct product unit within an order is counted individually.

## Related Concepts

*   **Order Item:** A single unit of a single product within an order. This is the fundamental unit for all units-sold calculations.
*   **Return Rate:** Units Sold is used as the denominator in calculating the Return Rate, which is defined as `Returned units / sold units`.

## Source References
* [theLook eCommerce — Metric Definitions](1pVOj6ZQvZYFY3Udclcot2dJEW2Ncwoaw12ibxEWKETs)
* [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)

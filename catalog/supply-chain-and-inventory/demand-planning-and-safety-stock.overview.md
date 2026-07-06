# Demand Planning & Safety Stock Overview

Demand Planning & Safety Stock refers to the strategic calculations and stock buffering targets implemented to protect inventory availability against potential delivery delays and spikes in consumer demand. This critical aspect of supply chain management ensures resilience and mitigates the risk of stockouts.

## Key Concepts

### Safety Stock
Safety stock functions as a protective buffer, maintained at a level above the base forecast. Its primary purpose is to absorb sudden increases in demand and unexpected delays in inbound shipments. A key risk factor highlighted is that failing to dynamically size safety stock according to current demand variability can lead to inventory "near-misses."

### Reorder Point (ROP)
The Reorder Point (ROP) is a specific on-hand inventory level that, when reached, triggers a replenishment order for a given Stock Keeping Unit (SKU). The formula for calculating the Reorder Point is:

$$\text{ROP} = (\text{average daily demand} \times \text{lead time in days}) + \text{safety stock}$$

### Class-A Stock Policy
Following a Q3 apparel stockout incident caused by undersized safety stock bounds, the safety stock policy for Class-A items was updated. It was raised to **21 days of supply** to accurately reflect current-year demand variability, thereby superseding previous figures detailed in the Inventory Policy Memo.

## Source References
* [Demand Planning — Weekly Sync Notes](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8486956)
* [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
* [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)

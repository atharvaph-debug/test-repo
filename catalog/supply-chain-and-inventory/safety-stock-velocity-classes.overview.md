# Safety Stock Velocity Classes Overview

Safety Stock Velocity Classes categorize days-of-supply buffer policies across different priority tiers. These policies are managed to prevent inventory stockouts by protecting against demand and replenishment volatility. This classification helps in defining the default and overridden safety stock levels for different inventory items.

## Key Features

Safety Stock Velocity Classes are used to define the days-of-supply buffer maintained for inventory. There are three primary classes:

*   **Class A (Fast Movers):** The default policy memo specifies 14 days of supply for this class. However, due to documented Q3 apparel stockouts, this parameter was overridden and raised to **21 days of supply** to account for rising demand variability.
*   **Class B:** The default policy for Class B is 10 days of supply.
*   **Class C:** The default policy for Class C is 7 days of supply.

These classes are also known by the aliases "Class A", "Class B", and "Class C".

## Source References

*   [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
*   [Postmortem: Q3 Apparel Class-A Stockouts](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585237)

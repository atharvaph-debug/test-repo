# Reorder Point Overview

The Reorder Point (ROP), also known as rop, is a critical inventory level threshold that initiates automated replenishment processes. It represents the specific inventory quantity at which a new order must be placed to avoid stockouts.

## Definition and Purpose

The Reorder Point is an inventory level that triggers automatic replenishment. When a Stock Keeping Unit (SKU)'s on-hand inventory position drops to its designated reorder point, the planning system initiates a purchase requisition. This mechanism ensures that replenishment is entirely demand-driven.

## Calculation Formula

The Reorder Point is mathematically defined as the sum of safety stock and the demand expected over the lead time. More specifically, the inventory reorder threshold is formulated as:

$$ROP = (\text{average daily demand} \times \text{lead time in days}) + \text{safety stock}$$

This can also be expressed as:

$$\text{Reorder Point} = \text{Safety Stock} + \text{Demand over Lead Time}$$

## Operational Management

To prevent direct manual adjustments to the Reorder Point, operational processes dictate that changes to the **Safety Stock** parameter will programmatically shift the dependent Reorder Point. This makes Safety Stock a key control parameter for managing ROP.

## Role in Procurement

Upon reaching the designated Reorder Point, the planning system triggers a purchase requisition. For manufactured products, this requisition is automatically "exploded" against the product’s Bill of Materials (BOM) to determine the necessary component requirements.

## Source References

*   [Demand Planning — Weekly Sync Notes](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8486956)
*   [Inventory Policy Memo](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8650773)
*   [Procurement Standard Operating Procedure](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/9043969)

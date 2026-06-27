# Sale Price Overview

The **Sale Price** represents the actual price paid by a customer for a single unit of an item. It is a critical metric for financial tracking and is the basis for all revenue calculations within the system.

## Key Features

*   **Definition:** Sale Price is the final amount a customer pays for an item, distinguishing it from the advertised `Retail Price` (`products.retail_price`) or the company's `Cost` (`products.cost`).
*   **Data Location:** This value is recorded in the `order_items.sale_price` field.
*   **Purpose:** It is explicitly used for calculating revenue, making it fundamental to understanding sales performance and financial outcomes. Each "Order Item" represents a single unit of a product within an order, serving as the grain for these calculations.

## Source References

*   [theLook eCommerce — Business Glossary](1-eJsLFIxSetKfyTwhU3mtQLNHwdEjKfMqGgzytYomDw)

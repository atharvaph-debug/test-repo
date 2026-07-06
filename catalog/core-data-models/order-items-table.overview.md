# Order Items Table Overview

The `Order Items Table` (also known as `order_items`) serves as the central fact table for transactional revenue calculations, tracking sold units at the order-line level, also referred to as the order item grain.

## Key Features

This table represents individual items within a customer's order, providing detailed information about each sold unit. It is crucial for understanding realized revenue and item-level fulfillment statuses.

## Schema and Relationships

The `Order Items Table` links to several other core data models through foreign keys:
*   `order_items.order_id` connects to the `orders` table, which represents the overall checkout event.
*   `order_items.user_id` links to the `users` table, identifying the individual customer.
*   `order_items.product_id` associates with the `products` table, detailing the specific sellable stock-keeping unit (SKU).
*   `order_items.inventory_item_id` relates to the `inventory_items` table, representing the physical unit of stock that was sold.

### Key Columns

*   **`sale_price`**: This column documents the actual realized transaction amount paid by the customer. It is the authoritative column for all realized revenue calculations.
*   **`status`**: This column indicates the current lifecycle stage of an individual order item. Its values can include:
    *   **Processing**: The order item has been submitted and payment captured, but fulfillment has not started.
    *   **Shipped**: The parcel containing this item has departed a distribution center.
    *   **Complete**: The shipment including this item has been delivered successfully, and the return eligibility window has closed.
    *   **Returned**: The item was returned by the customer.
    *   **Cancelled**: The item was cancelled before warehouse fulfillment occurred, generating zero revenue for this specific item.

## Discrepancy Handling

It is important to note that `order_items.status` may differ from the `orders.status` of its parent order, as orders can be partially fulfilled or partially returned. For instance, an order might be `Complete` while a single line-item within it is `Returned`. When item-level precision is required for fulfillment and return metrics, all calculations should be derived directly from `order_items.status`.

## Source References
*   [data_model.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B423E5830-5F28-4962-A091-FC1A61A25899%7D&file=data_model.docx&action=default&mobileredirect=true)
*   [theLook eCommerce Business Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2D911FEB-A467-42E5-BBAD-05F55BDB02F2%7D&file=business_glossary.docx&action=default&mobileredirect=true)
*   [theLook eCommerce — Order Lifecycle and Status](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B45B111CA-405B-4917-AAC3-8EED2EB6786C%7D&file=order_lifecycle.docx&action=default&mobileredirect=true)

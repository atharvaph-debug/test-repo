# Supply Chain & Inventory Metadata

Identifiers, metrics, and replenishment policies used to map physical items and optimize inventory holding levels.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/supply-chain-and-inventory-metadata/bill-of-materials | Bill of Materials | file | The hierarchical multi-level engineering specification recipe that links a finished-good SKU to its component materials and sub-assemblies. |
| catalog/supply-chain-and-inventory-metadata/reorder-point | Reorder Point | file | The configured inventory level calculated using daily demand, lead times, and safety stock that triggers automatic replenishment purchase orders. |
| catalog/supply-chain-and-inventory-metadata/safety-stock | Safety Stock | file | The buffer inventory held to mitigate demand volatility and supply chain delays, dynamically sized based on SKU velocity class. |
| catalog/supply-chain-and-inventory-metadata/stock-keeping-unit | Stock Keeping Unit | file | The granular internal identifier used to track, forecast, and reconcile distinct, sellable product variants. |

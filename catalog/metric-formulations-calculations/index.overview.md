# Metric Formulations & Calculations

Analytical business intelligence metrics formulated on warehouse transactional logs.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/metric-formulations-calculations/average-order-value | Average Order Value | file | Gross revenue divided by the unique count of orders, excluding cancellations. |
| catalog/metric-formulations-calculations/gross-revenue | Gross Revenue | file | Sum of sales price excluding any transactions where the status is cancelled. |
| catalog/metric-formulations-calculations/net-revenue | Net Revenue | file | Sum of sales price excluding both cancelled and returned transactions. |
| catalog/metric-formulations-calculations/units-sold | Units Sold | file | Total count of order item-level lines processed, excluding cancelled orders. |

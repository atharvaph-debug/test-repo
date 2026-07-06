# Rating and Billing States Overview

Rating and Billing States describe the operational stages involved in mapping customer price plans to network usage events and subsequently aggregating these into validated, reconciled invoices throughout active billing cycles. This process covers two main phases: Rating State and Billing State.

## Key Concepts

### Rating State
The **Rating State** is a conceptual phase focused on calculating a monetary charge. During this phase, a customer’s assigned price plan is applied to raw, incoming network usage events to determine the cost.

### Billing State
The **Billing State** phase involves aggregating the charges computed during the Rating State. These rated charges are collected over a predefined, recurring "billing cycle" to ultimately produce a clean, reconciled invoice at the close of each cycle.

## Invoicing Controls
Several controls are in place to manage the invoicing process within the Billing State:

*   **Staggering:** To distribute the system load evenly throughout the month, billing cycle boundaries are staggered across the customer base.
*   **Reconciliation:** Before invoices are issued, all rated charges undergo a reconciliation process against the final invoice total. Any discrepancies detected during this reconciliation are put on hold for manual review, preventing incorrect charges from being processed.

## Source References
*   [Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)

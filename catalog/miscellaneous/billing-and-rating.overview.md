# Billing and Rating Overview

Billing and Rating describes the two-step operational process where raw usage events are first rated using defined tariff prices and then subsequently billed on a recurring cycle basis. This process is fundamental for converting service consumption into financial charges and is a key component of metadata enrichment for subscriber services.

## Operational Phases

The charging system performs two distinct phases to convert usage events into billable amounts:

*   **Rating:** This initial phase involves applying a subscriber's specific price plan to individual raw usage events to calculate the associated charges.
*   **Billing:** Following rating, this phase aggregates all rated charges over a defined recurring billing cycle to generate a comprehensive invoice for the subscriber.

## Cycle Management

Billing cycles are managed differently based on the subscriber's plan type and are strategically staggered to optimize system performance:

*   **Postpaid Plans:** Usage accumulates throughout the billing cycle, and subscribers are billed in arrears.
*   **Prepaid Plans:** Balances are decremented in real time as usage occurs, with the billing cycle primarily defining allowances.
*   **Staggered Cycles:** To distribute the invoicing processing load evenly across the month, billing cycle boundaries are staggered across the entire subscriber base.

## Data Interactions and Reconciliation

The Billing and Rating process involves critical data interactions and reconciliation steps:

*   **QoS Integration:** The charging system interacts with network policy functions. For example, if a subscriber crosses their data threshold, the charging system signals the policy function to move their traffic to a lower-priority Quality of Service (QoS) class (throttling), rather than cutting service entirely.
*   **Reconciliation:** After charges are rated, they undergo an audit and reconciliation process against the final invoice totals before being issued. Any discrepancies found during this reconciliation result in invoices being held for manual review by Billing Operations, preventing them from being sent to subscribers until resolved.

## Source References
*   [Copy of Billing Charging System Overview](1GPtX16AkNHHRYrkUk87lsfDHuMLXYVcVV3RycBtHexE)
*   [Copy of Customer Care Handbook](1mGNA1aQHvYEJS6N1cmr5N3nkTkZ8fX7Hjz-IvFOd_3o)

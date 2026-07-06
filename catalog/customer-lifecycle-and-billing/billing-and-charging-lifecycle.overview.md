# Billing and Charging Lifecycle Overview

The Billing and Charging Lifecycle, also referred to as rating, billing, or throttling, describes the end-to-end process of transforming raw usage data into priced, rated events and subsequently aggregating these events into invoice cycles. This lifecycle also incorporates balance-driven Quality of Service (QoS) throttling policies. It is a critical component of customer lifecycle management and billing operations.

## Key Concepts and Processes

The billing and charging lifecycle encompasses several distinct stages and policies:

*   **Rating vs. Billing:** This process is divided into two main stages:
    *   **Rating:** Applying a defined price plan to a raw usage event (e.g., data consumption, call duration) to calculate its associated cost.
    *   **Billing:** Aggregating these rated charges over a specific cycle duration to produce a customer invoice.
*   **Postpaid vs. Prepaid Cycles:** The system differentiates between customer payment models:
    *   **Postpaid Customers:** These customers pay for services in arrears, meaning they are billed after the usage cycle has concluded.
    *   **Prepaid Plans:** For prepaid services, customer balances are decremented in real time as usage occurs. While cycles exist, their primary function is to reset plan allowances rather than to generate retrospective invoices.
*   **Cycle Staggering:** Customer billing cycles are strategically staggered across the entire customer base. This operational practice aims to distribute the processing load on invoicing systems evenly throughout the month, preventing peak demand and ensuring system stability.
*   **QoS "Throttling" Policy:** Data plans can incorporate policies that link Quality of Service (QoS) to charging thresholds. When a customer's data limit is reached, the billing system signals a policy function. Instead of completely cutting off access, this function downgrades the subscriber to a lower-priority QoS class, a process commonly known as "throttling."

## Source References

*   [Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)
*   [Customer Care Handbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552469)

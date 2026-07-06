# Account Billing Mechanics Overview

Account Billing Mechanics define the logic governing real-time account updates and actions taken during a billing cycle, encompassing balance reductions, deferred payments, and Quality of Service (QoS) throttling loops. This entry, also referred to by aliases such as prepaid-accounts, postpaid-accounts, and charging-to-qos-policy-feedback-loops, describes the processes that convert subscriber activity into financial statements within the broader Revenue Lifecycle and Billing Metadata domain.

## Key Concepts

### Prepaid vs. Postpaid Account Mechanics
The system distinguishes between two primary account types:
*   **Postpaid Accounts:** Customers incur usage first and are billed in arrears. Usage metrics accumulate over an active billing cycle, leading to an invoice at the cycle's conclusion [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)].
*   **Prepaid Accounts:** Balances are reduced in real time as usage occurs. For prepaid models, the "cycle" denotes an active window for resetting plan allowances rather than an invoice period [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)].

### Rating and Billing States
The financial conversion of subscriber activity occurs in distinct conceptual phases:
*   **Rating State:** This phase maps a customer's assigned price plan (a form of metadata) to incoming network usage events to calculate a monetary charge [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)].
*   **Billing State:** This phase aggregates the rated charges over a predefined, recurring "billing cycle" to produce a reconciled invoice at the end of the cycle [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)].
    *   **Invoicing Controls:** To manage system load, billing cycle boundaries are staggered across the customer base. Prior to issuance, rated charges are reconciled against the final invoice total, with any discrepancies flagged for manual review [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)].

### Charging-to-QoS Policy Feedback Loops
This mechanism links usage-based charging with network quality of service:
*   **Throttling Loops:** For certain data plans, physical data allowances are directly tied to QoS classifications. When a subscriber, whether prepaid or postpaid, exceeds a specific usage threshold, the charging system signals the policy function [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681]].
*   **Execution:** Instead of terminating the connection, the policy engine downgrades the subscriber's session to a lower-priority QoS class, a process known as "throttling," for the remainder of the billing cycle [[Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681]]. This dynamic adjustment of QoS classification acts as a metadata update triggered by billing conditions.

## Source References
*   [Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)

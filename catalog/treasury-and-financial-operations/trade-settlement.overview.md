# Trade Settlement Overview

Trade Settlement is the critical process that finalizes a trade, ensuring the exchange of the buyer's cash for the seller's securities, thereby discharging both parties' obligations. A trade is considered economically complete only after settlement; prior to this, it remains a pending obligation with associated counterparty risk. This process is heavily reliant on specific daily cutoffs.

## Definition

Settlement is defined as the final stage of a trade where the actual transfer of cash and securities occurs between parties. This act concludes the transaction, moving it from a pending obligation to an economically complete event.

## Settlement Cutoff Times

Effective trade settlement depends on strict adherence to established cutoff times, which require system schedules and pipeline metadata to be accurately aligned with market infrastructure constraints to prevent settlement exposure and operational mismatches.

*   **Market Infrastructure Cutoff**: The strict daily cutoff for trade settlement processing is **16:00 ET**. Instructions matched before this time are processed in the current day's run, while those received after roll over to the next business day's settlement cycle.
*   **Current Operational Target**: The internal operational target for system processing is **15:30 ET**. This earlier target aims to ensure trades are submitted well in advance of the strict market cutoff.
*   **Legacy System Target**: Historically, some internal system processing schedules relied on a **16:00 ET** target. However, this is now considered a legacy approach for internal systems.
*   **Impact of Discrepancy**: If system processing schedules or operational runbooks are out of sync with upstream market infrastructure limits (e.g., relying on the legacy 16:00 ET for internal processing), trade settlement may slide to the next business day ($T+2$ execution window), introducing unanticipated settlement risk and operational errors.
*   **Warning Window**: System metadata rules should flag trade processing that approaches the **15:15 ET** warning window, allowing time to address potential delays before the operational target or strict market cutoff.

## Settlement Cycle

Equities and most fixed-income instruments settle on a **T+1 basis**, meaning one business day after the trade date. This calendar is extended accordingly for weekend and holiday schedules.

## Operational Process

To ensure timely settlement, daily operations involve a checklist of activities:
1.  Confirming that trades captured overnight are matched with counterparties.
2.  Resolving any unmatched or affirmed exceptions well before the cutoff.
3.  Releasing the settlement batch prior to **16:00 ET**.
4.  Reconciling settled positions at the end of the day and investigating any settlement fails, escalating persistent issues to the Settlements Lead.

## Source References

*   [Postmortem: Settlement Cutoff Migration Delay](1SsgbjuwQKjwAQHcXoTBiOPKJg9sZAtIHntksCJsCVf8)
*   [Copy of Trade Ops Runbook](1DItkIvyGbrC1vPDIKxuKP0_qBnC1ShzTYoxsgKWSuSk)
*   [Copy of Treasury Operations Guide](1kXDYTun6V0lc4d83F_HS1g-L6G_iTsTFt6eoYnTGtwA)

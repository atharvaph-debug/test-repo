# Settlement Cutoff Time Overview

The Settlement Cutoff Time defines the strict daily deadline that determines whether a trade settlement executes on the same day or rolls over to the next business day. This critical operational parameter is essential for managing counterparty risk and ensuring timely financial operations.

## Key Features

*   **Definition**: The Settlement Cutoff Time is the absolute processing deadline by which trade instructions must be matched and received to be included in the same-day settlement batch. Instructions that arrive after this time are automatically deferred to the next business day's settlement cycle.
*   **T+1 Settlement Standard**: Financial instruments, including equities and most fixed-income instruments, typically operate on a T+1 (Trade Date plus one business day) settlement basis, meaning settlement occurs one business day after the trade date, with adjustments for weekends and holidays. The daily cutoff time determines which trades meet the "Trade Date" requirement for same-day processing in relation to the T+1 cycle.
*   **Cutoff Time Changes and Impact**:
    *   Historically or generally, the daily settlement cutoff was set at **16:00 ET**. Instructions received before this time would execute in the same-day batch, while those after would roll to the next business day, introducing an extra day of counterparty risk.
    *   With a transition to a new settlement platform, the authoritative cutoff time was revised and moved from the legacy **16:00 ET** to **15:30 ET** to align with upstream market infrastructure.
    *   Failure to update this metadata in operational runbooks, such as the *Trade Operations Runbook*, has led to delayed settlements, resulting in unexpected overnight exposure and client inquiries.
*   **Metadata Alignment and Automation**: Operational runbooks must be synchronized with the current **15:30 ET** cutoff. To support this, automated platform alerts are configured to trigger at **15:15 ET**, providing a buffer before the final deadline.
*   **Operational Procedure**: Releasing the settlement batch prior to the daily cutoff time is a key step in the daily settlement checklist.

## Aliases

*   daily-settlement-cutoff

## Source References

*   [Copy of Postmortem: Settlement Cutoff Migration Delay](1SsgbjuwQKjwAQHcXoTBiOPKJg9sZAtIHntksCJsCVf8)
*   [Copy of Treasury Operations Guide](1kXDYTun6V0lc4d83F_HS1g-L6G_iTsTFt6eoYnTGtwA)
*   [Copy of Trade Ops Runbook](1DItkIvyGbrC1vPDIKxuKP0_qBnC1ShzTYoxsgKWSuSk)

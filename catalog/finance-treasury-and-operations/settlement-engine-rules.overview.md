# Settlement Engine Rules Overview

Settlement Engine Rules define the temporal and systemic guidelines for trade clearing, managing various transition stages, and establishing cutoff thresholds, all operating on a T+1 cycle. These rules are crucial for ensuring the timely and accurate exchange of cash and securities, and for managing counterparty risk.

## Key Features and Definitions

### Settlement Standard (T+1)
Most equities and fixed-income instruments adhere to a T+1 settlement standard. This means that settlement, the process where cash and securities officially exchange hands, occurs one business day after the trade date. The calendar for settlement must account for weekends and holidays, extending the settlement period accordingly.

### Economic Completeness Status
A trade's status regarding economic completeness indicates its progression through the settlement process:
*   **Pending Obligation:** Before settlement is complete, a trade is marked as "pending obligation carrying counterparty risk." In this state, neither the cash nor the securities have been exchanged, and both parties still bear the risk associated with the trade.
*   **Economically Complete:** A trade achieves this status once settlement fully completes, signifying that the cash and securities have been successfully exchanged between the counterparties, and the associated counterparty risk is resolved.

### Daily Settlement Cutoff
A critical daily cutoff is established for processing trade instructions:
*   **16:00 ET:** This is the daily cutoff time for settlement instructions.
*   **Before 16:00 ET:** Instructions received and successfully matched before 4:00 PM ET are included in that day's settlement run.
*   **After 16:00 ET:** Instructions received after 4:00 PM ET will not be processed until the next business day's settlement cycle. This delay introduces an extra day of settlement risk for the trade.

## Source References
*   [Primary Source Document](1SsgbjuwQKjwAQHcXoTBiOPKJg9sZAtIHntksCJsCVf8)
*   [Copy of Treasury Operations Guide](1kXDYTun6V0lc4d83F_HS1g-L6G_iTsTFd6eoYnTGtwA)
*   [Copy of Trade Ops Runbook](1DItkIvyGbrC1vPDIKxuKP0_qBnC1ShzTYoxsgKWSuSk)

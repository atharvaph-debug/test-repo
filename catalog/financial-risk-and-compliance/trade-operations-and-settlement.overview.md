# Trade Operations and Settlement Overview

Trade Operations and Settlement define the standard guidelines, cutoff times, and workflows governing the clearing and settlement of equities and fixed-income trades. This process is also referred to as "t-plus-one" or "settlement-cutoff" in some contexts, and its definitions contribute to metadata enrichment efforts for financial operations.

## Key Features

### Settlement Timeline
Equities and most fixed-income instruments settle on a **T+1** basis, meaning one business day after the trade execution date. This timeline is extended accordingly by weekends and official holidays.

### Operational Cutoffs
Inclusion of trade execution in a daily settlement run is governed by a strict cutoff schedule.
*   Clearing and settlement analysts previously operated under a standing daily cutoff of **16:00 ET**.
*   Due to platform migrations, this operational window has shifted to **15:30 ET**.
*   Trades executed after the daily cutoff are pushed to the subsequent settlement batch. Discrepancies between physical platform migrations and outdated operational documentation can lead to processing delays if legacy runbooks are not updated.

## Source References
*   [Trade Operations Runbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8486936)
*   [Postmortem: Settlement Cutoff Migration Delay](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8880149)

# T+1 Settlement Cutoff Overview

The T+1 Settlement Cutoff refers to the operational daily deadline established to ensure that trades are included in the same-day settlement run for T+1 settlement. This critical cutoff time dictates whether capital market trades will settle one business day after the trade date, accounting for weekends and holidays. The accuracy of this metadata is crucial to prevent operational issues.

## Aliases
This entry may also be referred to as `settlement-cutoff-time` or `trade-settlement-cutoff`.

## Key Features

*   **T+1 Settlement Standard**: Capital market trades adhere to a strict T+1 basis, meaning they settle one business day after the trade date. Weekends and holidays can extend this settlement window.
*   **Operational Deadline**: The official operational deadline for trade settlement was initially set at 16:00 ET.
*   **Revised Cutoff**: Due to migrations to updated settlement platforms enforcing tighter processing windows, the trade settlement cutoff was revised to 15:30 ET. A postmortem analysis identified that outdated runbook references to the previous 16:00 ET cutoff led to missed trade batches, underscoring the importance of accurate metadata for workflow cutoff times.
*   **Purpose**: Adhering to this cutoff ensures same-day inclusion in the T+1 settlement run, which is vital for efficient trade operations.

## Source References
*   [Copy of Settlement Delay Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B086408F1-5359-45D7-B65D-F2AE2B1FC816%7D&file=Copy%20of%20Settlement%20Delay%20Postmortem.docx&action=default&mobileredirect=true)
*   [Copy of Trade Ops Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B466897B0-B0B2-47E3-8E5C-E72454C0D2E7%7D&file=Copy%20of%20Trade%20Ops%20Runbook.docx&action=default&mobileredirect=true)

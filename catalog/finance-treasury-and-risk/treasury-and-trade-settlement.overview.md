# Treasury and Trade Settlement Overview

This entry describes key treasury controls and trade settlement processes, including regulatory requirements like the Liquidity Coverage Ratio (LCR), financial performance indicators such as Net Interest Margin (NIM), and critical operational deadlines for trade clearing under the T+1 settlement window. It encompasses metadata related to these financial operations and their associated constraints.

## Key Financial Metrics and Controls

### Liquidity Coverage Ratio (LCR)

The Liquidity Coverage Ratio (LCR) is a short-term liquidity standard governed by the Basel III frameworks. It is defined by the formula:

$$\text{LCR} = \frac{\text{High-Quality Liquid Assets (HQLA)}}{\text{Total Net Cash Outflows over 30 days}}$$

or equivalently,
$$\text{LCR} = \frac{\text{HQLA (High-Quality Liquid Assets)}}{\text{Projected Net Cash Outflows over 30-day stress period}}$$

Key aspects of the LCR include:
*   **Regulatory Minimum**: The mandatory minimum ratio is **100%**. This ratio must never drop below 100%, even intraday on reporting dates. Any breach requires immediate escalation to Regulatory Reporting and Treasury leads.
*   **Internal Management Target**: The internal target is **110%**, set as a buffer above regulatory baselines to absorb business fluctuations without breaching compliance boundaries. This target is maintained to provide headroom above the regulatory minimum.
*   **Asset Tiers**: Asset tiers (Level 1 and Level 2) undergo standardized haircuts.

### Net Interest Margin (NIM)

Net Interest Margin (NIM) measures the net yield generated on the interest-bearing portfolio. It is evaluated daily to track asset/liability rate sensitivities. The formula for NIM is:

$$\text{NIM} = \frac{\text{Net Interest Income}}{\text{Average Interest-Earning Assets}}$$

This can also be expressed as:

$$\text{NIM} = \frac{\text{Interest Income} - \text{Interest Expense}}{\text{Average Earning Assets}}$$

## Trade Settlement Deadlines

### T+1 Settlement Window

In-scope trades require instructions to be matched and released by the daily system cutoff to settle on T+1. Trade clearing carries counterparty risk until settled. Equities and fixed-income trades operate on a T+1 settlement cycle.

### Daily Cutoff Times

Daily settlement instructions must be matched and released before strict cutoff times to avoid sliding into the next business day's batch. Following migration to a new processing platform, the active cutoff time has been modified:
*   **Legacy Cutoff**: 16:00 ET
*   **Current Platform Cutoff**: **15:30 ET**. This supersedes any legacy times documented in the Trade Operations Runbook.

## Related Financial Metric Distinctions

It is important to distinguish between related financial risk metrics:
*   **Credit Risk Score**: Evaluates default likelihood based on exposure, income, leverage, and repayment behavior.
*   **KYC Risk Rating**: Measures financial-crime risk profiles.

**Metadata Warning**: These are distinct measures. Credit scoring engines must not run on KYC validation variables, nor vice-versa, to ensure appropriate risk assessment.

## Source References

*   [Basel III Regulatory Minimums](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B091DEE28-85D7-479A-B4D6-EB0F98977078%7D&file=Copy%20of%20Basel%20III%20Filing%20Summary.docx&action=default&mobileredirect=true)
*   [Financial Metric Definition Mappings](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)
*   [Liquidity Risk Control Metrics](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BD5920DFD-0CA5-4A3C-8333-4EC7FE7114F9%7D&file=Copy%20of%20Risk%20Management%20Framework.docx&action=default&mobileredirect=true)
*   [Trade Settlement Cutoff Constraints](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B086408F1-5359-45D7-B65D-F2AE2B1FC816%7D&file=Copy%20of%20Settlement%20Delay%20Postmortem.docx&action=default&mobileredirect=true)
*   [Financial & Treasury Operations](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BDDA00735-3CD1-426F-B72A-919A5A59156C%7D&file=Copy%20of%20Treasury%20Operations%20Guide.docx&action=default&mobileredirect=true)
*   [Trade Settlements & Deadlines](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B466897B0-B0B2-47E3-8E5C-E72454C0D2E7%7D&file=Copy%20of%20Trade%20Ops%20Runbook.docx&action=default&mobileredirect=true)

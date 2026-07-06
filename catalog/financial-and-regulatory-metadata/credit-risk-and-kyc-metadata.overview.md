# Credit Risk and KYC Metadata Overview

Credit Risk and KYC Metadata define distinct customer risk profiles, differentiating default probabilities from financial-crime and money laundering risk ratings. These profiles serve as critical structural metadata on customer records, enabling robust metadata enrichment for various downstream financial processes and regulatory compliance.

## Key Concepts and Definitions

This entry encompasses two primary, distinct metadata types:

*   **KYC Risk Rating**: This metadata categorizes customers into bands, such as standard or enhanced due diligence (EDD), to assess their financial-crime risk. This categorization is established during **KYC Profile Creation**, a mandatory step for every new customer account, where Know Your Customer (KYC) / Customer Due Diligence (CDD) verification is completed. Activating an account without prior KYC verification is considered a critical process error. For non-individual customers, establishing beneficial ownership is also required.
*   **Credit Risk Score**: This metadata quantifies the likelihood of a borrower defaulting on their obligations. It is derived from factors such as repayment history, existing exposure, income, and leverage. The Credit Risk Score is used to determine pricing limits and credit terms.

It is a critical distinction that financial-crime risk metadata (KYC Risk Rating) and credit-risk metadata (Credit Risk Score) serve distinct purposes and must not be confused. The KYC Risk Rating specifically measures financial-crime risk, while the Credit Risk Score measures credit default risk.

## Metadata Enrichment and Persistence

Both the KYC Risk Rating and Credit Risk Score are persisted as structural metadata on the customer's profile. This persistence is crucial for guiding subsequent operations and ensuring the accuracy and context of financial data.

## Downstream Application

These metadata elements are leveraged across various operational and analytical functions:

*   **Monitoring and Underwriting**: They guide downstream monitoring, servicing, and manual underwriting processes.
*   **Transaction Monitoring**: Ongoing transaction monitoring is risk-based, utilizing the customer's KYC profile and assigned risk rating to detect deviations from expected behaviors, such as unusual volumes, structuring patterns, or inconsistent fund movements.
*   **AML Alert Investigations**: During anti-money laundering (AML) investigations, investigators pull the KYC file to evaluate the customer's identity, expected activity, and risk rating. Stale KYC metadata in these processes automatically triggers a profile refresh to ensure accuracy.
*   **Risk Management and Provisioning**: Individual Credit Risk Scores are aggregated to feed expected-loss provisioning models and serve as key portfolio health metrics for overall risk management.

## Regulatory and Operational Constraints

Metadata related to financial crime investigations is subject to strict regulatory constraints:

*   **Confidentiality (No Tipping Off)**: Customer-facing metadata or accounts must under no circumstances indicate that a Suspicious Activity Report (SAR) is contemplated or has been filed.
*   **Time-Bounded Window**: The regulatory filing window for a SAR begins immediately once suspicion is established.

## Source References

*   Compliance Policy Handbook
*   Customer Onboarding SOP
*   Finance Business Glossary
*   AML Investigations Playbook
*   Risk Management Framework

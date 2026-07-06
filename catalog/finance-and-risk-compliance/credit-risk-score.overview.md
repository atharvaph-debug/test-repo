# Credit Risk Score Overview

The Credit Risk Score is a calculated estimate of borrower default risk generated from historical repayment schedules, leverage ratios, and outstanding exposure metrics. It serves as a critical piece of credit risk metadata, measuring default risk based on factors such as repayment history, exposure, income, and leverage.

## Key Features

*   **Definition and Calculation**: The Credit Risk Score is a quantified estimate of default probability built from repayment history, exposure, and leverage. It is a borrower-level metric estimating default likelihood, calculated using repayment history, current exposure, and income/leverage.
*   **Metadata Distinction**: It is crucial to distinguish credit risk metadata, such as the Credit Risk Score, which measures default risk, from financial-crime risk metadata like the Know Your Customer (KYC) risk rating. The KYC risk rating measures financial-crime and compliance risk. Both the Credit Risk Score and the KYC risk rating must reside as separate, distinct metadata attributes on the customer profile to guide downstream monitoring and servicing. Operational procedures specifically warn against confusing these two metadata types.
*   **Applications**:
    *   **Lending Decisions**: Used at origination to price and decide lending.
    *   **Risk Provisioning**: Aggregated to feed expected-loss provisioning.
    *   **Early Warning**: A deteriorating average score serves as an early portfolio warning indicator.

## Source References
*   Risk Management Framework
*   Finance Business Glossary
*   Customer Onboarding SOP

# Metadata Compliance Auditor Overview

The Metadata Compliance Auditor is an automated auditing tool designed to continuously scan metadata repositories. It audits corporate data and transactional metadata against compliance policies, financial controls, and corporate expense guidelines. Its primary function is to ensure that these repositories comply with both enterprise-specific standards and regulatory requirements.

## Category
This entry belongs to the `Financial and Regulatory Metadata` category.

## Key Responsibilities

The Metadata Compliance Auditor plays a critical role in ensuring data integrity and adherence to organizational policies and regulatory mandates by auditing various metadata points. Its responsibilities include:

*   **Corporate Expense Governance**: It verifies adherence to corporate travel and expense policies outlined in the `Corporate Travel & Expense Policy`. This includes auditing metadata related to:
    *   **Booking Channels**: Ensuring all travel (flights and hotels) is booked through approved corporate tools, flagging out-of-tool bookings for prior manager approval.
    *   **Flight Class Policies**: Verifying adherence to flight class standards, such as economy for flights under six hours, and requiring director-level sign-off for premium economy on longer flights.
    *   **Lodging and Meals**: Checking compliance with published per-city nightly caps for hotels and per-diem rates for meals.
    *   **Ground Transportation**: Confirming the use of standard ride-share or taxi services and strictly prohibiting luxury tiers.
*   **Financial Controls**: The Auditor examines financial control metadata, such as:
    *   **Expense Submission Timelines**: Ensuring expenses are submitted within 30 days of the spend date, and flagging submissions older than 60 days for exception approval.
    *   **Receipt Thresholds**: Verifying that itemized receipts are provided for expenses exceeding established corporate thresholds.
    *   **Corporate Card Governance**: Auditing against the mixing of personal expenses on corporate cards, requiring immediate flagging and reimbursement if accidental mixing occurs.
    *   **Approval Routing**: Ensuring correct routing of standard expense reports to direct managers and policy exceptions to both the direct manager and Finance Shared Services for secondary auditing.
*   **Regulatory Compliance**: The Auditor supports adherence to broader regulatory and financial metadata policies by cross-referencing information against defined standards, including:
    *   **KYC Profile Creation**: Verifying the completion of Know Your Customer (KYC) / Customer Due Diligence (CDD) verification for new customer accounts before activation, as per the `Customer Onboarding SOP`.
    *   **Risk Ratings**: Distinguishing between and ensuring correct application of KYC Risk Ratings (for financial-crime risk) and Credit Risk Scores (for borrower default probability) where applicable, as noted in the `Compliance Policy Handbook` and `Finance Business Glossary`.
    *   **Liquidity Coverage Ratio (LCR)**: Potentially verifying metadata related to the calculation and adherence to the regulatory minimums for LCR, as defined under Basel III regulations in the `Basel III Regulatory Filing — Internal Summary`.

## Source References
*   Basel III Regulatory Filing — Internal Summary
*   Compliance Policy Handbook
*   Corporate Travel & Expense Policy
*   Customer Onboarding SOP
*   Finance Business Glossary
*   Risk Management Framework
*   Treasury Operations Guide

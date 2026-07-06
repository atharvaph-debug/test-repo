# Customer Due Diligence Overview

Customer Due Diligence (CDD), also known interchangeably as Know Your Customer (KYC), is a localized process performed at customer onboarding and refreshed periodically to verify customer identity, establish beneficial ownership for non-individual customers, and evaluate initial financial-crime risk. This process is crucial for establishing a foundational risk profile for customers.

## Key Concepts and Process

Customer Due Diligence (CDD) involves several critical steps:
*   **Identity Verification**: Ensuring the customer's identity is verified through acceptable documents.
*   **Beneficial Ownership**: Establishing the beneficial owners for non-individual customers.
*   **Risk Rating Determination**: Assessing an initial financial-crime risk level for the customer.

The output of these processes is a **customer KYC risk rating**, which can be "standard" or "enhanced due diligence" Customer Onboarding SOP. This risk rating serves as a critical piece of metadata stored on the customer profile and forms the basis for all ongoing financial-crime monitoring Customer Onboarding SOP, Compliance Policy Handbook.

## Relationship with Financial-Crime Compliance

CDD is a cornerstone of an organization's Anti-Money Laundering (AML) framework. The KYC profile and risk rating, established through CDD, provide the expectations against which transaction monitoring controls analyze activity patterns Compliance Policy Handbook.

In the event of unusual activity flagged by transaction monitoring, investigators pull the KYC file to reconstruct the flow of funds AML Investigations Playbook. If this reconstruction establishes reasonable suspicion of illicit conduct, it can lead to the filing of a Suspicious Activity Report (SAR) [AML Investigations Playbook](gs://test-input-gcs-atharva/eval%20corpus/aml_investigations_playbook.

## Distinction from Credit Risk

It is critical to distinguish between a customer's financial-crime risk rating (derived from CDD/KYC) and their credit risk score.
*   **KYC Risk Rating**: Measures financial-crime risk.
*   **Credit Risk Score**: Quantifies a borrower's likelihood of default based on factors like income, leverage, and repayment history Customer Onboarding SOP, Finance Business Glossary.

These two metadata classifications must be tracked independently and remain distinct Finance Business Glossary.

## Source References
*   Customer Onboarding SOP
*   Compliance Policy Handbook
*   AML Investigations Playbook
*   Finance Business Glossary

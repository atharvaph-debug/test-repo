# Anti-Money Laundering Overview

Anti-Money Laundering (AML) refers to transaction monitoring systems and protocols designed to dynamically scrutinize behaviors based on customer compliance profiles. It forms a critical part of the compliance pipeline, following Know Your Customer (KYC) procedures and potentially leading to Suspicious Activity Report (SAR) generation.

## Key Features and Metadata Application

AML monitoring operates on a risk-based model, where its scrutiny is dynamically adjusted based on a customer's KYC profile and risk rating. The KYC risk rating serves as the foundational metadata for downstream monitoring efforts.

*   **KYC Risk Rating:** This metadata measures financial-crime risk and dictates the requirements for standard versus enhanced due diligence. It is established during customer onboarding and periodically updated. The KYC risk rating is a critical compliance metric and the metadata foundation for AML monitoring.
*   **Customer Metadata Distinction:** It is crucial for customer metadata to treat KYC Risk Rating and Credit Risk Score as distinct fields. Confusing default risk (quantified by Credit Risk Score) with compliance risk (quantified by KYC Risk Rating) is flagged as a common operational error.
*   **Metadata Freshness:** Stale KYC metadata is identified as a finding in active investigations, highlighting the necessity of up-to-date customer compliance profiles for effective AML.
*   **SAR Generation:** When AML alerts reveal behavior inconsistent with a customer's KYC profile, investigators escalate findings to a Suspicious Activity Report (SAR). SAR metadata is highly sensitive, time-bound, and strictly confidential, with a strict "no tipping off" policy.

## Compliance Pipeline

AML is an integral stage in the compliance pipeline:
1.  **KYC Foundation:** Identity verification must be complete and a KYC risk rating established before any customer account activation.
2.  **AML Monitoring:** Transaction monitoring systems utilize the KYC risk rating metadata to dynamically adjust scrutiny.
3.  **SAR Generation:** If AML monitoring uncovers suspicious activity inconsistent with the KYC profile, a Suspicious Activity Report is generated.

## Source References
*   [Compliance Policy Handbook](10ivoRcx7RyKcugHb7zVnJSgIRV98XZgVjtV10CZro04)
*   [AML Investigations Playbook](1dSWNVjfYvUmeb-kA8ETaZ38K6YCJG7SkC5oOksvxKeo)
*   [Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRmINv-Zt8r9aJVpFGILAtE)
*   [Finance Business Glossary](1lX_2XEm4jpiN-gNOv30UEBoJ1eYAvDUl2BL-g-FZ2KE)
*   [Risk Management Framework](1qWcFBL9LnXxm2iOegMjnO4_Qywbt17Kw-hAOH-arSUs)

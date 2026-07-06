# Know Your Customer Overview

Know Your Customer (KYC), also known by aliases such as `kyc`, `kyc-risk-rating`, or `kyc-profile`, refers to a financial compliance metric and a due diligence process designed to verify customer identity and establish risk ratings. It is a critical component for enriching customer metadata, requiring strict separation and clear correlation with other financial attributes.

## Key Features and Metadata Role

The core output of the KYC process is the **KYC Risk Rating**, which measures financial-crime risk. This rating is pivotal for determining whether standard or enhanced due diligence requirements apply to a customer. It is initially established during customer onboarding and subsequently updated through periodic reviews ([Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRnINv-Zt8r9aJVpFGILAtE), [Finance Business Glossary](1lX_2XEm4jpiN-gNOv30UEBoJ1eYAvDUl2BL-g-FZ2KE)).

### Distinction in Customer Metadata

For effective metadata enrichment, it is crucial to differentiate the KYC Risk Rating from the Credit Risk Score:

*   **KYC Risk Rating:** This attribute specifically measures **financial-crime risk**. It dictates compliance requirements and is a critical piece of customer metadata.
*   **Credit Risk Score:** In contrast, this quantifies **default likelihood** based on factors like repayment history, exposure, income, or leverage. It drives decisions related to interest pricing, credit limits, and manual underwriting ([Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRnINv-Zt8r9aJVpFGILAtE), [Risk Management Framework](1qWcFBL9LnXxm2iOegMjnO4_Qywbt17Kw-hAOH-arSUs)).

Customer metadata systems must treat these as distinct fields, as confusing default risk with compliance risk is a common operational error in metadata enrichment processes ([Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRnINv-Zt8r9aJVpFGILAtE)).

## The Compliance Pipeline: KYC as Foundational Metadata

KYC serves as the metadata foundation for subsequent stages within the compliance pipeline:

*   **KYC Foundation:** No customer account can be activated until identity verification is complete, with the resulting KYC risk rating forming the foundational metadata for all downstream monitoring activities ([Compliance Policy Handbook](10ivoRcx7RyKcugHb7zVnJSgIRV98XZgVjtV10CZro04), [Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRnINv-Zt8r9aJVpFGILAtE)).
*   **AML Monitoring:** Transaction monitoring systems utilize a risk-based model, dynamically adjusting their scrutiny levels based on the customer's KYC profile and associated risk rating. Stale KYC metadata is specifically flagged as a finding during active investigations, highlighting the need for up-to-date enrichment ([Compliance Policy Handbook](10ivoRcx7RyKcugHb7zVnJSgIRV98XZgVjtV10CZro04), [AML Investigations Playbook](1dSWNVjfYvUmeb-kA8ETaZ38K6YCJG7SkC5oOksvxKeo)).
*   **SAR Generation:** When Anti-Money Laundering (AML) alerts reveal behavior inconsistent with a customer's established KYC profile, investigators escalate these findings, which can lead to the generation of a Suspicious Activity Report (SAR) ([Compliance Policy Handbook](10ivoRcx7RyKcugHb7zVnJSgIRV98XZgVjtV10CZro04), [AML Investigations Playbook](1dSWNVjfYvUmeb-kA8ETaZ38K6YCJG7SkC5oOksvxKeo)).

## Source References

*   [Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRnINv-Zt8r9aJVpFGILAtE)
*   [Finance Business Glossary](1lX_2XEm4jpiN-gNOv30UEBoJ1eYAvDUl2BL-g-FZ2KE)
*   [Compliance Policy Handbook](10ivoRcx7RyKcugHb7zVnJSgIRV98XZgVjtV10CZro04)

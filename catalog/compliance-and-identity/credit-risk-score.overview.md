# Credit Risk Score Overview

The Credit Risk Score is a metric that quantifies the probability of default, based on an individual's repayment history, exposure, and income or leverage. It is also known as `credit-score`.

## Key Characteristics and Impact

This score is crucial for driving various financial decisions. It directly influences interest pricing, sets credit limits, and establishes thresholds for manual underwriting processes. The Credit Risk Score is based on an assessment of repayment history, financial exposure, and either income or leverage.

## Distinction in Customer Metadata

For robust customer metadata enrichment, it is critical to maintain a strict separation between the Credit Risk Score and the KYC Risk Rating. The Credit Risk Score specifically measures **default risk**, while the KYC Risk Rating addresses **financial-crime risk**. Customer metadata systems must treat these as distinct fields. Confusing default risk with compliance risk is identified as a common operational error, which downstream monitoring and onboarding systems need to correctly resolve to ensure accurate attribute management.

## Source References
* [Customer Onboarding SOP](1Axp8e_zvhvHjyJ0B3sSuDRzINv-Zt8r9aJVpFGILAtE)
* [Risk Management Framework](1qWcFBL9LnXxm2iOegMjnO4_Qywbt17Kw-hAOH-arSUs)

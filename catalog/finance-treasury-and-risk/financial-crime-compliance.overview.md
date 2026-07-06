# Financial Crime Compliance Overview

Financial Crime Compliance encompasses the standard baselines for identity verification, risk evaluation, anomaly monitoring, and the filing of Suspicious Activity Reports (SARs). This framework is crucial for preventing illicit financial activities such as money laundering.

## Key Components

### Know Your Customer (KYC) Profiling
KYC Profiling forms the core of compliance, involving the verification of identity and beneficial ownership. This process assigns a risk rating, which can be either **Standard** or **Enhanced**. If KYC information becomes stale or weak, it is categorized as a compliance finding, necessitating an active refresh.
*   Source: [Copy of AML Investigations Playbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B679B9CDF-5F01-4CE5-BAB7-5CE2C016624B%7D&file=Copy%20of%20AML%20Investigations%20Playbook.docx&action=default&mobileredirect=true), [Copy of Compliance Policy Handbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B1CFD6FA8-6227-4F7A-882C-1A8BAF7B85FE%7D&file=Copy%20of%20Compliance%20Policy%20Handbook.docx&action=default&mobileredirect=true), [Customer Onboarding SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B59E2FE38-9732-4336-9DD1-87040BBE0F0A%7D&file=Copy%20of%20Customer%20Onboarding%20SOP.docx&action=default&mobileredirect=true)

### Transaction Monitoring
This is a risk-based mechanism designed to detect deviations from expected customer profiles, such as structuring or unusual transaction volumes. Transaction monitoring relies heavily on the established KYC rating to define and identify expected behavioral patterns.
*   Source: [Copy of AML Investigations Playbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B679B9CDF-5F01-4CE5-BAB7-5CE2C016624B%7D&file=Copy%20of%20AML%20Investigations%20Playbook.docx&action=default&mobileredirect=true), [Copy of Compliance Policy Handbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B1CFD6FA8-6227-4F7A-882C-1A8BAF7B85FE%7D&file=Copy%20of%20Compliance%20Policy%20Handbook.docx&action=default&mobileredirect=true)

### SAR Process Requirements
When reasonable suspicion of illicit activity is established, a Suspicious Activity Report (SAR) must be drafted and submitted. Regulatory mandates for this process include prohibiting "tipping off" the customer, requiring that the account continues to be serviced normally, and demanding strict adherence to filing windows.
*   Source: [Copy of AML Investigations Playbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B679B9CDF-5F01-4CE5-BAB7-5CE2C016624B%7D&file=Copy%20of%20AML%20Investigations%20Playbook.docx&action=default&mobileredirect=true), [Copy of Compliance Policy Handbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B1CFD6FA8-6227-4F7A-882C-1A8BAF7B85FE%7D&file=Copy%20of%20Compliance%20Policy%20Handbook.docx&action=default&mobileredirect=true)

## Key Definitions

### KYC Risk Rating vs. Credit Risk Score
It is important to distinguish between KYC Risk Rating and Credit Risk Score, as they serve different purposes and must not be conflated in data models or analytics.

*   **KYC Risk Rating**: This rating measures compliance and vulnerability to financial crime, categorized as **Standard** or **Enhanced Due Diligence**. It assesses financial-crime risk profiles.
    *   Source: [Customer Onboarding SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B59E2FE38-9732-4336-9DD1-87040BBE0F0A%7D&file=Copy%20of%20Customer%20Onboarding%20SOP.docx&action=default&mobileredirect=true), [Copy of Finance Business Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)

*   **Credit Risk Score**: This score evaluates standard default probabilities based on factors like repayment history, existing exposure, income, and leverage. Low scores may lead to tighter pricing/limits or manual underwriting.
    *   Source: [Customer Onboarding SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B59E2FE38-9732-4336-9DD1-87040BBE0F0A%7D&file=Copy%20of%20Customer%20Onboarding%20SOP.docx&action=default&mobileredirect=true), [Copy of Finance Business Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)

A critical metadata warning specifies that credit scoring engines must not operate on KYC validation variables, and vice-versa, due to their distinct purposes.
*   Source: [Copy of Finance Business Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)

## Source References
*   [Copy of AML Investigations Playbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B679B9CDF-5F01-4CE5-BAB7-5CE2C016624B%7D&file=Copy%20of%20AML%20Investigations%20Playbook.docx&action=default&mobileredirect=true)
*   [Copy of Compliance Policy Handbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B1CFD6FA8-6227-4F7A-882C-1A8BAF7B85FE%7D&file=Copy%20of%20Compliance%20Policy%20Handbook.docx&action=default&mobileredirect=true)
*   [Customer Onboarding SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B59E2FE38-9732-4336-9DD1-87040BBE0F0A%7D&file=Copy%20of%20Customer%20Onboarding%20SOP.docx&action=default&mobileredirect=true)
*   [Copy of Finance Business Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)

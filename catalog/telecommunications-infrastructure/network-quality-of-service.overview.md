# Network Quality of Service Overview

Network Quality of Service (QoS) outlines packet latency budgets and defines traffic prioritizations across LTE scheduler and core transport platforms. It is also known as Quality of Service (QoS) & Policy Integration, VoLTE Services, Real-Time QoS Metrics & Monitoring Thresholds, Network Quality of Service (QoS) & Performance Targets, and Conversational-Voice Class Latency Target.

## Key Features and Applications

Network QoS is a critical component in managing network performance and user experience.

### Policy Integration and Throttling
For data plans, QoS policy integration dictates that if allowance thresholds are exceeded, a policy function will migrate the subscriber's traffic to a lower-priority QoS class, also known as "throttling," rather than dropping connectivity entirely. This mechanism ensures continued, albeit degraded, service.

### VoLTE Services
QoS is essential for VoLTE (Voice-over-LTE) services, which are delay-sensitive and carried over the LTE data network. VoLTE, also referred to as Voice-over-LTE or IMS voice, relies on defined QoS parameters to ensure call quality.

### Real-Time QoS Metrics and Monitoring Thresholds
Network Quality of Service involves specific metrics and monitoring thresholds, particularly for conversational-voice class latency. Updated QoS policy parameters were introduced to address legacy limitations that previously led to audible clipping and call drops in the metro region.

Key metrics and thresholds include:
*   **Conversational-Voice Class Latency Target:** The current target for one-way latency is $\le 80\text{ ms}$, which replaced the legacy $100\text{ ms}$ baseline.
*   **Monitoring Alert Rule:**
    *   **Warning Alert:** Triggered when latency reaches $70\text{ ms}$.
    *   **Critical Alarm:** Triggered at $80\text{ ms}$ latency, indicating an active dropped-call risk.

## Source References
*   [Copy of Churn Analysis Quarterly Report.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0A751BED-229A-4FF3-B357-6BBC7BB90201%7D&file=Copy%20of%20Churn%20Analysis%20Quarterly%20Report.docx&action=default&mobileredirect=true)
*   [Copy of Customer Care Handbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0825D7A7-7590-43A6-97D4-9435A6848A1E%7D&file=Copy%20of%20Customer%20Care%20Handbook.docx&action=default&mobileredirect=true)
*   [Copy of Billing Charging System Overview](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BF9B4322C-D9B6-4C28-917E-879383903E0E%7D&file=Copy%20of%20Billing%20Charging%20System%20Overview.docx&action=default&mobileredirect=true)
*   [Copy of Finance Business Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B7DBF0243-8930-473A-9AA2-C00D2988A08E%7D&file=Copy%20of%20Finance%20Business%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Marketing Analytics Deck Notes](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B78809E3B-BFC2-417E-8231-C987D368F4A1%7D&file=Copy%20of%20Marketing%20Analytics%20Deck%20Notes.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Management Glossary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B23A163E5-F431-4DCA-AD24-D1D34F9877C7%7D&file=Copy%20of%20Inventory%20Management%20Glossary.docx&action=default&mobileredirect=true)
*   [Copy of Inventory Systems Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0F27271E-9229-41C3-9E28-91EC2AB1B691%7D&file=Copy%20of%20Inventory%20Systems%20Overview.docx&action=default&mobileredirect=true)
*   [Network Engineering Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B8311332E-F22F-4C2B-8EB6-EAC3F55B22A2%7D&file=Copy%20of%20Network%20Engineering%20Glossary.docx&action=default&mobileredirect=true)
*   [Number Portability Process SOP](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B9409E39A-8DA8-4F4B-8671-9CEDB0ABE017%7D&file=Copy%20of%20Number%20Portability%20Process%20SOP.docx&action=default&mobileredirect=true)
*   [Copy of Dropped Calls Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BBD2C2B47-FBAC-4778-AEC8-28A556556CE6%7D&file=Copy%20of%20Dropped%20Calls%20Postmortem.docx&action=default&mobileredirect=true)
*   [Copy of QoS Policy Doc.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2EF9FBD3-5015-454C-8A3A-AC1332142749%7D&file=Copy%20of%20QoS%20Policy%20Doc.docx&action=default&mobileredirect=true)

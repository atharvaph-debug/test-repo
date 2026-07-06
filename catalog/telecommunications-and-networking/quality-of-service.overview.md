# Quality of Service Overview

Quality of Service (QoS) refers to the set of mechanisms and rules employed to prioritize network traffic and ensure it meets strict performance targets. These targets primarily include latency, packet loss, and jitter. Traffic is categorized into distinct classes, each assigned a specific priority and treatment tailored to its operational requirements.

## Key Features and Applications

*   **Definition and Mechanisms**: QoS defines how network traffic is managed to guarantee a certain level of performance. It involves sorting traffic into different classes and applying appropriate prioritization and treatment to each class to achieve specified performance metrics like low latency, minimal packet loss, and stable jitter.

*   **VoLTE Requirements**: Voice over LTE (VoLTE), which transmits voice as packets over the LTE data network via IMS, is critically dependent on QoS for acceptable performance. VoLTE traffic must be assigned to the highest-priority "conversational voice" class to ensure clear and reliable voice communication.

*   **Latency Targets for Conversational Voice**: The legacy QoS policy for conversational voice aimed for a one-way packet latency budget of 100 ms and a packet loss target under 1%. However, a postmortem analysis of a metro region dropped-calls incident revealed that latencies between 80–100 ms led to severe clipping and dropped calls without triggering existing alarms. Consequently, the VoLTE one-way latency target was tightened to **80 ms**, with a warning threshold set at 70 ms, superseding the previous policy.

*   **QoS and Data Plan Throttling**: In data plans, QoS treatments are sometimes linked to data allowances. When a subscriber exceeds their allocated data threshold, the charging system instructs the policy function to reclassify their traffic to a lower-priority QoS class. This mechanism, known as throttling, reduces bandwidth without completely cutting off service.

## Source References
*   [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of QoS Policy Doc](1K6Yoj4uE_IwHJHezZKDCY5bC_URWnCHE9BSm5dSd1-0)
*   [Copy of Dropped Calls Postmortem](145vwcMxn2xKFP5uxq624N5QnBZEbU-Wton8ZUI8QwD0)
*   [Copy of Billing Charging System Overview](1GPtX16AkNHHRYrkUk87lsfDHuMLXYVcVV3RycBtHexE)

# Voice over LTE Overview

Voice over LTE (VoLTE) is a technology designed to carry voice calls as packets over the existing LTE data network, leveraging the IP Multimedia Subsystem (IMS). This approach contrasts with traditional mobile voice services that use legacy circuit-switched voice paths. VoLTE's reliance on the data network necessitates strict Quality of Service (QoS) treatments to ensure call quality, making it a critical area for network metadata management and policy.

## Key Features and Technical Requirements

VoLTE relies heavily on specific QoS classes to function effectively, primarily the `conversational-voice` class. This is due to the delay-sensitive nature of packet-based voice, where maintaining high QoS is essential to prevent issues like clipping, delay, and dropped calls.

Historically, the QoS policy for the `conversational-voice` class stipulated a one-way packet latency budget of **100 ms** with a packet loss target under **1%**. However, an investigation into a two-week dropped-call incident in the Metro Region revealed that the 100 ms budget was too lenient, allowing call quality to degrade significantly within the 80–100 ms range without triggering alarms. Consequently, the one-way latency target for `conversational-voice` carrying VoLTE has been tightened to **80 ms**. Monitoring systems are now updated to issue a warning at 70 ms and an alarm at 80 ms to proactively address potential quality degradation.

## Metadata and Configuration

VoLTE functionality is deeply intertwined with several key metadata elements used for network configuration and subscriber identification:

*   **Access Point Names (APNs):** An APN serves as the identifier a device presents to the network core to specify which packet data network (PDN) and gateway it wishes to route a data session through. For VoLTE, a typical subscriber profile includes a dedicated **internal IMS APN** reserved specifically for VoLTE signaling, alongside other APNs for services like general public internet browsing. This dedicated APN acts as critical metadata, defining the appropriate gateway and policies for voice traffic. Misconfiguring or missing an APN can lead to "attached but no data" scenarios, preventing subscribers from accessing intended services like VoLTE even if they are otherwise connected to the network.
*   **International Mobile Subscriber Identity (IMSI):** The IMSI is the globally unique identifier of a subscriber, stored on the SIM card, serving as the foundational metadata element for subscriber identity. It is crucial for network actions, including resolving "which subscriber" is active, and acts as a primary join key in subscriber records and session logs. For roaming, **IMSI ranges** are used as policy keys to differentiate home subscribers from visiting roamers, enabling the authorization of services such as VoLTE and the application of wholesale inter-operator charges.

## Impact on Subscriber Churn

Network quality, particularly the quality of VoLTE service, is a significant driver of subscriber churn. Poor VoLTE quality can degrade the customer experience, directly leading to service cancellations. Addressing and maintaining high VoLTE quality is therefore a critical retention recommendation for frontline care agents, especially for high-value customer lifetime value segments.

## Source References

*   [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of QoS Policy Doc](1K6Yoj4uE_IwHJHezZKDCY5bC_URWnCHE9BSm5dSd1-0)
*   [Copy of Dropped Calls Postmortem](145vwcMxn2xKFP5uxq624N5QnBZEbU-Wton8ZUI8QwD0)
*   [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
*   [Copy of Churn Analysis Quarterly Report](https://docs.google.com/document/d/15XrKEZF7PSXKCzdRbRj7BxleBcFn2onBv1QAkvDDlgs/edit)
*   [Copy of Customer Care Handbook](1mGNA1aQHvYEJS6N1cmr5N3nkTkZ8fX7Hjz-IvFOd_3o)
*   [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)
*   [Copy of Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ)

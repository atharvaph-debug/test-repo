# Voice over LTE Overview

Voice over LTE (VoLTE), also known by its alias `volte`, is a telecommunications technology that routes real-time voice calls as IP packets over the existing LTE data network. This system replaces legacy circuit-switched paths by utilizing the IP Multimedia Subsystem (IMS).

## Technical Characteristics and Quality of Service

VoLTE is critical for modern voice communication within LTE networks, requiring strict Quality of Service (QoS) management due to the delay-sensitive nature of voice calls. It operates on the high-priority "conversational voice" traffic class to prevent issues such as clipping, audible delay, and dropped calls.

Historically, the latency target for conversational voice was 100 ms. However, following incidents of elevated dropped calls and clipping, the VoLTE one-way latency target was tightened to 80 ms. Network monitoring is now re-tuned to alarm at 80 ms and warn at 70 ms.

## Related Network Concepts

*   **IP Multimedia Subsystem (IMS):** VoLTE routes calls via the IMS, which handles the signaling and session management for IP-based multimedia services.
*   **Access Point Name (APN):** The APN specifies the packet data network a session connects to. For VoLTE, an IMS APN is used to separate voice signaling from general internet traffic, selecting the appropriate gateway and routing policies. In logs, APN indicates "which service/network" a session utilized.
*   **International Mobile Subscriber Identity (IMSI):** While not directly part of VoLTE's routing, the IMSI is the globally unique identifier on the SIM that identifies the subscriber. It serves as a fundamental join key across subscriber records and is used in roaming to identify the home operator and for settling wholesale inter-operator charges for services like VoLTE.

## Business Impact

Poor network quality, particularly in "VoLTE dropped-call zones," is identified as a primary driver of customer churn (attrition). Ensuring the stability and quality of VoLTE services is thus crucial for customer retention.

## Source References
*   [Copy of QoS Policy Doc](1K6Yoj4uE_IwHJHezZKDCY5bC_URWnCHE9BSm5dSd1-0)
*   [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of Dropped Calls Postmortem](145vwcMxn2xKFP5uxq624N5QnBZEbU-Wton8ZUI8QwD0)
*   [Copy of Churn Analysis Quarterly Report](https://docs.google.com/document/d/15XrKEZF7PSXKCzdRbRj7BxleBcFn2onBv1QAkvDDlgs/edit)
*   [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)
*   [Copy of Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ)

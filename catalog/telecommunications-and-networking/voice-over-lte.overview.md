# Voice over LTE Overview

Voice over LTE (VoLTE) is a telecommunications technology that carries voice calls as packet data over existing LTE networks. Unlike traditional circuit-switched voice, VoLTE relies on the IP Multimedia Subsystem (IMS) for delivering voice, with high-priority treatment to ensure acceptable call quality.

## Key Features and Requirements

VoLTE is entirely dependent on Quality of Service (QoS) mechanisms to provide an acceptable user experience.
*   **QoS Class**: VoLTE traffic must be carried on the highest-priority "conversational voice" class, which is designed to hold traffic to strict performance targets.
*   **Latency Targets**: To ensure quality, VoLTE has specific latency requirements. While the legacy QoS policy targeted a one-way packet latency budget of 100 ms, a postmortem analysis led to a tightened VoLTE one-way latency target of **80 ms**, with a warning threshold at 70 ms. This supersedes the older policy, as latency in the 80–100 ms band was found to cause severe clipping and dropped calls.

## Integration with Network Identifiers

VoLTE sessions interact with network identifiers for proper routing and policy application:
*   **Access Point Name (APN)**: For VoLTE signaling, a dedicated internal IMS APN is used. The APN acts as an identifier that a device presents to the network, specifying which packet data network (PDN) and gateway to route a data session through. APNs are applied per-session and map to specific services and policies.
*   **International Mobile Subscriber Identity (IMSI)**: While not directly part of the VoLTE data path itself, the IMSI is the globally unique subscriber identifier provisioned on the SIM card and registered in the subscriber database. Its correct provisioning, along with the correct APNs, is crucial for making a subscriber usable for services like VoLTE. A missing or incorrect APN can lead to an "attached but no data" fault, preventing VoLTE service.

### Aliases
*   volte
*   volte-requirements

## Source References
*   [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of QoS Policy Doc](1K6Yoj4uE_IwHJHezZKDCY5bC_URWnCHE9BSm5dSd1-0)
*   [Copy of Dropped Calls Postmortem](145vwcMxn2xKFP5uxq624N5QnBZEbU-Wton8ZUI8QwD0)
*   [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
*   [Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)

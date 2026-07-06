# Subscriber Identity and Routing Overview

This entry provides technical profiles for key telecommunications identifiers, specifically International Mobile Subscriber Identity (IMSI) and Access Point Name (APN). These identifiers are crucial for mapping subscriber identity, segmenting services, and defining roaming boundaries, serving as core metadata for network operations and analysis. Other sources refer to this concept as International Mobile Subscriber Identity (IMSI), Subscriber Identity & Network Routing Metadata, Core Identifier Definitions & Join Keys, APN (Access Point Name), Identity vs. Access Mapping, Bilateral Roaming Keying, and Error Profiling Diagnostics.

## Core Identifier Definitions & Join Keys

*   **IMSI (International Mobile Subscriber Identity)**: This is the globally unique, multi-digit identifier assigned to a subscriber. It is written to the physical SIM during personalization and registered in central subscriber databases such as the Home Subscriber Server (HSS) or Home Location Register (HLR). The IMSI acts as the primary "passport" for both home-network authentication and validation when a subscriber is in a visited network. While "SIM identity" is sometimes used loosely in legacy drafts, **IMSI** is the authoritative term and must be used in all current network engineering documentation.
    *   *Data Integration Role:* The IMSI serves as the **absolute join key** in subscriber records and session logs to identify "which subscriber" is associated with specific activities.
*   **APN (Access Point Name)**: An APN is a metadata tag within a subscriber's profile that determines how a data session is routed. It specifies the packet data gateway, network segment, and policy set (e.g., general internet access versus a dedicated service like IMS for VoLTE signaling) that a data session will use.
    *   *Data Integration Role:* In logs and session tracking, the APN functions as the **indicator** for "which service/network" a particular session utilized.

## Functional Metadata Alignments

*   **Identity vs. Access Mapping**: The IMSI answers the fundamental question *"Who is this subscriber?"*, providing the unique identity. In contrast, the APN clarifies *"What network/service is this session for?"*, detailing the type of access being requested or provided.
*   **Bilateral Roaming Keying**: Roaming agreements, which specify wholesale rates and supported services (such as VoLTE availability), directly map subscriber scopes and routing authorizations to allocated IMSI ranges. This ensures proper identification and service provision for roaming subscribers.
*   **Error Profiling Diagnostics**: Understanding the roles of IMSI and APN is critical for diagnosing network issues.
    *   An **IMSI misconfiguration** typically results in "Attach Failures", meaning the device cannot successfully authenticate with the network.
    *   An **APN misconfiguration**, however, leads to "Attached but No Data" states, where the device can connect to the network but cannot access data services.

## Source References
*   [SIM Provisioning Runbook](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B774023A8-1498-43F1-9B6A-5C84311B59C1%7D&file=Copy%20of%20SIM%20Provisioning%20Runbook.docx&action=default&mobileredirect=true)
*   [Telecom Systems Terminology Overview](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B194C726C-A83C-46CD-BDB6-A6CC59E58FB6%7D&file=Copy%20of%20Telecom%20Systems%20Terminology%20Overview.docx&action=default&mobileredirect=true)
*   [Network Engineering Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B8311332E-F22F-4C2B-8EB6-EAC3F55B22A2%7D&file=Copy%20of%20Network%20Engineering%20Glossary.docx&action=default&mobileredirect=true)

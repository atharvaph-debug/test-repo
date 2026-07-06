# Voice over LTE QoS Overview

Voice over LTE QoS refers to the network policies and packet quality constraints specifically applied to voice sessions carried directly over long-term evolution (LTE) data networks. This topic details how network-level quality of service (QoS) parameters, real-time data throttling, and Voice-over-LTE (VoLTE) performance targets are defined and shared across systems This sub-topic details how network-level quality of service (QoS) parameters.... It is also known by the aliases VoLTE and Voice-over-LTE, and internally as IMS Voice Network Engineering Glossary.

## Voice over LTE (VoLTE) Definition

VoLTE is a service that carries voice calls as packets over the LTE data network via the IP Multimedia Subsystem (IMS), thereby replacing traditional circuit-switched voice paths. The performance and reliability of VoLTE are highly dependent on the QoS class parameters applied to its traffic [Network Engineering Glossary](gs://test-input-gcs-atharva/eval%20corpus/network_engineering_glossary.html).

## Quality of Service (QoS) Parameters for VoLTE

VoLTE voice traffic must be strictly mapped to the "conversational-voice" QoS class Postmortem: Metro Region Dropped-Calls Incident, Quality of Service (QoS) Policy. Key performance targets for this class include:

*   **One-way packet latency budget**: The target for one-way packet latency must be set to $\le 80\text{ ms}$ to ensure acceptable service quality Postmortem: Metro Region Dropped-Calls Incident. Previously, legacy QoS policy metadata tolerated 100 ms, which was found to cause audible clipping and dropped calls with modern VoLTE codecs and jitter profiles Postmortem: Metro Region Dropped-Calls Incident.
*   **Packet loss**: Must be less than 1% Quality of Service (QoS) Policy.
*   **Guaranteed bit rate**: An end-to-end guaranteed bit rate, appropriate to the voice codec in use, must be enforced to prevent clipping and dropped calls Quality of Service (QoS) Policy.

## Associated Subscriber & Session Metadata

For effective metadata enrichment related to VoLTE QoS, several key identifiers are crucial:

*   **IMSI (International Mobile Subscriber Identity)**: This is the globally unique identifier of a subscriber, provisioned onto the physical SIM card. It serves as the primary key reference for network authentication, home connections, and roaming Network Engineering Glossary, Telecom Systems & Terminology Overview. In subscriber records, network signaling, and session logs, the IMSI is the foundational join key representing "which subscriber" Telecom Systems & Terminology Overview. Inter-operator routing, roaming, and billing processes utilize IMSI ranges to distinguish home subscribers from visiting subscribers on partner networks Roaming Partner Agreement — Summary. The term "SIM identity" should be avoided in favor of IMSI Network Engineering Glossary.
*   **APN (Access Point Name)**: The APN is an identifier that a mobile device presents to the network to specify which packet data network (e.g., public internet APN or internal IMS APN for voice signaling) and gateway to route a data session through Network Engineering Glossary. In session logs, APNs indicate "which service/network" a session accessed, for example, distinguishing a general internet APN from an IMS APN used for VoLTE signaling Telecom Systems & Terminology Overview. Missing or misconfigured APN data profiles are a common cause for "attached but no data" alerts SIM Provisioning Runbook.

## Source References

*   Postmortem: Metro Region Dropped-Calls Incident
*   Network Engineering Glossary
*   Quality of Service (QoS) Policy
*   Roaming Partner Agreement — Summary
*   SIM Provisioning Runbook
*   Telecom Systems & Terminology Overview

# Voice over LTE Overview

Voice over LTE (VoLTE) is a telecommunications service that enables packet-based voice communication services routed over LTE data networks via IP Multimedia Subsystems (IMS). It is recognized by several aliases including "VoLTE," "Voice-over-LTE," and "IMS voice".

## Key Features and Metadata

VoLTE relies heavily on specific metadata definitions and configurations to ensure its quality and functionality, particularly concerning Quality of Service (QoS) and network routing.

### Quality of Service (QoS) Metadata
VoLTE is classified as "Conversational Voice," which is the highest priority traffic class in the network. It carries voice as packets and requires specific QoS parameters to prevent issues like audio clipping, delay, and dropped calls.

*   **Latency Target**: Historically, the one-way packet latency budget for conversational voice was 100 ms. Following operational failures, this QoS metadata target was immediately tightened for VoLTE to **80 ms** one-way latency. Alarm systems rely on this metadata, with alarms triggering at 80 ms and warnings at 70 ms to prevent call degradation and subscriber churn.
*   **Packet Loss Target**: The target for packet loss is **< 1%**.
*   **Guaranteed Bit Rate (GBR)**: The GBR must align with the specific voice codec being used.
*   **Throttling Impact**: If a subscriber exceeds a high-speed data allowance threshold, real-time charging systems can signal the policy function to alter the subscriber's QoS class metadata, potentially triggering downstream packet "throttling" for the remainder of that billing cycle, which could affect VoLTE performance.

### Access Point Name (APN) Metadata
VoLTE signaling relies on a specialized **IMS APN**. An APN acts as metadata that identifies the target packet data network, selects the appropriate gateway, and determines the policy set for a subscriber's data session. For VoLTE, a subscriber's data profile must map to an IMS APN. A misconfigured or missing APN, even with correct IMSI authentication, can result in an "attached but no data" state.

### Subscriber Identification Metadata
While not unique to VoLTE, the IMSI (International Mobile Subscriber Identity) is the globally unique identifier of a subscriber provisioned onto a SIM, used for network authentication, including for VoLTE services. Engineering metadata should standardize on "IMSI" even though it is sometimes informally called "SIM identity".

## Source References

*   Postmortem: Metro Region Dropped-Calls Incident
*   Network Engineering Glossary
*   Quality of Service (QoS) Policy
*   Billing & Charging System Overview
*   Churn Analysis — Quarterly Report
*   Customer Care Handbook
*   Telecom Systems & Terminology Overview
*   SIM Provisioning Runbook
*   Number Portability Process SOP

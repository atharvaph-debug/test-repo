# Voice-over-LTE Overview

Voice-over-LTE (VoLTE), also known as VoLTE or IMS voice, is a high-priority telecommunication service designed to route conversational voice calls as packets over the LTE data network using the IP Multimedia Subsystem (IMS). It represents the highest priority traffic class within network Quality of Service (QoS) policies.

## Key Characteristics and Performance Targets

VoLTE is crucial for delivering high-quality voice communications and is subject to strict performance targets to prevent issues like audio clipping or dropped calls:

*   **Service Function:** Carries voice calls as packets over the LTE network utilizing IMS Network Engineering Glossary.
*   **Priority:** As a "Conversational Voice Class," it must be assigned the highest network priority Quality of Service (QoS) Policy.
*   **Latency Budget:**
    *   Historically, network policies allowed a one-way packet latency budget of 100 ms for conversational voice Postmortem: Metro Region Dropped-Calls Incident, Quality of Service (QoS) Policy.
    *   Current VoLTE codecs require a tighter budget of 80 ms to prevent call drops and audio clipping Postmortem: Metro Region Dropped-Calls Incident.
    *   Warning thresholds are set to alert at 80 ms, with early warnings at 70 ms, to allow operational intervention before customer-facing quality degradation occurs, which can lead to subscriber churn Postmortem: Metro Region Dropped-Calls Incident, Churn Analysis — Quarterly Report.
*   **Packet Loss Target:** Must maintain less than 1% packet loss Quality of Service (QoS) Policy.
*   **Guaranteed Bit Rate (GBR):** Dynamically adjusted according to the active voice codec Quality of Service (QoS) Policy.

## Network Configuration

VoLTE signaling typically relies on a dedicated Access Point Name (APN):

*   **IMS APN:** A specific APN (`IMS APN`) is reserved for VoLTE signaling, serving as a dedicated gateway SIM Provisioning Runbook.
*   **Configuration Impact:** Misconfiguration of the APN for VoLTE can result in an "Attach fine, no data" error state, where a subscriber successfully authenticates but cannot establish sessions due to incorrect gateway routing SIM Provisioning Runbook.

## Synonyms

The terms "Voice-over-LTE," "VoLTE," and "IMS voice" are all synonymous and refer to this service Network Engineering Glossary.

## Source References
* Network Engineering Glossary
* Postmortem: Metro Region Dropped-Calls Incident
* Quality of Service (QoS) Policy
* Churn Analysis — Quarterly Report
* SIM Provisioning Runbook

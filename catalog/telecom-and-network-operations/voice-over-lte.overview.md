# Voice over LTE Overview

Voice over LTE (VoLTE) is a packet-based voice communication protocol that operates over the LTE data network, utilizing the IP Multimedia Subsystem (IMS) framework. It serves as a modern replacement for legacy circuit-switched voice paths, transmitting voice calls as packet data.

## Aliases and Standardizations

VoLTE is also known as **IMS voice** and **conversational-voice**. The terms **Voice-over-LTE**, **VoLTE**, and **IMS voice** refer to the exact same service.

## Key Characteristics and Performance Targets

VoLTE calls are highly delay-sensitive and depend on the `conversational-voice` Quality of Service (QoS) class.

### QoS Targets and Metrics

*   **Initial Latency Budget**: Historically, the one-way packet latency budget for the `conversational-voice` QoS class was 100 ms, inherited from legacy network budgets. This budget was found to tolerate excessive call degradation, clipping, and dropped calls in the metro region before triggering alerts.
*   **Updated Latency Target**: The updated one-way latency target for the `conversational-voice` QoS class is tightened to **80 ms**.
*   **Monitoring Thresholds**: Monitoring alarm thresholds are configured to trigger a **Warning at 70 ms** and an **Alarm at 80 ms**.
*   **Packet Loss**: Network policies for conversational voice (VoLTE) also mandate packet loss under **1%**.

QoS policies are designed to enforce these end-to-end performance targets on both the radio scheduler and core transport.

## Network Integration and Signaling

To ensure real-time performance, VoLTE utilizes specific network mechanisms:

*   **Dedicated APNs**: Subscriber profiles separate signaling across dedicated Access Point Names (APNs). A distinct IMS APN is used specifically for VoLTE signaling, while a general internet APN handles standard data traffic. This separation is crucial for safeguarding real-time performance.
*   **IMS Voice-Signaling APNs**: These are a type of APN that devices present to designate the packet data network they wish to access, specifically for IMS voice signaling.
*   **Roaming Support**: International Mobile Subscriber Identity (IMSI) ranges are leveraged in bilateral Roaming Partner Agreements to identify home versus visited subscribers, which in turn drives correct routing, service authorization (including VoLTE support), and billing settlement processes.

## Source References
* [Network Engineering Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B8311332E-F22F-4C2B-8EB6-EAC3F55B22A2%7D&file=Copy%20of%20Network%20Engineering%20Glossary.docx&action=default&mobileredirect=true)
* [Copy of Dropped Calls Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BBD2C2B47-FBAC-4778-AEC8-28A556556CE6%7D&file=Copy%20of%20Dropped%20Calls%20Postmortem.docx&action=default&mobileredirect=true)
* [Copy of QoS Policy Doc.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2EF9FBD3-5015-454C-8A3A-AC1332142749%7D&file=Copy%20of%20QoS%20Policy%20Doc.docx&action=default&mobileredirect=true)
* [SIM Provisioning Runbook](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B774023A8-1498-43F1-9B6A-5C84311B59C1%7D&file=Copy%20of%20SIM%20Provisioning%20Runbook.docx&action=default&mobileredirect=true)
* [Copy of Telecom Systems Terminology Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B194C726C-A83C-46CD-BDB6-A6CC59E58FB6%7D&file=Copy%20of%20Telecom%20Systems%20Terminology%20Overview.docx&action=default&mobileredirect=true)
* [Copy of Roaming Partner Agreement Summary.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B0605CD2B-47D4-4297-AFD6-8D5638CD25E3%7D&file=Copy%20of%20Roaming%20Partner%20Agreement%20Summary.docx&action=default&mobileredirect=true)

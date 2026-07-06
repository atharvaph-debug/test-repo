# Access Point Name Overview

The Access Point Name (APN), also referred to simply as APN, is the identifier presented by a mobile device to initiate and route active data or IMS voice sessions. It acts as a crucial component in defining how a device connects to external networks.

## Key Functionality

An APN designates the specific packet data network a device wishes to access and dictates the gateway through which the core network routes the data session. This allows for different types of sessions to be routed appropriately, such as public-internet APNs for general data browsing versus IMS voice-signaling APNs for voice services. It specifies the packet data gateway, network, and policy rules that govern an active data session.

## Operational Impact and Use Cases

APN configuration is vital for proper network connectivity; misconfigurations are a primary cause of "attached but no data" issues for subscribers. To safeguard real-time performance, particularly for services like Voice-over-LTE (VoLTE), subscriber profiles often split signaling across dedicated APNs. This includes using a general internet APN for standard data traffic and a distinct IMS APN specifically for VoLTE signaling. It is noted that Voice-over-LTE, VoLTE, and IMS voice all refer to the exact same service.

## Distinction from IMSI

While the International Mobile Subscriber Identity (IMSI) serves as a globally unique subscriber identifier personalized onto the SIM for authentication and identity, the APN primarily governs session routing and the application of policy rules for data sessions, rather than subscriber identification.

## Source References
* [Copy of SIM Provisioning Runbook.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B774023A8-1498-43F1-9B6A-5C84311B59C1%7D&file=Copy%20of%20SIM%20Provisioning%20Runbook.docx&action=default&mobileredirect=true)
* [Copy of Telecom Systems Terminology Overview.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B194C726C-A83C-46CD-BDB6-A6CC59E58FB6%7D&file=Copy%20of%20Telecom%20Systems%20Terminology%20Overview.docx&action=default&mobileredirect=true)
* [Network Engineering Glossary](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B8311332E-F22F-4C2B-8EB6-EAC3F55B22A2%7D&file=Copy%20of%20Network%20Engineering%20Glossary.docx&action=default&mobileredirect=true)

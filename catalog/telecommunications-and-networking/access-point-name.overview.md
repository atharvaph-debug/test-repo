# Access Point Name Overview

The Access Point Name (APN) is a critical identifier presented by a mobile device to the network to specify the target packet data network (PDN) and the routing gateway for a data session. It is applied per-session and is fundamental for directing network traffic and applying specific service policies.

## Key Concepts and Functionality

An APN serves to designate the intended network and service for a given data session, effectively answering the question: "What network/service is this session for?"

Key aspects of APN functionality include:

*   **Network and Service Selection:** The APN determines which packet data network the session should connect to. This can range from a general public internet APN to a specialized internal IMS APN used for VoLTE signaling.
*   **Gateway and Policy Application:** It selects the appropriate gateway and the policies that will be applied to the data session, ensuring traffic is handled according to service requirements.
*   **Session-Specific Application:** APNs are applied on a per-session basis, allowing for dynamic allocation of network resources and services.
*   **Provisioning and Fault Detection:** During subscriber provisioning, the correct APNs must be applied to a subscriber's data profile. A missing or incorrect APN can lead to an "attached but no data" fault, preventing the device from accessing data services despite being connected to the network.

## Source References

*   [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
*   [Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)

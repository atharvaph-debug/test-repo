# Access Point Name Overview

An Access Point Name (APN), also known by its alias `apn`, is a critical metadata label used by a device to communicate with the network core. It identifies which packet data network (PDN) and gateway a data session should be routed through. While the International Mobile Subscriber Identity (IMSI) identifies "who is the subscriber," the APN clarifies "what network or service this session is for" by selecting the appropriate gateway and applying corresponding policies.

## Key Functions and Characteristics

*   **Data Session Routing**: The APN serves as the identifier for establishing a data session, directing traffic to the correct packet data network and associated gateway.
*   **Policy Application**: It determines the policies to be applied to a given data session.
*   **Subscriber Profiles**: A typical subscriber profile often includes multiple APNs, each mapping to different services and policies. Examples include a public-internet APN for general browsing and a separate internal IMS APN reserved for Voice over LTE (VoLTE) signaling.
*   **Metadata Role**: The APN functions as a metadata label that defines the network connection parameters for a session.
*   **Impact of Misconfiguration**: An incorrect or missing APN is a frequent cause of "attached but no data" service issues. In such cases, a subscriber successfully authenticates via their IMSI but is unable to route data sessions to the intended gateway, preventing access to services. This differs from an IMSI misconfiguration, which would result in a complete failure of the device to attach to the network.

## Source References
* [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
* [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
* [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)

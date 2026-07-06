# Access Point Name Overview

An Access Point Name (APN), also referred to as `apn`, is an identifier presented by a mobile device to route data sessions through specific packet data gateways and networks. It defines the path taken for data communication by specifying the packet data network a session connects to.

## Key Features and Role

*   **Data Session Routing**: The APN specifies the packet data network a session connects to, selecting the appropriate gateway and routing policies. For example, it can separate general internet traffic from voice signaling, such as via an IMS APN for Voice over LTE (VoLTE) services.
*   **Subscriber Data Profiles**: A subscriber's data profile contains one or more APNs. A typical profile includes a public-internet APN for general data access and an internal IMS APN specifically for voice signaling.
*   **Data Logging and Identification**: In system logs, the APN maps to "which service/network" a data session used, serving as a critical identifier for understanding traffic patterns and service usage.
*   **Provisioning and Troubleshooting**: Applying the correct APNs is a crucial step in the subscriber provisioning workflow. If a device successfully attaches to the network but cannot transmit data, it often indicates that the APN is misconfigured or missing from the subscriber's profile.

## Source References

*   [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
*   [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)

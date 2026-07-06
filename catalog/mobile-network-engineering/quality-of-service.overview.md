# Quality of Service Overview

Quality of Service (QoS) is a system for prioritizing network traffic classes based on specific metadata attributes, including latency, packet loss, and jitter targets. Its primary purpose is to prevent high-bandwidth data transfers from degrading the performance of real-time services.

## Key Features and Metadata Definition

QoS defines and enforces performance targets for different types of network traffic. These targets act as metadata, classifying traffic based on criticality and performance requirements:
*   **Latency**: The time delay for data packets to travel across the network.
*   **Packet Loss**: The percentage of data packets that fail to reach their destination.
*   **Jitter**: The variation in packet delay.

## Voice over LTE (VoLTE) QoS Requirements

A critical application of QoS is Voice over LTE (VoLTE), also known as "Voice-over-LTE" or "IMS voice." VoLTE carries voice calls as packets over the LTE data network via IMS. It represents a specialized QoS metadata class with strict requirements:
*   VoLTE traffic must run on the highest priority "conversational voice" traffic class end-to-end, enforced by both the radio scheduler and core transport.
*   Policy targets for VoLTE demand:
    *   One-way packet latency budget of **<100 ms**.
    *   Packet loss of **<1%**.
    *   A guaranteed bit rate aligned with the specific voice codec being used.

These specific numeric targets and traffic class designations are critical metadata defining the expected performance for conversational voice services.

## QoS and Charging Lifecycle: Metadata-Driven Policy Enforcement

QoS policies are also integrated with billing and charging systems, enabling metadata-driven policy enforcement known as "throttling." In this mechanism:
*   Data plans can link QoS levels to charging thresholds.
*   When a subscriber crosses a defined data usage limit, the billing system signals the policy function.
*   This signal triggers a downgrade of the subscriber to a lower-priority QoS class, effectively "throttling" their data speed rather than cutting off access entirely. This action is a direct modification of a subscriber's QoS class metadata based on usage metadata.

## Related Network Metadata Identifiers

Within the Mobile Core Network, other key metadata identifiers are essential for managing subscriber sessions and applying QoS policies:
*   **Access Point Name (APN)**: An identifier presented by a device that tells the core network which gateway to route a data session through (e.g., public internet vs. internal IMS voice signaling APN).
*   **International Mobile Subscriber Identity (IMSI)**: The globally unique identity provisioned on the SIM, used for subscriber recognition and authentication (both domestic and roaming). This identifier is crucial for associating QoS policies with individual subscribers.

## Source References
*   [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)
*   [Quality of Service (QoS) Policy](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8683521)
*   [Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)
*   [Customer Care Handbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552469)

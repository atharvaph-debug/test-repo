# Quality of Service Overview

Quality of Service (QoS) refers to the mechanisms used to prioritize network traffic and manage packet delivery to meet specific performance targets, such as latency, packet loss, and throughput. It represents an operational control that holds network sessions to these defined performance standards.

## Key Features and Operational Control

QoS facilitates the prioritization of network traffic through **class differentiation**. Traffic is mapped to distinct QoS classes, each receiving appropriate priority treatments. For instance, real-time services like voice communication demand stricter QoS envelopes compared to standard "best-effort" data traffic, ensuring their critical performance requirements are met.

## Applications and Dependencies

### Voice over LTE (VoLTE)
VoLTE, also known as "Voice-over-LTE" or "IMS voice," routes voice calls as packetized data over the LTE network using the IP Multimedia Subsystem (IMS) core. VoLTE calls critically rely on a dedicated, high-priority QoS class to guarantee call clarity. The target thresholds for this are formalized within the system's QoS Policy. High-priority voice signaling for VoLTE is carried across a distinct IMS Access Point Name (APN).

### Charging-to-QoS Policy Feedback Loops
QoS classifications are integrated into certain data plans, directly linking physical data allowances to network prioritization. In scenarios where a prepaid or postpaid subscriber exceeds a specific usage threshold, the charging system signals the policy function. Instead of completely cutting off the connection, the policy engine then downgrades the subscriber's session to a lower-priority QoS class, a process commonly referred to as "throttling," for the remainder of the billing cycle.

## Source References
*   [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)
*   [Telecom Systems & Terminology Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552489)
*   [Billing & Charging System Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519681)

# Quality of Service Overview

Quality of Service (QoS) refers to network traffic classification mechanisms and latency performance budgets designed to prioritize time-sensitive applications like conversational voice. These mechanisms segment and treat network traffic differently to prevent high-bandwidth, non-real-time actions, such as file downloads, from degrading the performance of time-sensitive applications.

## Key Mechanisms and Targets

QoS functions by classifying network traffic, assigning priorities, and establishing strict performance targets. These targets are primarily centered around:
*   **Latency**: The delay before a transfer of data begins following an instruction for its transfer.
*   **Packet Loss**: The failure of one or more transmitted packets to arrive at their destination.
*   **Jitter**: The variation in the delay of received packets.

## Application: Voice over LTE (VoLTE)

Voice over LTE (VoLTE) is a direct application that relies entirely on QoS principles. VoLTE carries voice traffic as packets over an LTE network. For VoLTE, the `conversational-voice` QoS class is critical. Following an investigation into a metro-region dropped-calls incident, the one-way packet latency budget target for the `conversational-voice` QoS class was tightened from 100 milliseconds (ms) to 80 ms to ensure voice quality.

## Source References
* [Quality of Service (QoS) Policy](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8683521)
* [Postmortem: Metro Region Dropped-Calls Incident](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585217)
* [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)

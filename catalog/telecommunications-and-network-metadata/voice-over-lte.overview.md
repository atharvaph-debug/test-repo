# Voice over LTE Overview

Voice over LTE (VoLTE) is a telecommunication service that facilitates voice communications as packet data transmitted over LTE networks. Its ability to maintain acceptable call quality is entirely dependent on effective Quality of Service (QoS) policies.

## Key Characteristics

VoLTE services, particularly for conversational voice traffic, are subject to stringent Quality of Service (QoS) policies to ensure performance.

*   **Latency Thresholds**:
    *   The baseline QoS policy originally established a one-way packet latency budget of 100 ms for conversational-voice traffic.
    *   However, real-world monitoring indicated that this 100 ms threshold often led to clipping and dropped calls.
    *   Consequently, the target latency was adjusted downwards to 80 ms to improve call quality.
*   **Packet Loss**: The performance target for packet loss within the conversational-voice class must be strictly maintained under 1%.

## Aliases

VoLTE is also commonly referred to as:
*   volte

## Source References
*   [Quality of Service (QoS) Policy](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8683521)
*   [Postmortem: Metro Region Dropped-Calls Incident](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585217)

# Quality of Service Overview

Quality of Service (QoS), also known by its alias `qos`, refers to a set of mechanisms designed to sort network traffic into distinct classes. Each class is assigned a priority and specific performance targets, such as latency, packet loss, and jitter, to ensure that traffic meets its individual needs. Real-time services, for instance, demand stricter QoS treatments compared to default classes used for general interactive or best-effort data.

## Principles and Mechanisms

QoS operates by categorizing network traffic and applying policies to manage its performance.
*   **Definition and Mechanics**: QoS mechanisms classify network traffic, assigning each class a priority and performance goals including latency, packet loss, and jitter. This ensures that different types of traffic receive appropriate handling, with stricter treatment for delay-sensitive services like real-time communications.
*   **Enforcement**: QoS policy is applied end-to-end across the network. It is enforced at key points such as the radio scheduler and throughout the core transport layer for each bearer when a session is established.

## Applications and Dependencies

QoS is critical for the performance of various network services, especially those sensitive to delay.

### Voice over LTE (VoLTE) Requirements
Voice over LTE (VoLTE) carries voice calls as packets over the LTE data network via the IP Multimedia Subsystem (IMS), differing from traditional circuit-switched voice paths. VoLTE is highly dependent on high-priority QoS classes due to the delay-sensitive nature of packet-based voice.
*   **QoS Dependency**: To prevent issues like clipping, delay, and dropped calls, VoLTE relies entirely on high-priority QoS classes, specifically the `conversational-voice` class.
*   **Latency Policy Revisions for `conversational-voice`**:
    *   Historically, the QoS Policy set a one-way packet latency budget of **100 ms** with a packet loss target under **1%** for the `conversational-voice` class.
    *   Following an investigation into a dropped-call incident, it was determined that the 100 ms budget was too lenient, allowing call quality degradation in the 80–100 ms range without triggering alarms.
    *   Consequently, the one-way latency target for `conversational-voice` carrying VoLTE has been tightened to **80 ms**, superseding the previous 100 ms policy. Monitoring has been updated to trigger a warning at 70 ms and an alarm at 80 ms.

## Integration with Policy Enforcement

QoS mechanisms are also integrated with billing and policy functions to manage subscriber data usage effectively.
*   **Throttling**: When a subscriber exceeds their high-speed data allowance threshold, the charging system signals the policy function. This function then transitions the subscriber's traffic to a lower-priority QoS class for the remainder of their billing cycle, rather than terminating the session.

## Source References
*   [Copy of QoS Policy Doc](1K6Yoj4uE_IwHJHezZKDCY5bC_URWnCHE9BSm5dSd1-0)
*   [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of Dropped Calls Postmortem](145vwcMxn2xKFP5uxq624N5QnBZEbU-Wton8ZUI8QwD0)
*   [Copy of Billing Charging System Overview](1GPtX16AkNHHRYrkUk87lsfDHuMLXYVcVV3RycBtHexE)
*   [Copy of Customer Care Handbook](1mGNA1aQHvYEJS6N1cmr5N3nkTkZ8fX7Hjz-IvFOd_3o)

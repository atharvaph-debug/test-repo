# Quality of Service Overview

Quality of Service (QoS) refers to network traffic prioritization mechanisms configured against performance targets like latency, packet loss, and throughput constraints. These mechanisms ensure specific performance levels for different types of network traffic by using standardized QoS class identifiers. QoS is also known as QoS and QoS class metadata.

## Key Features and Metadata Management

QoS extensively uses metadata to define and manage performance targets for various traffic classes. Network operators enforce these standardized QoS class identifiers end-to-end, from the radio scheduler to the core transport, when sessions are established. Changes to these class targets require formal Architecture review.

### QoS Classes and Performance Metadata

*   **Conversational Voice (VoLTE):** This is the highest priority traffic class, vital for Voice over LTE (VoLTE) calls which carry voice as packets. Its performance metadata includes:
    *   **One-Way Latency Budget:** Historically targeted 100 ms. An immediate metadata update tightened this to 80 ms following operational failures, as the 100 ms threshold was too high.
    *   **Packet Loss Target:** Less than 1%.
    *   **Guaranteed Bit Rate:** Must align with the specific voice codec in use.
    *   **Failure Impact:** Exceeding the latency budget or failing to place VoLTE on this class results in audio clipping, delay, and dropped calls.
    Alarm systems rely directly on this QoS metadata and were re-tuned to trigger exactly at 80 ms, with warnings configured at 70 ms to prevent call degradation and churn.

*   **Real-Time Streaming:** A high-priority class, more tolerant of delay than conversational voice.

*   **Interactive / Best-Effort Data:** These are the default priority classes used for general internet traffic.

### Dynamic QoS Metadata Updates

QoS class metadata can be dynamically altered based on subscriber activity and billing cycles:
*   **Billing Cycles:** Telecom billing systems map subscribers to staggered billing cycles, which represent recurring usage aggregation periods. In Prepaid plans, the "billing cycle" specifically refers to allowance/quota resets.
*   **Data Allowance Thresholds:** If a subscriber crosses a high-speed data allowance threshold, real-time charging systems signal the policy function to alter the subscriber's QoS class metadata. This triggers downstream packet "throttling" for the remainder of that billing cycle.

## Aliases

*   QoS
*   QoS class metadata

## Source References

*   Postmortem: Metro Region Dropped-Calls Incident
*   Churn Analysis — Quarterly Report
*   Billing & Charging System Overview
*   Customer Care Handbook
*   Network Engineering Glossary
*   Quality of Service (QoS) Policy
*   Number Portability Process SOP

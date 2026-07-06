# Quality of Service Overview

Quality of Service (QoS) refers to network traffic prioritization policies designed to ensure target latencies and performance bounds for real-time services. It involves network policies that provide differentiated treatment to various classes of traffic, such as conversational voice, real-time streaming, and interactive data. This approach is crucial to prevent high-volume, best-effort traffic, like large file downloads, from degrading the performance of real-time services, including Voice over LTE (VoLTE).

## Key Policies and Metrics

A key aspect of QoS involves setting and adjusting performance targets for critical services. For instance, to safeguard conversational-voice classes, the one-way latency target for Voice over LTE (VoLTE) has been tightened. The target was adjusted from 100 ms to a maximum threshold of 80 ms.

## Source References
* [Postmortem: Metro Region Dropped-Calls Incident](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585217)
* [Quality of Service (QoS) Policy](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8683521)

# Quality of Service Policy Overview

A Quality of Service Policy defines performance mechanisms used to prioritize network traffic based on specific latency, packet loss, and throughput targets. This particular policy is specifically tuned for Voice-over-LTE (VoLTE) services, ensuring optimal performance for real-time voice communications.

## Aliases

The terms "Voice-over-LTE," "VoLTE," and "IMS voice" all semantically map to this identical core service and its associated Quality of Service Policy.

## Key Features

The Quality of Service Policy for conversational voice traffic has undergone a significant modification to its targets. Following a regional incident involving call drops, the one-way packet latency target was tightened from **100 ms to 80 ms**. This adjustment was made to better accommodate modern VoLTE codecs and their associated jitter profiles, aiming to prevent similar incidents and improve voice quality.

## Source References
* [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)
* [Postmortem: Metro Region Dropped-Calls Incident](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8585217)

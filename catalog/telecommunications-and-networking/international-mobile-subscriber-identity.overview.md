# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is a globally unique identifier for a mobile subscriber. It is provisioned directly onto the SIM card and registered in central subscriber databases like the Home Subscriber Server (HSS) or Home Location Register (HLR). The IMSI serves as the core identifier used by mobile networks to recognize, authenticate, and grant access to a subscriber when their device attempts to connect.

## Core Identity and Provisioning

The IMSI is the globally unique identity of a mobile subscriber. Every physical SIM card must be provisioned with an IMSI during the SIM personalization phase, where it is written directly to the SIM card. Concurrently, this identifier is registered in central subscriber databases such as the Home Subscriber Server (HSS) or Home Location Register (HLR) to facilitate network operations.

## Role in Network Operations

The mobile network uses the IMSI as the primary means to recognize, authenticate, and authorize a subscriber's access. While the IMSI handles subscriber network entry, it is distinct from the Access Point Name (APN), which determines what destination network or services the subscriber can actually access. A subscriber's operational data profile must link their unique IMSI to one or more APNs to govern network connectivity and routing rules.

## Roaming Authentication

International roaming processes heavily rely on the IMSI to differentiate home subscribers from visiting subscribers on a visited network. The authentication sequence for roaming involves:
1.  A roaming device attempts to attach to a visited network.
2.  The visited network reads the IMSI from the device.
3.  The visited network identifies the subscriber's home operator using the IMSI prefix.
4.  The visited network routes a signal to the home operator to authenticate the subscriber and authorize service delivery.

## Source References

*   [Roaming Partner Agreement — Summary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519701)
*   [Telecom Systems & Terminology Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552489)
*   [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)
*   [SIM Provisioning Runbook](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8749057)

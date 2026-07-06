# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is a globally unique identifier provisioned onto a SIM card during personalization. It functions as the core authentication credential and an anchor for all subscriber services, both on the home network and during roaming. While "SIM identity" is sometimes used loosely, engineering documentation strictly uses "IMSI" to refer to this identifier.

## Definition and Core Role

The IMSI is registered in the Home Subscriber Server (HSS) or Home Location Register (HLR) and is essential for subscriber services. It serves as the fundamental join key for identifying "which subscriber" across various records, including subscriber records, session logs, and roaming transactions. Visited networks utilize the IMSI to identify the home operator and authenticate travelers, and it is crucial for reconciling charges in bilateral roaming agreements against defined IMSI ranges and services.

## Lifecycle and Operations

The provisioning workflow involves several steps where the IMSI plays a critical role:
1.  **Personalization:** The SIM is personalized with the IMSI and associated security keys.
2.  **Registration:** The IMSI is registered in the HSS/HLR under the correct service plan.
3.  **Troubleshooting:** If network attachment fails, it often indicates that the IMSI is unregistered or that a key mismatch has occurred.

A subscriber's data profile, linked to their IMSI, contains one or more Access Point Names (APNs). While the IMSI identifies the subscriber, APNs are identifiers used by a device to route data sessions through specific packet data gateways.

## Metadata Context

As a unique identifier, the IMSI is a central piece of metadata for telecommunications systems. It acts as the primary key linking subscriber information to service usage, authentication events, and financial settlements across different network entities and roaming partners. Understanding its provisioning, registration, and usage is key to comprehending subscriber lifecycle management and network operations.

## Source References
*   [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
*   [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
*   [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)
*   [Copy of Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ)

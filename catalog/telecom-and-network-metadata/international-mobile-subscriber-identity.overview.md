# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is the globally unique identifier assigned to a mobile subscriber. It is provisioned onto the Subscriber Identity Module (SIM) during personalization and registered within the operator's subscriber databases, such as the Home Subscriber Server (HSS) or Home Location Register (HLR). The IMSI is critical for network connection authentication, both in the subscriber's home network and when roaming.

## Key Features and Data Role

The IMSI serves as a foundational piece of metadata in telecom systems:

*   **Globally Unique Identifier**: It uniquely identifies "who is this subscriber?" and must be authenticated before any network session can be established.
*   **Authentication Key**: Used for authenticating subscribers on both home and roaming networks.
*   **Metadata Join Key**: It acts as the primary join key across various subscriber records, session logs, and roaming bilateral agreements to accurately resolve and link data pertaining to a specific subscriber. For instance, the IMSI range prefix is used to resolve the "Visited Network Identifier" when a subscriber is operating outside their home coverage.
*   **Provisioning and Registration**: The IMSI is written to the SIM card and registered in the HSS/HLR. Misconfiguration or lack of registration in these databases will lead to an "Attach Fail" error, preventing the device from connecting to the network.
*   **Nomenclature**: Engineers should prefer the term "IMSI" in technical documentation over the less precise "SIM identity" to maintain clarity and consistency.

## Conceptual Distinction

The IMSI's primary role is to establish the identity of the subscriber, distinguishing it from other identifiers like the Access Point Name (APN), which determines the network or service for an authenticated session.

## Source References

*   Network Engineering Glossary
*   SIM Provisioning Runbook
*   Telecom Systems & Terminology Overview

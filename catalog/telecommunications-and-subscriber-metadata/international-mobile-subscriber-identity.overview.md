# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is a globally unique identifier for a mobile subscriber, provisioned onto the physical SIM card. It serves as the primary key for authentication and network attachments, essential for mobile telecommunications systems.

## Key Features and Role

*   **Globally Unique Identifier**: The IMSI is the unique identifier of a subscriber, stored directly on the SIM card.
*   **Primary Key for Network Interaction**: It functions as the primary key reference for networks to authenticate subscribers, manage home connections, and handle roaming.
*   **Roaming and Billing**: IMSI ranges are used in roaming and billing processes to distinguish between a network's home subscribers and visiting subscribers on partner networks.
*   **Network Attachment**: When an IMSI is unregistered, it can lead to network attachment failures, which is a common fault metadata point.
*   **Terminology**: In engineering documentation, it is recommended to prefer the term "IMSI" over the more general "SIM identity."

## Metadata Enrichment and Use Cases

For metadata enrichment, the IMSI is crucial as it represents the fundamental identifier for "which subscriber." In subscriber records, network signaling, and session logs, the IMSI must be treated as the foundational join key for accurate data correlation and analysis.

## Source References

*   Network Engineering Glossary
*   Telecom Systems & Terminology Overview
*   SIM Provisioning Runbook
*   Roaming Partner Agreement — Summary

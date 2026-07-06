# International Mobile Subscriber Identity (IMSI) Overview

The International Mobile Subscriber Identity (IMSI) is the globally unique identifier provisioned onto a SIM card. It acts as the subscriber's "passport" within telecommunications networks and serves as the primary anchor for all subscriber information.

## Aliases

The IMSI is sometimes informally referred to as "SIM identity". For engineering metadata, "IMSI" is the standardized term.

## Definition and Role

The IMSI is the globally unique identifier of a subscriber. It is provisioned onto a SIM card and is critical for network operations, acting as the primary join key for connecting subscriber-level network records and log files. It anchors all subscriber-related information, providing a unified identifier for "which subscriber" across various data sources.

## Operational Aspects

*   **Provisioning:** The IMSI is written to the SIM during its personalization phase and simultaneously registered in the subscriber database (typically the Home Subscriber Server - HSS, or Home Location Register - HLR).
*   **Authentication:** When a device attempts to connect to a network, the home network authenticates the IMSI. Without a valid and registered IMSI, the device cannot successfully authenticate or attach to the network.
*   **Roaming:** In roaming scenarios, the visited network reads the IMSI to identify the subscriber's home operator. It then signals the home network for authentication and service authorization. Specific IMSI ranges are used to determine which subscribers are covered under bilateral roaming agreements.

## Impact of Misconfiguration

Misconfiguring or failing to correctly register the IMSI will lead to complete device attachment failure, preventing the subscriber from accessing network services.

## Metadata Enrichment Relevance

Given its role as the globally unique subscriber identifier and the anchor for all subscriber information, the IMSI is foundational for metadata enrichment. It serves as the primary key to link diverse network logs, operational records, and customer data to a specific subscriber, enabling comprehensive analysis and troubleshooting of subscriber-level activities and issues.

## Source References

*   Network Engineering Glossary
*   Telecom Systems & Terminology Overview
*   SIM Provisioning Runbook
*   Roaming Partner Agreement — Summary

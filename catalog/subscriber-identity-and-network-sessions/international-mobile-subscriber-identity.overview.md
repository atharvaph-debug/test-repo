# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is a globally unique identifier provisioned onto the physical SIM card, serving as the subscriber's digital passport. It proves identity to the home network and allows a visited network to locate and verify the home operator. The IMSI is crucial for network authentication, roaming, and data logging.

## Key Features and Role

*   **Globally Unique Identifier**: IMSI is the unique identity of a subscriber, stored on the physical SIM card.
*   **Network Authentication**: Before any session can be established, the network must authenticate the IMSI. Misconfiguration of the IMSI prevents a device from attaching to the network at all.
*   **Roaming**: In roaming scenarios, networks use IMSI ranges to differentiate home subscribers from those of a visited network. The visited network reads the IMSI to identify the home operator, signaling back to authenticate the subscriber and authorize service under bilateral wholesale terms.
*   **Data Analysis and Metadata Enrichment**: In subscriber records and network session logs, the IMSI acts as the primary join key. It is used to resolve "which subscriber" initiated an action, providing a fundamental piece of metadata for understanding user activity.
*   **Terminology**: While "SIM identity" is a loose synonym, "International Mobile Subscriber Identity" or "IMSI" is the preferred term in engineering documentation.
*   **Distinction from APN**: The IMSI answers the question "who is this subscriber?", distinguishing it from the Access Point Name (APN), which answers "what network/service is this session for?".

## Source References

*   [Telecom Systems & Terminology Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552489)
*   [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)
*   [Roaming Partner Agreement — Summary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8519701)

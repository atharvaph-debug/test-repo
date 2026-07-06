# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is the globally unique identifier for a mobile subscriber. It is provisioned onto the physical or electronic SIM card during personalization and registered in the central subscriber database (HSS/HLR). The network uses the IMSI to recognize and authenticate subscribers, whether they are on their home network or roaming.

## Core Identity and Network Function

The IMSI functions as the subscriber's "passport" to both home and visited networks. It serves as the anchor for all services and policies assigned to a subscriber; without a valid, registered IMSI, network attach actions will fail. Its misconfiguration results in a complete failure of the device to attach to the network.

## Foundational Metadata Element and Key

The IMSI is an absolute foundational metadata element for subscriber identity. Almost all network actions begin by resolving the IMSI, and it serves as the primary join key in subscriber records and session logs to determine "which subscriber" is active. While the IMSI answers "who is the subscriber," an Access Point Name (APN) defines "what network or service a session is for." Unlike an IMSI misconfiguration, which prevents network attachment, an APN misconfiguration allows a device to attach to the network but prevents it from accessing the intended service.

## Role in Roaming and Inter-Operator Settlement

IMSI ranges are crucial as policy keys in roaming partner agreements. They differentiate home subscribers from visiting roamers, serving as metadata to authorize services (such as data or VoLTE) and apply wholesale inter-operator charges. Settlement analysts and roaming managers utilize real-time usage exchange and rate tables for wholesale billing based on this information.

## Source References
* [Copy of Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
* [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
* [Copy of Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)
* [Copy of Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ)

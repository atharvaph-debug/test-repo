# International Mobile Subscriber Identity Overview

The International Mobile Subscriber Identity (IMSI) is a globally unique identifier crucial for mobile telecommunications. It is stored on the physical SIM card and serves to identify and authenticate a subscriber within mobile networks, whether they are connecting at home or roaming.

## Definition and Purpose
The IMSI is a unique subscriber identifier that answers the question "Who is this subscriber?" It is provisioned onto the SIM card and registered in the subscriber database, known as the Home Subscriber Server (HSS) or Home Location Register (HLR) [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U), [Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ).

## Operational Role
Networks utilize the IMSI to recognize and authenticate a subscriber attempting to connect. It acts as the primary join key for subscriber records and session logs, linking various data points related to a subscriber's activity [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U), [Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ).

## Usage in Roaming and Billing
For roaming subscribers, partner networks identify "visited" subscribers by reading their IMSI. This identifier is mapped against ranges specified by the home operator, which triggers wholesale billing and settlement workflows based on pre-negotiated rates for voice, messaging, and data services [Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ).

## Provisioning Context
Making a subscriber usable involves personalizing the SIM card with the IMSI and associated security keys, as well as registering the IMSI in the HSS/HLR. An unregistered IMSI or a key mismatch will lead to an attach failure, preventing the subscriber from connecting to the network [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA).

## Aliases
In non-engineering contexts, the IMSI is often referred to as "SIM identity" [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U).

## Source References
* [Network Engineering Glossary](https://docs.google.com/document/d/1jdHG_-0mgrVIOR10oZf5bF44j9qXkp9UEGnppu4v30U)
* [Copy of SIM Provisioning Runbook](1r8JdSHyWNkmXNa3_di80tSJJaBeJMPKAzB2_J-IzJdA)
* [Telecom Systems Terminology Overview](1LPeSLuvREqR9ql9k32aWivsTU8kUWQmH-bi10HPcwZQ)
* [Roaming Partner Agreement Summary](1hevfD6a2hojbAU42dp215AX7mN-KY0sLIeJSowu6LcQ)

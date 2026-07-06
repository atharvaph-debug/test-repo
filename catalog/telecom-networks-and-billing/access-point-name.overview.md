# Access Point Name Overview

An **Access Point Name (APN)** is a critical identifier presented by a cellular device to the network, indicating the specific packet data network it wishes to connect to. It acts as a routing instruction for the core network, determining which gateway to use and what data policies should be applied for the data session.

## Key Functionality and Purpose

The primary role of an APN is to designate the packet data network to which a session should connect. When a device presents an APN, it directs the core network to:
*   **Select the appropriate gateway**: This routes the data session to the intended network.
*   **Apply specific data policies**: These policies govern how the data session is handled.

Essentially, the APN tells the core network how to route a data session through its infrastructure.

## Examples

Subscribers can be mapped to multiple APNs simultaneously to serve different purposes. Common examples include:
*   A **general internet APN** for standard web browsing and data services.
*   A separate **IMS APN** (IP Multimedia Subsystem Access Point Name) specifically to route voice signaling for services like Voice over LTE (VoLTE).

## Aliases

This entry may also be referred to by the following aliases:
*   apn
*   access-point-names
*   access-routing

## Related Concepts

While APNs handle data session routing, other identifiers like the **International Mobile Subscriber Identity (IMSI)** are used for subscriber authentication and authorization. Both are fundamental components in establishing cellular network access and managing subscriber services.

## Source References
*   [Telecom Systems & Terminology Overview](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8552489)
*   [Network Engineering Glossary](https://atharva-test-izfs7ihz.atlassian.net/wiki/spaces/KCD/pages/8617985)

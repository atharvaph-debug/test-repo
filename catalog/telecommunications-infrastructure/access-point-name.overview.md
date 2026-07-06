# Access Point Name Overview

An Access Point Name (APN), also known as APN, is a piece of metadata that identifies the target packet data network, selects the appropriate gateway, and determines the policy parameters for a subscriber's data session. It is the identifier presented by a device to route its data session through a specific core gateway to a targeted packet data network. In logs, the APN indicates "which service/network" a session used.

## Key Features and Role

The APN serves several critical metadata functions in telecommunications:
*   **Target Network Identification:** It specifies the particular packet data network (e.g., public internet or an internal IMS APN for voice signaling) to which a device's data session should connect.
*   **Gateway Selection:** The APN dictates which core gateway is selected to route the data session.
*   **Policy Determination:** It defines the policy set that applies to a subscriber's data session.
*   **Session Context:** In operational logs, the APN provides crucial metadata, indicating the specific service or network a data session utilized. For instance, a general internet APN is used for standard data, while a specialized IMS APN might be used for VoLTE signaling.

## Operational Rules and Impact

*   **Subscriber Data Profile:** Every subscriber data profile must map one or more APNs. This mapping ensures that the device can access the intended services.
*   **Misconfiguration Impact:** A critical consequence of misconfiguration or absence of an APN is the "attached but no data" state. This occurs even if the IMSI (International Mobile Subscriber Identity) authentication is correct, meaning the device is authenticated to the network but cannot exchange data.

## Aliases

*   APN

## Source References
*   Network Engineering Glossary
*   Telecom Systems & Terminology Overview
*   SIM Provisioning Runbook

# Access Point Name Metadata Overview

Access Point Name (APN) Metadata refers to the logical packet network identifier that a mobile device presents to a network. It specifies which packet data network (PDN) and gateway a data session should be routed through, determining the service gateway and dynamic routing policies applied to that session.

## Key Features

An APN is crucial for establishing data connections, as it names the specific packet data network a session connects to, thereby selecting the appropriate gateway and policies for that session. Examples include a public-internet APN or an internal IMS APN used for voice signaling (e.g., for VoLTE).

## Metadata Enrichment Use Cases

For metadata enrichment, APNs serve as a critical identifier in session logs, representing "which service/network" a session accessed. This allows for distinguishing between different types of sessions, such as a general internet APN from an IMS APN used for VoLTE signaling. In common fault metadata, "Attached but no data" alerts often indicate missing or misconfigured APN data profiles, in contrast to network attachment failures which typically map to unregistered IMSIs.

## Aliases

*   APN

## Source References

*   Network Engineering Glossary
*   Telecom Systems & Terminology Overview

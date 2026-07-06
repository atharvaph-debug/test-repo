# Quality of Service Overview

Quality of Service (QoS), also known as qos, refers to network policies and targets designed to configure traffic prioritization to prevent degradation in critical real-time services. Its primary purpose is to manage network resources to ensure that essential applications and services receive the necessary performance levels.

## Key Features

QoS is used to prevent issues like large file downloads from consuming bandwidth needed by critical services such as live voice calls. It achieves this by assigning specific priority ratings and performance targets to different traffic classes. These targets are based on key network performance parameters including latency, packet loss, and jitter.

For instance, the standing QoS policy for the conversational-voice class has a packet latency budget of 100 ms. However, postmortem analysis has indicated that call quality degrades, exhibiting clipping and drops, within the 80–100 ms latency band without triggering system alarms. This highlights a monitoring blindspot, necessitating VoLTE QoS target modifications. These modifications are crucial to resolve the observed call quality issues.

## Source References

*   [Copy of Dropped Calls Postmortem.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7BBD2C2B47-FBAC-4778-AEC8-28A556556CE6%7D&file=Copy%20of%20Dropped%20Calls%20Postmortem.docx&action=default&mobileredirect=true)
*   [Copy of QoS Policy Doc.docx](https://atharvasptest.sharepoint.com/sites/agent-demo/_layouts/15/Doc.aspx?sourcedoc=%7B2EF9FBD3-5015-454C-8A3A-AC1332142749%7D&file=Copy%20of%20QoS%20Policy%20Doc.docx&action=default&mobileredirect=true)

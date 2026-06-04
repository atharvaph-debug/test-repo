---
userManaged: true
---
# Table Documentation: ucs_gaab_gwslog_stats

## Overview
The `ucs_gaab_gwslog_stats` table provides aggregated user-level statistics derived from Google Web Server (GWS) logs. It encapsulates key metrics such as request volume and error rates to facilitate user behavior analysis, and system health checks. 

## Usage Guidelines
- **Partitioning:** This table is date-partitioned. Always include a date filter on the aggregation timestamp in your queries to optimize performance and control querying costs.
- **Monitoring:** Utilize the `request_count` to measure overall user engagement and `error_count` to identify anomalous spikes indicating potential client-side or service issues.
- **Access Management:** Ensure you have the `bigquery.dataViewer` IAM role on the `concord-prod.analysis_userlevel` dataset before attempting to run analytical queries.

---
userManaged: true
---
# BigQuery Table Documentation: `cloud_apis`

## Overview
The `cloud_apis` table is a unified source for Google Cloud API usage logs. It combines logs from various sources including OnePlatform (OP), Apiary, SourceRepo, and GCS to provide a comprehensive view of API activities across Google Cloud services.

- **Project**: `concord-prod`
- **Dataset**: `analysis_userlevel`
- **Table Name**: `cloud_apis`
- **PRD**: [go/cloud-unified-api-table-prd](http://go/cloud-unified-api-table-prd)
- **FAQ**: [go/cloud_apis_faq](http://go/cloud_apis_faq)

## Ownership
- **Owners**: `siyuch`, `cloudmill-eng` (Google Group)
- **Bug Component**: 1432229

## Data Sources
The table aggregates data from the following input sources:
- **Apiary**: `concord-prod:analysis_userlevel.apiary_cloud_usage_1_7_30_day_aggregates`
- **OnePlatform (OP)**: `concord-prod:analysis_userlevel.cloud_apis_usage`
- **SourceRepo**: `concord-prod:analysis_userlevel.sourcerepo_access_log_with_facts`
- **GCS**: `concord-prod:analysis_userlevel.gcs_api_v2`
- **Project Facts**: `concord-prod:analysis_entity.project_facts` (used for internal/first-party classification)

## Related Tables
- `concord-prod.analysis_userlevel.cloud_apis_usage`: A downstream table containing unique services used by any person.
- `concord-prod.analysis_entity.project_facts`: Provides metadata about projects, such as internal status.

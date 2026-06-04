---
userManaged: true
---
# Table Documentation: semantic_search_usage

## Overview
The `semantic_search_usage` table is a Tier 1 synthesized datamart that aggregates API telemetry and interaction metrics specifically for the **Knowledge Catalog Discovery Agent** and **Semantic Search** infrastructure. It acts as the primary analytical foundation for product managers and engineering teams to monitor Semantic Search adoption, backend performance, and retrieval latency.

## Key Usage Scenarios
1. **Adoption & CUJ Monitoring**: Analyze usage across different `execution_mode` parameters (e.g., fast, medium, thinking) to evaluate how users leverage the Discovery Agent for their Critical User Journeys (CUJs).
2. **Performance Diagnostics**: Track `latency_ms` and `response_code` to ensure strict SLAs (such as the <=500ms bounds for 1-hop subgraph discovery) are met during complex `multi_search` orchestrations.
3. **Traffic Attribution**: Use the `referrer` field to properly attribute semantic query traffic across the internal UI, automated probers, and external integration tools.
4. **Token Optimization**: Evaluate `tokens_used` against API volumes to manage LookupContext bounds and maintain LLM token budgets dynamically.

## Core Architecture
- **Source**: Edge Security Filter (ESF) Sawmill logs generated natively by Dataplex Catalog Search services. 
- **Pipeline**: Processed daily via the Concord pipeline to map technical log components into business-friendly dimensions. 
- **Privacy Considerations**: Fully adheres to privacy specifications by securely substituting user and organization references with standard Concord privacy blocks (pseudonymized identifiers).

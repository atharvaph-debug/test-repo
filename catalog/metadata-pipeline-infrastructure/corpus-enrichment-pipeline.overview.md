# Corpus Enrichment Pipeline Overview

The Corpus Enrichment Pipeline (CEP), also known as `corpus-enricher`, is a seed pipeline responsible for ingesting raw documents and enhancing internal document corpuses with structured metadata attributes. This system is designed to enrich documents with valuable structural and semantic metadata. It falls under the `Metadata Pipeline Infrastructure` category.

## Role and Scope of Metadata Enrichment

The Corpus Enrichment Pipeline facilitates the creation and maintenance of a comprehensive metadata layer, crucial for data continuity, operational efficiency, and regulatory compliance across various domains. It captures and harmonizes diverse metadata types, enabling clear definitions, consistent terminology, and accurate data relationships.

Key areas of metadata enrichment include:

*   **Unified Glossaries and Terminology Reconciliation:**
    The pipeline addresses disparate terms used across business units by establishing single, authoritative definitions. This includes reconciling synonyms (e.g., "Customer Lifetime Value" (CLV) and "LTV", "IMSI" and "SIM identity", "VoLTE" and "IMS voice", "Local Number Portability" (LNP) and "Mobile Number Portability" (MNP), "SKU" and "item number", "Safety stock" and "buffer stock"). It also clarifies conceptual distinctions, such as "Credit Risk Score" (default likelihood) versus "KYC Risk Rating" (financial-crime risk).
*   **Business Metrics and Financial Definitions:**
    It defines key financial metrics such as "Customer Lifetime Value" (CLV), "Net Interest Margin" (NIM), and "Liquidity Coverage Ratio" (LCR), including their calculations and strategic uses.
*   **Supply Chain, Inventory, and Product Identity:**
    The pipeline structures metadata around inventory identifiers like "SKU" (Stock Keeping Unit) and external standards like "UPC/GTIN". It establishes mapping rules to prevent data quality issues such as double-counting and defines structural relationships through the "Bill of Materials" (BOM), which links finished goods to their components.
*   **Parametric Metadata and System Configuration Rules:**
    It centralizes dynamic operational parameters such as "Reorder Point" (ROP) with its authoritative formula (`average daily demand × lead time in days + safety stock`) and "Safety Stock" levels, which are policy-driven based on SKU velocity classifications (e.g., 14, 10, or 7 days of supply for Class A, B, and C respectively). Lead time definitions, lead-time drift triggers, and "Supplier Scorecards" (based on on-time delivery, quality, and price competitiveness) are also managed.
*   **Subscriber and Network Metadata (Telecom):**
    For telecom operations, the pipeline defines core entities like "International Mobile Subscriber Identity" (IMSI) as a primary join key for subscriber records and "Access Point Name" (APN) to determine network segment and policy. It also includes Quality of Service (QoS) metadata (e.g., latency and packet loss targets for "Conversational Voice Class" (VoLTE)) and roaming metadata such as "Visited Network Identifier" and "Wholesale Settlement Rates".
*   **Trade Operations and Settlements Metadata:**
    Metadata related to financial transaction processing is captured, including "Settlement Timing" (e.g., T+1 for equities), "Settlement Cutoff Time" (historically 16:00 ET, updated to 15:30 ET), and the "Settlement Fail Flag" which triggers re-attempts and escalations.
*   **Financial Risk and Compliance Metadata:**
    Critical risk control metrics like "Credit Risk Score" and "Liquidity Coverage Ratio" (LCR) are defined, including their formulas, regulatory floors (e.g., Basel III), and internal management targets (e.g., 110% for LCR).
*   **Operational Checklists and Policy Metadata:**
    Even procedural metadata for retail operations, such as "Security Metadata" (alarm state), "Inventory Verification," "Merchandising Compliance" (planogram, price list), and "Financial Reconciliation" are included, highlighting the broad application of metadata enrichment.

This pipeline ensures that document corpuses are not just collections of text but rich, structured information sources, enabling accurate reporting, automated processes, and informed decision-making.

## Source References
* AML Investigations Playbook
* Basel III Regulatory Filing — Internal Summary
* Bill of Materials — Engineering Specification
* Billing & Charging System Overview
* Churn Analysis — Quarterly Report
* Compliance Policy Handbook
* Corporate Travel & Expense Policy
* Customer Care Handbook
* Customer Onboarding SOP
* Demand Planning — Weekly Sync Notes
* Finance Business Glossary
* Inventory Management Glossary
* Inventory Policy Memo
* Inventory Systems Overview
* Logistics Network Overview
* Marketing Analytics — Deck Notes
* Network Engineering Glossary
* Number Portability Process SOP
* Postmortem: Metro Region Dropped-Calls Incident
* Postmortem: Q3 Apparel Class-A Stockouts
* Postmortem: Settlement Cutoff Migration Delay
* Procurement Standard Operating Procedure
* Quality of Service (QoS) Policy
* Retail Store Opening Checklist
* Risk Management Framework
* Roaming Partner Agreement — Summary
* SIM Provisioning Runbook
* Supplier Onboarding Guide
* Telecom Systems & Terminology Overview
* Trade Operations Runbook
* Treasury Operations Guide
* Warehouse Operations Runbook
* [example-corpus-enrichment](https://docs.google.com/document/d/example-corpus-enrichment)

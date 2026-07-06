# Semantic Metadata Generator Overview

The Semantic Metadata Generator is an automated pipeline designed for metadata extraction and enrichment. It functions as an enrichment engine that translates technical operational schemas into standardized business taxonomies. Its primary function is to analyze unstructured documents, identifying and extracting key entities, topics, and taxonomies, then enriching these documents by appending the extracted information as structured metadata attributes.

## Aliases

This entry is also known by the aliases: `smg`, and `semantic-metadata-enrichment-tool`.

## Supported Metadata Domains and Concepts

The Semantic Metadata Generator facilitates the enrichment of metadata across diverse operational and business domains by defining, standardizing, and mapping key terminologies and relationships. This includes:

*   **Customer Profiles and Financial-Crime Risk Metadata:** Captures metadata related to Know Your Customer (KYC) / Customer Due Diligence (CDD) verification, financial-crime risk ratings (distinct from credit risk scores), and how this metadata guides downstream transaction monitoring and Anti-Money Laundering (AML) investigations. It includes specifics on investigation workflow metadata and regulatory Suspicious Activity Report (SAR) constraints.
*   **Subscriber Lifecycle, Billing, and Telecommunications Metadata:** Addresses metadata related to billing system operations (rating vs. billing phases, postpaid/prepaid plans), number portability (LNP/MNP, porting state tracking), and subscriber churn analytics (identifying churn drivers, risk profiles, Customer Lifetime Value (CLV/LTV)).
*   **Network Quality of Service (QoS) and Charging System Integration:** Defines metadata for network policy functions (dynamic signaling, data throttling), and Voice-over-LTE (VoLTE) performance targets, including QoS class dependencies and latency specifications. Key identifiers like IMSI (International Mobile Subscriber Identity) and APN (Access Point Name) are foundational for network and subscriber session mapping.
*   **Operational Assets, Supply Chain, and Inventory Metadata:** Encompasses metadata for Bill of Materials (BOM) specifications (hierarchy, reusability, versioning), inventory policy control parameters (safety stock, reorder point), and core identifiers like Stock Keeping Units (SKU) and Universal Product Codes (UPC/GTIN). It also includes metrics like lead time and supplier scorecard parameters.
*   **Regulatory Liquidity Reporting and Financial Risk Metadata:** Covers authoritative terminology and regulatory metrics such as the Liquidity Coverage Ratio (LCR), including its definition, calculation constraints (HQLA, net cash outflows), and regulatory floor limits. It also specifies the Net Interest Margin (NIM) formula and the distinct role of Credit Risk Scores in financial assessment. Trade settlement timing metadata (e.g., T+1 settlement and processing cutoffs) is also a key area for metadata alignment.
*   **Corporate Compliance and Expense Governance:** Involves metadata for corporate travel and expense policies (booking channels, flight class, lodging/meals, ground transportation), financial control (submission timelines, receipt thresholds), and approval routing based on policy adherence.

The enrichment process involves understanding and applying system rules, active parameter updates (e.g., safety stock adjustments), and synchronization of metadata values across various operational runbooks and policy documents to ensure accuracy and compliance.

## Source References

*   AML Investigations Playbook
*   Basel III Regulatory Filing — Internal Summary
*   Bill of Materials — Engineering Specification
*   Billing & Charging System Overview
*   Churn Analysis — Quarterly Report
*   Compliance Policy Handbook
*   Corporate Travel & Expense Policy
*   Customer Care Handbook
*   Customer Onboarding SOP
*   Demand Planning — Weekly Sync Notes
*   dropped_calls_postmortem.md
*   Finance Business Glossary
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Logistics Network Overview
*   Marketing Analytics — Deck Notes
*   Network Engineering Glossary
*   Number Portability Process SOP
*   Postmortem: Metro Region Dropped-Calls Incident
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Postmortem: Settlement Cutoff Migration Delay
*   Procurement Standard Operating Procedure
*   Quality of Service (QoS) Policy
*   Risk Management Framework
*   Roaming Partner Agreement — Summary
*   SIM Provisioning Runbook
*   Supplier Onboarding Guide
*   Telecom Systems & Terminology Overview
*   Trade Operations Runbook
*   Treasury Operations Guide
*   Warehouse Operations Runbook

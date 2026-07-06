# Unified Catalog Platform Overview

The Unified Catalog Platform is a centralized infrastructure platform designed to host corporate data definitions, structural metadata, and data access policies. It serves as the primary implementation of the Metadata Enrichment project, which aims to build a coherent, cross-referenced data dictionary and rule set for the enterprise, facilitating comprehensive data discovery and consistent metadata tagging.

## Key Features

The platform centralizes various types of enriched schemas, data lineage, and operational metadata. It encompasses:

*   **Enriched Schemas and Domain Glossaries:** The platform provides detailed and enhanced descriptions of data structures and establishes core conceptual models and identifiers across systems to prevent analytical errors. This includes:
    *   **Finance Metadata:** Definitions for `Customer Lifetime Value (CLV)` (distinguishing it from "Customer LTV" and "LTV"), `Net Interest Margin (NIM)`, and `Credit Risk Score`.
    *   **Inventory & Supply Chain Metadata:** Definitions for `SKU` (clarifying its internal nature versus `UPC/GTIN`), `Bill of Materials (BOM)` as a structured recipe, `Lead Time`, `Safety Stock`, and `Reorder Point (ROP)`.
    *   **Telecommunications Metadata:** Definitions for `APN (Access Point Name)` (for data session routing), `IMSI (International Mobile Subscriber Identity)` (as the unique subscriber identifier, distinct from "SIM identity"), `QoS (Quality of Service)` mechanisms, `VoLTE` (synonymous with "Voice-over-LTE" and "IMS voice"), and `Number Portability` (encompassing "LNP" and "MNP").
*   **Operational Metadata and Dynamic Rules:** The platform stores critical operational parameters, formulas, and system configuration metadata, including:
    *   **Customer & Compliance Metadata:** Rules for `KYC risk rating` (standard or enhanced), the distinction between `financial-crime risk metadata` (KYC risk rating) and `credit risk metadata` (credit risk score), and requirements for `AML Suspicious Activity Reports (SARs)`.
    *   **Telecom Service & Network Quality Metadata:** Specific `QoS performance targets` such as the VoLTE one-way latency target (updated from 100 ms to 80 ms, with warnings at 70 ms) and packet loss targets, and parameters for `billing cycles` (including how they represent allowance resets for prepaid plans) and `QoS class metadata` changes for throttling. The `Conversational Voice` (VoLTE) class is prioritized with specific latency and packet loss targets.
    *   **Product Supply Chain & Inventory Metadata:** The multi-level `hierarchical Bill of Materials (BOM)` capturing component identity and per-parent quantity metadata, `Safety Stock` (cushion for demand variability), and `Reorder Point` (trigger for replenishment).
    *   **Inventory Planning & Replenishment Formulas:** The formula for `Reorder Point (ROP)`:
        $$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
        and `Safety Stock Categorization` based on SKU velocity (Class A: 14 days initially, updated to 21 days for apparel; Class B: 10 days; Class C: 7 days).
    *   **Supplier Management:** `Supplier Scorecard Parameters` including on-time delivery, quality control, and price competitiveness, which determine purchase order volume allocation. Planned lead times are validated through trial orders.
    *   **Logistics Network & Routing Metadata:** `Node Types` (Regional DCs, Forward DCs), `Lead Time Parameters` (inbound, inter-node), and `Routing Logic` for order fulfillment (selecting nearest DC, fallback routines).
    *   **Financial Risk & Trade Operations Metadata:** `Liquidity Coverage Ratio (LCR)` with an internal target of 110%, `Trade Settlement Cutoff Rules` (T+1 basis, with the current cutoff at 15:30 ET, superseding the legacy 16:00 ET). `Corporate Travel & Expense Compliance` rules cover booking, flight tiers, submission timelines, and receipt thresholds.
*   **Data Lineage:** Tracks hierarchical relationships, such as the `Bill of Materials` structure that enables "exploding" finished-good demand for component-level purchasing schedules, and routing logic within logistics.

The platform is critical for ensuring data integrity, consistent operational behavior, and enterprise-wide data discovery by centralizing and standardizing these diverse metadata types and rules.

## Source References
*   Customer Onboarding SOP
*   Compliance Policy Handbook
*   AML Investigations Playbook
*   Postmortem: Metro Region Dropped-Calls Incident
*   Churn Analysis — Quarterly Report
*   Customer Care Handbook
*   Billing & Charging System Overview
*   Bill of Materials — Engineering Specification
*   Demand Planning — Weekly Sync Notes
*   Finance Business Glossary
*   Marketing Analytics — Deck Notes
*   Inventory Management Glossary
*   Inventory Policy Memo
*   Inventory Systems Overview
*   Procurement Standard Operating Procedure
*   Network Engineering Glossary
*   Number Portability Process SOP
*   Logistics Network Overview
*   Telecom Systems & Terminology Overview
*   SIM Provisioning Runbook
*   Roaming Partner Agreement — Summary
*   Quality of Service (QoS) Policy
*   Risk Management Framework
*   Trade Operations Runbook
*   Postmortem: Settlement Cutoff Migration Delay
*   Postmortem: Q3 Apparel Class-A Stockouts
*   Supplier Onboarding Guide
*   Treasury Operations Guide
*   travel_expense_policy.md
*   Warehouse Operations Runbook

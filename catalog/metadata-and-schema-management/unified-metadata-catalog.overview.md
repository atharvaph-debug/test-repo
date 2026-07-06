# Unified Metadata Catalog Overview

The Unified Metadata Catalog (UMC) serves as a centralized repository designed to store and manage enriched metadata assets. It provides capabilities for unified discovery and search across an enterprise's various data sources. This catalog acts as a central directory hosting technical definitions, schemas, and structural metadata across all operational systems.

## Aliases
This entry is also known by its aliases: `umc` and `central-metadata-repository`.

## Category
This entry falls under the "Metadata and Schema Management" category.

## Scope of Metadata Enrichment

The Unified Metadata Catalog synthesizes metadata, operational definitions, and relational concepts from across the enterprise to support robust metadata enrichment pipelines and schema development. It aims to provide structured findings, cross-domain terminologies, and system mappings, ensuring data quality and pipeline integration. Key domains of metadata enriched and maintained within the catalog include:

### Customer & Financial Risk Metadata
The catalog incorporates metadata related to customer onboarding, financial-crime risk assessment, and anti-money laundering (AML) investigations. This includes:
*   **KYC Profile Creation** and **Risk Categorization**, defining **KYC Risk Rating** (for financial-crime risk, categorizing customers for standard or enhanced due diligence) and distinguishing it from **Credit Risk Score** (quantifying borrower default likelihood based on repayment history, exposure, income, and leverage).
*   **Downstream Persistence** of both KYC risk rating and credit risk score on customer profiles.
*   **Transaction Monitoring & AML Alert Investigations** metadata, including the evaluation of customer identity, expected activity, and risk rating during investigations, and metadata constraints for **Suspicious Activity Report (SAR)** filing (e.g., confidentiality and time-bounded windows).

### Subscriber Lifecycle & Telecommunications Metadata
It details metadata linking customer care operations, commercial lifecycle statuses, and billing system logic. This encompasses:
*   **Billing and Charge Rating Systems** metadata, distinguishing between the `Rating` phase (applying price plan metadata to usage events) and the `Billing` phase (aggregating charges).
*   **Plan-Type Attributes** such as `Postpaid` (usage invoiced in arrears) and `Prepaid` (usage decremented in real-time).
*   **Number Portability Metadata**, represented interchangeably as `Porting`, `LNP` (Local Number Portability), or `MNP` (Mobile Number Portability), and tracking of `validation window` statuses.
*   **Churn and Customer Attrition Analytics** metadata, defining `Customer churn` and `customer attrition` as identical commercial measures, and identifying **Churn Driver Segmentation** (e.g., Price, Network Quality) and **Risk Profiles & Stickiness Attributes** like contract status and product depth.
*   **Customer Lifetime Value (CLV / LTV)**, defined as the total net profit expected from a customer.

### Network Quality of Service (QoS) & Provisioning Metadata
This domain covers parameters, real-time data throttling, and Voice-over-LTE (VoLTE) performance targets:
*   **Policy Function & Data Throttling Integration**, where charging systems signal network policy functions to assign lower-priority QoS classes.
*   **VoLTE (Voice over LTE)**, also known as `Voice-over-LTE` or `IMS Voice`, which carries voice calls as packets over the LTE data network.
*   **QoS Class Dependency** for VoLTE traffic, requiring the "conversational-voice" QoS class with specific performance targets for packet latency ($\le 100\text{ ms}$, or tightened to 80 ms for modern codecs) and packet loss ($< 1\%$).
*   **IMSI (International Mobile Subscriber Identity)** as the globally unique subscriber identifier on the SIM card, serving as the primary key for authentication and inter-operator routing.
*   **APN (Access Point Name)** as the identifier for which packet data network a session connects to.

### Operational Assets, Supply Chain & Inventory Metadata
The catalog includes metadata structures for engineering designs, manufacturing procurement, and retail inventory management:
*   **Bill of Materials (BOM)**, a multi-level tree structure for finished goods, sub-assemblies, and components, defined once and strictly versioned.
*   **Inventory Policy Control Parameters** such as **Safety Stock** (cushion against demand variability, e.g., 14 days for Class A SKUs, 10 for Class B, 7 for Class C, or updated to 21 days for Class-A apparel SKUs) and **Reorder Point (ROP)**, calculated as $(\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$.
*   **SKU (Stock Keeping Unit)** as the internal identifier for a distinct, sellable product variant, distinct from **UPC / GTIN** (an external barcode standard).
*   **Lead Time** as the total duration from purchase order (PO) placement to goods availability, including inbound and inter-node lead times.
*   **Supplier Scorecard (Vendor Rating)**, combining on-time delivery, quality, and price competitiveness.

### Regulatory & Corporate Compliance Metadata
Metadata supporting banking compliance, treasury operations, and internal corporate policies:
*   **Liquidity Coverage Ratio (LCR)** rules, a Basel III regulatory metric calculated as $\text{HQLA} / \text{Total Net Cash Outflows over 30 Days}$, with a regulatory minimum floor of 100%.
*   **Net Interest Margin (NIM)**, a profitability metric calculated as $(\text{Interest Income} - \text{Interest Expense}) / \text{Average Earning Assets}$.
*   **T+1 Settlement** for trade finalization.
*   **Settlement Processing Cutoffs**, with updates to `15:30 ET` for trade settlement operations, superseding a legacy `16:00 ET` cutoff.
*   **Corporate Travel and Expense Rules**, covering booking channels, flight class policies, lodging/meal caps, ground transportation, submission timelines, receipt thresholds, corporate card governance, and approval routing logic.

## Source References
*   AML Investigations Playbook
*   Basel III Regulatory Filing — Internal Summary
*   Billing & Charging System Overview
*   Bill of Materials — Engineering Specification
*   Churn Analysis — Quarterly Report
*   Compliance Policy Handbook
*   Corporate Travel & Expense Policy
*   Customer Care Handbook
*   Customer Onboarding SOP
*   Demand Planning — Weekly Sync Notes
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

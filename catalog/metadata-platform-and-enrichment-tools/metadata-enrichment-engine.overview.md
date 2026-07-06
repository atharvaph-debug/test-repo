# Metadata Enrichment Engine Overview

The Metadata Enrichment Engine (MEE), also known as a metadata-enricher, is a computing system designed to automatically analyze raw assets and append metadata tags, properties, and relationships. It serves as a core framework for enhancing metadata quality and discoverability within data systems by managing and applying domain-specific definitions, operational rules, and conceptual schemas.

This engine is central to the "Metadata Enrichment" project, which consolidates business terminology, technical parameters, and operational metadata across various enterprise domains, enabling consistent tagging, preventing analytical errors, and supporting automated system actions.

## Key Metadata Domains and Rules

The Metadata Enrichment Engine would be responsible for processing and applying rules and definitions across several critical domains:

### Customer Profiles, Risk Ratings, & Compliance Metadata
The engine handles metadata related to customer risk and compliance, including:
*   **Customer Risk Profiles & KYC Metadata**: Establishes and stores Know Your Customer (KYC) risk ratings (standard or enhanced) at onboarding, which determines required scrutiny and monitoring. It distinguishes financial-crime risk metadata (KYC risk rating) from credit risk metadata (credit risk score), ensuring both reside as separate attributes on customer profiles. Stale KYC metadata is considered a significant audit finding requiring remediation.
*   **AML Suspicious Activity Metadata**: Processes rigorous, evidence-based metadata for Suspicious Activity Reports (SARs), requiring specific details rather than vague rationales.

### Telecom Service & Network Quality Metadata
For telecommunications operations, the engine manages schemas for performance monitoring and subscription lifecycles:
*   **Network Latency & Class Budgets (QoS Metadata)**: Maintains Quality of Service (QoS) classes with specific performance targets. For example, it updates VoLTE one-way latency targets from a legacy 100 ms to 80 ms, with warnings configured at 70 ms to prevent call degradation. Alarm systems rely on these QoS metadata thresholds. The engine would manage QoS class identifiers end-to-end, distinguishing:
    *   **Conversational Voice (VoLTE)**: Highest priority, targeting 80 ms one-way latency, < 1% packet loss, and guaranteed bit rate.
    *   **Real-Time Streaming**: High priority, tolerant of slightly higher delay.
    *   **Interactive / Best-Effort Data**: Default for general internet traffic.
*   **Subscriber Terminology & Portability Alignment**: Consolidates metadata definitions for CRM and agent routing, such as "Porting," "LNP," and "MNP" all mapping to "Number Portability." Similarly, "customer attrition" and "customer churn" are unified as the same system measure.
    *   **IMSI (International Mobile Subscriber Identity)**: The globally unique subscriber identifier on the SIM card, serving as the primary anchor and join key for subscriber information and network authentication. Misconfiguration leads to device attachment failure. Engineering metadata standardizes on "IMSI" over "SIM identity."
    *   **APN (Access Point Name)**: Identifies the target packet data network, selects the appropriate gateway, and determines the policy set for a subscriber's data session. Misconfigured APNs can result in "attached but no data" states.
*   **Billing and Charging Metadata**: Maps subscribers to staggered billing cycles for processing loads. In Prepaid plans, the "billing cycle" represents allowance/quota resets. The engine can trigger downstream packet "throttling" by altering a subscriber's QoS class metadata if a data allowance threshold is crossed within a billing cycle.

### Product Supply Chain & Inventory Metadata
The engine handles hierarchical structures and policy variables for engineering, manufacturing, and inventory systems:
*   **Hierarchical Bill of Materials (BOM) Metadata**: Manages the multi-level hierarchical metadata tree linking finished-good SKUs to component and sub-assembly identity and per-parent quantity metadata. This structure enables "exploding" finished-good demand for purchasing schedules, with no alterations permitted outside the version-controlled BOM metadata schema.
*   **Inventory Policy Metadata**: Uses attributes like **Safety Stock** (cushion for demand variability) and **Reorder Point** (trigger for replenishment).
    *   **Safety Stock Categorization (Velocity Classes)**: Configured as "days of supply" and parameterized by SKU velocity. Historically, Class A (Fast Movers) required 14 days, Class B (Medium Movers) 10 days, and Class C (Slow Movers) 7 days. An update for Class A SKUs in apparel raised the standard to **21 days of supply** due to high demand variability.
    *   **Reorder Point (ROP) Calculation**:
        $$ROP = (\text{Average Daily Demand} \times \text{Lead Time in Days}) + \text{Safety Stock}$$
    *   **SKU (Stock Keeping Unit)**: The fundamental internal identifier for a distinct, sellable product variant, tracked at a granular level. It is distinct from UPC/GTIN (Universal Product Code/Global Trade Item Number), an external barcode standard, and treating them interchangeably causes analytical errors. Inventory must be scanned to the exact SKU.
    *   **Lead Time**: Total elapsed time from placing a purchase order to when goods are available, with trial orders used to establish a reliable baseline.
*   **Supplier Scorecard Parameters**: Generates rolling performance metrics for each supplier-part combination based on on-time delivery percentage, quality control, and price competitiveness. Higher-rated suppliers automatically receive a larger share of purchase order volume.
*   **Network Graph & Logistics Routing Metadata**: Models the logistics network with node types like Regional DCs and Forward DCs. Uses Lead Time Parameters (Inbound, Inter-node) and Routing Logic to select the nearest fulfillment node with available inventory, falling back to other nodes if out of stock.
*   **System Workflows & Escalation Mappings**: Integrates with and informs processes like Inbound Inventory Intake (receive, inspect, putaway) and Outbound Fulfillment (picks, batching, packing, manifesting). It generates alerts and escalations for issues like mismatched POs (to Procurement) or persistent stockouts (to Demand Planning).

### Financial Risk and Trade Operations Metadata
The engine helps maintain financial controls and reporting:
*   **Customer Lifetime Value (CLV)**: Defines the total net profit expected from a customer. Synonyms like "Customer LTV" and "LTV" are mapped to this single metadata concept.
*   **Net Interest Margin (NIM)**: A balance-sheet profitability metric, calculated as:
    $$\text{NIM} = \frac{\text{Interest Income} - \text{Interest Expense}}{\text{Average Earning Assets}}$$
*   **Credit Risk Score**: A borrower-level metric estimating default likelihood, distinct from KYC risk rating.
*   **Liquidity Coverage Ratio (LCR)**: The ratio of high-quality liquid assets to projected net cash outflows over 30 days, with an internal management target of 110%.
*   **Trade Settlement Rules**: Governs the finalization of trades. Equities and most fixed-income instruments settle on a T+1 basis. The processing cutoff for trades is **15:30 ET** (updated from a legacy 16:00 ET), with instructions after this time rolling to the next business day.
*   **Corporate Travel & Expense Compliance**: Enforces booking rules (approved tools, manager approval for out-of-tool), flight tier policies (economy standard, premium economy for 6+ hours with director sign-off), submission timelines (within 30 days), and receipt thresholds.

## Source References
*   [example-mee-doc](https://docs.google.com/document/d/example-mee-doc/edit)
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

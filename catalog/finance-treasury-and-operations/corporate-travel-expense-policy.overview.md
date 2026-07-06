# Corporate Travel Expense Policy Overview

The Corporate Travel Expense Policy (`travel-expense-policy`) defines the corporate guidelines and systemic constraints governing employee reimbursement limits, receipt thresholds, and exception approval processes for business travel. It functions as a critical set of metadata schemas enabling programmatic audit and automated expense report validation within the Finance, Treasury, and Operations domain.

## Purpose and Application

This policy is designed to facilitate programmatic audit and automated validation of expense reports. The rules embedded within the policy act as metadata configurations that systems use to evaluate, approve, or flag travel-related expenditures.

## Key Policy Metadata

The policy defines various metadata attributes and their corresponding values or conditions for different expense categories:

### Lodging and Transportation Rules
*   **Booking Channel:** Mandates the use of the approved corporate travel tool. Bookings made outside this tool are flagged as exceptions requiring manager approval.
*   **Flight Class Threshold:** Specifies that flights under 6 hours are restricted to Economy Class (Standard), while flights of 6 hours or more permit Premium Economy, which requires Director sign-off.
*   **Nightly Lodging Limits:** Expense systems apply caps based on published per-city nightly limits.
*   **Ground Transportation:** Allows reimbursement for standard ride-share or taxi services, while luxury tiers are strictly non-reimbursable.
*   **Personal Vehicle Mileage:** Reimbursable at the standard published mileage rate.

### Allowances and Exception Routing Rules
*   **Daily Meals:** Governed by published per-diem tables, which are indexed by city.
*   **Client Entertainment:** Requires documentation of a business purpose and an attendee list.
*   **Corporate Card Segregation:** Mandates that mixed personal/corporate expenses be flagged, with the personal portion requiring immediate reimbursement.
*   **Submission Windows:** Defines a standard submission window of within 30 days of the spend date. Claims older than 60 days trigger an exception flag and require specific approval.
*   **Receipt Threshold:** Itemized receipts are programmatically required for any expense exceeding a predefined standard receipt threshold.

## Exception Handling and Approval Workflow

The policy integrates an approval routing tree that is dynamically applied based on metadata conditions:
*   **Standard Report:** Follows a Claimant $\rightarrow$ Manager $\rightarrow$ Payment workflow.
*   **Exception Flagged Report:** Reports that contain policy violations or are older than 60 days follow an escalated workflow: Claimant $\rightarrow$ Manager $\rightarrow$ Finance Shared Services $\rightarrow$ Payment.

## Source References
*   [Copy of Travel Expense Policy](1tSCGhnctQOuy4Vdjz7IArJ7B6n-PJBlO29Z0ipKc-UE)

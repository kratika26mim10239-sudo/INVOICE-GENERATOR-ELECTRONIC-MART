``markdown
# Problem Statement & System Requirements

## Context
Electronics retail outlets handle multiple fast-paced customer transactions daily. Paper receipts are easy to lose, and dedicated POS hardware can be cost-prohibitive for smaller stores.

## Objective
Develop a lightweight desktop application in Python that allows store clerks to:
1. Register customer details (Name, Contact Number).
2. Enter multiple purchased items (Description, Quantity, Unit Price).
3. Review total amounts dynamically.
4. Export a formatted PDF invoice for customer records and printing.

## Functional Requirements
- **FR-1**: Tkinter-based user interface with validation for non-negative numerical inputs.
- **FR-2**: Real-time recalculation of item-line totals and grand totals.
- **FR-3**: PDF generation containing store metadata, item breakdown, invoice timestamp, and legal warranty text using `reportlab`.

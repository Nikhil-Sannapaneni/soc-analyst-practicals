# Module 08 — Detection Engineering

## Detection Concept

Detect repeated failed authentication followed by a successful login from the same source.

## Logic

1. Count failed authentication events by source and account.
2. Apply a time window.
3. Identify a subsequent successful login.
4. Exclude known administrative automation where appropriate.
5. Generate an alert for analyst review.

## Detection Quality

Document:

- Data source
- Query
- Threshold
- Time window
- False-positive considerations
- Severity rationale
- ATT&CK mapping
- Test cases

Potential ATT&CK mapping: **T1110 — Brute Force**.

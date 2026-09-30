# Module 06 — Threat Hunting

## Hypothesis

A compromised endpoint may show unusual process execution followed by an unexpected outbound network connection.

## Hunt Plan

Search for:

- Unusual parent-child process relationships
- New or rare executables
- Unexpected PowerShell or scripting activity
- New persistence mechanisms
- Rare outbound destinations
- Authentication anomalies

## Hunt Cycle

**Hypothesis → Data sources → Query → Triage → Evidence → Conclusion → Detection improvement**

A hunt conclusion must distinguish confirmed evidence from assumptions.

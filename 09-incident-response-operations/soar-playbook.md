# SOAR Playbook — Suspicious IP Investigation

## Trigger

A SIEM detection identifies a suspicious source IP.

## Steps

1. Create incident.
2. Extract source IP.
3. Validate indicator format.
4. Enrich through an approved threat-intelligence source.
5. Add enrichment to the incident.
6. Assign analyst.
7. Escalate if confidence is high.
8. Record outcome.

## Guardrails

- Never automatically block an indicator solely because it appears in an unverified feed.
- Require approval for disruptive actions.
- Log every automated action.
- Keep credentials and API keys outside GitHub.

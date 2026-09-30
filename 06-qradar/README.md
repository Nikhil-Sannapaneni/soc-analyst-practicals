# 06 — IBM QRadar SIEM

## Project: QRadar Investigation Lab

This project uses documented/simulated data so the portfolio does not imply access to a production QRadar environment.

### Core Areas
- Events and flows
- Ariel Query Language (AQL)
- Offense management
- Assets
- Reports
- Dashboards

### Example AQL Patterns

Search recent events:

```sql
SELECT * FROM events
LAST 1 HOURS
```

Count events by source IP:

```sql
SELECT sourceIP, COUNT(*) AS event_count
FROM events
GROUP BY sourceIP
ORDER BY event_count DESC
LAST 1 HOURS
```

> Exact field names depend on the QRadar environment and DSM configuration. Validate queries against the target lab.

### Analyst Workflow

**Event → AQL search → correlation → offense → investigation → response**


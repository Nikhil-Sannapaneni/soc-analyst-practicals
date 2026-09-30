# 07 — Splunk Security Operations

## Project: Splunk Detection Lab

This project focuses on SPL, ingestion, knowledge objects, alerts and dashboards using safe sample data.

### SPL Fundamentals

Search all events:

```
index=security
```

Failed authentication:

```
index=security action=failure
```

Count by source:

```
index=security action=failure
| stats count by src_ip
| sort - count
```

Successful login after failures should be investigated using time windows and correlation rather than a single event.

### Splunk Topics
- Apps and add-ons
- Data ingestion
- SPL
- Data models / pivots
- Knowledge objects
- Alerts
- Dashboards

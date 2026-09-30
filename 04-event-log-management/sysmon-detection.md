# Sysmon Detection Exercise

## Scenario

A Windows endpoint generates process-creation telemetry.

## Detection Fields

Review:
- Image
- CommandLine
- ParentImage
- User
- ProcessId
- Hash
- DestinationIp where network telemetry is available

## Investigation

Compare the process with the normal endpoint baseline and investigate unusual parent-child relationships.

### Analyst Principle

A suspicious command line is an investigation lead, not automatic proof of compromise.

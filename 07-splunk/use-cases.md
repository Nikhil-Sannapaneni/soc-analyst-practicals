# Splunk SOC Use Cases

## 1. Brute-Force Indicator

```
index=security action=failure
| stats count by user, src_ip
| where count >= 5
```

## 2. Suspicious Process

Search process telemetry for unusual command lines and parent-child relationships.

## 3. Phishing Indicator

Search email/security telemetry for suspicious domains or URLs.

### Tuning

Every detection should document:
- Threshold
- Time window
- Exclusions
- Expected false positives
- Severity
- ATT&CK technique

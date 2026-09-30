# Microsoft Sentinel KQL Practice

## Failed authentication

A generic practice pattern:

```kusto
SigninLogs
| where ResultType != 0
| summarize FailedAttempts=count() by UserPrincipalName, IPAddress
| order by FailedAttempts desc
```

## Investigation Notes

Document:
- Time range
- User
- Source IP
- Result code
- Geographic/contextual information available in the authorised tenant
- Correlated endpoint/network activity

Field availability depends on the connected Microsoft data source.

# Module 02 — Log Analysis

## Scenario

A SOC analyst receives authentication logs containing successful and failed login attempts.

## Investigation

Look for:

- Repeated failed authentication
- Successful login after multiple failures
- Unusual usernames
- Unusual source IP addresses
- Activity outside the expected baseline

## Example Linux commands

```bash
grep -i "failed" auth.log
grep -i "accepted" auth.log
awk '{print $1,$2,$3,$9,$11}' auth.log
```

## Analyst Output

Record:

- Timestamp
- Username
- Source IP
- Event
- Evidence
- Assessment
- Recommended action

## ATT&CK

Potential mapping: **T1110 — Brute Force**, when the evidence supports repeated password-guessing behaviour.

# Module 04 — Phishing Email Analysis

## Objective

Practise analysing a suspicious email without opening unsafe attachments or links.

## Analysis Checklist

- Sender address
- Reply-To address
- Subject
- Authentication results
- Received headers
- URLs
- Domain age/reputation where authorised tools are available
- Attachment name and type
- Urgency or credential-request indicators

## Safe Workflow

1. Preserve the original message.
2. Extract indicators.
3. Defang URLs for documentation.
4. Analyse headers.
5. Check indicators using approved security tools.
6. Map confirmed behaviour to ATT&CK.
7. Recommend containment and user notification when appropriate.

Potential ATT&CK technique: **T1566 — Phishing**.

Never upload confidential company emails or personal information to a public repository.

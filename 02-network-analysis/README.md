# 02 — Network Traffic Analysis

## Project: Network Investigation Lab

### Tools
- Wireshark
- tcpdump

### Practical Tasks
1. Capture traffic in an authorised lab.
2. Identify source and destination IPs.
3. Identify TCP/UDP ports.
4. Inspect DNS queries.
5. Follow a TCP stream where appropriate.
6. Identify unusual connection patterns.
7. Document evidence.

### Useful tcpdump commands

```bash
sudo tcpdump -i any
sudo tcpdump -i any port 53
sudo tcpdump -i any tcp
sudo tcpdump -nn -r capture.pcap
```

### Investigation Questions
- What hosts communicated?
- Which protocols were used?
- Were there repeated connection attempts?
- Were unusual ports observed?
- Does the traffic match the expected baseline?

Only analyse traffic you are authorised to capture.

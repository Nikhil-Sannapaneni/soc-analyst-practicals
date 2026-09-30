#!/usr/bin/env python3
"""Simple defensive authentication-log analyser for lab data."""

from collections import Counter
import re
import sys

FAILED = re.compile(r"Failed password .* from (\S+)")
ACCEPTED = re.compile(r"Accepted .* for (\S+) from (\S+)")

def analyse(path: str) -> None:
    failed_sources = Counter()
    successful_logins = []

    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = FAILED.search(line)
            if match:
                failed_sources[match.group(1)] += 1

            match = ACCEPTED.search(line)
            if match:
                successful_logins.append(
                    {"user": match.group(1), "source": match.group(2)}
                )

    print("Failed authentication sources:")
    for source, count in failed_sources.most_common():
        print(f"  {source}: {count}")

    print("\nSuccessful logins:")
    for item in successful_logins:
        print(f"  {item['user']} from {item['source']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 log_analyser.py <auth.log>")
    analyse(sys.argv[1])

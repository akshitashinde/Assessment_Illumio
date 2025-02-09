Flow Log Parser
Overview
This script processes AWS flow log files, matches them with a lookup table, and generates reports on matched tags and port/protocol combinations.

Features
Parses AWS VPC flow logs (version 2 only).
Matches logs with a lookup table for tagging.
Counts occurrences of each tag and each port/protocol combination.
Writes output to a structured file.
Assumptions
The script only supports AWS default flow log format (not custom).
Only version 2 logs are processed.
TCP/UDP are mapped using protocol number (6 → TCP, 17 → UDP).
Case-insensitive comparisons for protocol names.
If no tag matches, it is categorized as "Untagged".
Malformed log entries are ignored.

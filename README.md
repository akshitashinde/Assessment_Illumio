Overview
The Flow Log Parser is a simple Python script that processes AWS VPC flow logs (version 2) and maps each log entry to a tag based on a lookup table. This tool helps in analyzing network traffic, categorizing logs, and understanding the distribution of different ports and protocols.

🔹 Why This Project?

Helps security teams analyze network traffic.
Assists in troubleshooting blocked/rejected connections.
Organizes logs into human-readable reports.
📂 Project Structure

flow-log-parser/
│── flow_log_parser.py      # The main Python script
│── flow_logs.txt           # Sample flow log file
│── lookup.csv              # Lookup table for mapping tags
│── output.txt              # Output report (generated after running the script)
│── README.md               # Documentation (this file)
🛠 How It Works
Reads the flow log file (flow_logs.txt).
Extracts port & protocol information from each log entry.
Matches the log entries to the lookup table (lookup.csv) to assign tags.
Counts the occurrences of each tag and port/protocol combination.
Generates an output file (output.txt) with structured results.
📌 Assumptions & Rules
✅ The script only supports AWS default log format (version 2).
✅ Protocols are matched case-insensitively (e.g., tcp, TCP are treated the same).
✅ If no matching tag is found, the entry is marked as "Untagged".
✅ Handles malformed log entries by skipping them.
✅ Supports up to 10MB log files and 10,000 lookup entries.

🚀 Getting Started
🔧 Prerequisites
Python 3.x (Make sure Python is installed on your system).
No external libraries required (runs on pure Python).
💻 Running the Script

 Run the Script

python flow_log_parser.py flow_logs.txt lookup.csv output.txt

View the Output
Check the output.txt file for results.

📊 Sample Input & Output
📝 Sample Log File (flow_logs.txt)

2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
2 123456789012 eni-9h8g7f6e 172.16.0.100 203.0.113.102 110 49156 6 12 9000 1620140761 1620140821 ACCEPT OK
📋 Sample Lookup File (lookup.csv)

dstport,protocol,tag
25,tcp,sv_P1
23,tcp,sv_P1
443,tcp,sv_P2
110,tcp,email
993,tcp,email
143,tcp,email
📌 Generated Output (output.txt)
Tag Counts
mathematica

Tag,Count
sv_P2,1
sv_P1,2
email,1
Untagged,0
Port/Protocol Combination Counts
mathematica

Port,Protocol,Count
23,tcp,1
25,tcp,1
110,tcp,1
443,tcp,1
🛠 How It Works Internally
Reads the flow log file line-by-line.
Extracts:
Destination Port (Column 6)
Protocol (Column 7 → converted from number to name)
Checks the Lookup Table (lookup.csv):
If a matching (Port, Protocol) pair is found → Assigns the Tag
If no match → Categorized as "Untagged"
Counts the occurrences of each tag & port/protocol combo.
Writes the summary report to output.txt.
🧪 Testing & Validation
✅ Edge Cases Covered
✔ Unknown Ports & Protocols → Correctly categorized as "Untagged".
✔ Malformed Logs → Skipped without crashing.
✔ Case Insensitivity → tcp and TCP treated the same.
✔ Large Input Handling → Supports up to 10MB files.

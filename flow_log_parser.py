import csv
import sys
from collections import defaultdict

def load_lookup_table(lookup_file):
    """Loads the lookup table from a CSV file into a dictionary."""
    lookup_dict = {}
    try:
        with open(lookup_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) != 3:
                    continue  # Skip malformed lines
                dstport, protocol, tag = row
                key = (dstport.strip().lower(), protocol.strip().lower())
                lookup_dict[key] = tag.strip()
    except FileNotFoundError:
        print("Lookup file not found!")
        sys.exit(1)
    return lookup_dict

def process_flow_logs(flow_file, lookup_dict):
    """Processes flow logs and maps entries to tags."""
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    try:
        with open(flow_file, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) < 13:
                    continue  # Skip malformed lines

                dstport = parts[5].strip().lower()
                protocol = "tcp" if parts[7] == "6" else "udp" if parts[7] == "17" else "unknown"
                key = (dstport, protocol)

                tag = lookup_dict.get(key, "Untagged")
                tag_counts[tag] += 1
                port_protocol_counts[key] += 1
    except FileNotFoundError:
        print("Flow log file not found!")
        sys.exit(1)

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    """Writes the processed output to a file."""
    with open(output_file, 'w') as file:
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")

        file.write("\nPort/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <flow_log_file> <lookup_file> <output_file>")
        sys.exit(1)

    flow_file = sys.argv[1]
    lookup_file = sys.argv[2]
    output_file = sys.argv[3]

    lookup_dict = load_lookup_table(lookup_file)
    tag_counts, port_protocol_counts = process_flow_logs(flow_file, lookup_dict)
    write_output(tag_counts, port_protocol_counts, output_file)

    print("Processing completed. Results saved to", output_file)

if __name__ == "__main__":
    main()

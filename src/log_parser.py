"""
log_parser.py
Author: Wessel
Purpose: Parse log files, filter suspicious events (WARNING/ERROR),
         and display them with timestamp and IP.
"""

for line in logs:
    # Check if line contains WARNING or ERROR
    if "WARNING" in line or "ERROR" in line:
        # Extract timestamp
        timestamp = re.search(timestamp_pattern, line).group()
        # Extract IP if present
        ip_match = re.search(ip_pattern, line)
        ip = ip_match.group() if ip_match else "N/A"
        # Extract message content after timestamp and level
        message = line.strip().split(" ", 3)[3]
        print(f"Timestamp: {timestamp}, IP: {ip}, Event: {message}")

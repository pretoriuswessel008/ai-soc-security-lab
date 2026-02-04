"""
soc_monitor.py
Author: Wessel
Purpose: Detect brute-force login attempts and AI-style anomalies.
         Generates alerts in terminal and writes them to 'soc_alerts.txt'.
"""

# Count failed login attempts per IP
for line in logs:
    ip_match = re.search(ip_pattern, line)
    if ip_match:
        ip = ip_match.group()
        total_events[ip] += 1

        if "Failed login" in line:
            failed_logins[ip] += 1

# Simple AI-style anomaly detection
average_events = sum(total_events.values()) / len(total_events) if total_events else 0
anomaly_threshold = average_events * 2

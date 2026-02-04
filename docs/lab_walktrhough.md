# AI SOC Security Lab – Walkthrough

## 1. Overview
This lab simulates a simplified Security Operations Center (SOC) monitoring pipeline.
It demonstrates how raw log data is transformed into actionable security alerts using
rule-based logic and AI-style anomaly detection.

The goal is to understand **how security tools think**, not just how to use them.

---

## 2. Log Ingestion
Logs are read from a static log file (`sample.log`) to simulate real-world system or application logs.

Key concepts:
- Centralized log collection
- Structured vs unstructured data
- Security visibility

---

## 3. Log Parsing
Regular expressions are used to extract:
- Timestamps
- IP addresses
- Event messages

Why this matters:
SOC tools must normalize raw logs before analysis.

---

## 4. Security Event Filtering
The system filters for:
- WARNING events
- ERROR events

This reduces noise and focuses analyst attention on events that matter.

---

## 5. Brute-Force Detection
Failed login attempts are counted per IP address.
If an IP exceeds a defined threshold, it is flagged as suspicious.

Security concepts demonstrated:
- Brute-force attack detection
- Event correlation
- Threshold-based alerts

---

## 6. Alert Generation
Suspicious activity generates alerts that:
- Appear in the terminal
- Are written to an alerts file

This simulates how SOC alerts are logged and escalated.

---

## 7. AI-Style Anomaly Detection
A simple frequency-based model is used to detect abnormal behavior.

Process:
- Calculate average events per IP
- Flag IPs with activity far above normal

This represents how AI assists SOC teams by identifying patterns
without relying solely on predefined rules.

---

## 8. Automation Concept
The script is designed to be scheduled (e.g., via Task Scheduler),
simulating continuous monitoring without manual execution.

---

## 9. Key Takeaway
This lab demonstrates the internal logic behind:
- SIEM platforms
- SOAR workflows
- AI-assisted SOC monitoring

Rather than relying on enterprise tools, the lab exposes
the architectural thinking behind modern cybersecurity systems.

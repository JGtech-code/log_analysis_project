from detection import detect_failed_logins
from report import save_suspicious, generate_summary

log_file = "logs/example.log"

# Step 1: Read logs
with open(log_file, "r") as f:
    logs = f.readlines()

# Step 2: Detect anomalies
failed_logins = detect_failed_logins(logs)

# Step 3: Output suspicious logs and summary
save_suspicious(failed_logins, "suspicious_logs.txt")
generate_summary(failed_logins, "summary_report.csv")

print("Analysis complete. Reports generated.")
print(f"Suspicious entries found : {len(failed_logins)}")
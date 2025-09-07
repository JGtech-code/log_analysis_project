import pandas as pd

def save_suspicious(logs, filename):
    with open(filename, "w") as f:
        for line in logs:
            f.write(line)

def generate_summary(logs, filename):
# Ensure logs are strings
    logs = [str(line).strip() for line in logs]
    df = pd.DataFrame({"log": logs})
# Extract IP addresses
    df["ip"] = df["log"].str.extract(r"from (\d+\.\d+\.\d+\.\d+)")
# Count failed attempts
    failed_counts = df["ip"].value_counts()
# Save report
    failed_counts.to_csv(filename, index=True)
    print(f"[+] Report saved to {filename}")
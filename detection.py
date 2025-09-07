def detect_failed_logins(logs):
    suspicious = []
    for line in logs:
        if "Failed login" in line:
            suspicious.append(line)
    return suspicious
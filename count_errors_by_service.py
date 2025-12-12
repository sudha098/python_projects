def count_errors_by_service(logs):
    counts = {}
    for line in logs:
        parts = line.split()
        if len(parts) < 3:
            continue
        level = parts[2]
        if level != "ERROR":
            continue
        service = parts[3].rstrip(":")
        counts[service] = counts.get(service, 0) + 1

    return counts

logs = [
    "[2025-12-10 10:01:02] ERROR payment-service: timeout",
    "[2025-12-10 10:01:03] INFO auth-service: user login",
    "[2025-12-10 10:01:04] ERROR payment-service: failed transaction",
    "[2025-12-10 10:01:05] ERROR auth-service: token expired"
]


result = count_errors_by_service(logs)
print(result)

def count_errors_by_service_from_file(filename):
    counts = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) < 4:
                    continue
                level = parts[2]  # ERROR is at index 2
                if level != "ERROR":
                    continue
                service = parts[3].rstrip(":")  # service is at index 3
                counts[service] = counts.get(service, 0) + 1
        return counts
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}


log_file = "application.log"
result = count_errors_by_service_from_file(log_file)
print(result)

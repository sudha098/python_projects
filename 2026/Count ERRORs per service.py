def count_error_by_service(log_file_path):
    result = {}
    with open(log_file_path, "r") as logs:
        for line in logs:
            parts = line.split()
            if len(parts) >= 2 and parts[0].lower() == "error":
                service = parts[1]
                result[service] = result.get(service, 0) + 1
    return result

file_path = input("Log file path:\n")
print(count_error_by_service(file_path))

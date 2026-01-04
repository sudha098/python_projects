def count_errors(logs_file_path):
    count = 0
    with open(logs_file_path, "r") as logs_file:
        for line in logs_file:
            if "error" in line.lower():
                count += 1
    return count
file_path = input("Enter log file:\n")
print(count_errors(file_path))

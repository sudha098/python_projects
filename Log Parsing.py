from collections import defaultdict

error_count = defaultdict(int)

with open("app.log") as f:
    for line in f:
        parts = line.split()

        if len(parts) >= 2 and parts[1] == "ERROR":
            service = parts[0]
            error_count[service] += 1

for service, count in error_count.items():
    print(f"{service} : {count} errors")

import shutil

def disk_usage(disk_usage_path):
    total, used, free = shutil.disk_usage(disk_usage_path)
    return {
        "total_gb" : total // (2**30),
        "used_gb" : used // (2**30),
        "free_gb" : free // (2**30)
    }

path = input("Enter the path:\n")
usage = disk_usage(path)
print(f"Disk usage of {path} is: \n {usage}")

--------------------------------------------------------

root@host01 ~/code via 🐍 v3.12.3 ✖ python disk_usage.py 
Enter the path:
/
Disk usage of / is: 
 {'total_gb': 736, 'used_gb': 238, 'free_gb': 460}

root@host01 ~/code via 🐍 v3.12.3 ➜  python disk_usage.py 
Enter the path:
/tmp
Disk usage of /tmp is: 
 {'total_gb': 19, 'used_gb': 10, 'free_gb': 8}

root@host01 ~/code via 🐍 v3.12.3 ➜  

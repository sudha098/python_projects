import subprocess

def run_command(command):
    result = subprocess.run(command, shell = True, capture_output = True, text = True)
    return result

command = input("Enter the command\n")
result = run_command(command)
print(f"Command is: \n {command}")

if result.stdout:
    print("Output")
    print(result.stdout)
if result.stderr:
    print("Error")
    print(result.stderr)

-------------------------------

root@host01 ~/code via 🐍 v3.12.3 ➜  python run_shell_commands.py 
Enter the command
ls
Command is: 
 ls
Output
README.md
disk_usage.py
run_shell_commands.py


root@host01 ~/code via 🐍 v3.12.3 ➜  python run_shell_commands.py 
Enter the command
pwd
Command is: 
 pwd
Output
/root/code


import socket

def is_port_open(host: str, port: int, timeout: int=3) -> bool:
    """
    Check if TCP port is open on given Port 
    """
    if not (1 <= port <= 65535):
        raise ValueError("Port must be between 1 and 65535")
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, OSError):
        return False

if __name__ == "__main__":
    hostname = input("Enter host:\n").strip()
    portname = int(input("Enter port:\n").strip())
    status = is_port_open(hostname, portname)
    print(f"Port {portname} on {hostname} is {'OPEN' if status else 'CLOSED' }")


-----------------------------------------------------

root@host01 ~/code via 🐍 v3.12.3 ✖ python networking.py 
Enter host:
localhost
Enter port:
5000
Port 5000 on localhost is CLOSED

root@host01 ~/code via 🐍 v3.12.3 ➜  python networking.py 
Enter host:
localhost
Enter port:
80
Port 80 on localhost is OPEN

root@host01 ~/code via 🐍 v3.12.3 ➜  

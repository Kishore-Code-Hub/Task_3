import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                return port
    except:
        return None

def scan_ports(host):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(1, 1025)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)

    if open_ports:
        return f"Open ports on {host}: {', '.join(map(str, open_ports))}"
    else:
        return f"No open ports found on {host}."

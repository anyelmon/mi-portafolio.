import socket

objetive = "scanme.nmap.org"
ports = [80, 843, 8080, 3306, 5432]

print(f"scanning {objetive}...")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((objetive, port))
    if result == 0:
        print(f"port {port}: OPEN")
    else:
        print(f"port {port}: close")
    s.close()
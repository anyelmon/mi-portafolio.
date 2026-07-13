import socket

objective = input("Enter objective:")
results = []

print(f"\nScanning {objective}...\n")

for port in range(1, 1001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((objective, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        try:
            s.send(b"HEAD / HTTP 1.0\r\n\r\n")
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        print(f"Port {port}: OPEN | Service: {service} | Banner: {banner}")
        results.append((port, service, banner))
    s.close()

print(f"\nScan Finished.")

with open("services_results2.txt", "w") as file:
    file.write(f"Objective: {objective}\n\n")
    for port, service, banner in results:
        file.write(f"Port {port}: | {service} | {banner}\n")

print(f"\nResumen:")
print(f"Total open ports found: {len(results)}")
for port, service, banner in results:
    print(f" Port {port} -> {service}")

print("Results saved in services_results2.txt")
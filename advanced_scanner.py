import socket

objetive = input("Enter the target IP address or hostname: ")
results = []

print(f"\nScanning {objetive}...\n")

for port in range(1, 1001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((objetive, port))
    if result == 0:
        print(f"Port {port}: OPEN")
        results.append(port)
    s.close()

print(f"\nScan completed. Open ports on: {results}")

with open("results.txt", "w") as file:
    file.write(f"Objetives: {objetive}\n")
    file.write(f"Open ports: {results}\n")

print("Results saved to results.txt")
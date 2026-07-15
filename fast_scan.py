import socket
import threading

objective = input("Enter objective: ")
results = []
lock = threading.Lock()
start = int(input("port start: "))
fin = int(input("port finish: "))

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((objective, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        with lock:
            results.append((port, service))
            print(f"Port {port}: OPEN | Service: {service}")
    s.close()

print(f"\nScanning {objective}...\n")

threads = []
for port in range(start, fin + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

results.sort()
print(f"\nScan Finished. {len(results)} open ports found.")

with open("fast_results.txt", "w") as file:
    file.write(f"Objective: {objective}\n\n")
    for port, service in results:
        file.write(f"Port {port}: | {service}\n")

print("Results saved in fast_results.txt")
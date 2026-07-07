import socket

objetivo = "scanme.nmap.org"
puertos = [21, 22, 80, 443, 8080]

print(f"Escaneando {objetivo}...")

for puerto in puertos:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((objetivo, puerto))
    if resultado == 0:
        print(f"Puerto {puerto}: ABIERTO")
    else:
        print(f"Puerto {puerto}: cerrado")
    s.close()

print("Escaneo terminado.")
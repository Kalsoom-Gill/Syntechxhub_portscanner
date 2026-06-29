import socket
import threading
from datetime import datetime

print("=" * 50)
print("TCP Port Scanner")
print("=" * 50)

target = input("Enter Target IP or Website: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}")
print("Scan Started:", datetime.now())

file = open("scan_results.txt", "w")

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            message = f"Port {port}: OPEN"
        else:
            message = f"Port {port}: CLOSED"

        print(message)
        file.write(message + "\n")

        sock.close()

    except Exception as e:
        print(f"Error on port {port}: {e}")

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

file.close()

print("\nScanning Completed!")
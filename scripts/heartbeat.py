import time
import requests

NODES = ["http://localhost:8080/health", "https://your-railway-app.com/health"]

def check_system_vitals():
    for node in NODES:
        try:
            status = requests.get(node, timeout=1).status_code
            print(f"Node {node}: {'ONLINE' if status == 200 else 'OFFLINE'}")
        except:
            print(f"CRITICAL: Node {node} is UNREACHABLE")

if __name__ == "__main__":
    while True:
        check_system_vitals()
        time.sleep(60) # Run every minute

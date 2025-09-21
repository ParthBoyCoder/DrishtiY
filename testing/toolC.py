import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 send_and_play.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
PC_IP = "192.168.0.11"  # 🔥 change to your PC IP

url = f"http://{PC_IP}:5000/upload"
with open(filename, 'rb') as f:
    files = {'file': (filename, f)}
    r = requests.post(url, files=files)

print("Triggered:", r.status_code)
if r.status_code == 200:
    print(f"Uploaded and playing {filename} on PC website!")
else:
    print("Error:", r.text)

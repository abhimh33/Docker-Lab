import os

host = "www.google.com"
response = os.system(f"ping -c 4 {host}")

if response == 0:
    print("Host is reachable")
else:
    print("Host is not reachable")
import time
start = time.time()
while time.time() - start < 30:
    x = 0
    for i in range (1000000):
        x = x + i * i

print("Task complete.!!")
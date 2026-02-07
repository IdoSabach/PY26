import sys
import time

def calc(a):
    for i in range(1000000):
        a * 2

start = time.perf_counter()
calc(2**1000000)
end = time.perf_counter()
print(start)
print(end)

print(end - start)
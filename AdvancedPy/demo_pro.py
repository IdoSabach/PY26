from memory_profiler import profile
import time

@profile
def my_heavy_function():
    a = [i for i in range(1000000)]
    time.sleep(1)
    b = [i**2 for i in range(500000)]
    del a 
    return b

if __name__ == "__main__":
    my_heavy_function()
import time
import sys
sys.set_int_max_str_digits(0)

def add(x, y):
    result = 0
    result += x
    result += y
    return result


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def do_stuff():
    result = []
    for i in range(10000000):
        result.append(i ** 2)
    return result

def sleep_func():
    time.sleep(5)
    print('Hello')


if __name__ ==  "__main__":
    print(add(100, 5000))
    print(fact(70000))
    print(do_stuff())
    sleep_func()


import sys
num1 = 123_123
num2 = 877_877
print(num1+num2)

def data(obj):
    addressHex = hex(id(obj))
    size = sys.getsizeof(obj)
    refcount = sys.getrefcount(obj)
    return addressHex, size, refcount

print(data(num1),'\n',data(num2),'\n',data(num1+num2))

# BMI
# w = int(input('input your weigh!'))
# h = float(input('input your heigh!'))
# bmi = w / h**2
# print(round(bmi,2)) 

# calculate tips
cost = float(input('What was the total bill?'))
tip = int(input('how much tip would you like to give? 10,12 or 15?'))
people = int(input('how many people to split the bill?'))

sum = (cost * ((tip/100)+1)) / people

print(f'Each person should pay: {round(sum,2)}$')


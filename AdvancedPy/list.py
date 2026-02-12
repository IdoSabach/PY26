
num = [1,2,3,4,5,6,7,8,9]
my_list = []

for n in num:
    my_list.append(n)
print(my_list)

my_list1 = [n for n in num]
print(my_list1)

my_list2 = []
for n in num:
    my_list2.append(n*n)
print(my_list2)

my_list3 = (n*n for n in num)
print(my_list3)


import timeit

setup = "num = list(range(1_000_000))"

print(timeit.timeit("lst = []\nfor n in num: lst.append(n)", setup=setup, number=10))
print(timeit.timeit("lst = [n for n in num]", setup=setup, number=10))

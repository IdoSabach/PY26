import random
let = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
num = [1,2,3,4,5,6,7,8,9,0]
sign = ['!','@','#','$','%','^','&','*','-','>','<']

password = []

print('Welcome to agent Password!')
num_of_length = int(input('how long your password?'))
num_of_num = int(input('how much num?'))
num_of_sign = int(input('how much sign?'))
num_of_let = num_of_length - (num_of_num + num_of_sign)


for i in range(num_of_let):
    x = random.randrange(len(let))
    password.append(let[x])

for i in range(num_of_num):
    x = random.randrange(len(num))
    password.append(num[x])

for i in range(num_of_sign):
    x = random.randrange(len(sign))
    password.append(sign[x])

suf = random.shuffle(password)
curr = "".join(password)
print(curr)

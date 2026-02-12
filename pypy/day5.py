import random

let = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
num = ['1','2','3','4','5','6','7','8','9','0'] 
sign = ['!','@','#','$','%','^','&','*','-','>','<']

password = []

print('Welcome to agent Password!')
num_of_length = int(input('How long your password? '))
num_of_num = int(input('How many numbers? '))
num_of_sign = int(input('How many signs? '))

num_of_let = num_of_length - (num_of_num + num_of_sign)

for i in range(num_of_let):
    password.append(random.choice(let))

for i in range(num_of_num):
    password.append(random.choice(num))

for i in range(num_of_sign):
    password.append(random.choice(sign))

random.shuffle(password)

final_password = "".join(password)

print(f"Your strong password is: {final_password}")
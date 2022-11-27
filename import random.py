import random

print('Password Generator')

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*().,0123456789'

number = input('Amount of passwords to be generated: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are the passwords generated: ')

for pwd in range(number):
    passwords=''
    for c in range(length):
        passwords += random.choice(chars)
        print(passwords) 

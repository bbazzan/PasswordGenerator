import random

print('==================')
print('PASSWORD GENERATOR')
print('==================')

# String of characters to use in the password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_+=[]{}><?/!@#$%&*'

amount = int(input('Input the amount of passwords to generate: '))

length = int(input('Input the desired length of the passwords: '))

print('These are the generated passwords:')

for pwd in range(amount):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

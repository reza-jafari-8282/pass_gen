from random import randint
from string import ascii_uppercase,ascii_lowercase,digits

def passGen(pass_length):
    password = ''
    all_char = ascii_uppercase + ascii_lowercase + digits + '~!@#$%^&*()-_=+./<>'
    for length in range(pass_length):
        password += all_char[randint(0 , len(all_char) - 1)]
    return password
pass_length = int(input("Character length : "))
print(passGen(pass_length))

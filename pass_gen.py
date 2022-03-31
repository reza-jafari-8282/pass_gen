import random
import string

def passGen(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = '~!@#$%^&*()-_=+./<>'
    all = lower + upper + digits + symbols
    return "".join(random.sample(all, length))
length = int(input("Character length (n <= 81) : "))

print(passGen(length))

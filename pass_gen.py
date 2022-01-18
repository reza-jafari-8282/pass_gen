import random
import string
length = input("Character length (n <= 94) : ")
length = int(length)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all = lower + upper + digits + symbols
password = "".join(random.sample(all, length))
print(password)
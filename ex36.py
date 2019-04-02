import random

name = input("first and last name ")

namename = name.replace(" ", "")

num = random.randint(10, 1999)

gmail = "@gmail.com"

email = namename + str(num) + gmail

print(email.lower())

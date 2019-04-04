# Import random, will be used for random.randint()
import random

firstName = input("Enter your first name: ")

lastName = input("Enter your last name: ")
# The random part of the email generator will be the numbers. It could be either one, two, three, or four digits long. 
num = random.randint(1, 1199)

gmail = "@gmail.com"
#combine variables starting with lastName + "."(period) + firstName + num + gmail
email = lastName + "." + firstName + num + gmail
# use .lower() function to make entire email lower case no matter the input.
print(email.lower())

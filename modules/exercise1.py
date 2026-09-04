# Write a function which generates a six digit/character random_user_id.
from random import random, randint
import secrets
import string
def random_user_id(start, end):
    return randint(start,end)


def generate_random_userId() -> str:
    characters = string.ascii_letters + string.digits
    user_id = ''.join(secrets.choice(characters) for _  in range(6))
    
    return user_id
    

"""
print("Let's create a random user id \n Please type a range of two numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(random_user_id(num1,num2))
"""

#print(generate_random_userId())

def generate_random_userId() -> str:
    
    characters = string.ascii_letters + string.digits
    user_id = ''.join(secrets.choice(characters) for _  in range(int(input("Please type the number of characters you want in your generated user id"))))
    number_of_ids = int(input("Please type how many ids do you want to generate: "))
    if number_of_ids == 0 or number_of_ids>2:
          for i in range(number_of_ids):
                user_id = ''.join(secrets.choice(characters) for _  in range(int(input("Please type the number of characters you want in your generated user id {i}"))))
        
    return user_id

print(generate_random_userId())
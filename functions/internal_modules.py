import math #(here I am importing the module from python)

sqrt_value = math.sqrt(25)
print(f"SQRT: {sqrt_value}")
print(math.pi)
print(f"Fac: {math.factorial(5)}")

# module is nothing but a python file
import random

# return a number between 1 and 10
value = random.randint(1, 10)
print(f"Value from randint: {value}")
print(random.choice(['apple', 'banana', 'cherry']))

import datetime

now = datetime.datetime.now()
print("Current date & time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


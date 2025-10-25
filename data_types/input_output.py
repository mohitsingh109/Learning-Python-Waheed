# input() function is use to take input from user
# By default input function return always string value
"""
I am multi line comment
I am multi line comment
I am multi line comment
"""
user_input = input("Enter your name:")
print("Hello", user_input,"!!!", type(user_input))

# string to int
# If input value is not a valid int that python throw ValueError
# If any type conversion fail python throw ValueError
user_age = int(input("Enter your age:"))
print("Your age is", user_age, type(user_age))

# How to print using + operator
# print("Your age is " + str(user_age) + " " + str(type(user_age)))

# How to print using f function
print(f'Your age is [{user_age}] {type(user_age)}')

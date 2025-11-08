# def <name of the function>(<arguments>):

# def greet():
#     print("Hello, Welcome to my python learning")
#
# # calling the function
# greet()
# greet()

# This function take two argument and return a result
# default return type of any function is None
def add_func(a, b):
    result = a + b
    return result

sum_value = add_func(10, 20) # calling the function
print(f"Sum is: {sum_value}")
sum_value = add_func(10.5, 20.22) # calling the function
print(f"Sum is: {sum_value}")
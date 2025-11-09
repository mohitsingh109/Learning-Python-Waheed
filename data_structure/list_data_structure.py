# list (Ordered, mutable (we can modify))

# this is a string list
fruits = ['apple', 'banana', 'cherry']

print(type(fruits))

# Start Index = 0 , Last Index = len of array - 1

# get the len of the list
print(len(fruits))

print("First Element:", fruits[0])
last_index = len(fruits) - 1
print("Last Element:", fruits[last_index])
print("Last Element:", fruits[-1]) # negative index
print("Second last Element:", fruits[-2])

# Add orange to the list
fruits.append('orange') # this will add to the last index

print("=========Add Orange============")
for fruit in fruits:
    print(fruit)
print("=====================")

# Remove banana from list
fruits.remove('banana')

print("==========Remove Banana===========")
for fruit in fruits:
    print(fruit)
print("=====================")

fruits[0] = "grape"

print("==========Update apple to grape===========")
for fruit in fruits:
    print(fruit)
print("=====================")

# Slicing in list
# list[startIndex:EndIndex] startIndex will be included, EndIndex will be exclusive
test = ['A', 'B', 'C', 'D', 'E']
print(test[1:])
print(test[2:])
print(test[1:3])
print(test[:4])


# arithmetic (+, -, /, *, %)

a = 10
b = 5

print("a + b:", a + b)
print("a - b:", a - b)
print("a / b:", a / b) # if b is zero we'll get ZeroDivisionError
print("a * b:", a * b)
print("a % b:", a % b) # it returns the remainder

# relational (>, <, >=, <=, ==, !=)
# relational operator always return boolean response
a = 10
b = 5

print("a > b:", a > b) # True
print("a < b:", a < b) # False
print("a >= 10:", a >= 10) # True
print("b <= 5:", b <= 5) # True
print("a == b:", a == b) # False
print("a != b:", a != b) # True

# logical (and, or, not)
a = 10
b = 5
result = (a == 10 and b != 6)
print("(a == 10 and b != 6)", result)

result = (a > 10 or b <= 6)
print("(a > 10 or b <= 6)", result)

result = not (a > 10 or b <= 4)
print("not (a > 10 or b <= 4)", result)

# assignment operators (=, +=, -=, *=, /=, %=)
a = 10
b = 5

a += 2 # a = a + 2
print("a += 2:", a)

a -= 3 # a = a - 3
print("a -= 2:", a)

# short-circuit evaluation
a = 10
b = 5
c = 7

result = (a >= 10 and b == 4 and c > 6)
print("(a >=10 and b == 4 and c > 6):", result)

result = (a < 10 or b != 4 or c > 6)
print("(a < 10 or b != 4 or c > 6):", result)

# Python support dynamic data type
# Java is strickly typed language

# data type : [int, float, string, char, boolean]
# int a = 10; this is java style
a = 10 # int
b = 11.4 # float & double
c = "Some String"
d = 'Z'
f = False

print(a, b, c, d, f) # Printing multiple variable
print(f'a: [{a}], b: [{b}], c: [{c}], d: [{d}], f: [{f}]')

a = "Now i am string" # string
print(a)
a = False
print(a)

# How to know what is the data type of variable?
# type()

print("Data Type of b:", type(b)) # THis will tell me the data type of b
print("Data Type of c:", type(c))
print("Data Type of c:", type(f))


# Type conversion string to int, float to int, int to string ...

# int to string
data1 = 20 # int
str_convert = str(data1)
print("str_convert:", str_convert, type(str_convert))

# float to string
data2 = 20.33 # float
str_convert2 = str(data2)
print("str_convert2:", str_convert2, type(str_convert2))

# string to float
data3 = "34.55" # string
float_convert3 = float(data3) # float is a function
print("float_convert3:", float_convert3, type(float_convert3))

# float to int
data4 = 97.65 # float
int_convert4 = int(data4)
print("int_convert4:", int_convert4, type(int_convert4))


x = 10 # global variable

def blabla():
    print(f"[blabla] Doing nothing: {x}") # I am using the global variable

def blabla1():
    result = 13 # local variable
    print(f"[blabla1] Doing nothing: {result}")

def blabla2():
    x = 5 # local variable (shadow the global variable)
    print(f"[blabla2] Doing nothing: {x}")

def blabla3():
    global x
    x = 8
    print(f"[blabla3] Doing nothing: {x}") # 8

blabla()
blabla1()
blabla2()
print(f"Value of X: {x}") # 10
blabla3()
print(f"Value of X: {x}") # 8
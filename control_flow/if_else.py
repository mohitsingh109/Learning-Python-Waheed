# Implement conditional statements (if, elif, else).
# Phone number validation
# Age validation
# Password validation etc..


# len() -> length function that tell you the length of the string, list, dict
# name = "Mohit"
# print(len(name) > 3)

name = input("Enter name:")
# check if name is min 3 char
# if else condition
if len(name) >= 3:
    print("Successfully Registered...", name)
else:
    print(f"Registered Failed for {name} min 3 char required")

# Password must be 6 char, and it should not exceed 10 char len & at least 1 special character [@,!,&,$,%]

password = input("Enter password:")

if len(password) < 6:
    print("Password should be min 6 char")
elif len(password) > 10:
    print("Password should be at max 10 char")
elif not ('@' in password or '!' in password or '&' in password or '$' in password or '%' in password):
    print("Password should contain at least 1 special character [@,!,&,$,%]")
else:
    print("Password successfully verified")


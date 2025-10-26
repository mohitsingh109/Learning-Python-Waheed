# for -> used for looping over collection(list, dict, tuple, set) of data like list of employee

# for i in range(10): # range is a function in python that start from 0 and end at < 10
#     print(i)
#
# print("===================")
#
# for i in range(5, 10): # range is a function in python that start from 5 and end at < 10
#     print(i)
#
# print("===================")
#
# for i in range(1, 10, 2): # range is a function in python that start from 1 and end at < 10 and step up by 2
#     print(i)
#
# # for e in employees:
# #     e.add_bonus(5$)
#

# number = int(input("Enter number:")) # 10
#
# for i in range(1, 11): # i = 2
#     print(f'{number} X {i} = {number * i}') # 10 X 2 = 20

# while
active = True
score = 10

# while active:
#     print("I am playing with score:", score)
#     score -= 1
#     if score == 0:
#         active = False # this help to break the loop
#         print("My player is dead...")

# do while
# do:
#     # code will appear here
# while(<condition>)

# break, continue -> both for & while loop can use it
# break -> it break the loop (take you out of the loop)
# continue -> it will skip the below code execution

while True:
    name = input("Enter your name:")
    if len(name) < 5:
        print("Please Enter a valid name")
        continue

    print("Your name is :", name)
    yes_no = input("Do you want to continue (yes or no):")
    if yes_no == "no":
        break




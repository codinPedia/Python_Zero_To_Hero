# A = True
# B = True

#### and
# print(A == True and B == True)

# if A == 5 and B == 10:
#     print("Satisfied")

#### or
# if A == 5 or B == 5:
#     print("We Have 5!")

#### not
# print(not True)
# print(not(A == True or B == True))

# import sys # For sys.exit()

# username = input("Enter Username: ")
# password = input("Enter Password: ")

#### Nested Ifs
# if username != "":
#
#     if len(username) >= 6:
#
#         if password != "":
#
#             if len(password) >= 6:
#
#                 print("Success: Signed Up!")
#
#             else:
#                 sys.exit("Error: Password Must Be Min 6 Characters Long")
#
#         else:
#             sys.exit("Error: Password Is Empty")
#
#     else:
#         sys.exit("Error: Username Must Be Min 6 Characters Long")
#
# else:
#     sys.exit("Error: Username Is Empty")

#### Guard Clauses
# if username == "":
#     sys.exit("Error: Username Is Empty")
#
# if len(username) < 6:
#     sys.exit("Error: Username Must Be Min 6 Characters Long")
#
# if password == "":
#     sys.exit("Error: password Is Empty")
#
# if len(password) < 6:
#     sys.exit("Error: Password Must Be Min 6 Characters Long")
#
# print("Success: Signed Up!")


#### ShortHand If ... Else (Ternary Operators)
# a = 5
# b = 10

# Setting m to max of a and b
# m = a if a > b else b

# print(m)

# print("TRUE!" if True else "FALSE!")

#### ShortHand Ternary
# c = True
# print(c or "Not True!")

message = "CodinPedia"

## Long Code
if message == "":
    print("Nothing To Print!")
else:
    print(message)

## Short Code
print(message or "Nothing To Print!")
